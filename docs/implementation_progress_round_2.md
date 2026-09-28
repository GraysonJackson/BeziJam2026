# Date and Deduce — round 2 progress

Active guide: [implementation_guide_round_2.md](implementation_guide_round_2.md). Updated September 28, 2026.

## Resume here

**Release checkpoint, September 28:** The creator narrowed the work to necessary fixes because the game must ship within hours. The final pass is complete; see [release_check_2026-09-28.md](release_check_2026-09-28.md) for the four fixes, verification, and built PC package. Do not automatically resume the larger editorial backlog before this release. The earlier batch notes below are historical; Batch 6 supersedes their test-failure status.

The new guide contains 116 findings/tasks. The creator authorized staged implementation and made UI the second-highest priority. First repair case/ending logic, then UI, then writing, then music. Preserve current user changes and the protected introduction/briefing. Do not restore historical planning files or use `bezi-contributions.md` as reference.

The broader implementation remains incomplete. Read the batch records below before editing. An unchecked item remains open even if another item in its section is complete.

## Status meanings

- **OPEN**: not implemented in this pass.
- **IN PROGRESS**: partial change; acceptance checks outstanding.
- **IMPLEMENTED / SOURCE-TESTED**: logic or text checks passed; does not imply visual playtesting.
- **VERIFIED**: specified acceptance checks passed, with evidence recorded.
- **AWAITING CREATOR**: dependent detail is unresolved; work on independent items continues.
- **PRODUCTION / PLAYTEST**: requires supplied assets, listening, or a real graphical playtest.

## Batch 0 — review and handoff

- [x] Wrote the full second-pass guide, including character voice, all routes/reports, ending logic, all ten games, UI, music mapping, attribution, and a 20-question character bank.
- [x] Confirmed creator approval of Decisions 78–103 and Blackjack for bouncy minigames.
- [x] Recorded Smooth Driving as a candidate for Ulysses pending listening, per creator reply.
- [x] Added historical-status notices to the previous guide and ledger. Preserved their contents.
- [x] Kept Bezi contributions as ignored historical material.
- [ ] Completed interactive/visual testing of the current game. The graphical runner now renders fresh pause screenshots, but the interaction suite still has one finale-menu timeout and the full route set remains unplayed.

Review checks: six existing Python suites passed; evidence suite reported 19,606 deduplicated transitions. Ren'Py 8.5.3 lint reported no script issues. Initial lint printed a save-token permission error; subsequent engine checks must use a project-local save directory. This is not evidence that 42 legal ending paths were played.

## Current questions

Answered and recorded as Decisions 104–106 and 109–110: Ica secures evidence while Nicky pursues; all nine suspects are ATLAS staff with badges, Enrico died at home, and the lockbox is at the warehouse; Day Six offers the next personal Ulysses episode after mandatory preparation; forensic exclusions may receive brief independent corroboration while Razzle's removable-feature clues remain decisive. Smooth Driving still needs an actual audition/approval.

## Implementation batches

### Batch 1 — case and ending repairs (verification in progress)

Source changes now exist in `game/day_seven.rpy`, `game/day_seven_state.rpy`, `game/script.rpy` (Ica Visit Six), and `game/ulysses_evenings.rpy`. Fixed accusation order, differentiated insufficient support, recorded dismissal response and relationship intent, saved replay context, and moved gallery unlock after the outro. Ica now interrupts destruction of the opened warehouse lockbox's contents, secures the evidence, and calls Nicky. Late Ulysses personal scenes retain episode order on Day Six. Deadline dialogue is outside the protected briefing. Full-focus versus provisional success wording is partly repaired; later overconfident summaries still need review.

### Batch 2 — shared UI (verification in progress)

All ten minigame screens now expose Pause / Rules and freeze screen timers while paused. Escape/right-click opens that panel; assistance is explicit. Rules have an independent scroll area and corrected mechanics. Finale screens expose the save/settings menu and Escape dismisses an uncommitted confirmation. Save metadata captures day, investigator and visit with legacy/empty-slot fallbacks. Changes are in `game/screens/`, plus `game/save_context.rpy`.

Ren'Py lint passes with project-local saves. A real graphical test run now renders successfully; the previous dummy-display limitation was environmental. Existing screenshot comparisons failed against old images of a different size, so these are not yet approved baselines. The new five-test regression file passes. The bounded pause interaction run passed all ten minigame pause cases, but its separate finale accusation-menu case timed out; no completed route coverage is claimed.

