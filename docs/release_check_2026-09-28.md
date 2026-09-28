# Final release check — September 28, 2026

The creator requested only changes necessary for release within hours. This checkpoint covers that bounded pass. Preserve the author-written introduction and first briefing; do not restart the broader writing rewrite before shipping.

## Necessary fixes completed

- [x] **Save/load layout:** Five horizontal slots ran into the navigation area. Replaced them with five readable rows inside the notebook, retaining thumbnails, timestamps, and case context.
- [x] **Winston's final timeline question:** Players were asked to distinguish events without receiving the statement that identifies the answer. The existing reaction-specific witness statement is now shown before the question and repeated on retries. Puzzle answers are unchanged.
- [x] **Dialogue overflow:** Dialogue could run beyond the paper panel, and the final confession was too long for a single screen. Adjusted the shared dialogue width and spacing, and paginated every confession without rewriting its text.
- [x] **Build exclusions:** The raw music pack patterns used square brackets, which Ren'Py interpreted as a character class. Fixed the patterns and excluded local verification scripts and project-only files from the package.

## Verification completed

- [x] 28 Python tests pass. The evidence model check reports 19,606 deduplicated transitions with no mismatches.
- [x] Ren'Py 8.5.3: 40 test cases, 17 hooks, and 96 assertions pass across six suites. Evidence: `tmp/release-check/verified-stdout.txt`.
- [x] All ten minigame pause/resume checks pass, including timer freeze. Finale menu and cancellation checks pass.
- [x] All 42 catalog ending scenes execute with their replay setup and outro. This checks those scenes, **not** 42 complete legal routes through Days One–Six.
- [x] One successful final accusation plays through confession, partner choice, gallery unlock, and credits. All nine confessions retain their complete original text across their new pages.
- [x] Fresh save/load and long-dialogue screenshots inspected; all five save buttons are present. Accusation, card, memory, and centrifuge captures were also inspected. Evidence: `tests/screenshots/release/` and `tests/screenshots/round2/`.
- [x] Built ZIP and internal game archive inspected. All 11 selected OGG tracks are included; raw packs, project docs/tests/tools, saves, and local test scripts are excluded. All 67 archived source-script/audio files match the current project.
- [x] Extracted Windows executable starts, initializes its renderer, and responds. Packaged lint exits successfully without script issues. Evidence: `tmp/release-check/packaged-lint.txt` and the extracted build's `log.txt`.

The SDK build printed permission warnings while attempting to write its external Python cache. It nevertheless completed the package; the extracted build passed the checks above. No claim is made that the build command was warning-free.

## Build to use

- Package: [DateAndDeduce-1.0-pc.zip](../tmp/release-check/distributions/DateAndDeduce-1.0-pc.zip)
- Size: 99,206,907 bytes (about 99 MB).
- SHA-256: `676cc53cf981fe2d3119d50cbdbe5818a85d3f1176cac763eb7a2a9cb224e3e3`
- Windows: extract the ZIP, then launch `DateAndDeduce.exe` inside `DateAndDeduce-1.0-pc`.
- The PC package also includes Linux, which was not tested. No browser package or external upload was made.

## Handoff

The necessary fixes from this pass are complete. No further release-blocking defect was found in these checks. Full manual route playthroughs, music audition, and the unchecked editorial work in the round-two guide remain uncompleted; they are not implicitly approved or verified by this checkpoint. Smooth Driving remains a provisional Ulysses choice pending listening.

If further work is requested, preserve the existing changes and start from this package's verified source. Check the current platform requirement before producing a different build. Do not treat the old broad backlog as a mandate to delay this release.
