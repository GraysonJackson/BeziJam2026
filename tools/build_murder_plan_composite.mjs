import fs from "node:fs/promises";
import path from "node:path";
import sharp from "file:///C:/Users/grays/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp/dist/index.mjs";

const sourceRoot = "C:/Users/grays/Nextcloud/Documents/NeatNotes/MD";
const canvasPath = path.join(sourceRoot, "MurderGamePlan.canvas");
const outputPath = "C:/Users/grays/Desktop/sw/gameJam/BeziJam2026/docs/murder-game-plan-composite.png";
const canvasWidth = 25408;
const canvasHeight = 13476;
const tileWidth = 794;
const tileHeight = 1123;

const canvas = JSON.parse(await fs.readFile(canvasPath, "utf8"));
const nodes = canvas.nodes.filter((node) => node.type === "file");
const assetDirectory = path.join(sourceRoot, "MurderGamePlan", "Assets");
const sourceTiles = (await fs.readdir(assetDirectory)).filter((name) => /^chunk_.*\.png$/i.test(name));

if (nodes.length !== 142) {
  throw new Error(`Expected 142 image nodes; found ${nodes.length}.`);
}
if (sourceTiles.length !== 142) {
  throw new Error(`Expected 142 source tiles; found ${sourceTiles.length}.`);
}

const seen = new Set();
const seenPositions = new Set();
const inputs = [];
for (const node of nodes) {
  if (node.width !== tileWidth || node.height !== tileHeight) {
    throw new Error(`Unexpected tile size for ${node.file}: ${node.width}x${node.height}.`);
  }
  if (node.x < 0 || node.y < 0 || node.x + node.width > canvasWidth || node.y + node.height > canvasHeight) {
    throw new Error(`Tile is outside the canvas: ${node.file}.`);
  }
  if (seen.has(node.file)) {
    throw new Error(`Duplicate canvas tile: ${node.file}.`);
  }
  seen.add(node.file);
  const positionKey = `${node.x},${node.y}`;
  if (seenPositions.has(positionKey)) {
    throw new Error(`Duplicate canvas position: ${positionKey}.`);
  }
  seenPositions.add(positionKey);

  const inputPath = path.join(sourceRoot, ...node.file.split("/"));
  const metadata = await sharp(inputPath).metadata();
  if (metadata.width !== tileWidth || metadata.height !== tileHeight) {
    throw new Error(`Source dimensions differ for ${node.file}: ${metadata.width}x${metadata.height}.`);
  }
  inputs.push({ input: inputPath, left: node.x, top: node.y });
}

const canvasTileNames = new Set([...seen].map((file) => path.basename(file)));
const missingFromCanvas = sourceTiles.filter((name) => !canvasTileNames.has(name));
if (missingFromCanvas.length) {
  throw new Error(`Source tiles missing from canvas: ${missingFromCanvas.join(", ")}.`);
}

sharp.cache({ memory: 256, files: 32, items: 256 });
sharp.concurrency(2);

await sharp({
  create: {
    width: canvasWidth,
    height: canvasHeight,
    channels: 3,
    background: "#F8F6F1",
  },
  limitInputPixels: false,
})
  .composite(inputs)
  .png({ compressionLevel: 9, adaptiveFiltering: false })
  .toFile(outputPath);

const result = await sharp(outputPath, { limitInputPixels: false }).metadata();
if (result.width !== canvasWidth || result.height !== canvasHeight || result.format !== "png") {
  throw new Error(`Composite verification failed: ${result.width}x${result.height} ${result.format}.`);
}

console.log(JSON.stringify({
  outputPath,
  canvas: `${result.width}x${result.height}`,
  tileCount: nodes.length,
  uniqueSources: seen.size,
  uniquePositions: seenPositions.size,
  background: "#F8F6F1",
}));
