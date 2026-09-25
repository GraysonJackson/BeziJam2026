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
| 1 — Victor | Barry — Missing Arm | Tall | Brown |
| 2 — Jermiah | Victor — Mole | Short | Black |
| 3 — Barry | Jermiah — Glasses | Average | Blonde |
| 4 — Carl | Tucker — Birthmark | Tall | Brown |
| 5 — Tucker | Edgar — Tattoos | Short | Black |
| 6 — Edgar | Carl — Scar | Average | Blonde |
| 7 — Simon | Alan — Vitiligo | Tall | Brown |
| 8 — Kyle | Simon — Piercings | Short | Black |
| 9 — Alan | Kyle — Eye Patch | Average | Blonde |

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

| Seed / killer | Visit 1: interrogation clears | Visit 3: stress profiles clear | Visit 6: retain reaction category |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Barry and Edgar | Calculated |
| 2 — Jermiah | Tucker | Victor and Kyle | Panicked |
| 3 — Barry | Victor | Jermiah and Simon | No Visible Reaction |
| 4 — Carl | Simon | Victor and Jermiah | No Visible Reaction |
| 5 — Tucker | Carl | Jermiah and Simon | Calculated |
| 6 — Edgar | Alan | Victor and Kyle | Panicked |
| 7 — Simon | Kyle | Victor and Tucker | Panicked |
| 8 — Kyle | Tucker | Victor and Jermiah | No Visible Reaction |
| 9 — Alan | Edgar | Barry and Kyle | Calculated |

Winston's pressure exercise tests every active suspect but formally clears two
individual profiles. Visit 6 is a positive identification: retain the complete
Panicked, Calculated, or No Visible Reaction trio. His Visit 4 clean-versus-
messy behavior and quiet hand-condition observation, followed by the Visit 5
reconstruction, remain player-facing hints and are not entered in the notebook.

## Mixed-route adaptation

The player advances each character by visits, not by the global calendar. A
later Visit 1 or Visit 3 can therefore encounter a suspect already cleared by
another investigator. The shared resolver keeps pure six-visit routes on the
authored tables above. In mixed routes it deterministically selects unused,
killer-safe candidates from the same scene's available evidence. If a complete
attribute category no longer contains two usable suspects, the scene reports
two individually tested profile mismatches instead of making a false category
claim. Formal clues never cross out the killer or repeat an eliminated suspect.

The automated Ren'Py test explores every reachable six-day combination for all
nine seeds. Each triggered Visit 1, Visit 3, or Visit 6 removes exactly one, two,
or three new innocents respectively; Ica visits do not use this notebook system.

### Ulysses one-each synthesis

Ulysses is encountered automatically after every investigation day and is not
a daytime route. Ordinarily he comments on and organizes evidence without
eliminating anyone. There is one exception: visiting each of the six daytime
characters exactly once leaves four suspects after the five investigative
Visit 1 clues. During the sixth evening, a dialogue-based cross-report analysis
records `ulysses_cross_report`, clears the three remaining innocents, and leaves
the seeded killer as the sole suspect. Other inefficient distributions do not
receive a compensating elimination.

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

| Seed / killer | Day 1: alibi clears | Day 3: remove build | Day 6: keep matching hygiene |
| --- | --- | --- | --- |
| 1 — Victor | Jermiah | Skinny | Clean |
| 2 — Jermiah | Tucker | Average | Messy |
| 3 — Barry | Carl | Skinny | Clean |
| 4 — Carl | Simon | Average | Clean |
| 5 — Tucker | Carl | Skinny | Messy |
| 6 — Edgar | Alan | Skinny | Messy |
| 7 — Simon | Alan | Skinny | Clean |
| 8 — Kyle | Barry | Average | Messy |
| 9 — Alan | Barry | Average | Clean |

Nicky's focused mapping always progresses from nine suspects to eight, then
six, then three. Day 1 clears one member of the build group that Day 3 later
excludes. Day 6 positively identifies the attacker's Clean or Messy personal-
hygiene category. The Day 4 hand-condition observation and Day 5 A/B/O plus Rh
reaction are subtle player-facing hints and are never added to the notebook.
Together, those two observations uniquely distinguish the killer in every
possible final trio.

## Implementation names

- Shared single-person clearing: `singleEliminationByKiller`
- Winston single-person clearing: `winstonDayOneEliminationByKiller`
- Winston stress-profile pairs: `winstonDayThreeEliminationsByKiller`
- Madeline fingerprint clearing: `madelineDayOneEliminationByKiller`
- Madeline blood-type lookup: `madelineFocusedRoutePlan`
- Nicky alibi clearing: `nickyDayOneEliminationByKiller`
- Nicky build lookup: `nickyFocusedRoutePlan`
- All route definitions: `investigationRoutes`
- Razzle-only height lookup: `razzleFocusedRoutePlan`
- Automatic application and notebook logging: `record_planned_route_reveal(route_id, visit)`
- Saved reveal snapshots: `recordedRouteReveals`
- Ulysses one-each detection: `ulysses_one_each_strategy()`
- Ulysses cross-report application: `record_ulysses_cross_report_reveal()`

The player-facing reference is the in-game **Suspects** notebook. It crosses out eliminated suspects and lists the exact clue and names removed. The separate **Notes** page is free-form player writing and is saved with the game.