### Batch 3 — bounded follow-up completed

Added independent alibi/context language to Dhampir's first and third investigations while preserving the existing puzzle answers, and recorded the creator's two clarifications in `audit_decisions.md`. Added `tests/test_round2_regressions.py`, which exercises the actual ending catalog/replay helpers, insufficiency-versus-contradiction result, pause/resume helpers, and save metadata. Those five tests pass. The Ren'Py pause interaction run produced ten fresh pause screenshots and passed all ten minigame pause cases; the same run still has a separate finale accusation-menu timeout, so the UI batch remains in progress. Stop here for this handoff; do not begin music integration or broader writing rewrites in this checkpoint.

### Batch 4 — UI repairs and music integration completed

- **UI Hardening & Interaction Tests (R2-026, R2-027, R2-028, R2-033, R2-034)**:
  - Fixed the accusation menu test hang by explicitly resetting `$ main_menu = False` and `$ _in_replay = False` during test label execution, enabling Ren'Py's native `ShowMenu("save")` action.
  - Ran the `global.round2_interactions` suite: all 36 logic and control assertions passed in 23.75s, verifying pause/resume/timer-freeze across all 10 minigames, Escape handling, and finale save/settings invocation.
  - Accusation comparison panel layout verified against 1760x960 boundaries (fits horizontally with 140px margin, inner columns ~578px within 606px viewport).
  - Notebook text input selection verified with `draggable False`, character count counter `[len(playerInvestigationNotes)]/4000`, and Escape dismiss key.
  - Credits scroll extended to 48.0s at `ypos -3800` with Escape return.
- **Music Integration (R2-102, R2-103, R2-104, R2-105, R2-107, R2-108, R2-109)**:
  - Imported 11 stereo OGG tracks into `game/audio/music/` and created `game/audio_definitions.rpy` with audio controller helpers (`play_route_music`, `stop_route_music`, `push_minigame_music`, `pop_minigame_music`).
  - Wired Blackjack minigame music into start/finish/abort routines across all 7 minigame files.
  - Routed character daytime music into daytime dispatchers in `game/script.rpy` and smooth fadeout on day advance.
  - Wired Ulysses personal evening cues in `game/ulysses_evenings.rpy` (Smooth Driving audition on Evenings 1-5; deliberate silence on Evening 6).
  - Wired Day Seven finale music: deliberate silence during briefing/accusation/review; Treehouse Party on confession; partner-specific themes for solved ending vignettes; silence for failure endings; credits music conditional on case outcome.
  - Enabled main menu music in `game/options.rpy` and added distribution exclusions for raw source packs, docs, tests, and temporary files.
  - Added visible creator music attribution to JDSherbert in `screen about` and `screen day_seven_credits`.


### Batch 5 — Route audits, minigame feedback, and regression hardening completed

- **Winston Route Audits (R2-070 – R2-074)**:
  - Differentiated Visit 5 fear disclosure from Visit 2; grounded powers in real situational danger (shutting off power, rooms on fire) instead of repeating duplicate "emergency brake" monologue.
  - Guarded Visit 5 intimacy and handholding on `winston_day_five_care != "pushed"`; pushing witnesses keeps Winston strictly professional.
  - Removed magical sobriety reset framing; grounded in ordinary patrol endurance and bitter coffee.
  - Removed stray spacing and grounded cleared alibis with front-desk access logs.
- **Ica Route Audits (R2-075 – R2-081)**:
  - Visit 1 candy eating respects `ica_day_one_candy == "none"`.
  - Staring contest win dialogue acknowledges holding out longer even with blinks.
  - Board game AI prioritizes winning moves over bumps; withdrawal branches cleanly without forced extra rounds or false win announcements.
  - Food contest aftermath respects food leftover on timeout/withdrawal and ties tray disposal to player action.
  - Prank minigame: fixed sightline description to floating office junk; added visible transition after prank withdrawal; checkpointing verified.
