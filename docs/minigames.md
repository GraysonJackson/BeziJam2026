# Minigames & Gameplay Mechanics Plan

This document lists all the minigames and interactive mechanics sketched out across the planning flowchart in `docs/murder-game-plan-composite.png`. 

It is divided into two main sections:
1. **Ica Route Minigames (Days 1–6)**: The casual hangout/dating minigames branching to the left of the introductory briefing.
2. **Investigation Evidence Minigames (Day 3 & Beyond)**: The specific interactive puzzles and tests written next to detective route blocks.

---

## 1. Ica Hangout Route (Days 1–6)

These minigames represent the hangout activities spent with Ica throughout the week:

### Day 1: Cards
* **Notes in Plan**: `cards`
* **General Idea**: A casual, low-stakes card game (such as poker, speed, or high-card) played with Ica to break the ice and establish her relaxed, slacker personality.

### Day 2: Staring Contest (Fishing Bar Mechanic)
* **Notes in Plan**: `staring contest` (annotated underneath with `clicking bar`, `stardew fishing`)
* **General Idea**: A staring contest against Ica. The gameplay uses a vertical bar mechanic directly inspired by *Stardew Valley* fishing: the player clicks/holds to keep a moving bar balanced over an indicator without blinking.

### Day 3: Three-Player Pawn Race
* **Notes in Plan**: The handwritten `board game` note is implemented as an original, compact pawn race rather than a full recreation of a commercial game.
* **Scene**: Ica and an extremely enthusiastic Winston recruit the player for a three-person game in Winston's office. The dialogue choice happens before the game and establishes whether the player joins nonchalantly, flirts with Ica, or complains about doing actual work.
* **Gameplay**: The player, Ica, and Winston each control one pawn on a short linear track. Each participant holds two small movement cards, chooses or automatically plays one, and bumps any opponent they land on back to the start. Ica and Winston prefer a bump when one is available, then use their largest card.
* **Relationship handling**: The scene dialogue owns Ica's approach points. Completing the minigame only adds the shared small win bonus, preventing the same attitude from being scored twice.
* **Presentation**: All three pawn positions, the full turn order, bump feedback, and the eventual winner must remain visible. Winston is a real competitor who can win, not a commentator standing outside the game.

### Day 4: Eating Competition
* **Notes in Plan**: `eating comp` (annotated underneath with `cheat`, `flirt`, `play fair`)
* **Scene**: Ica has exploited a bulk discount to cover two trays with hot dogs. The player's approach and response to Ica's first gravity-assisted cheat both happen in the normal scene dialogue before the playable contest. The minigame does not ask the player to make either choice a second time.
* **Gameplay**: The contest is a short, finite race with visible trays, stamina, and time. Taking bites is fastest but drains stamina; pacing restores it and still makes a little progress. Both contestants advance on their own, so the scene always reaches a result even if the player stops clicking.
  * **Play Fair / Power Through**: No special trick. The player balances bites and recovery and receives Ica's best dialogue score for matching her casual competitive energy.
  * **Flirt / Make It Weird**: A one-use interruption distracts Ica and slows her pace. Existing affection makes the distraction last longer, but the dialogue remains noncommittal rather than turning into a confession.
  * **Cheat / Get Sneaky**: Ica refuses the player's bad plan to make the food lighter, but the player can later palm one hot dog for a one-use progress boost.
* **Ica's Cheating**: Ica automatically floats hot dogs into the trash during the contest. This is a character beat, not a separate moral system, and her progress visibly reflects every cheat.
* **Relationship handling**: Both dialogue menus own their attitude points. Completing the minigame adds only the shared small win bonus, preventing the selected approach from being scored twice.
* **Outcome**: Win, loss, and withdrawal return to distinct dialogue in the existing Day 4 scene, which continues into the setup for painting Ulysses's office pink on Day 5.

