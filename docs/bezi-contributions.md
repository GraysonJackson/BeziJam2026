# Bezi Contributions to Date and Deduce

> **HISTORICAL RECORD — IGNORE FOR IMPLEMENTATION.** The creator has retained this file only as a contribution history. Do not use it as a reference for writing, characterization, canon, mechanics, current implementation status, or development instructions. Do not follow its handoff links or restore deleted documents based on this record. Use `docs/implementation_guide.md`, `docs/audit_decisions.md`, and the current source instead; the creator-authored intro and briefing remain the writing standard. Some documents named below have been deleted.

This document records Bezi's historical contributions to the `BeziJam2026` project. The descriptions below are preserved as history and may no longer describe the current game.

## Project Onboarding and Documentation

- **`/Pages/Private/Project Handoff - Future Agents.md`** — A full onboarding brief for future agents: repository map, source-of-truth file table, the investigation data model (killer seeding, suspect attributes, route reveal logic), the route evidence summary table, player-facing systems, working conventions, and a list of known unknowns/TODOs.
- **`/Pages/Private/GDD/GDD - Overview.md`** — Game design document overview: project summary, game overview, core mechanics, story flow table, tech stack, and open design questions.
- **`/Pages/Private/GDD/GDD - Features.md`** — Feature-by-feature breakdown: murder investigation, evidence routes, suspect notebook/notes, daily team and relationship layer, planned minigames, character presentation, and the Ren'Py interface/persistence layer, each with related-script references.

## Quality Audits and Design Decisions (`/BeziJam2026/docs/`)

- **`audit_report.md`** and **`quality_audit_report.md`** — Duplicate exhaustive architectural/quality audits of the codebase covering narrative consistency, investigative mechanics, engine stability, and UX, benchmarked against the "gold standard" intro and case-briefing scenes.
- **`writing_quality_evaluation.md`** — A deep, line-by-line literary critique of narrative voice, character consistency, emotional progression, dialogue repetition, branching continuity, and the Ulysses evening debriefs.
- **`audit_decisions.md`** — Recorded the creator's decisions after reviewing the audits above, locking in canon/design directions (e.g., rollback disabled, Madeline/Ulysses backstory, Dhampir's dark-comedy arc) so future audits don't flag intentional choices as defects.
- **`day-4-5-character-ideas.md`** — A planning guide for what Day 4 and Day 5 of each investigator route need to accomplish narratively, with soft-lead and pacing guidance that avoids duplicating hard clues.
- **`ulysses-evenings.md`** — Design reference for the nightly Ulysses report structure: per-investigator report scenes, response to player time distribution, and his six-evening personal/romantic arc.

## Minigame Design Plans (`/Plans/`)

Bezi authored a full slate of implementation plans for the game's interactive minigames, each specifying state helpers, screen UI, integration points, and validation rules consistent with the shared `Flirt` / `Cheat` / `Play Fair` approach system:

| Plan | Route / Visit | Concept |
| --- | --- | --- |
| `Razzle Height Memory Cleanup.md` | Razzle, Visit 3 | Click-based "thought board" cleanup minigame to surface height evidence; established the reusable pattern other plans build on. |
| `Ica Cards.md` | Ica, Day 1 | Casual high-card/draw card game introducing the shared approach system. |
| `Ica Staring Contest.md` | Ica, Day 2 | Stardew Valley–style balance-bar staring contest. |
| `Ica Board Game.md` | Ica, Day 3 | Original Sorry!-inspired pawn-race board game. |
| `Ica Eating Competition.md` | Ica, Day 4 | Competitive eating contest with cheat/flirt/play-fair timed-action mechanics. |
| `Ica Prank Ulysses.md` | Ica, Day 5 | Top-down stealth sequence to prank Ulysses without altering investigation state. |
| `Ica Killer Encounter Chicken.md` | Ica, Day 6 | Final visit: witnessing the killer, then a flirtatious "game of chicken" romantic resolution (no win/loss scoring). |
| `Madeline Centrifuge Test.md` | Madeline, Visit 3 | Laboratory centrifuge minigame gating the blood-type clue reveal. |
| `Winston Blackjack Stress Test.md` | Winston, Visit 3 | Interrogation blackjack minigame gating the temperament clue reveal. |
| `Nicky Memory Matching.md` | Nicky, Visit 3 | Face-down memory-matching minigame gating the build clue reveal. |

Each plan is explicit that minigame performance flavors the encounter and dialogue but never determines investigation truth (killer identity, eliminations, or clue values) — those remain governed by the seeded route data in `game/investigation.rpy`.

## Implemented Ren'Py Screens (`/BeziJam2026/game/screens/`)

From the plans above, the following minigame screens exist in the project (implemented directly or scaffolded from Bezi's plans):

- `height_memory_minigame.rpy` (Razzle)
- `ica_cards_minigame.rpy`
- `ica_staring_minigame.rpy`
- `ica_board_game_minigame.rpy`
- `ica_eating_minigame.rpy`
- `ica_prank_minigame.rpy`
- `madeline_centrifuge_minigame.rpy`
- `winston_pressure_minigame.rpy`
- `nicky_memory_minigame.rpy`
- `dhampir_ispy_minigame.rpy`
- `minigame_rules.rpy` (shared rules/help presentation)

## How Bezi Helped

- **Project comprehension:** Read and mapped the entire Ren'Py codebase (`script.rpy`, `investigation.rpy`, screens) to understand the killer-seeding system, route-reveal architecture, and notebook/notes UI, then distilled it into onboarding docs so future work doesn't require re-discovery.
- **Design planning:** Turned loose minigame ideas from `docs/minigames.md` into fully specified, implementation-ready plans with concrete helper-function names, state shapes, screen layouts, and validation/error-handling rules — while explicitly protecting investigation integrity (killer safety, no duplicate clue awards, no untracked ties).
- **Quality assurance:** Performed structural and prose-level audits of the narrative and mechanics, then helped the team lock in canonical design decisions so future review passes focus on real regressions instead of already-settled creative choices.
- **Consistency enforcement:** Established and documented working conventions (snake_case identifiers, asset naming, keeping `docs/route-reveals.md` in sync with `investigation.rpy`) so the team and future agents build on a single source of truth.

## Notes for Future Agents

Ignore this document when implementing or reviewing the game. Its plan descriptions and external handoff references are historical, not current instructions. Follow `docs/implementation_guide.md` and `docs/audit_decisions.md`, and verify behavior against the current source.
