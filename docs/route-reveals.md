# Evidence Route Writing Reference

Use this sheet when writing the major evidence visits. A seed is the saved killer ID. Each cell states the suspect or attribute value that the scene must rule out.

- Day 1, Day 3, and Day 6 below mean that character's first, third, and sixth visits—not the global calendar day.
- For an attribute value, remove every still-active suspect with that value.
- For a named Day 1 result, clear only that suspect.
- The investigation helper prevents the selected killer from being removed and automatically records the actual removals in the player's **Suspects** notebook.
- Update these tables whenever the corresponding values in `game/investigation.rpy` change.

## Seed key

| Seed | Killer |
| ---: | --- |
| 1 | Victor Veytovi |
| 2 | Jermiah Jones |
| 3 | Barry Baxter |
| 4 | Carl Creek |
| 5 | Tucker Thompson |
| 6 | Edgar Ebbington |
| 7 | Simon Streep |
| 8 | Kyle Kallus |
| 9 | Alan Ashmore |

## Razzle — appearance

| Seed / killer | Day 1: clear unique ID | Day 3: remove height | Day 6: keep matching hair |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah — Glasses | Average | Brown |
| 2 — Jermiah | Tucker — Birthmark | Tall | Black |
| 3 — Barry | Victor — Mole | Short | Blonde |
| 4 — Carl | Simon — Piercings | Short | Brown |
| 5 — Tucker | Carl — Scar | Average | Black |
| 6 — Edgar | Alan — Vitiligo | Tall | Blonde |
| 7 — Simon | Kyle — Eye Patch | Average | Brown |
| 8 — Kyle | Barry — Missing Arm | Tall | Black |
| 9 — Alan | Edgar — Tattoos | Short | Blonde |

Day 6 is a positive identification. Once the witness confirms the killer's
hair color, remove every still-active suspect whose hair does **not** match it.

## Madeline — laboratory evidence

| Seed / killer | Day 1: fingerprint clears | Day 3: remove blood type | Day 6: remove power |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | B | Ice |
| 2 — Jermiah | Tucker | O | Light |
| 3 — Barry | Victor | B | Light |
| 4 — Carl | Simon | A | Light |
| 5 — Tucker | Carl | A | Ice |
| 6 — Edgar | Alan | O | Ice |
| 7 — Simon | Kyle | B | Fire |
| 8 — Kyle | Barry | A | Fire |
| 9 — Alan | Edgar | O | Fire |

## Winston — interrogation

| Seed / killer | Day 1: interrogation clears | Day 3: remove temperament | Day 6: remove killing reaction |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Passionate | Calculated |
| 2 — Jermiah | Tucker | Calm | None |
| 3 — Barry | Victor | Passionate | Panicked |
| 4 — Carl | Simon | Passionate | Calculated |
| 5 — Tucker | Carl | Calm | None |
| 6 — Edgar | Alan | Calm | Panicked |
| 7 — Simon | Kyle | Passionate | Calculated |
| 8 — Kyle | Barry | Calm | None |
| 9 — Alan | Edgar | Passionate | Panicked |

## Dhampir — crime-scene evidence

| Seed / killer | Day 1: remove power | Day 3: remove injuries | Day 6: remove unique drop |
| --- | --- | --- | --- |
| 1 — Victor | Ice | Scuffed Hands | Missing Tooth |
| 2 — Jermiah | Light | None | Ear Chunk |
| 3 — Barry | Light | Bruised Knuckles | Missing Hair |
| 4 — Carl | Light | Scuffed Hands | Missing Tooth |
| 5 — Tucker | Ice | None | Ear Chunk |
| 6 — Edgar | Ice | Bruised Knuckles | Missing Hair |
| 7 — Simon | Fire | Scuffed Hands | Missing Tooth |
| 8 — Kyle | Fire | None | Ear Chunk |
| 9 — Alan | Fire | Bruised Knuckles | Missing Hair |

## Nicky — records and alibis

| Seed / killer | Day 1: alibi clears | Day 3: remove build | Day 6: remove organization |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Skinny | Messy |
| 2 — Jermiah | Tucker | Average | Clean |
| 3 — Barry | Victor | Brawny | Messy |
| 4 — Carl | Simon | Skinny | Messy |
| 5 — Tucker | Carl | Average | Clean |
| 6 — Edgar | Alan | Brawny | Clean |
| 7 — Simon | Kyle | Skinny | Messy |
| 8 — Kyle | Barry | Average | Clean |
| 9 — Alan | Edgar | Brawny | Messy |

## Implementation names

- Shared single-person clearing: `singleEliminationByKiller`
- All route definitions: `investigationRoutes`
- Razzle-only height lookup: `razzleFocusedRoutePlan`
- Automatic application and notebook logging: `record_planned_route_reveal(route_id, visit)`

The player-facing reference is the in-game **Suspects** notebook. It crosses out eliminated suspects and lists the exact clue and names removed. The separate **Notes** page is free-form player writing and is saved with the game.
