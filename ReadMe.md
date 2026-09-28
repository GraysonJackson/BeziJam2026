# Date and Deduce: A D&D Spinoff!

A Ren'Py visual novel where the player joins the ATLAS superhero team as a new investigator in 1996 Los Angeles. Enrico Edge has been murdered, nine suspects remain, and the player has one week to gather enough evidence to name the killer. Each day the player chooses which ATLAS member to work with, balancing investigation progress against getting to know the team — and possibly starting a romance.

## Core Mechanics

* **Seeded murder investigation** — a new game secretly picks one of nine suspects as the killer; evidence can eliminate suspects without ever eliminating the real killer.
* **Route-based evidence** — Razzle, Madeline, Winston, Dhampir, and Nicky each run a distinct investigation route (appearance, lab evidence, interrogation, crime-scene details, and records/alibis) with first, third, and sixth visits.
* **Ulysses evenings** — visiting all six daytime characters once unlocks a sixth-evening cross-report reveal from Ulysses that clears the remaining innocent suspects.
* **Deduction notebook** — tracks remaining suspects, eliminated names, and discovered clues; a companion notepad holds free-form player notes in the save file.
* **Interactive minigames** — every route and the Ica social route has its own minigame: I-Spy, height memory, a board game, cards, an eating contest, a prank, a staring contest, a centrifuge test, memory matching, and an interrogation "pressure" game.
* **Day Seven finale** — the last day of the investigation week has its own dedicated flow separate from the daily route loop.
* **Gallery and replay** — an unlockable gallery plus standard save/load, preferences, and history screens.

## Project Structure

* `game/` — root scripts: intro/day-loop flow (`script.rpy`), investigation data and logic (`investigation.rpy`), route state, minigames, save/context handling, and options.
* `game/screens/` — screen-language UI: menus, dialogue, choice, notebook, save/load, and per-minigame screens.
* `game/optional files/` — gallery, mobile input, confirm-action, and other supporting screens.
* `docs/` — design references, including `route-reveals.md` (per-killer route outcomes) and implementation guides.

See the [@ id="/Pages/Private/GDD/GDD - Overview.md" label="GDD - Overview"] and [@ id="/Pages/Private/GDD/GDD - Features.md" label="GDD - Features"] pages for the full game design documentation.

## Authors

* Grayson ("TriUnity") Jackson
* Haven ("Rabbit") Herring
* AB ("PoeBeau") Manness

## Coding Conventions

* snakeCase
* Asset Styling = characterVersionEmotionVariation
* Background Styling = placeVersionInverted
* give our artist unmonitored committing powers to main