### Day 5: Prank Ulysses
* **Notes in Plan**: `prank Uly`
* **Scene**: The existing dialogue remains the frame: Ica floats Ulysses's furniture out of the way while the player paints his entire office pink. Ulysses returns earlier than expected, creating the stealth section, and opens the office door after the last wall is finished so his written reaction remains intact.
* **Gameplay**: A compact top-down grid shows Ica's desk area, the hall, the paint, the office entrance, three wall sections, Ulysses, and his visible line of sight. The player collects the paint, crosses the hall, enters the office, and paints all three marked sections. Walls block sight, and Ulysses follows the same readable patrol every time.
* **Checkpoints**: Getting caught triggers a short gag and returns the player to the beginning of the current objective. Collected paint and completed wall sections are preserved, there is no retry limit, and Ulysses restarts the same patrol so the route cannot become unwinnable.
* **Approaches**:
  * **Just Paint**: The helpful, nonchalant dialogue option. It receives Ica's best relationship score but no stealth assistance.
  * **Make It Weird**: The flirt dialogue option gives one player-triggered distraction during each objective.
  * **Get It Over With**: The complaining dialogue option maps to the shared `cheat` gameplay ID and gives one brief gravity-assisted cover during each objective. The dialogue remains unchanged and still loses relationship points.
* **Relationship handling**: The opening dialogue owns the approach points. Completing the prank adds only the shared small win bonus, and withdrawal adds nothing.
* **Presentation**: The map uses the project's existing paper, choice-frame, and color styling instead of introducing mismatched art. Keyboard and visible button controls are both provided.

### Day 6: Killer Encounter / Game of Chicken
* **Notes in Plan**: `sees the killer` (annotated underneath with `chicken`)
* **General Idea**: While out with Ica, the duo spots the killer. The scene turns into a tense "game of chicken" or nerve test—holding ground, timing a confrontation, or deciding whether to stand firm or back down.

---

## 2. Investigation Route Evidence Minigames

These minigames appear next to specific character days on the right-hand investigation branch to make evidence gathering and elimination interactive.

### Day 3 — Madeline: Centrifuge Test (`centri test`)
* **Route**: Madeline (Laboratory Evidence)
* **Evidence Block**: `blood type`
* **Notes in Plan**: `centri test` written directly above the block
* **General Idea**: A laboratory centrifuge puzzle where the player balances test tubes and spins blood samples to separate layers, identifying the killer's blood type (A, B, or O) to eliminate suspects.

### Day 3 — Winston: Interrogation Blackjack Stress Test (`blackjack stress`)
* **Route**: Winston (Interrogation Evidence)
* **Evidence Block**: `temperament`
* **Notes in Plan**: `black jack stress` written directly above the block
* **General Idea**: Winston plays a game of blackjack against a suspect during interrogation to monitor their biometric stress responses, bluffing, and reactions under pressure, revealing whether their temperament is *Calm*, *Passionate*, or *Nervous*.

### Day 3 — Nicky: Face-Down Memory Matching (`card down matching`)
* **Route**: Nicky (Records & Alibis)
* **Evidence Block**: `Build`
* **Notes in Plan**: `card down matching` written directly below the block
* **General Idea**: A classic concentration / memory card-matching game where face-down suspect cards, alibi statements, and physical descriptions are flipped two at a time to match details and confirm the suspect's build (Skinny, Average, Brawny).

### Day 3 — Dhampir: Scanner I-Spy Reconstruction (`i spy`)
* **Route**: Dhampir (Crime-Scene Evidence)
* **Evidence Block**: `Victim wounds vs. suspects`
* **Cameo**: Madeline brings and operates a forensic scanner. She is a competent, friendly collaborator rather than a source of complications.
* **General Idea**: Madeline projects the original crime-scene photographs and documented wounds over Enrico's house while Dhampir recreates several possible attack paths. The player searches the projected room for marks that do not belong: contact at the wrong height, residue beneath an undisturbed object, or an injury-producing surface missed by the original investigators.
* **Outcome**: The discovered pattern rules out exactly two additional suspects through the planned `Bruised Knuckles`, `Scuffed Hands`, or `None` injury category. Performance changes follow-up dialogue only; the required evidence is always recovered.
* **Implementation status**: Implemented. The scanner presents nine inspectable room details, with three useful contradictions selected by the seeded injury category. False leads and optional hints only change Dhampir and Madeline's follow-up dialogue; the route evidence is still recovered if the player asks Madeline to finish.