- **Ulysses Personal Scenes & Reports (R2-082 – R2-090)**:
  - Personal scenes dispatch in experienced order on Day Six (`ulyssesPersonalEvenings < 6`).
  - Room props (photograph, cassette player, chessboard) conditioned on experienced session counts; cassette drawer sequence resolved before menu.
  - Guarded lingering contact in Evening 3 on `ulyssesRomanceInterest >= ULYSSES_ROMANCE_WARM_THRESHOLD`.
  - Foresight explanation grounded in concrete early attempt where backlash nearly stopped Ulysses's heart.
  - Protected private confidences in mandatory reports across all routes (Razzle 2, Dhampir 2, Madeline 2, etc.); conditioned reporting choices on actual player actions (Nicky hints used, Winston assistance).
  - Refactored `ULYSSES_REPEAT_COMMENTS` across all 6 daytime characters to reflect time spent and procedural methods rather than unearned emotional intimacy.
  - Final briefing: eliminated 12 repetitive round-robin evidence lectures; preserved Nicky/Madeline file conflict and Winston joke; partner perspective branched to favorite investigator.
- **Minigame Substance & Feedback (R2-091 – R2-101)**:
  - Scanner "perfect" aligned to require strictly zero mistakes and zero hints.
  - Blackjack intuition feedback rewritten to character-driven qualitative reads; "canonical result" jargon removed.
  - Height memory game framed as sorting irrelevant memories into the background rather than erasing testimony.
  - High-card assistance clearly indicates leeway calculation (+/-) and tiebreak resolution.
  - Staring rules accurately describe bidirectional impulse drift and accumulated hold requirement.
  - Eating minigame UI (R2-099): updated buttons to show stamina cost (-0.9), stamina gain (+1.5), and choke risk when stamina < 0.9; cheat counter explicitly labeled as including pre-game incident.
  - Prank checkpoints and board AI / withdrawal (R2-100) verified with unit tests.
  - Nicky matching equivalence and full completion (R2-101) covered with automated regression tests.
- **Engine & Regression Verification (R2-110, R2-111, R2-113, R2-116)**:
  - Python test suite: all 28 automated tests passing in `tests/test_round2_regressions.py`, `tests/test_phase1_minigames.py`, `tests/test_phase2_features.py`, `tests/test_phase3_continuity.py`, `tests/test_phase5_minigames.py`, `tests/test_phase7_endings.py`.
  - Ren'Py 8.5.3 lint: 0 errors, 0 warnings across 3,333 dialogue blocks, 247 menus, and 49 screens.


### Batch 6 — final release pass completed (September 28)

- [x] Repaired the five-slot save/load layout so rows and their case metadata fit inside the notebook without covering navigation. Files: `game/screens/save_load.rpy`. Fresh save screenshot inspected; all five slot buttons asserted in the engine.
- [x] Supplied the actual witness statement before Winston's Visit Six reconstruction question and on retries, using the existing reaction-specific descriptions and answers. Removed the incorrect claim that the timestamps alone distinguish the answer. File: `game/script.rpy`. R2-012 is implemented; lint and the full engine suite pass.
- [x] Kept dialogue inside the paper panel and split all nine final confessions into readable pages without changing their wording. Files: `game/screens/dialogue_screens.rpy`, `game/day_seven_state.rpy`, `game/day_seven.rpy`. Inspected the longest static dialogue screenshot; tested every confession's text preservation and page length; played the final accusation through credits.
- [x] Fixed raw music pack exclusions: `[FREE]` was being interpreted as a pattern character class. Excluded local test scripts and project-only tools/metadata as well. File: `game/options.rpy`. Inspected the ZIP and its game archive: all 11 selected music tracks are included, while raw packs, project docs/tests/tools, saves, and local test scripts are absent. R2-108 is now package-verified.
- [x] Added `game/release_testcases.rpy` (excluded from distribution) and corrected test isolation in `game/testcases.rpy`: reset the personal-evening counter and use dedicated test save slots. Verification: 28 Python tests pass; the full Ren'Py run passes 40 test cases and 96 assertions. It renders all 42 catalog ending scenes and exercises one complete final-accusation-to-credits flow. This does not establish 42 legal six-day playthroughs.
- [x] Built `tmp/release-check/distributions/DateAndDeduce-1.0-pc.zip`. The extracted Windows executable initializes and responds, and packaged lint reports no script issues. All 67 archived source-script/audio files match the current project. The SDK build printed cache-write permission warnings, but completed; package verification and the extracted runtime checks passed. No upload was performed.

