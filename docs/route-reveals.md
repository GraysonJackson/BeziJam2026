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

| Seed / killer | Day 1: fingerprint clears | Day 3: remove blood type | Day 6: keep matching power |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | B | Fire |
| 2 — Jermiah | Tucker | O | Ice |
| 3 — Barry | Kyle | O | Ice |
| 4 — Carl | Alan | O | Ice |
| 5 — Tucker | Carl | B | Fire |
| 6 — Edgar | Simon | B | Fire |
| 7 — Simon | Victor | A | Light |
| 8 — Kyle | Barry | A | Light |
| 9 — Alan | Edgar | A | Light |

Madeline's route always progresses from nine suspects to eight, then six,
then three. The Day 1 fingerprint mismatch clears one member of the blood-type
group that Day 3 excludes, so the centrifuge removes exactly two additional
suspects. Day 6 positively retains the complete Fire, Ice, or Light trio. The
Day 4 hand-condition observation and Day 5 clean-versus-messy observation are
subtle player-facing hints and are never added to the notebook.

## Winston — interrogation

| Seed / killer | Day 1: interrogation clears | Day 3: remove temperament | Day 6: remove killing reaction |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Passionate | None |
| 2 — Jermiah | Tucker | Calm | Calculated |
| 3 — Barry | Victor | Passionate | Panicked |
| 4 — Carl | Simon | Passionate | Panicked |
| 5 — Tucker | Carl | Calm | None |
| 6 — Edgar | Alan | Calm | Calculated |
| 7 — Simon | Kyle | Passionate | Calculated |
| 8 — Kyle | Barry | Calm | Panicked |
| 9 — Alan | Edgar | Passionate | None |

## Dhampir — crime-scene evidence

| Seed / killer | Day 1: clear suspect | Day 3: remove injuries | Day 6: keep matching drop |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Scuffed Hands | Missing Hair |
| 2 — Jermiah | Barry | None | Missing Tooth |
| 3 — Barry | Victor | Bruised Knuckles | Ear Chunk |
| 4 — Carl | Tucker | Scuffed Hands | Missing Hair |
| 5 — Tucker | Edgar | None | Missing Tooth |
| 6 — Edgar | Carl | Bruised Knuckles | Ear Chunk |
| 7 — Simon | Kyle | Scuffed Hands | Missing Hair |
| 8 — Kyle | Alan | None | Missing Tooth |
| 9 — Alan | Simon | Bruised Knuckles | Ear Chunk |

Dhampir's focused route always progresses from nine suspects to eight, then
six, then three. Day 6 is a positive identification: retain suspects whose
missing hair, missing tooth, or damaged ear matches the recovered evidence.
The Day 4 reaction and Day 5 build observations are intentionally not added to
the notebook; they are player-facing hints for choosing between the final trio.

## Nicky — records and alibis

| Seed / killer | Day 1: alibi clears | Day 3: remove build | Day 6: remove organization |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Skinny | Messy |
| 2 — Jermiah | Tucker | Average | Clean |
| 3 — Barry | Victor | Brawny | Messy |
| 4 — Carl | Simon | Average | Messy |
| 5 — Tucker | Carl | Brawny | Clean |
| 6 — Edgar | Alan | Skinny | Clean |
| 7 — Simon | Kyle | Brawny | Messy |
| 8 — Kyle | Barry | Skinny | Clean |
| 9 — Alan | Edgar | Average | Messy |

## Implementation names

- Shared single-person clearing: `singleEliminationByKiller`
- Madeline fingerprint clearing: `madelineDayOneEliminationByKiller`
- Madeline blood-type lookup: `madelineFocusedRoutePlan`
- All route definitions: `investigationRoutes`
- Razzle-only height lookup: `razzleFocusedRoutePlan`
- Automatic application and notebook logging: `record_planned_route_reveal(route_id, visit)`

The player-facing reference is the in-game **Suspects** notebook. It crosses out eliminated suspects and lists the exact clue and names removed. The separate **Notes** page is free-form player writing and is saved with the game.
