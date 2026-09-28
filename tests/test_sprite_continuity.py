"""Automated sprite dialogue audit test.
Scans game/script.rpy, game/day_seven.rpy, and game/ulysses_evenings.rpy.
Asserts that speaking characters (w, d, i, m, r, n, u, f) always have an active on-screen sprite.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAR_MAP = {
    'w': 'winston',
    'd': 'dhampir',
    'i': 'ica',
    'm': 'madeline',
    'r': 'razzle',
    'n': 'nicky',
    'u': 'ulysses',
    'f': 'freddy'
}


class SpriteContinuityTests(unittest.TestCase):
    @classmethod
    def get_violations(cls):
        script_files = [
            ROOT / "game" / "script.rpy",
            ROOT / "game" / "day_seven.rpy",
            ROOT / "game" / "ulysses_evenings.rpy",
        ]

        violations = []

        for script_file in script_files:
            lines = script_file.read_text(encoding="utf-8").splitlines()
            active_sprites = set()

            for line_no, line in enumerate(lines, 1):
                stripped = line.strip()

                # Reset on scene statement
                if stripped.startswith("scene ") or stripped == "scene":
                    active_sprites.clear()
                    continue

                # Add on show statement
                if stripped.startswith("show "):
                    parts = stripped.split()
                    if len(parts) > 1:
                        tag = parts[1]
                        if tag in CHAR_MAP.values():
                            active_sprites.add(tag)
                        elif tag == "umbral":
                            active_sprites.add("ulysses")
                    continue

                # Discard on hide statement
                if stripped.startswith("hide "):
                    parts = stripped.split()
                    if len(parts) > 1:
                        tag = parts[1]
                        if tag in CHAR_MAP.values():
                            active_sprites.discard(tag)
                        elif tag == "umbral":
                            active_sprites.discard("ulysses")
                    continue

                # Match dialogue statements: char "dialogue" or char @ expr "dialogue"
                m = re.match(r'^([wdimrnuf])\s+(?:@\s+[\w\s]+\s+)?\"(.*)\"', stripped)
                if m:
                    speaker_char = m.group(1)
                    target_sprite = CHAR_MAP[speaker_char]
                    if target_sprite not in active_sprites:
                        violations.append({
                            "file": script_file.name,
                            "line": line_no,
                            "speaker": speaker_char,
                            "sprite": target_sprite,
                            "text": stripped[:70]
                        })

        return violations

    def test_all_dialogue_has_active_sprite(self):
        violations = self.get_violations()
        if violations:
            msg_lines = [f"Found {len(violations)} dialogue lines without active sprite:"]
            for v in violations[:10]:
                msg_lines.append(f"  {v['file']}:{v['line']} -> {v['speaker']} ({v['sprite']}): {v['text']}")
            if len(violations) > 10:
                msg_lines.append(f"  ... and {len(violations) - 10} more.")
            self.fail("\n".join(msg_lines))


if __name__ == "__main__":
    import sys
    if "--list" in sys.argv:
        viols = SpriteContinuityTests.get_violations()
        print(f"Total violations: {len(viols)}")
        for v in viols:
            print(f"{v['file']}:{v['line']} [{v['speaker']}/{v['sprite']}]: {v['text']}")
    else:
        unittest.main()