Remaining production limits: Linux is included in the PC package but untested; a browser build has not been produced; full manual route playthroughs and music audition remain outstanding. These are not marked complete by the automated suite. No additional release-blocking defect was found in the bounded final checks.

## Item checklist

The complete checklist is generated from the guide below. Status changes must include a batch note naming affected files and verification.

| Done | ID | Finding | Status |
|---|---|---|---|
| [x] | R2-001 | Wrong accusation happens in the wrong order | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-002 | A correct guess becomes a supposedly unique deduction | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-003 | Insufficient evidence is called a contradiction | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-004 | Finale introduces facts the route did not establish | OPEN |
| [x] | R2-005 | Deadline explanation is still absent from played dialogue | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-006 | Ica's intruder destroys the key before using it | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-007 | Ica's report invents a different break-in | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-008 | Heavy chair does not prevent pursuit from the floor | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-009 | Cross-report access logs overstate what a swipe proves | OPEN |
| [ ] | R2-010 | Several exclusions still confuse absence with innocence | OPEN |
| [ ] | R2-011 | Behavioral labels remain more certain than their evidence | OPEN |
| [x] | R2-012 | Winston's timeline question lacks discriminating evidence | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-013 | Failure-response callbacks read the wrong choice | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-014 | Friendship is rewritten as failed romance | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-015 | Gallery replays lack relationship context | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-016 | Gallery unlock precedes the outro | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-017 | Failure endings drift back inside the office | OPEN |
| [x] | R2-018 | Weekend transitions are incomplete | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-019 | Confessions are assembled correctly but weakly individualized | OPEN |
| [ ] | R2-020 | Legal ending paths are not established by the current tests | OPEN |
| [x] | R2-021 | Pause is not reachable | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-022 | Escape can silently surrender a game | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-023 | Rules pages have fixed-height, unscrollable content | IMPLEMENTED / VISUALLY CHECKED |
| [x] | R2-024 | Controls and labels disagree with mechanics | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-025 | Save thumbnails lack useful case context | IMPLEMENTED / VISUALLY CHECKED |
| [x] | R2-026 | Accusation comparison needs a current overflow check | IMPLEMENTED / VISUALLY CHECKED |
| [x] | R2-027 | Finale screens suppress the normal menu | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-028 | Notes need a realistic long-input check | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-029 | Readability needs current screenshots, not old claims | OPEN |
| [ ] | R2-030 | Sprite coverage and staging remain production work | OPEN |
| [ ] | R2-031 | Reused backgrounds can contradict the location | OPEN |
| [ ] | R2-032 | Gallery hints and replay need UI verification | OPEN |
| [x] | R2-033 | Credits must remain readable after music is added | IMPLEMENTED / VISUALLY CHECKED |
| [x] | R2-034 | A screenshot smoke test is not an interaction test | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-035 | Audit every later scene against the opening, not just highlighted lines | OPEN |
| [ ] | R2-036 | Reduce the procedure-lesson loop | OPEN |
| [ ] | R2-037 | Cut interpretation after the scene already shows emotion | OPEN |
| [ ] | R2-038 | Differentiate reassurance, flirting, and rejection | OPEN |
| [ ] | R2-039 | Deep disclosures still arrive on schedule rather than through trust | OPEN |
| [ ] | R2-040 | Kindness can still be treated as mutual attraction | OPEN |
| [ ] | R2-041 | Calendar language still assumes consecutive visits | OPEN |
| [ ] | R2-042 | Cleanup and report endings overstay their purpose | OPEN |
| [ ] | R2-043 | Protect the open protagonist | OPEN |
| [ ] | R2-044 | False departures | OPEN |
| [ ] | R2-045 | Fire exposition sounds imported from design notes | OPEN |
| [ ] | R2-046 | Witness uncertainty is inconsistently described | OPEN |
| [ ] | R2-047 | Leading questions recur despite the lesson | OPEN |
| [ ] | R2-048 | Motive/biography arrives without its source | OPEN |
| [ ] | R2-049 | Tape handling loses track of the tape | OPEN |
| [ ] | R2-050 | Reconstruction credit and agency are uneven | OPEN |
| [ ] | R2-051 | Repetition and result-insensitive praise | OPEN |
| [ ] | R2-052 | Keep the suit persona intentional | OPEN |
| [ ] | R2-053 | Reputation is reduced to appearance | OPEN |
| [ ] | R2-054 | Visits 4 and 5 need distinct emotional work | OPEN |
| [ ] | R2-055 | Physical evidence location varies without a matching search | OPEN |
| [ ] | R2-056 | Result claims exceed the recorded result | OPEN |
| [ ] | R2-057 | Technical language becomes a personality substitute | OPEN |
| [ ] | R2-058 | A brilliant scientist needs a credible wrong premise | OPEN |
| [ ] | R2-059 | Helmet boundaries have three different severities | OPEN |
| [ ] | R2-060 | Visit 6's apology threat is empty | OPEN |
| [ ] | R2-061 | Emotional disclosure needs an actual test-related cause | OPEN |
| [ ] | R2-062 | Small physical transitions remain missing | OPEN |
| [ ] | R2-063 | Music/format continuity is only partially fixed | OPEN |
| [ ] | R2-064 | Respecting a boundary has no lasting memory | OPEN |
| [ ] | R2-065 | The same institutional complaint is disclosed twice | OPEN |
| [ ] | R2-066 | Local case paperwork is called federal | OPEN |
| [ ] | R2-067 | Police coverup claims outrun the shown evidence | OPEN |
| [ ] | R2-068 | Contaminated evidence stays soft, then the finale treats it as proof | OPEN |
| [ ] | R2-069 | Break duration and behavior need agreement | OPEN |
| [x] | R2-070 | The same fear is disclosed twice | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-071 | Pushing a witness does not affect later trust | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-072 | His power and coffee should not function as a sobriety reset | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-073 | Comedy sometimes becomes a neat maxim | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-074 | Pager and copyedit cleanup | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-075 | Declined candy still gets eaten | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-076 | “One round” has no effect on the activity | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-077 | Perfect-stare dialogue ignores misses | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-078 | Food contest aftermath assumes empty trays | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-079 | Prank withdrawal skips to a finished room | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-080 | Gravity accidentally becomes a light power | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-081 | Sincerity is too often explained for her | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-082 | Calendar-six personal scene bypasses experienced order | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-083 | Room props follow the calendar while conversations follow visits | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-084 | Professional trust is narrated as personal intimacy | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-085 | Foresight explanation sounds like an FAQ | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-086 | Reports still reveal confidences by default | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-087 | Reporting choices sometimes assert actions never taken | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-088 | Focus commentary makes unearned claims about trust | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-089 | Ulysses loses the opening's range | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-090 | Final briefing repeats the same lesson seven times | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-091 | Scanner offers hidden correctness rather than visible deduction | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-092 | Scanner “perfect” is inconsistent | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-093 | Centrifuge abstraction needs a clear promise | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-094 | Blackjack intuition spends a limited use to repeat the meter | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-095 | Blackjack interviews need case-specific answers | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-096 | Razzle's board still teaches erasing unwanted memories | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-097 | High-card assistance obscures the comparison | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-098 | Staring instructions misdescribe the input | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-099 | Eating UI hides the most useful input information | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-100 | Board and prank improvements need complete outcome checks | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-101 | Nicky's repaired matching needs regression coverage | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-102 | Import only chosen playback files | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-103 | Cue by scene owner and activity | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-104 | Give serious scenes deliberate silence | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-105 | Make music state survive navigation | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-106 | Listen before finalizing placement or loops | PENDING AUDITION |
| [x] | R2-107 | Add visible creator credit in two places | IMPLEMENTED / VISUALLY CHECKED |
| [x] | R2-108 | Keep raw source packs out of distributions | VERIFIED / PACKAGE INSPECTED |
| [x] | R2-109 | Separate score from the albums in dialogue | IMPLEMENTED / EDITORIAL |
| [x] | R2-110 | Make completion claims match evidence | IMPLEMENTED / SOURCE-TESTED |
| [x] | R2-111 | Test actual helpers rather than copied expected models | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-112 | Keep an explicit route/scene coverage matrix | OPEN |
| [x] | R2-113 | Validate with the current engine and fresh saves | IMPLEMENTED / SOURCE-TESTED |
| [ ] | R2-114 | Keep asset deferrals honest | OPEN |
| [ ] | R2-115 | Check supporting/template files without expanding scope | OPEN |
| [x] | R2-116 | Preserve a resumable checkpoint after each batch | IMPLEMENTED / SOURCE-TESTED |
