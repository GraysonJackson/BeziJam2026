# Date and Deduce: implementation guide

> Historical first-pass guide. The active follow-up is [implementation_guide_round_2.md](implementation_guide_round_2.md), with status in [implementation_progress_round_2.md](implementation_progress_round_2.md). Do not treat this older checklist as the remaining implementation queue. Approved canon stays in `audit_decisions.md`.

Prepared from the September 27, 2026 conversation audit. This document preserves all **234 findings**, using matching IDs A001–A234. It turns criticism into bounded work, checks, and questions. It is a handoff for an implementing model; creating this guide did not change the game.

## Start here: instructions to the implementing model

Improve the current game using this guide. Read the relevant source before changing it. Some findings are confirmed code defects; others are editorial judgments, questions about canon, or unfinished production work. A finding is not permission to invent lore, reverse a locked decision, or rewrite the whole game.

**The creator wrote the introductory recruitment scene and the Day One briefing. Those scenes are the primary standard for the game's writing. Match their vocabulary, cadence, bluntness, humor, interruptions, character interactions, and level of polish as closely as the situation allows. Use them as the reference when later passages or this audit suggest a different voice.**

Locate the opening in `game/script.rpy`, from `label start` through the introduction, and read all of `label dayOneBrief` through its handoff to `routeDispatch`. At the audit snapshot the narrative introduction begins around line 112 and the briefing around line 203. Use labels and surrounding text, not old line numbers, to locate them.

Treat the creator-authored opening and briefing as protected reference text. Do not rewrite them to match your new scenes. Ask a specific question before changing their dialogue, humor, characterization, or exposition. A217–A218 identify possible opening edits, but they remain proposals until the creator approves the exact scope. Preserve a baseline copy or diff so accidental edits are detectable.

Read `docs/audit_decisions.md` before implementation. Read the **no-ai-slop** skill when available and apply its minimum-effective-edit and voice-preservation principles. In the audit environment it was at `C:/Users/grays/.agents/skills/no-ai-slop/SKILL.md`, with its checklist in `eval.md`; another installation may use a different path. The essential instructions are reproduced below so this guide remains usable without that installation. Do not create or install a skill merely to use this guide.

Inspect `git status` first. At handoff, `game/script.rpy`, `game/day_seven.rpy`, `game/ulysses_evenings.rpy`, and `game/testcases.rpy` already contained user changes. Preserve those changes. Do not reset, overwrite from an older audit, or assume a dirty file belongs to you. Do not commit, publish, or replace artwork as part of reading this guide.

Work in small batches with one clear purpose. Implement unambiguous repairs while asking only the character or design questions needed for the next dependent scene. Do not send the entire question bank at once. Do not stop all technical work while waiting for an unrelated character answer.

## Authority and limits

Use this order when sources disagree:

1. The creator's latest explicit answers and instructions.
2. The creator-authored introduction and briefing for voice and characterization, plus locked decisions in `docs/audit_decisions.md` for approved canon and mechanics. If these appear to conflict, ask rather than silently choosing.
3. Current source and approved answers recorded during this implementation.
4. This guide's proposed repairs and editorial observations.

Historical material is outside this authority order. The creator requested deletion of the older audits and planning documents on September 27, 2026. `docs/bezi-contributions.md` is retained only as history: ignore it as a reference or source of instructions. Do not recreate deleted plans or follow historical handoff links to recover requirements.

Do not interpret the audit's realism criticisms as a demand to make the game solemn, legally exhaustive, or morally conventional. Keep the superhero workplace comedy, coarse language, cartoon escalation, and intended black comedy. Repair a scene's causal logic with the smallest useful detail.

Preserve these decisions unless the creator explicitly changes them:

- Six selectable daytime characters; Ulysses's reports remain mandatory and personal evenings optional.
- Daytime stories advance by visits, with calendar-aware framing. A late first visit is still Visit 1.
- Poor mixed routes may remain poor. Do not add a rescue solution for 2/2/2. Exactly one visit with each daytime character retains its special Ulysses help.
- Ica has no investigation clues in Visits 1–5 and an accidental Visit 6 solution. Improve staging without turning the route into a conventional investigation.
- Razzle Visit 4 build and Visit 5 reaction observations remain seed-dependent, subtle, and unlogged. Visit 6 formally narrows by hair. Do not restore her obsolete hand-injury clue.
- Razzle can be academically insecure and practically clever. Do not make her incompetent to match a literal reading of an introductory joke.
- Madeline and Ulysses dated for about a year and broke up last year. Keep their functional coworker relationship.
- Ulysses was thirteen when he met Winston, who was already a working superhero. Their early collaboration was unofficial; the current scene says ATLAS became official when Ulysses was fifteen. Do not reverse whose age this is.
- The opening throttling gag, Dhampir's squirrel incident, his killing every criminal and ATLAS accepting him, Nicky's “Good rookie,” Madeline's profanity, Ica's modern-feeling slang, and Razzle's available “hot and bothered” pun are intentional.
- Replace Ica's board-game copyright joke with an in-world off-brand name. Differentiate the “not a date” setups: Winston can acknowledge the date-like meal; Mads may keep denying mini-golf is a date. These directions are already approved.
- Freddy appears only in the introduction and must clearly say goodbye permanently. Do not solve A218 by promising a return.
- Civilian technology fits 1996; ATLAS/Madeline technology may be futuristic.
- Rollback stays disabled. History stays at 250 lines unless separately authorized. Five manual save slots per page remain.
- Approximate excellent-play romance targets: Razzle/Winston three visits; Nicky/Ica four; Madeline/Dhampir/Ulysses five. Friendship normally requires two visits. These targets must be tested through actual attainable choices.
- Ulysses's professional trust and romantic interest remain separate. Explicit romantic actions require player choice.
- Wrong accusation still costs the player their job. Failure relationships need not be uniformly cruel.
- The culprit speaks live. Confession variants use temperament, reaction, and habits with one common underlying motive; do not invent nine unrelated plots.
- Title art is deferred; other missing art/audio is production work, not permission to generate substitute assets. Ica's board does not require new artwork.

## Writing rules, including no-ai-slop

The reference scenes use direct second-person narration, colloquial dialogue, stretched words and capitalization for performance, interruptions, profanity, and jokes caused by characters getting in one another's way. Ulysses can lose his temper; Madeline can be rude and excitable; Nicky can speak casually; a competent person need not sound like a training manual. These are observations from the source, not a license to exaggerate every trait in every line.

Before editing a character, collect three short examples of their speech from the reference scenes and note what each demonstrates. Compare the revised scene against those examples. Do not copy catchphrases into every response.

Use these rules for new and revised prose:

- Keep strong existing lines. Make the smallest edit that fixes the specific problem.
- Preserve the author's roughness, jokes, slang, bluntness, fragments, contractions, profanity, and varied rhythm when they carry voice. Correct accidental errors without making everyone formal.
- Let characters act, interrupt, dodge, argue, and make mistakes. Avoid replacing this with uniformly insightful reassurance.
- Show an emotional change through a concrete action or response. Cut narration explaining its meaning when the scene already conveys it.
- Do not make every serious scene end in silence, mutual understanding, or a polished maxim.
- Avoid repeated “not X, but Y” constructions, artificial mic-drop endings, generalized therapy language, fake profundity, filler, and long strings of interchangeable compliments.
- Prefer specific behavior over abstract claims such as “trust deepens” or “the moment becomes meaningful.”
- Do not mechanically ban ordinary words, em dashes, or sentence shapes from character dialogue. The creator's demonstrated voice takes priority over an editing checklist.
- Do not add sensory paragraphs, paperwork, food, or cleanup merely to lengthen a scene. Keep them when they create a joke, decision, clue, or character change.
- Do not force a vulnerable disclosure because it is the scheduled fourth or fifth visit. Establish a trigger, sufficient trust, a guarded alternative, and a later consequence.
- Preserve uncertainty when evidence is uncertain. Do not make the narration declare an inference true solely because the hidden killer data says so.
- Do not write new protagonist attraction, gender, touch, promises, or personal history as though the player chose them.

Before accepting a rewrite, ask: Would these people sound at home beside the creator's briefing dialogue? Did I keep the character's edge? Did I change canon? Did I explain a joke or emotion that already worked? Could another character say this response unchanged? Does every branch remember what happened?

If a skill rule would flatten the creator's style, preserve the style. If a new character reaction is uncertain, ask a short scenario question from the bank below. Do not infer that any source was AI-written from stylistic patterns.

## How to implement and report progress

Use a progress ledger such as `docs/implementation_progress.md` when implementation begins. Do not mark this guide's checkboxes complete merely because a proposal has been written. For each ID record: status, current evidence, changed files/labels, creator decision if needed, validation performed, and remaining limitation.

Status meanings:

- **FIX**: A bounded repair with an existing intended behavior. Reproduce against current source, then implement without asking routine permission.
- **EDIT**: Editorial work within established canon. Use the style rules; ask only where the reaction or meaning is uncertain.
- **ASK**: A canon, policy, scope, or major design choice needs the creator's answer before dependent implementation. Continue unrelated work.
- **VERIFY**: A risk or judgment requiring reproduction or inspection; do not claim it is a confirmed bug until checked.
- **DEFER**: Production or separately approved scope. Document the need and dependency; do not manufacture completion.

The checklist shows initial classification, not execution status. All items start unchecked. A004–A005 are reproduction cases for A003, not separate architectures. Several later items deepen earlier findings; cross-reference the same fix rather than applying duplicate rewrites.

For each batch:

1. Read the relevant full scene, callers, state helpers, report, ending, and rules screen.
2. Describe the exact failing path or editorial problem and the intended change in plain language.
3. Check locked decisions and any creator answers. Ask 3–5 related questions at most when needed.
4. Fix the source with the smallest coherent change. Use explicit saved state for consequential events; do not substitute affection thresholds for facts.
5. Update every dependent report, callback, notebook entry, and ending affected by that event.
6. Run targeted checks. Use real engine tests for engine behavior and label execution where possible; a mocked Python harness does not establish screen or save/load behavior.
7. Read changed dialogue aloud or perform an equivalent cadence pass against the introduction. Inspect the full diff for unrelated edits.
8. Update the ledger and report IDs completed, checks passed, questions pending, and next batch. Do not declare the whole guide complete while ASK/VERIFY/DEFER items remain unresolved; report their separate status honestly.

### Suggested order

| Phase | Work | Gate before proceeding |
| --- | --- | --- |
| 0 | Read canon/style, preserve dirty files, establish baseline and ledger | No game changes yet; identify missing answers |
| 1 | A001–A002; A003–A005; A009; necessary regression tests | Allowed paths no longer crash or block assistance; evidence categories agree |
| 2 | A006–A008, A013–A034, A112–A113; evidence provenance and finale | Creator answers world/puzzle questions; no invented proof |
| 3 | A010–A012, A069–A070, A095–A098, A121–A128, A129–A142, A175, A209; continuity ledger | Consequential events survive choices, reports, save/load, endings |
| 4 | One character route at a time, including its reports and endings; A035–A144 | Approve uncertain reactions before large prose changes |
| 5 | Remaining A145–A182; game interactions and rules | Outcomes, assists, withdrawals, and explanations match |
| 6 | A183–A203; UI/accessibility and production inventory | Inspect representative full/long/late states, not only opening screens |
| 7 | A204–A215; endings and attainable scoring | Test actual routes, direct friendship decision if approved |
| 8 | A216–A234; copyedit, docs, cleanup, full regression | No protected-text drift; unresolved production/design items explicitly listed |

Phases can overlap when independent. Fix a report alongside its underlying event instead of waiting for its nominal phase. Do not perform a project-wide prose rewrite in one batch.

## Source map

| Area | Read together |
| --- | --- |
| Reference voice and daytime routes | `game/script.rpy`; `game/*_route_state.rpy` |
| Evidence | `game/investigation.rpy`; five investigator state files; `docs/route-reveals.md` |
| Ulysses | `game/ulysses_evenings.rpy`; `game/ulysses_evening_state.rpy` |
| Finale | `game/day_seven.rpy`; `game/day_seven_state.rpy`; `game/screens/day_seven_screens.rpy` |
| Minigames | Matching `game/*_minigame.rpy` and `game/screens/*_minigame.rpy`; `game/ica_minigame_state.rpy`; `game/screens/minigame_rules.rpy` |
| General UI | `game/screens/`; `game/styles.rpy`; `game/options.rpy`; `game/image_definitions.rpy` |
| Tests | `game/testcases.rpy`; `tests/screenshots/` |
| Current decisions and tasks | `docs/audit_decisions.md`; this guide. Earlier audit and planning Markdown files were removed; ignore `docs/bezi-contributions.md` for implementation. |

At audit time Ren'Py lint passed. Existing model validators passed in an isolated logic harness. Additional state enumeration found 31 category/value mismatches among 19,270 deduplicated evidence transitions across all nine killers. This is baseline evidence, not a claim that every engine path or ending was played. Stored screenshots were inspected; live engine UI testing was not completed. Recheck the current version before carrying those claims forward.

## Complete implementation checklist: A001–A234

### Blockers and direct contradictions

- [x] **A001 [FIX] Skipping Ulysses Evening Three breaks Evening Four.** Initialize the tension state safely and track whether the conversation occurred. Fix both the missing-variable error and the false recollection. Pass: skip Day 3 personal time, stay Day 4; no crash and no invented prior conversation. See A129–A130.
- [x] **A002 [FIX] Razzle's assistance action leaves her game active.** Separate assisted completion from the normal progress requirement. Award the correct planned clue once, set assisted quality, close the interaction, and continue. Pass: assistance and Escape work at zero and partial progress without duplicate clues or false perfect praise.
- [x] **A003 [FIX] Mixed-route clue categories disagree with eliminated suspects.** Repair `get_planned_route_reveal` and consumers so adapted category values, scope, descriptions, and eliminated IDs agree. Do not merely hide the mismatch in the notebook. Pass: all reachable evidence transitions preserve the killer and support every named category; individual exclusions have individual wording.
- [x] **A004 [FIX] Reproduce the Carl/Razzle/Madeline mismatch.** With killer 4, visit Razzle three times then Madeline three times. The old result says type O but eliminates Victor and Edgar, type A. Pass: the revised clue, lab display, dialogue, report, and eliminations agree. This is an A003 regression case.
- [x] **A005 [FIX] Cover the other mixed-route category failures.** Killer 1: Nicky/Dhampir/Madeline/Razzle/Razzle/Razzle previously said Tall but removed Average; Madeline/Dhampir/Nicky/Nicky/Razzle/Nicky said Skinny but removed Average. Killer 3: Winston three times, Dhampir three times said Bruised Knuckles but removed Scuffed Hands. Pass: all four investigator categories stay truthful.
- [x] **A006 [FIX] Wrong-accusation feedback reads the hidden answer key.** Generate criticism from evidence actually available to the player, not the first difference from `suspectAttributes[killer]`. Pass: an undiscovered mole cannot become the stated contradiction. Insufficient evidence must be acknowledged without reversing the locked failure outcome; consult QW06.
- [x] **A007 [ASK] Final profiles imply innocent suspects committed the murder.** Decide what neutral information “Reaction After Killing” and “Trace Left at Scene” are supposed to represent. Ask QW04 before changing the puzzle model. Pass: profiles distinguish known background facts from observations of this crime and undiscovered facts.
- [x] **A008 [ASK] The one-each deduction lacks a demonstrated logical bridge.** Preserve the breadth reward but design a real additional comparison or corroboration with the creator. Ask QW05. Pass: the player can explain why one of four survivors fits without reading the hidden killer or guessing through retries.
- [x] **A009 [FIX] Nicky's identical cards require different hidden matches.** Add meaningful visible identity/provenance or accept genuinely interchangeable semantic answers. Pass: Carl and Alan's identical narrow-frame descriptions cannot cause a visually correct pairing to be penalized. Test all seeds and adapted reveals.
- [x] **A010 [ASK] Ignoring Madeline's stop request is only a point penalty.** Ask QM01 for the lasting consequence and any repair path. Track what the player did independently of affection. Pass: response, later intimacy, report, and ending honor that decision; ordinary positive points cannot silently erase the event.
- [x] **A011 [FIX] Winston's second report says he ignored calls he answered.** Track and report the actual call-handling sequence and final choice. Pass: no branch says he answered none when earlier calls were answered; report choices cannot earn honesty credit for false claims.
- [x] **A012 [ASK] Ica's culprit escapes, then supposedly never escaped.** Ask QI05/QW06 whether an offscreen capture or different final wording is intended. Pass: scene, report, and Day Seven describe one consistent escape/capture timeline without removing the accidental solution.

### Investigation and story structure

- [x] **A013 [ASK] Enrico has little identity beyond being the victim.** Ask QW01 for a few concrete facts and a relevant relationship. Integrate them into existing evidence or banter. Pass: players can say who he was and why his death matters without a new exposition lecture.
- [x] **A014 [ASK] The confession never specifies what Enrico discovered.** Ask QW02 for the common underlying wrongdoing. Seed it and resolve it in temperament-based admissions. Pass: all nine culprits retain the approved common motive and the ending answers what was being exposed.
- [x] **A015 [ASK] Suspects function mainly as attribute rows.** Agree a small scope for distinct ties, lies, and opportunities. Pass: approved suspect details appear through existing scenes, stay compatible with every seed, and do not become nine unrelated confession plots.
- [x] **A016 [ASK] Killer randomization changes values more than drama.** Ask QW03 how much seed-dependent narrative variation is wanted. Pass: any added variation changes a concrete observation, exchange, or interpretation and remains within jam scope; do not promise nine complete stories.
- [x] **A017 [EDIT] Non-implication is mistaken for innocence.** Audit exclusions such as the paramedic shoeprint. Add the missing case-specific reason the suspect is excluded, or revise the evidence with creator input. Pass: removing an incriminating trace alone is not described as an alibi.
- [x] **A018 [EDIT] Fingerprint exclusion lacks a necessary premise.** Establish why the relevant print must belong to the murderer and why comparison is reliable in this case. Ask if a new fact is needed. Pass: the explanation supports exclusion without a long forensic lecture.
- [x] **A019 [EDIT] Removable or concealed features are treated as absolute exclusions.** Review glasses, tattoos, piercings, and eye-patch testimony. Add approved corroboration or revise the inference. Pass: “not visible” does not silently mean “the suspect cannot have done it.”
- [x] **A020 [EDIT] Witness certainty substitutes for reliability.** Distinguish confidence from viewing conditions and independent support. Pass: each decisive visual clue has a stated opportunity to observe, not merely a confident witness.
- [x] **A021 [ASK] Supernatural strength invalidates and then enables body inference.** Ask QW07 for the setting's limits. Pass: Dhampir's build inference and Nicky's warning can both be true under a stated, consistent condition.
- [x] **A022 [ASK] General cleanliness acts as a deterministic murder signature.** Agree the specific evidence connecting personal habits to this scene. Pass: Nicky's final deduction does more than equate a tidy person with tidy crime handling.
- [x] **A023 [ASK] Temperament and post-crime behavior act like fixed forensic properties.** Resolve with QW04/QW07. Pass: ordinary personality, observed reaction, and this crime's evidence are separate concepts; rules are understandable before accusation.
- [x] **A024 [EDIT] Anti-stereotyping dialogue conflicts with category-based deductions.** Keep power/personality tendencies tentative unless approved canon says otherwise. Pass: the story never calls a stereotype insufficient and then uses it alone as proof.
- [x] **A025 [ASK] The protagonist's intuition is underintroduced.** Ask QW08 about its existence, limits, and sensations. Add the approved introduction outside protected text where practical. Pass: the first use needs no unexplained new ability.
- [x] **A026 [ASK] Intuition shifts between hint and hidden factual knowledge.** Set one rule with QW08 and apply it to Winston and cross-report help. Pass: intuition cannot reveal uncollected exact attributes while dialogue calls it a minor nudge.
- [x] **A027 [ASK] The deadline lacks a persuasive cause.** Ask QW09 why a decision is mandatory after a week. Seed the answer without rewriting the creator's briefing unapproved. Pass: the player understands the constraint and why further investigation is unavailable.
- [x] **A028 [ASK] Unselected investigators appear to stop making useful progress.** Ask QW10 how independent work should appear. Pass: small updates make the team active without adding unapproved eliminations or rescuing poor route distributions.
- [x] **A029 [FIX] A correct guess is described as a complete evidence chain.** Branch finale wording by actual evidence and observations collected. Pass: 2/2/2 success can remain possible but cannot claim unvisited scenes were investigated.
- [x] **A030 [ASK] The finale supplies the reasoning after the player selects a name.** Ask QW11 whether a supporting-evidence choice is desired. Pass: any new deduction interaction uses available information and preserves existing success/failure policy; avoid an extra quiz without approval.
- [x] **A031 [ASK] Wrongful accusation consequences occur before a clear causal sequence.** Agree when accusation becomes official, detention occurs, and the killer is warned. Pass: one readable timeline explains the consequence rather than retroactively inventing actions.
- [x] **A032 [ASK] Ulysses can disprove the accusation immediately but cannot review a draft.** Clarify the institutional procedure while retaining dismissal. Pass: the failure is causally coherent and leadership's role is acknowledged as the creator intends.
- [x] **A033 [EDIT] Provisional clues become decisive without explaining why.** Distinguish “insufficient alone” from “unreliable.” Pass: a player can combine soft observations legitimately without being told to disregard uncertainty previously emphasized.
- [x] **A034 [VERIFY] Attribute correlations make clues redundant or exploitable.** Map hair, injury, tissue, and other correlations across all seeds. Do not rebalance the grid casually. Pass: document intentional redundancy and ask before any table change; rerun route solvability if changed.

### Shared writing problems

- [x] **A035 [EDIT] Emotional arcs repeat the same work/food/misunderstanding/reassurance sequence.** Map each route's emotional turns before editing. Pass: each route has a distinct conflict and change; variation comes from character behavior rather than renamed food or locations.
- [x] **A036 [EDIT] The player acts as a portable therapist.** Replace interchangeable diagnoses and reassurance with practical choices, disagreement, humor, or specific help. Pass: character questions and answers concern the actual scene, without sanitizing the cast.
- [x] **A037 [EDIT] Romantic voices converge.** Use the reference scenes and character answers to vary attraction responses. Pass: a response cannot move unchanged between most cast members; literal safety uses of “careful” remain.
- [x] **A038 [EDIT] Obvious reassurance too reliably buys intimacy.** Include competing reasonable responses and consequences tied to the individual. Pass: warmth develops through remembered behavior, not only selecting the most affirming sentence.
- [x] **A039 [EDIT] Menus repeat supportive/flirtatious/gratuitously cruel options.** Replace weak hostile choices with plausible caution, skepticism, impatience, or dry humor. Pass: at least two choices represent reasonable but distinct priorities where the scene supports them.
- [x] **A040 [EDIT] Accurate criticism loses affection while flattery wins.** Inspect each such choice in context; ask the creator how defensiveness should persist. Pass: professional correctness, delivery, and personal compatibility are not automatically treated as the same score.
- [x] **A041 [VERIFY] Trivial preferences carry disproportionate affection weight.** Compare food/music points with trust decisions on attainable routes. Pass: approved minimum-visit targets remain possible and important events cannot be erased by snack optimization.
- [x] **A042 [EDIT] Competence becomes attraction too quickly.** Separate respectful praise from flirtation where appropriate. Pass: professional players receive coherent warmth without narration asserting romantic intent they did not express.
- [x] **A043 [EDIT] Low-affection branches return to the same intimacy.** Write guarded alternatives for disclosures, touch, and comfortable familiarity. Pass: hostile/neutral/warm paths remain playable and differ beyond one response line.
- [x] **A044 [FIX] Preference callbacks are better tracked than major emotional events.** Add explicit state for the events selected in the continuity ledger. Pass: refusals, violations, apologies, gifts, and commitments govern later prose independently of total affection.
- [x] **A045 [EDIT] Narration interprets emotions after showing them.** Remove redundant emotional commentary while preserving the author's direct, sometimes comic narration. Pass: the action or response carries the beat without a second explanatory moral.
- [x] **A046 [EDIT] Quietness is the default serious-scene signal.** Vary scenes through each character's coping and communication style. Pass: important moments can be awkward, noisy, funny, practical, or unresolved where fitting; no mechanical synonym replacement.
- [x] **A047 [EDIT] Everyone adopts the same procedural lecture voice.** Keep necessary facts but phrase them through character-specific priorities and interruptions. Pass: accuracy remains, and the dialogue still resembles the briefing's people.
- [x] **A048 [EDIT] Debriefs repeat lessons already fully explained.** Report the new implication, complication, or missing fact instead of replaying the scene. Pass: mandatory reports remain useful and unique without becoming full summaries.
- [x] **A049 [EDIT] Food theft repeatedly stands in for closeness.** Keep the strongest character-specific instance; diversify others through sharing, asking, trading, noticing, or another approved action. Pass: replacements preserve choices and ownership continuity.
- [x] **A050 [ASK] Interpersonal friction resolves too easily.** Ask QC03 and route-specific questions about disagreements that can survive affection. Pass: selected disagreements have remembered consequences without creating unapproved breakups or moral repudiation arcs.
- [x] **A051 [ASK] The protagonist has little identity beyond pleasing people.** Ask QC01 about intended player definition and expressive scope. Pass: approved viewpoints can recur without forcing biography, gender, attraction, or a single personality.
- [x] **A052 [ASK] Companions learn little about the protagonist.** Agree optional, bounded disclosures or preferences they can remember. Pass: interest responds to something specific the player chose, not invented history.
- [x] **A053 [EDIT] The ensemble loses the briefing's competing personalities.** Improve existing cameos with a small goal or disagreement for each participant. Pass: scenes remain focused and cameos do more than introduce a game or certify competence.
- [x] **A054 [EDIT] Administrative departures become repetitive.** Keep custody facts needed for later logic, but compress redundant packing/signing/cleaning. Pass: scenes end on a useful action, joke, clue, or decision rather than the same checklist.
- [x] **A055 [ASK] The six-visit schedule is too visible.** Vary emotional peaks and scene activity inside the locked evidence schedule. Ask before moving formal reveals. Pass: character arcs differ without changing visit-based progression or clue guarantees.
- [x] **A056 [EDIT] Added aftermath weakens strong scene endings.** Identify the first effective ending and retain later material only if it changes something. Pass: no required state, clue, or meaningful callback is cut for brevity alone.

### Razzle: A057–A068

- [x] **A057 [EDIT] Visits three and four repeat their opening energy.** Compare greetings, player responses, and the first change of subject. Keep the stronger exchange and make the other respond to the previous visit or current task. Pass: the visits do not feel like alternate drafts of the same opening.
- [x] **A058 [EDIT] The fire-hazard insecurity repeats instead of developing.** Track what the early scene establishes and what the Elena scene adds. Give the later scene a new consequence or response. Pass: Razzle has not forgotten an earlier conversation just to repeat its emotional reveal.
- [x] **A059 [ASK] The pizza-shop scene blurs exclusion with reasonable fire precautions.** Ask QR01. Let the scene distinguish dismissive treatment from a practical safety requirement without deciding the creator's intended moral for them. Pass: the employee's observable behavior supports the reaction the scene asks of the player.
- [x] **A060 [ASK] Razzle's fire rules change with the scene.** Ask QR02 about paper, chairs, clothes, food, touching, and kissing. Record the answers before revising contact scenes. Pass: each apparently safe interaction has a consistent explanation, and flame cabs/protected borrowed vehicles remain allowed.
- [x] **A061 [EDIT] Razzle penalizes criticism while delivering her own lesson.** Review the leading questions and affection changes. Preserve defensiveness if intentional, but let the response acknowledge what the player actually said. Pass: disagreement is not rewritten as cruelty merely to justify a penalty.
- [x] **A062 [EDIT] Visits four and five over-explain the bundle's perspective.** Establish the spatial observation once, then use the next scene to test or refine it. Pass: the player can reconstruct the observation without hearing the same explanation twice.
- [x] **A063 [VERIFY] Grainy footage supports implausibly fine hair detail.** Identify exactly what the three frames establish and what remains uncertain. If individual strands are unsupported, use an approved visible silhouette, movement, or other observation. Pass: image quality and inference strength agree; do not invent a new forensic fact without checking the case design.
- [x] **A064 [VERIFY] Wig reconstruction offers fewer meaningful controls than its confident conclusion suggests.** Compare player input with the final claim. Add an approved discriminating step or narrow the claim. Pass: the game does not credit the player with a reconstruction they never performed.
- [x] **A065 [EDIT] “You handle thinking, I handle fire” undermines practical intelligence.** Keep the banter's intent while acknowledging what Razzle actually contributes. Pass: she remains practically clever rather than being reduced to destructive muscle.
- [x] **A066 [FIX] The affectionate celebration offers only two ways to say yes.** Add a friendly decline or defer option with a coherent exit and correct state. Pass: accepting affection does not force accepting this invitation, and declining does not invent hostility.
- [x] **A067 [FIX] Report five repeats a removed hand-against-brick clue.** Match the report and planning notes to the current approved scene. Pass: no report, hint, or deduction relies on an event absent from the route.
- [x] **A068 [FIX] Minigame praise ignores poor performance or assistance.** Branch the response on the actual outcome while preserving required clue delivery. Pass: failure, assistance, and strong play receive believable, distinct reactions.

### Dhampir: A069–A080

- [x] **A069 [FIX] A stated fear of heights is respected temporarily, then ignored on departure.** Remember the stairs/flight choice through the return to Ulysses. Pass: the player is not flown away after declining flight unless a new explicit choice changes that decision.
- [x] **A070 [FIX] Dhampir steals popcorn the player may not own.** Track the purchased snack and no-purchase branch. Pass: each action names something actually present, or a short alternative plays.
- [x] **A071 [ASK] Rooftop reactions are treated as appearance prejudice despite Dhampir's public record.** Ask QD01 about what strangers know and the intended joke. Preserve the locked lethal black-comedy premise. Pass: empathy does not require narration to deny established reasons people might fear him.
- [x] **A072 [ASK] Processing the squirrel incident is treated as a relationship mistake.** Ask QD02 about acceptable surprise, humor, and objections. Pass: reasonable player reactions remain expressible within the creator's tone; do not add a repudiation or redemption arc.
- [x] **A073 [EDIT] Narration repeatedly explains the meaning of Dhampir's casual manner.** Review “practiced,” “not detached,” “not wounded,” and similar interpretation. Keep behavior and his own words where sufficient. Pass: ambiguity is allowed when the scene benefits from it.
- [x] **A074 [ASK] Comfort with death and trauma-driven efficiency need a consistent relationship.** Ask QD03. Distinguish what he believes, what he claims, and what his habits reveal. Pass: later vulnerability complicates his outlook without accidentally declaring the earlier characterization false.
- [x] **A075 [FIX] Visits four and five both ask who trained him as if it is new.** Make the later question follow the earlier answer, with a fallback only if that answer could actually be skipped. Pass: neither participant forgets a conversation the player saw.
- [x] **A076 [ASK] Manison appears without enough context.** Ask QD04 who this is and how much the player should understand. Add only the minimum approved identification. Pass: the reference feels intentionally withheld or understandable, rather than an unexplained drafting remnant.
- [x] **A077 [VERIFY] A photographed evidence marker implies a recovered item that was never found.** Establish what the marker identifies: a location, trace, or recovered object. Pass: dialogue, image description, inventory, and report agree.
- [x] **A078 [ASK] Photos from “during” the attack have no established source.** Ask QW12 about surveillance, witnesses, or reconstruction. Pass: the scene states a plausible approved source and does not silently turn reconstructed images into direct evidence.
- [x] **A079 [FIX] An item in Dhampir's palm is described as still beside a baseboard or radiator.** Separate the object's description from its discovery location. Pass: every variant reads naturally both when discovered and when held or reported.
- [x] **A080 [EDIT] Heartbeat narration assumes attraction after professional choices.** Gate romantic interpretation on an appropriate explicit signal, or describe an ambiguous physical response without naming desire. Pass: the professional route does not assign attraction to the protagonist.

### Mads: A081–A092

- [x] **A081 [ASK] The helmet's required disinhibition feels engineered to force a confession.** Ask QM01–QM02 about the device's purpose, limits, and Mads's reason for accepting the test. Pass: the activity makes sense before its emotional payoff, and any revised mechanism is approved canon.
- [x] **A082 [FIX] A player who proposes ignoring the limit still receives control without a reset.** Give Mads a response and require agreement to the operating boundary, or use an approved alternative operator/outcome. Pass: she does not entrust the device to someone who has just refused its condition without acknowledging the risk.
- [x] **A083 [FIX] Anger and embarrassment collapse into the same warm flirtation after different conduct.** Separate respectful participation, a mistake, and deliberate boundary violation; coordinate with A010. Pass: an unresolved violation cannot flow directly into an affectionate version of the scene.
- [x] **A084 [FIX] The report rewards the claim that the player stopped even when they did not.** Read the actual cutoff state. Pass: false reporting is not treated as a true action or awarded the same trust; any deception response follows approved characterization.
- [x] **A085 [FIX] The first lab report says the player passed after contaminating the slide.** Preserve the result through the debrief. Pass: the report describes the observed outcome and any recovery accurately.
- [x] **A086 [EDIT] Repeated “idiot,” “dumbass,” and efficiency dismissals flatten Mads.** Keep profanity and sharpness, but give her insults specific targets, varied intent, and occasional different reactions. Pass: the edit preserves the author's abrasive voice rather than making her polite.
- [x] **A087 [EDIT] Mini-golf narration over-explains safe failure.** Let the scorecard, her choices, and the interaction carry more of the point. Pass: the emotional shift remains understandable without a paragraph translating it into a lesson.
- [x] **A088 [VERIFY] The blue-ice-cream response and affection penalty imply different reactions.** Decide whether she is intrigued, annoyed, or both; ask QM03 if that changes her characterization. Pass: the text makes the scored reaction credible rather than surprising the player after a seemingly positive exchange.
- [x] **A089 [FIX] The prototype scene ends and then resumes with six minutes remaining.** Choose a single chronology and move departure text after the actual final exchange. Pass: elapsed time, device state, and everyone's location stay consistent.
- [x] **A090 [VERIFY] “Watch” and “document” choices promise roles the scene barely delivers.** Give each role a small observable responsibility or describe the choice more modestly. Pass: the later account matches what the protagonist did.
- [x] **A091 [EDIT] “Recalculated eleven times” becomes flirting even on a professional path.** Keep a professional explanation or gate the romantic framing. Ask QM04 about how consciously she signals interest. Pass: competence and gratitude do not automatically become mutual attraction.
- [x] **A092 [ASK] The ending repeats the earlier mini-golf-and-ice-cream date without enough change.** Ask QM05 what she now does differently. Reuse the setting if meaningful, but pay off a specific earlier interaction. Pass: the ending shows development instead of replaying visit two.

### Nicky: A093–A106

- [x] **A093 [ASK] Pheromone sensing alternates between stress detection and reliable lie detection.** Ask QN01 for its exact limits and check existing decisions. Pass: stress, deception, attraction, and inference remain distinct wherever the ability is used.
- [x] **A094 [EDIT] Nicky's nose assigns the protagonist feelings they did not choose.** Preserve her ability within approved limits, but allow uncertainty, correction, or explicitly chosen attraction. Pass: her interpretation does not silently overwrite player intent.
- [x] **A095 [FIX] The selected music is replaced by Backseat Royalty in every departure.** Carry the selection through, or establish an explicit change in the scene. Pass: each menu branch has a matching playback description.
- [x] **A096 [VERIFY] Stored vinyl appears to become bike audio without a transition.** Identify the playback format and available equipment under the 1996/ATLAS rules. Pass: the same recording can plausibly be played where the scene says it is played.
- [x] **A097 [FIX] Visit six assumes a loan after branches that gifted a new album or only shared a title.** Track the actual exchange and ownership. Pass: return, thanks, and callbacks fit every visit-two branch.
- [x] **A098 [FIX] Report two assumes a physical gift even when none was exchanged.** Use the same state as A097. Pass: the debrief does not manufacture an object or gesture.
- [x] **A099 [EDIT] The headphones exchange offers flirtation or hostility but no ordinary boundary.** Add a straightforward, non-romantic response. Pass: asking for personal space does not require insulting Nicky.
- [x] **A100 [ASK] Another strangers-staring scene repeats an ensemble-wide insecurity pattern.** Ask QN02 whether her LAPD/ATLAS position offers a more specific tension. Pass: any replacement expresses her own problem without inventing institutional history.
- [x] **A101 [EDIT] Visit four and its report repeat antenna praise and fries beats.** Keep the most effective instance of each and make the report add information. Pass: the same emotional exchange is not delivered twice in one day.
- [x] **A102 [ASK] The suspicious chain-of-custody correction raises a threat that never resolves.** Ask QN03 whether it is a real lead, a red herring, or routine correction. Pass: the player receives an appropriate resolution or clearly bounded uncertainty.
- [x] **A103 [FIX] The scene's elapsed time expands while the report still claims seven minutes.** Audit all activities between arrival and departure. Pass: the reported duration matches the revised sequence, or is clearly identified as one part of it.
- [x] **A104 [VERIFY] Three weak cleanliness observations are treated as strong proof because there are three.** Apply A022's evidence rules: check independence and alternative explanations. Pass: confidence rests on what each observation establishes, not merely its count.
- [x] **A105 [EDIT] Rejection warns the player to “take no properly” before any pushback occurs.** Make the default refusal address the actual respectful request; reserve corrective language for demonstrated misconduct. Pass: the scene does not invent a bad response for the protagonist.
- [x] **A106 [ASK] Off-duty hobbies do not yet reveal a distinctive personal decision.** Ask QN04 what Nicky wants, avoids, or risks outside work. Pass: added depth grows from an approved choice or tension, not a pasted-in confession.

### Winston: A107–A116

- [x] **A107 [FIX] The scene tells someone to unplug a pager.** Use an action appropriate to the established device, such as switching it off, unless a charger or dock is explicitly present. Pass: the physical action makes sense in context.
- [x] **A108 [ASK] Sobriety introduces an unexplained power-negation rule.** Ask QV01 about the role of alcohol, control, and inhibition. Pass: earlier scenes and later tactics obey one approved rule without adding a medical explanation the author did not intend.
- [x] **A109 [EDIT] The emergency-brake explanation gives away the later disclosure early.** Decide what the early glimpse establishes and what the later scene genuinely adds. Pass: later intimacy changes the player's understanding instead of repeating the same full explanation.
- [x] **A110 [ASK] Protective witness dampening and rejection of coercion need a clear distinction.** Ask QV02 about consent, urgency, and what his power changes. Pass: his line in the sand is understandable and consistently applied, including exceptions he consciously makes.
- [x] **A111 [EDIT] Blackjack exchanges lose the suspect's personality.** Tailor a small number of responses to the current suspect's temperament and circumstances. Pass: the common game still works, but the suspect does not become a generic dealer with a name attached.
- [x] **A112 [FIX] Visit-six deductions rely on numbers never shown to the player.** Display the relevant information in dialogue or the puzzle before asking for the answer. Pass: the solution is inferable from the visible scene without reading source code.
- [x] **A113 [FIX] Answers describe different behaviors although the question asks for an order of sounds.** Make the prompt, choices, and feedback ask and evaluate the same thing. Pass: a reader can explain why one offered answer fits the presented evidence.
- [x] **A114 [ASK] Pressuring the witness sets a flag with little later relational meaning.** Ask QV03 what Winston would remember or challenge. Pass: the choice has an appropriate, bounded response and does not vanish when the scene ends.
- [x] **A115 [EDIT] “Not a date” repeats Mads's deflection.** Follow the approved distinction: Winston can acknowledge that the meal looks like a date while Mads may continue denying mini-golf is one. Pass: Winston's joke-then-lost-composure style remains distinct from Mads's intellectualizing.
- [x] **A116 [EDIT] Competence is explained more often than demonstrated.** Let a tactic produce an observable response before naming the lesson. Pass: the player sees why it worked, with only the explanation needed to understand the clue.

### Ica: A117–A128

- [x] **A117 [FIX] “Told you he'd be into it” assigns the protagonist a gender.** Use established player information if available, otherwise a neutral construction. Pass: no unselected gender is introduced by this callback.
- [x] **A118 [FIX] The pawn-color choice is overridden later.** Store and use the selection consistently in game and narrative references. Pass: each available color survives the whole sequence.
- [x] **A119 [EDIT] “Legally distinct” jokes invoke copyright rather than the game's world.** The creator already approved an in-world off-brand title without a fourth-wall reference. Apply that direction and preserve Ica's playful slang. Pass: this joke works inside the setting; ask QI01 only if other fourth-wall jokes need a broader policy.
- [x] **A120 [ASK] Repeated “cringe” responses punish sincerity and narrow Ica's emotional range.** Ask QI02 how she handles sincere affection, discomfort, and private concern. Pass: modern slang remains, but different emotional situations do not all receive the same dismissal.
- [x] **A121 [FIX] A hot dog rises from the protagonist's tray before Ica catches it, implying the wrong power user.** Establish Ica's action, a trick, or the approved physical cause. Pass: the protagonist is not accidentally given telekinesis.
- [x] **A122 [FIX] The winner handles trash despite a wager assigning it to the loser.** Follow the result or explicitly negotiate a change. Pass: every outcome honors or knowingly revises the bet.
- [x] **A123 [FIX] Carpet protection scores poorly while every report claims the player protected it.** Separate action, consequence, and report. Pass: safe and risky branches describe what happened; any preference for mischief is legible in Ica's reaction.
- [x] **A124 [FIX] Painting finishes all walls and then continues for another hour.** Specify remaining work or move the completion statement. Pass: task progress and elapsed time agree.
- [x] **A125 [FIX] Furniture is lowered but a desk edge remains floating in the next beat.** Track which objects are still suspended. Pass: physical descriptions follow the same room state.
- [x] **A126 [ASK] The killer brings a wallet inside to destroy something already in their own coat.** Ask QI03 about the cabinet objective and why returning is necessary. Pass: preserve the intentionally accidental sixth-visit solution while making the culprit's immediate action coherent.
- [x] **A127 [ASK] Ica stops the wallet but not the fleeing killer despite object control.** Ask QI04 about power limits, obstacles, attention, or policy. Pass: an approved obstacle is visible at the moment it matters, rather than explained away afterward.
- [x] **A128 [FIX] The chicken game and chair pull assume participation, then narrate mutual flirting after resistance.** Add clear opt-in and a usable exit; remember both through the afternoon. Pass: confusion or refusal does not become consent by the next paragraph.

### Ulysses and reports: A129–A144

- [x] **A129 [ASK] Personal scenes advance by calendar despite skipped foundations.** Ask QU01 whether to sequence personal conversations by participation or provide day-specific guarded variants. Preserve mandatory reports and day-six case help. Pass: every personal scene makes sense with the conversations the player actually had.
- [x] **A130 [FIX] Day four quotes a day-three question the player did not necessarily ask.** Gate the callback on the exact exchange or use a different opening. Pass: skipped evenings and alternate choices never produce a false memory.
- [x] **A131 [FIX] The coma disclosure ignores low trust or missing prior conversations.** Use approved trust/readiness conditions and a guarded alternative; ask QU02 about the disclosure threshold. Pass: required case reporting remains available without automatically receiving intimate history.
- [x] **A132 [FIX] An unresolved boundary violation still allows day-five handholding.** Carry the violation and any actual repair into eligibility. Pass: intimacy is consistent with the same boundary logic used elsewhere; do not silently invent forgiveness.
- [x] **A133 [FIX] Day-six near-kiss eligibility disagrees with the final romance gate.** Use a shared approved readiness rule or explicitly justify the difference. Pass: unresolved misconduct cannot qualify for a scene the ending says the relationship has not earned.
- [x] **A134 [FIX] Ica's fourth report gives Ulysses future knowledge beyond his restriction.** Review “cannot prevent” and “I already see the office” against the power rules. Pass: phrasing and content stay inside the approved restriction rather than exploiting tense to evade it.
- [x] **A135 [ASK] Winston's negation may create an unaddressed foresight/communication loophole.** Ask QU03 jointly with QV01–QV02. Pass: the limitation works in scenes where Winston is present and cannot be bypassed by an obvious unacknowledged step.
- [x] **A136 [VERIFY] Professional gratitude still sometimes grants romance.** Trace all Ulysses trust and romance changes. Pass: mandatory cooperation can build trust without assuming romantic intent; explicit romantic choices remain distinguishable.
- [x] **A137 [FIX] A second visit on day five is described as spending most of the week together.** Base familiarity on experienced visits and optional conversations. Pass: late starts and mixed routes receive accurate language.
- [x] **A138 [FIX] Reports praise investigative depth after a visit that was primarily a date.** Describe the actual visit and evidence gained. Pass: admiration, case progress, and personal closeness are not interchangeable measurements.
- [x] **A139 [ASK] The player automatically reports coworkers' private confidences to their boss.** Ask QC04 and QU04 what belongs in mandatory reports. Pass: case facts remain mandatory, while approved private details have a clear consent or relevance rule.
- [x] **A140 [VERIFY] Mads's privacy is protected while similar disclosures from others are not.** Apply the agreed privacy rule consistently, allowing intentional character-specific exceptions. Pass: exceptions have a narrative reason rather than reflecting whichever scene happened to get a choice menu.
- [x] **A141 [FIX] Reports praise honesty or personal growth without supporting flags.** Tie specific claims to observed actions, or use modest descriptions of the current interaction. Pass: generic approval does not contradict deception, refusal, or skipped experiences.
- [x] **A142 [EDIT] Calling the photographed thirteen-year-old Ulysses “cute” earns present-day romance points.** Move any romantic signal to the present adult interaction or use a non-romantic response to the childhood photo. Pass: the relationship change follows what the player expresses toward adult Ulysses now. Source clarification: Ulysses is the thirteen-year-old in this photograph; Winston is the established superhero beside him.
- [x] **A143 [EDIT] Ulysses answers every emotion with a polished maxim.** Compare his irritation, humor, and authority with the creator's briefing. Keep occasional concise insight but restore variation and specific reactions. Pass: he sounds like the same person under different pressure, not a uniform dispenser of advice.
- [x] **A144 [EDIT] Coffee, music, paper, and a loosened vest become a repeated office ritual.** Keep useful recurring motifs and vary the scene's activity, pacing, and exit. Pass: repeated details change meaning or establish state instead of padding every evening.

### Minigames: A145–A182

- [x] **A145 [ASK] Razzle's memory game mainly asks the player to read and click.** Ask QG01 whether the intended experience is memory, witness listening, or a light interaction. Align the rules and feedback with that goal. Pass: the activity's promise matches the skill it actually uses.
- [x] **A146 [VERIFY] Coat and footstep information is discarded as distraction despite later relevance.** Compare every accepted/rejected memory with later evidence. Pass: the game distinguishes information irrelevant to this question from information that is false or useless to the case.
- [x] **A147 [VERIFY] Reshuffling the entire board creates unnecessary visual reacquisition and accidental clicks.** Observe actual play, including rapid input. Stabilize positions or make transitions unmistakable. Pass: a click intended for one visible item cannot silently select a different item after a reshuffle.
- [x] **A148 [ASK] The timer conflicts with a patient witness-listening scene.** Ask QG01 what creates urgency here. Adjust framing, timing, or assistance accordingly. Pass: time pressure has a comprehensible purpose and does not contradict the companion's instructions.
- [x] **A149 [FIX] The scanner punishes exploration before the player has enough information.** Provide discoverable cues or an unpenalized orientation step. Pass: first-time players can make informed choices; a perfect result does not require already knowing hidden locations.
- [x] **A150 [ASK] Abstract labeled rectangles do little to support forensic observation.** Ask QG02 about permitted UI/art scope. Improve existing descriptions and interactions before commissioning or replacing assets. Pass: the player observes a meaningful difference before deciding where to inspect.
- [x] **A151 [FIX] Finding the third clue replaces its feedback immediately with completion.** Hold or incorporate that clue's description into the completion flow. Pass: all three discoveries can be read without catching a transient frame.
- [x] **A152 [FIX] Inspected scanner descriptions cannot be revisited.** Provide a review mechanism within the approved screen. Pass: the player can reread a discovered detail before leaving, without earning it twice or restarting the game.
- [x] **A153 [VERIFY] Centrifuge instructions imply opposing-position balance while the calculation compares left and right sums.** Compare diagram, instruction, and scoring; select the intended abstraction with QG03 if needed. Pass: the displayed arrangement predicts the implemented result. Do not introduce unsupported claims of scientific realism.
- [x] **A154 [VERIFY] The 6, 6, 4, 4 setup produces imbalances that make the ±2 trim decorative.** Enumerate permitted arrangements and trim effects. Adjust values, rules, or explanation within the approved design. Pass: every advertised control has a meaningful use, or is honestly presented as unnecessary in this exercise.
- [x] **A155 [ASK] “Read bands” is a button rather than an interpretation task.** Ask QG03 whether observation or interpretation is intended. Add a small informed choice only if appropriate to scope. Pass: the game does not claim to have tested an interpretation the player never made.
- [x] **A156 [VERIFY] Nicky's matching rules inconsistently treat support, correction, and unverified assumptions as pairs.** Define the relationship each valid pair demonstrates and revise ambiguous cards. Pass: every pair follows a rule the player can apply before seeing the answer.
- [x] **A157 [FIX] Long mismatched cards disappear after roughly 0.85 seconds.** Use readable timing or a deliberate dismiss action. Pass: a first-time reader can inspect both cards and understand the mismatch without racing the reset.
- [x] **A158 [FIX] Player-facing game text exposes “saved case seed,” “mixed route,” or “active innocents.”** Replace development terms with in-world meaning while keeping debug output available only where appropriate. Pass: ordinary play contains no implementation explanation masquerading as dialogue.
- [x] **A159 [ASK] Blackjack is framed as questioning but contains little questioning or interpretation.** Ask QG04 whether it should be a casino diversion or an interrogation mechanic. Pass: either the framing becomes honest or a small approved interaction connects play to suspect responses.
- [x] **A160 [FIX] “Limited” intuition is actually unlimited.** Match the rule and implementation: enforce an approved limit or change the promise. Pass: the number of uses and the visible explanation agree across restart, assistance, and normal play.
- [x] **A161 [VERIFY] Quality depends on busts, so repeated conservative attempts can produce a perfect result without meaningful skill.** Evaluate stand/retry behavior and intended difficulty. Pass: quality measures the advertised behavior, or the game is explicitly treated as a forgiving diversion without overstated performance claims.
- [x] **A162 [FIX] Requesting completion/assistance stops halfway and requires another request.** Preserve the player's request across all remaining rounds or label a single-round action accurately. Pass: the chosen scope finishes once and still grants required case information.
- [x] **A163 [VERIFY] Five or more dealer cards may overflow the card row.** Test large hands at supported window sizes and UI scale. Pass: all cards, totals, and controls remain visible; record this as a risk until reproduced, not as an observed rendering failure.
- [x] **A164 [VERIFY] Higher/lower modifiers can make an apparently wrong comparison win.** Show the relevant rule and resulting value, or make a deliberate trick narratively legible. Pass: a player can understand the result from information the game provides.
- [x] **A165 [FIX] Tie handling and fallback behavior are hidden.** Explain ties and test the highest/lowest-card edge cases. Pass: every legal card produces a predictable valid outcome without an unexplained fallback.
- [x] **A166 [FIX] Cheating promises a peek but applies a mathematical modifier.** Implement the promised peek or describe the actual cheat. Pass: the player chooses the effect they receive.
- [x] **A167 [VERIFY] Repeated pulses can automatically track the target without overshooting.** Reproduce the reported one-pulse-per-tick strategy across all rounds. Adjust input, movement, or the skill claim only after deciding intended challenge. Pass: the game is either deliberately forgiving or requires the control it advertises.
- [x] **A168 [FIX] Staring rules say the first blink loses while the system allows recovery.** Choose a consistent rule and update instructions, feedback, and result. Pass: a recoverable mistake is not narrated as an immediate loss.
- [x] **A169 [VERIFY] Success can fill in eight seconds but the round waits roughly twenty-four seconds.** Measure actual timing. End when the approved success condition is met or give the remaining interval meaningful play. Pass: a completed round does not leave unexplained dead time.
- [x] **A170 [FIX] One round and best-of-three lead to the same timed sequence.** Implement distinct advertised formats or simplify the choice. Pass: format selection changes the rules the player experiences.
- [x] **A171 [FIX] The board-game script handles withdrawal but the screen offers no withdrawal action.** Expose a usable action and ensure it returns the expected result. Pass: mouse and keyboard users can leave as promised without losing a required clue or corrupting turn state.
- [x] **A172 [ASK] Both AI turns require repeated manual resolve clicks.** Ask QG05 about preferred pace and readability. Automate with readable pauses or retain a clearly labeled step-through option. Pass: the player understands each move without unnecessary repeated confirmation.
- [x] **A173 [VERIFY] Both AI players choose the first available bump and feel identical.** Inspect tie-breaking and goals. Add small approved differences only where they affect play. Pass: character flavor corresponds to behavior, or dialogue stops claiming strategic differences that do not exist.
- [x] **A174 [ASK] Bumping takes priority even over winning.** Ask QG05 whether this is an intentional character joke or an AI mistake. Pass: the approved behavior is explicit and does not accidentally contradict either character's supposed competence.
- [x] **A175 [FIX] Every player loss is reported as Winston winning, including Ica victories.** Preserve the actual winner through the return value and report. Pass: player, Winston, Ica, withdrawal, and any draw outcomes all have accurate text.
- [x] **A176 [FIX] Eating cooldowns reject apparently available button presses.** Show cooldown/disabled state and make feedback readable. Pass: the UI communicates when an action is unavailable instead of seeming unresponsive.
- [x] **A177 [FIX] Eating instructions imply every approach has a special action, but playing fair has none.** Explain the actual controls for the selected approach. Pass: no player waits for a missing ability promised by the rules.
- [x] **A178 [ASK] A simple stamina-threshold strategy trivializes the eating approaches.** Reproduce the reported roughly 15.75/15/10.75-second outcomes and ask QG06 whether this should be a gag or a challenge. Pass: tuning serves the approved purpose; do not make a comic interlude difficult merely because an exploit exists.
- [x] **A179 [VERIFY] The prank's interior is safe because the hall patrol never enters, despite the threat.** Compare the visible threat with actual detection zones. Pass: safety and danger can be understood from play; change patrol behavior only if that fits the intended forgiving design.
- [x] **A180 [FIX] Being caught is described as happening before a good look, but the report records observations.** Carry observation count and discovery state into the caught branch. Pass: the story agrees about what the protagonist saw before interruption.
- [x] **A181 [ASK] Repeated captures reset the same prank without narrative escalation.** Ask QG06 whether retries are outside narrative time or repeated real attempts. Pass: retry framing matches the intended model; forgiving retries remain allowed.
- [x] **A182 [EDIT] Different games receive the same generic praise for investigative intelligence.** Write short, outcome-specific reactions in each companion's voice. Pass: good memory, careful observation, luck, cheating, assistance, and persistence are not all described as the same accomplishment.

### UI, accessibility, and presentation: A183–A203

- [x] **A183 [VERIFY] Save thumbnails and text are too small for comfortable use.** Inspect the reported roughly 91×50 thumbnails and 13-pixel text at 1080p and supported sizes. Improve hierarchy and space while retaining the locked five slots per page. Pass: a player can distinguish saves without magnifying the screen.
- [x] **A184 [EDIT] Save tags expose day/route/visit/clue counts without clear meaning.** Use concise labels a player understands and retain useful disambiguation. Pass: a player can identify the run and scene without understanding variable names.
- [x] **A185 [VERIFY] History uses a narrow reading column despite available width.** Review wrapping and readability without reintroducing the previously fixed overlap. Pass: readable history at supported sizes, preserving the locked 250-entry limit.
- [x] **A186 [ASK] Important soft clues can age out of history while rollback is disabled.** Ask QP01 about an approved rereading mechanism. Preserve the locked rollback/history settings and Razzle's unlogged, seed-dependent soft evidence. Pass: the chosen solution respects those constraints; do not silently turn a soft clue into an automatically logged suspect category.
- [x] **A187 [ASK] The notebook lacks useful suspect context until profiles appear on day seven.** Ask QP02 what the player should know earlier. Pass: any earlier information is approved, avoids spoilers, and supports the intended deductions rather than giving away the solution.
- [x] **A188 [VERIFY] A 4,000-character notes field may exceed its fixed editing area.** Test long notes, caret movement, selection, scrolling, save/load, and supported resolutions. Pass: all entered text remains reachable and editable without overlapping other controls.
- [x] **A189 [ASK] Day selection provides little overview of visits, remaining leads, or the deadline.** Ask QP02 which progress information should be visible. Pass: approved information is accurate for mixed routes and does not imply that calendar day equals visit number.
- [x] **A190 [FIX] Help text promises Escape/right-click opens a menu, but minigames use those inputs differently.** Inventory actual behavior and make it consistent or clearly explain local exceptions. Pass: the player can predict pause/menu/withdraw behavior before risking progress.
- [x] **A191 [FIX] Rules cannot be reopened during a game.** Add an accessible rules view that preserves state. Pass: opening and closing help neither advances the timer unexpectedly nor resets progress; document the intended pause behavior.
- [x] **A192 [ASK] Timed games lack a consistent pause or relaxed-timing option.** Ask QP03 about accessibility scope and the distinction between assistance and surrender. Pass: chosen settings are consistent and required evidence remains available through authorized assistance.
- [x] **A193 [VERIFY] Angled quick-menu labels may sacrifice legibility for decoration.** Inspect actual rendering, hit targets, focus, and hover state. Pass: every label and selected state is easy to read without relying on angle or color alone.
- [x] **A194 [VERIFY] Orange/white outlined dialogue may have poor contrast over the notebook.** Recheck current screens, not only old screenshots. Pass: dialogue and choices remain legible on the actual background; do not describe a screenshot-based concern as a reproduced live failure.
- [x] **A195 [VERIFY] Large panels leave controls small amid unused space.** Review each affected screen and improve proportions where useful. Pass: primary actions are easy to find and use while preserving the intended visual style.
- [x] **A196 [VERIFY] Pinned profiles compress comparison text too far.** Align equivalent fields and review font size at supported resolutions. Pass: comparing two suspects does not require deciphering cramped text or remembering mismatched field order.
- [x] **A197 [VERIFY] Long dialogue may overflow the shallow text area.** Test the longest static lines and expanded dynamic confessions. Pass: every rendered variant fits or breaks at sensible boundaries, with no clipped text or hidden choices.
- [x] **A198 [DEFER] Three romance routes lack finished sprites.** Record missing production assets and the scenes that need them. Pass: an approved asset checklist exists; do not invent or replace character designs while fixing writing.
- [x] **A199 [DEFER] Rough art, pink/outline placeholders, and polished UI create inconsistent presentation.** Identify temporary versus intended assets with the creator. Pass: the production plan names each unresolved asset and style decision; avoid a speculative global art makeover.
- [x] **A200 [DEFER] Major locations use black or reused backgrounds.** List locations and necessary scene distinctions for an approved asset pass. Pass: gameplay and text stay coherent meanwhile, and final art work has a concrete brief.
- [x] **A201 [DEFER] Atmosphere is narrated but unsupported by music or sound.** Ask QP04 about intended audio scope and tone. Pass: any later audio plan identifies cues, ownership/licensing, and fallback behavior; prose is not expanded merely to compensate for missing assets.
- [x] **A202 [FIX] Hover/click styles reference unavailable audio files.** Verify `audio/rollover3.ogg` and the referenced click asset. Remove/disable unavailable references or connect approved existing assets. Pass: no missing-resource reference remains in the relevant controls; do not claim it crashes unless reproduced.
- [x] **A203 [EDIT] Player-facing credits/about text contains “Music To Be Added.”** Use an honest release-appropriate credit or omit the placeholder until there is something to credit. Pass: credits reflect shipped content and do not imply nonexistent contributors or assets.

### Endings: A204–A215

- [x] **A204 [ASK] Individual friendship is reached through romantic rejection rather than a direct friendly invitation.** Ask QC05 about a direct friendship choice. Preserve the locked two-visit friendship threshold and group-friendship route. Pass: players can pursue the approved platonic outcome without falsely expressing romantic intent.
- [x] **A205 [ASK] Hidden eligibility has too few understandable signals.** Ask QC06 what readiness should look like in dialogue. Pass: relationship feedback helps players interpret the connection without revealing raw thresholds unless the creator wants that UI.
- [x] **A206 [EDIT] Everyone uses the literal phrase “romantic date.”** Preserve clear consent but vary delivery by character and player intent. Pass: invitations are unmistakable where needed without seven characters sharing one scripted formulation.
- [x] **A207 [ASK] Ending montages summarize dates instead of delivering much interaction.** Ask QC07 about desired ending length and scope. Add a small concrete exchange if approved. Pass: each major payoff includes a distinct moment rather than only a narrator's assurance that the relationship works.
- [x] **A208 [EDIT] Rejection scenes over-explain that the refusal is fair, honest, and direct.** Let the refusal and response demonstrate that. Pass: the writing does not repeatedly defend the scene to the reader.
- [x] **A209 [FIX] Mads says the player admitted failure even after arguing or joking.** Track the actual response or use wording compatible with all branches. Pass: the ending does not award an admission the player never made.
- [x] **A210 [ASK] An ongoing pursuit sits awkwardly beside private dating closure.** Ask QW13 about capture, outstanding danger, time elapsed, and permission to leave. Pass: every ending's timing fits the current case state.
- [x] **A211 [ASK] A fired protagonist retains unexplained access to secure offices or labs.** Ask QW14 about escort, visitor access, or off-site alternatives. Pass: professional consequences and later meetings can coexist without ignoring security.
- [x] **A212 [EDIT] The alone ending anxiously insists it is not lesser.** Show an approved satisfying or deliberately bittersweet activity without ranking it against romance. Pass: the scene has its own purpose and does not read as an apology for the player's choice.
- [x] **A213 [ASK] Forty-two ending variants promise more dramatic variation than they deliver.** Ask QC07 whether distinct scenes, concise variants, or the current scope is intended. Pass: each retained variant has an identifiable difference; do not delete endings merely to reduce workload.
- [x] **A214 [ASK] Forty-two locked “???” rows provide little useful discovery guidance.** Ask QP05 about spoiler-safe hints, grouping, and completion visibility. Pass: approved guidance helps players navigate without spoiling the case or implying unattainable combinations.
- [x] **A215 [ASK] Endings unlock before being fully viewed.** Verify the current unlock point and ask QP05 what “unlocked” should mean. Pass: reach, start, finish, skip, and load behavior follow one documented policy.

### Copy, documentation, and maintainability: A216–A234

Documentation cleanup note, September 27, 2026: the creator requested deletion of the old audit reports, writing evaluation, Day 4/5 ideas, Ulysses evening plan, and minigame plan. This removes the source documents discussed in A225–A227. Preserve those finding IDs for traceability, verify any remaining current references, and record their resolved scope during implementation. Do not recreate the deleted documents to perform these tasks. Bezi Contributions remains as an explicitly ignored historical record.

- [x] **A216 [FIX] Ulysses's clothing description contains “vestandbutton-upFreddy.”** Confirm the current occurrence and remove the stray token/spacing error. Pass: the intended clothing description reads correctly without changing the scene's voice. If inside protected authored text, present the exact correction for approval first.
- [x] **A217 [ASK] Freddy's farewell is repeated during the team's wrap-up.** This concerns protected opening material. Ask QA01 before changing it, showing both passages and the smallest proposed cut. Pass: any revision preserves the creator's intended farewell and introductory rhythm.
- [x] **A218 [ASK] “Extremely permanent goodbye” can read as death foreshadowing or a meta joke.** Ask QA01 about its intended meaning. Preserve the locked fact that Freddy says goodbye forever and appears only in the intro. Pass: approved wording conveys the intended tone without creating an unapproved return.
- [x] **A219 [FIX] Nicky's “admissiable then” has spelling/comparison errors.** Confirm context and correct to “admissible” and, where comparative, “than.” Pass: the line's meaning and cadence remain intact.
- [x] **A220 [FIX] Copy errors include “ergregious,” “thining,” and “madibles.”** Correct confirmed unintended instances to “egregious,” “thinking,” and “mandibles.” Pass: intentional speech quirks are preserved and replacements are reviewed in context.
- [x] **A221 [FIX] Dhampir text includes “alwasy,” “Atlest,” and “sombeers.”** Correct confirmed mistakes to “always,” “At least,” and the intended “some beers” wording. Pass: spacing and sentence context are checked rather than blindly replacing substrings.
- [x] **A222 [FIX] Winston has “enought”; Ulysses has “passtime.”** Correct to “enough” and “pastime” where intended. Pass: no speaker-specific wording is rewritten as part of this copy pass.
- [x] **A223 [EDIT] To/too errors and direct-address punctuation recur.** Review in context. Preserve intentional fragments, caps, and rhythm; ask before changing protected opening text. Pass: mechanical corrections improve comprehension without formalizing the author's dialogue.
- [x] **A224 [FIX] Stray punctuation and capitalization interrupt physical demonstrations.** Review the reported `.;` and “Holy shit, We” cases and nearby sentences. Pass: errors are corrected without expanding or sanitizing the scene.
- [x] **A225 [FIX] Older audits contain superseded instructions.** Mark their status and point to current decisions for phones, forced Ulysses scenes, and old thresholds. Pass: a future model can tell historical findings from active requirements before applying them.
- [x] **A226 [ASK] Duplicate audit reports obscure which one is authoritative.** Verify actual duplication and ask before deleting or archiving user documents. A clear historical banner or index may suffice. Pass: one obvious entry point exists and original material remains recoverable.
- [x] **A227 [FIX] Razzle planning notes retain the removed hand-injury clue.** Update current planning references to the approved soft-clue design; mark historical material as such. Pass: implementation guidance and game text agree about what the player can learn.
- [x] **A228 [VERIFY] Utility scripts contain machine-specific absolute paths.** Identify which tools are meant to be reusable and parameterize relevant source/output/runtime paths. Pass: a second checkout can run the documented utility without editing a developer's username; avoid rebuilding unrelated production assets.
- [x] **A229 [FIX] Tests validate counts more than evidence meaning.** Add targeted assertions tying a stated category/value to the suspects it excludes. Pass: a semantically false clue fails even when the expected number of suspects remains.
- [x] **A230 [FIX] Ending tests inject scores without proving those scores can be reached.** Keep useful isolated tests and add representative runs using actual choices and gates. Pass: each tested outcome has a legal path, not merely a manually constructed state.
- [x] **A231 [VERIFY] Screenshot checks fail on small fixture dimension changes.** Investigate the reported 2776/2778 mismatch and normalize the capture setup where appropriate. Pass: tests distinguish real layout regressions from fixture drift; do not blindly overwrite references to make a failure disappear.
- [x] **A232 [FIX] Critical branch combinations lack coverage.** Add focused checks for skipped personal scenes, unresolved violations followed by flirtation, assistance, AI winners, and album-exchange variants. Pass: the exact contradictions in this guide are exercised rather than only happy-path completion.
- [x] **A233 [VERIFY] Unused template/gallery demonstration files add noise.** Check runtime references, packaging, and useful development purpose before proposing removal. Pass: any cleanup is narrow, recoverable, and does not remove an intentional tool or user asset.
- [x] **A234 [FIX] Continuity facts have no reliable shared record.** Maintain a small ledger of ownership, refusals, cutoff behavior, captures, known clues, and relevant conversations; persist only facts that actually need runtime state. Pass: callbacks use established facts, new state has defaults/save compatibility, and the documentation identifies where each fact is set and read.

## Questions to ask the creator

These are prompts for the implementing model to select from, not a questionnaire the creator must complete before anything can happen. First check existing decisions and earlier answers. Ask only the questions that affect the next scene. Include the scene, the current contradiction, and the consequence of the answer. Offer examples as possibilities, never as new canon. The creator may answer in rough notes, sample dialogue, or “keep this as it is.”

An effective question sounds like: “In Mads's helmet scene, if the player deliberately ignores her stop request and apologizes afterward, would she end the test but keep working with them, refuse further personal time, or respond another way? This determines the later handholding and date gates.” Avoid “What is Mads like?” when a specific decision is needed.

### Authored reference and protagonist

- **QA01 — Protected opening edits (A216–A218).** “May I correct the stray clothing-description token and tighten the repeated Freddy farewell? What should ‘extremely permanent goodbye’ convey: his literal final appearance, an in-world reason, a joke, or something else? I will preserve his permanent goodbye and show the exact proposed changes.”
- **QA02 — Style calibration (A035–A056, all writing).** “Which three lines or exchanges from your intro/briefing best capture your intended voice? Which later passage sounds least like you? Are there jokes, rough phrasing, or pauses you want kept exactly?” Read the references first; do not make the creator supply material already present.
- **QC01 — Player identity (A051–A052, A117).** “How defined is the protagonist supposed to be? Which traits or history are fixed, and which should the player choose? May companions ask about a preference or past experience, and should declining to answer always remain possible?”
- **QC02 — Professional warmth versus romance (A037–A044, A080, A091, A094, A136).** “If the player is kind and competent but never flirts, should a companion show one-sided interest, remain entirely friendly, or vary by character? What behavior should count as the player's romantic interest?” Do not treat permission for a companion's attraction as permission to narrate mutual attraction.
- **QC03 — Persistent disagreement (A038–A043, A050).** “What is one thing each character would disagree with even when they like the protagonist? If the player is right but blunt, what changes: affection, respect, cooperation, or only the immediate mood?”
- **QC04 — Privacy in reports (A139–A140).** “Which personal details should stay between the player and a companion? When would Ulysses actually need to know? Should the player choose whether to share non-case confidences, and would the companion know if they did?”
- **QC05 — Direct friendship (A204, A212).** “Should the final invitation explicitly offer spending time as friends as well as asking for a date? What should a satisfying individual friendship ending give the player that the group or alone ending does not?”
- **QC06 — Readiness signals (A041, A205).** “What would show that each character is becoming comfortable or interested before the final invitation? Would you prefer signals entirely in dialogue, a simple relationship description, or another approach?” Preserve approved visit targets unless the answer changes them.
- **QC07 — Ending scope (A207, A213).** “How much unique interaction should each ending contain? Which outcomes deserve a full scene, and which can be shorter variants? What one changed behavior should a good ending demonstrate for each character?”
- **QC08 — Disclosure pace (A035, A043, A055, A129–A131).** “What should a second visit hint at without fully explaining? For each character, what experience earns the deeper conversation, and what would they say if the player has not earned it?” Use the existing early-glimpse/later-depth decision as the starting point.

### Case, setting, and powers

- **QW01 — Enrico (A013, A015).** “What did Enrico do, what was he like in ordinary conversation, and who here had a personal reason to care about him? Which two or three details should players remember?”
- **QW02 — Common motive (A014–A016).** “What exactly did Enrico discover, and why would any of the nine possible killers kill to hide it? What proof or admission resolves that question?” Keep one approved underlying motive with character-specific delivery.
- **QW03 — Suspect variation (A015–A016, A111).** “How much should the case change with the culprit: only evidence and confession delivery, a few suspect-specific exchanges, or more? What is one distinctive pressure or habit for each suspect?”
- **QW04 — Profile knowledge (A007, A023–A024, A187).** “Who compiled the suspect profiles, and how do they know the listed reaction and trace information? Are those background habits, observations from this case, or puzzle abstractions? What should the player know before day seven?”
- **QW05 — One-each deduction (A008).** “One visit with each teammate leaves four suspects under the existing exclusions. What genuinely new comparison should Ulysses contribute to distinguish them? May we add an approved observation, or should an existing observation be made available earlier?” Do not solve this by reading the hidden answer.
- **QW06 — Accusation procedure (A006, A012, A029–A032).** “When does the player's accusation become official, who checks it, what happens before the culprit can escape, and what information can Ulysses legitimately use to reject it? Wrong accusations will still cost the job.”
- **QW07 — What powers invalidate (A019, A021–A024).** “Which physical or behavioral deductions remain reliable in this superhero setting? Can powers disguise build, appearance, or traces? What specific conditions make the game's exclusions valid?” Ask about affected clues rather than requesting an encyclopedia.
- **QW08 — Protagonist intuition (A025–A026, A160).** “Is intuition an actual power, an ordinary hunch, or a game aid? What can it perceive, what can it never know, and how would the protagonist describe it?”
- **QW09 — Deadline (A027, A031–A032).** “Why must this accusation happen at the end of the week? What prevents another day of investigation, and who is responsible for that constraint?”
- **QW10 — Teammates' independent work (A028).** “What are unselected teammates doing during the week? Can they mention work without handing over extra eliminations, and what kind of update would fit?” Preserve the decision that poor route distribution can fail.
- **QW11 — Final deduction interaction (A030).** “Should the player name the suspect only, or also choose supporting evidence? If they guess correctly with weak evidence, what should the team credit them for?”
- **QW12 — Image provenance (A077–A078).** “Where do the before/during/after images come from, and what does the evidence marker actually mark? Which images are direct records and which are reconstructions?”
- **QW13 — After the case (A210).** “At each success/failure ending, is the culprit captured, being pursued, or still unknown? How much time passes before a private outing, and is there an ongoing danger that the scene should acknowledge?”
- **QW14 — Access after dismissal (A211).** “Can a dismissed protagonist enter ATLAS with an escort or visitor permission, or should later meetings happen elsewhere? How final is the professional separation?”

### Razzle

- **QR01 — Safety and exclusion (A058–A059).** “If a shop employee politely offers a fire-safe place to sit, would Razzle appreciate it, feel singled out, joke, or react another way? What specifically makes the current employee's treatment hurtful?”
- **QR02 — Fire/contact rules (A060).** “How does she keep clothes, food, paper, furniture, and people safe? Can she control heat, and can emotions disrupt that control? What would she do before touching or kissing someone?” Preserve ordinary-car risk and approved protected transport.
- **QR03 — Being corrected (A061, A065).** “If the rookie correctly spots something she missed and says it bluntly, does she get defensive, laugh, compete, or thank them? What would she do differently after trusting them?”
- **QR04 — Practical intelligence (A058, A062–A065).** “What is a small practical problem Razzle would solve before anyone else? What kind of praise would she believe, and what would sound patronizing?”
- **QR05 — Refused affection (A066, A037–A043).** “If the player likes her but declines a celebration or touch, how does she keep her escalating, laughing flirt style without treating the refusal as an insult? What would she remember next time?”
- **QR06 — Natural vulnerability (A035, A043, A058).** “What event would make her choose to talk about Elena or being seen as a hazard? What does she dodge on a low-trust route, and what changes after the player hears her?”

### Dhampir

- **QD01 — Public reputation (A071).** “What do ordinary people know about his lethal record? On the rooftop, is the discomfort meant to be prejudice, justified fear, a mixture, or primarily a joke? How aware is he of the distinction?”
- **QD02 — Player shock (A072).** “After the squirrel incident, how would he react to a startled pause, a dark joke, or a matter-of-fact objection? Which responses would he respect even if he disagrees?” Keep the incident and ATLAS's acceptance intact.
- **QD03 — Death and coping (A073–A075).** “Does he sincerely feel at ease with death, use casualness to cope, or vary by situation? What would make him stop joking, and what would he never admit aloud?”
- **QD04 — Manison (A075–A076).** “Who is Manison, what did they teach him, and how much should the rookie know at first mention? Is the name supposed to be mysterious?”
- **QD05 — Physical boundaries (A069–A070, A080).** “If the rookie refuses flight or asks him not to take their food, how would he respond while staying recognizably himself? How does consensual flirting differ from his ordinary teasing?”
- **QD06 — Disclosure trigger (A035, A043, A074).** “What shared experience makes him discuss his training or past? If the player asks too soon, does he deflect with humor, refuse directly, or offer a smaller truth?”

### Mads / Madeline

- **QM01 — Ignoring the stop request (A010, A081–A084).** “If the player deliberately continues after she says stop, what immediate and lasting consequence would she choose? Is there any repair path during this week, and what would a real apology or repair require?” Track conduct separately from affection regardless of the answer.
- **QM02 — Helmet purpose (A081–A082, A089–A090).** “What does the helmet test actually need to measure? Why is disinhibition part of it, why does she trust the rookie with it, and what does she expect them to do if something goes wrong?”
- **QM03 — Small preferences (A086–A088).** “With the blue ice cream or another unfamiliar suggestion, is she irritated, curious, hiding enjoyment, or something else? Should this affect the relationship much, or mainly shape banter?”
- **QM04 — Interest versus respect (A091, A136).** “If she admires a professional player who never flirts, would she show awkward interest, keep it private, or remain purely friendly? How does she intellectualize attraction when it is mutual?”
- **QM05 — Changed behavior in the ending (A087, A092, A207).** “On a later mini-golf outing, what does she now let herself do that she would not do before: lose, improvise, be silly, accept help, or something else?” These are options, not presumed lessons.
- **QM06 — Ex-partner and coworker (A050, A053, A139–A140).** “If the rookie asks about Ulysses, what would she freely say, what would she refuse to discuss, and what joke could she make without implying their functional relationship is secretly hostile?”
- **QM07 — Failure and bluntness (A085–A086, A209).** “If the player makes an honest lab mistake and owns it, what would her exact first reaction sound like? How would that differ if they bluff or blame the equipment?” A short creator-written example is particularly useful here.

### Nicky

- **QN01 — Sensing limits (A093–A094).** “Can she sense stress, particular emotions, attraction, or actual lying? How often can she misread it? If the rookie says she has interpreted them incorrectly, would she believe them, tease them, or reconsider?”
- **QN02 — Her particular pressure (A100).** “What does the LAPD/ATLAS divide mean to her personally? Is there a specific responsibility, prejudice, loyalty, or ambition you want the route to explore?”
- **QN03 — Custody correction (A102–A104).** “What causes the suspicious chain-of-custody correction? Is it misconduct, a mistake, or a misleading clue, and how should the player learn the answer?”
- **QN04 — Life outside work (A106).** “What does she want outside being useful or impressive at work? What personal decision would reveal that through an ordinary activity rather than a sudden backstory speech?”
- **QN05 — Gifts and boundaries (A095–A099).** “How would she react differently to a new album as a gift, lending the player's own copy, or just recommending a title? If the player politely asks for space or privacy, what does confident teasing sound like without overruling them?”
- **QN06 — Rejection and criticism (A040, A105).** “What would a respectful rejection sound like in her voice? If the rookie disputes a deduction correctly, does she enjoy the challenge, get defensive, or react according to delivery?” Preserve ‘Good rookie’ where appropriate.

### Winston

- **QV01 — Negation and sobriety (A108, A135).** “What exactly changes about his power when sober or drinking? Can he choose targets and duration, and which established powers can he affect? What limits prevent easy workarounds to the case?”
- **QV02 — Consent and emergencies (A110).** “Would he dampen a frightened witness's powers without asking to prevent immediate harm? What distinguishes that from coercion in his own mind, and would he explain or apologize afterward?”
- **QV03 — Pressuring a witness (A114).** “If the rookie ignores his caution and pushes a witness, what would he do in the moment and remember later? What would restore respect if repair is possible?”
- **QV04 — The emergency-brake disclosure (A109, A116).** “What can he casually reveal early, and what only comes out after trust? What event makes him choose to tell the deeper part?”
- **QV05 — Flirtation (A115, A037–A043).** “If the rookie accepts his joke as a sincere invitation, how does he lose composure? If they keep it friendly, what does he say next without making them responsible for his embarrassment?”
- **QV06 — Young Ulysses and Winston (A142).** “What should the old photograph show about thirteen-year-old Ulysses's relationship with the already established hero Winston? What is the adult emotional point of the present conversation, and which details should remain light or private?” Preserve the approved ages/timeline.

### Ica

- **QI01 — Broader fourth-wall humor (A119).** “Your existing decision replaces the board game's copyright joke with an in-world off-brand title. For any other meta jokes, should Ica stay entirely in-world, or are some references to genre/game conventions intentional?” Ask only if another scene needs clarification; the board-game decision is settled.
- **QI02 — Sincerity and defense (A120, A128).** “If someone sincerely thanks her in private, what does she do besides say ‘cringe’? What would make her briefly drop the performance, and how would she cover it afterward?”
- **QI03 — Wallet/cabinet objective (A126).** “Why does the killer return to this room, what is in the cabinet, and why must they handle the wallet there? What small setup makes the accidental discovery plausible?”
- **QI04 — Power limit during escape (A121, A125, A127).** “What stops her from restraining the culprit when she can stop the wallet? Is it line of sight, attention, weight, danger, policy, surprise, or something else you already intend?”
- **QI05 — Capture timeline (A012).** “Does the fleeing culprit get caught offscreen before day seven, or should the finale acknowledge an escape? Who knows the outcome, and when?”
- **QI06 — Losing and being refused (A122–A123, A128).** “When she loses a wager or the player refuses chicken, would she grumble and honor it, negotiate, cheat openly, or respond another way? What separates her nonchalant flirting from pushing past a boundary?”
- **QI07 — Low-trust fun (A043, A120).** “If the rookie has been distant or openly annoyed, why does she still involve them in the day's activity? What changes in the invitation, personal detail, or physical familiarity?”

### Ulysses

- **QU01 — Skipped evenings (A129–A130, A137).** “If the player stays late for the first time on day four, should they receive the first personal conversation in a later-day frame, or a guarded version of day four's topic? Which events must remain attached to a specific day?” Mandatory reports and day-six help remain available either way.
- **QU02 — Coma and trust (A131–A133).** “What makes him willing to discuss the coma? What does he tell a professional but distant rookie, and what is reserved for someone he personally trusts?”
- **QU03 — Foresight restriction (A134–A135).** “What precisely is he unable to know, say, or change, and why? Does Winston's negation affect that restriction? What would happen if they tried the obvious workaround?”
- **QU04 — Boss and confidant (A136, A139–A141).** “How does he respond when the rookie starts sharing a teammate's private life during a case report? Does he stop them, ask whether it is relevant, or accept it under specific circumstances?”
- **QU05 — Anger and restraint (A143).** “What brings out the impatient, forceful person from your briefing in later scenes? If the rookie challenges him fairly, what does he say before settling into a calmer response?” Keep the opening's throttling gag as canon.
- **QU06 — Boundary repair (A132–A133).** “After the player crosses his boundary, what must happen before personal closeness is possible again? Could he remain a supportive supervisor while declining any intimacy this week?”
- **QU07 — Romance and ordinary time (A144, A206–A207).** “What would he choose to do with someone when he is not supervising, explaining, or comforting them? How does his invitation sound different from his professional warmth?”

### Minigame and presentation decisions

- **QG01 — Razzle game's purpose (A145–A148).** “Should this feel like memory under pressure, careful listening, or a short character activity? What should a good result demonstrate?”
- **QG02 — Scanner scope (A149–A152).** “Can this pass change the scanner layout/interactions, or should it work with current assets and improve cues and text? What should players notice themselves?”
- **QG03 — Lab-game depth (A153–A155).** “Are these approachable toy science tasks or puzzles where players should infer a rule? How much added interpretation fits the intended pacing?”
- **QG04 — Blackjack purpose (A159–A162).** “Is blackjack primarily banter, a challenge, or a way to read a suspect? Should intuition be limited, and what should performance affect besides the reaction?”
- **QG05 — Board AI (A172–A174).** “Should Winston and Ica try to win, prioritize bothering each other, or have different goals? Should their turns play automatically with readable pauses?”
- **QG06 — Comic-game difficulty and retries (A167–A181).** “Are eating, staring, and the prank intended as easy jokes or genuine challenges? Do retries represent repeated attempts in the story, and should characters remember them?”
- **QP01 — Soft-clue review (A186).** “With rollback off and history capped at 250, what approved way should players have to revisit a scene? Razzle's subtle observations must remain unlogged; would replaying the conversation or another approach fit?”
- **QP02 — Investigation overview (A187–A189).** “What should the notebook and day selector reveal before the finale: visits, known facts, remaining leads, suspect backgrounds, or only some of these? What should stay for the player to infer?”
- **QP03 — Accessibility (A190–A192).** “Should all timed games offer pause and a relaxed mode? Should assistance preserve story rewards while changing performance feedback? Which inputs should always open help or the menu?” Required clues must remain available through the approved assist path.
- **QP04 — Production scope (A198–A203).** “Which art and audio gaps are placeholders for a later pass, and which are expected for this release? Are there existing approved assets or a style reference we should use?” Do not reopen deferred title art without a request.
- **QP05 — Gallery policy (A213–A215).** “Should an ending unlock when reached, started, or finished? Do you want spoiler-safe hints or grouping for locked endings, and how should skipping/loading affect completion?”

### Record answers once

Use the existing decision document or a clearly linked answer log. Keep the creator's words alongside a concise implementation interpretation. Do not turn a tentative preference into permanent canon without saying so.

| Field | Record |
| --- | --- |
| Question ID and date | Example: QM01, date answered |
| Creator's answer | Exact answer or faithful quotation |
| Approved interpretation | What this allows, requires, or forbids |
| Scope | Character, scene, route, or whole game |
| Related findings | All affected A IDs |
| Implementation | State, dialogue, reports, endings affected |
| Remaining uncertainty | Only genuinely unanswered points |
| Verification | How the answer will be checked in play |

If the creator supplies example dialogue, treat it as a new style reference for that character and situation. Do not distribute its catchphrases to the whole cast.

## Concrete implementation recipes

These recipes explain how to approach the highest-risk repairs. They are not replacement source code: names and control flow must be verified against the current project.

### Recipe 1: truthful evidence across mixed routes — A003–A009, A017–A034, A229

1. Read the suspect attribute table, reveal planner, every route adapter, descriptions shown in minigames, clue storage, report text, and finale comparisons. Locate `get_planned_route_reveal`. At the audit snapshot, adapted Visit 3 reveals could use selected category values for elimination while retaining an old singular value for text.
2. Trace one reported failure before changing anything. For killer 4, take Razzle three times then Mads three times. Immediately before the problematic Mads reveal, the audit's active set was `[1, 2, 4, 6, 7]`. A displayed O result removed suspects 1 and 6, whose relevant type was A. Confirm the current behavior.
3. Define one authoritative reveal result for the current active set. It must distinguish a whole category from individual suspects, and contain the values that all displays describe. Adapt callers deliberately; do not let each screen recompute its own explanation.
4. For a claimed category exclusion, verify that every excluded active suspect has a stated excluded value and that no active suspect with that value is silently exempted. Include the killer in this consistency check. Preserving the killer by special-casing them does not make false prose true.
5. If the design permits excluding named individuals without excluding their whole category, say so in the clue. Do not label an arbitrary collection of names as a blood type, build, or injury class.
6. Test killer preservation, truthful descriptions, idempotent award behavior, intended remaining counts, and agreement between game, report, and notebook. Test assistance as well as normal completion.
7. Cover the other reproductions: killer 1 with Nicky/Dhampir/Mads/Razzle/Razzle/Razzle; killer 1 with Mads/Dhampir/Nicky/Nicky/Razzle/Nicky; killer 3 with Winston/Winston/Winston/Dhampir/Dhampir/Dhampir. Use current internal route identifiers after inspecting the source.
8. Enumerate the reachable evidence transitions for all nine killers, deduplicating equivalent states when useful. Report what was enumerated. The old 19,270 transitions and 31 mismatches are a historical comparison, not a required test-result number.

For pure investigative routes, check the intended formal progression of nine to eight to six to three active suspects. Interpret exclusion counts relative to the active set, not the length of a list containing already-eliminated IDs. Razzle's remaining distinctions can use approved unlogged observations; do not force every route to formally reduce to one. Ica's clue-free first five visits and accidental final solution are a separate intentional structure.

Exactly one visit to each daytime character yields five investigative exclusions and ordinarily four survivors. Do not claim that this alone logically identifies one culprit. QW05 must supply an approved additional constraint or comparison. A 2/2/2 distribution does not need a rescue mechanism.

### Recipe 2: assistance and screen exits — A002, A068, A151, A162, A171, A190–A192

Treat assistance as its own completion outcome, not a request that must also satisfy normal success progress. Trace the screen action, callback, returned result, route continuation, clue award, quality state, and dialogue. The same assist request must not both award a clue and leave an interactive screen waiting for normal completion.

Test assistance immediately, halfway through, and near completion. Test repeated input during a transition. Each request must close or advance the interaction once, award the required clue once, record the actual outcome, and produce matching dialogue. A withdrawal from a required evidence activity must use the approved clue-delivery fallback. Separate optional-game withdrawal from required-evidence assistance if their narrative meanings differ.

Do not fix an exit by globally changing Escape/right-click without checking every game's documented behavior. Reopening rules must preserve game state and follow a stated timer policy.

### Recipe 3: optional evenings and consequential state — A001, A010–A012, A044, A129–A144, A234

At the audit snapshot, `ulysses_day_three_tension` was assigned inside Evening Three and later read by Evening Four without a safe default. Adding a default addresses the crash, but does not by itself fix the false memory. Track whether the relevant conversation happened, which choice occurred, and whether any resulting issue was repaired.

Separate these concepts wherever relevant: calendar day, visit count, conversation experienced, professional trust, romantic intent, specific refusal, boundary violation, repair, and current invitation. A single affection total cannot stand in for all of them.

Create a small continuity ledger, with entries such as:

| Fact | First established by | Later consumers | Required alternatives |
| --- | --- | --- | --- |
| Flight accepted or declined | Dhampir transport choice | Return trip, callback | Stairs/approved alternative versus consensual flight |
| Snack purchased | Snack menu | Food theft/sharing | Actual item or no item |
| Album exchange type/owner | Nicky Visit 2 | Report, Visit 6, ending | Gift, loan, title-only recommendation |
| Helmet cutoff respected | Mads test | Immediate response, report, intimacy, ending | Respected, mistake, deliberate violation, approved repair |
| Ulysses conversation seen | Optional evening | Future callback/disclosure | Seen, skipped, guarded alternative |
| Explicit physical invitation | Relevant menu | Touch/kiss/afternoon narration | Accepted, declined, deferred |
| Culprit escaped/captured | Ica finale and approved follow-up | Report, Day Seven, endings | One consistent timeline |
| Game winner/performance | Actual returned outcome | Praise, report, wager | Each winner, assist, withdrawal, failure |

Use Ren'Py-compatible saved defaults for new runtime facts, following the project's conventions. Inspect behavior on a fresh game and on older saves that predate the field. Do not migrate an unknown past choice into a confident intimate memory. Select a neutral fallback or approved inference and document it. Preserve new-game reset behavior and avoid accidentally storing run-specific facts in persistent gallery data.

Day-six case preparation and the special breadth-route help must still happen when the player declines personal time. Never solve an intimacy gate by making mandatory investigation help conditional on staying late.

### Recipe 4: a character writing pass — A035–A144, A204–A212

Before rewriting, make a short working card for the character. Include reference lines, characteristic diction, humor, what they want in the scene, what annoys them, what they hide, their approved power limits, and their response to a polite refusal. Label unknowns rather than filling them with generic traits.

For each scene, fill in these seven points in brief notes:

1. **Entry facts:** day, visit, prior conversations, objects, evidence, trust, and explicit romantic signals actually present.
2. **Immediate activity:** what both people are doing before the emotional subject comes up.
3. **Trigger:** the specific event or remark that brings up the subject now.
4. **Choice:** at least two reasonable approaches where the situation supports them; not only flattery versus cruelty.
5. **Reaction:** what this character does or says on each branch, including a guarded/platonic version.
6. **Change:** what is learned, decided, refused, or left unresolved, and what later scene remembers it.
7. **Exit:** the earliest effective ending after necessary consequences occur.

If a serious subject has no believable trigger or later consequence, repair that before polishing its dialogue. If the player skips the relevant exchange, later scenes cannot quote it. If two routes share the same emotional shape, change the action or conflict according to character answers, not just the food or scenery.

Use the approved romantic tendencies as a starting distinction: Razzle escalates and laughs; Dhampir uses dark humor; Mads intellectualizes; Nicky teases confidently; Winston jokes and then loses composure; Ica acts nonchalant. Ulysses requires his own approved voice and separation between authority, trust, and romantic interest. None of these tendencies overrides a refusal or requires every line to perform a gimmick.

Finish with a no-ai-slop pass: remove redundant explanations, interchangeable reassurance, abstract emotional conclusions, repeated “quiet” beats, and polished closing maxims where they dilute the scene. Keep creator-like edges. Read the whole resulting scene, including the lines immediately before and after each edit; good isolated replacement lines can still make a bad transition.

## Verification matrix

Use existing project test infrastructure where it fits. Locate the installed Ren'Py runner and current test instructions rather than hardcoding someone else's path. Run lint after script changes. Add focused regression tests for consequential bugs, evidence semantics, and state transitions. Do not write large tests that merely repeat the prose or assert that a rewritten adjective exists.

| Area | Minimum meaningful coverage | What must remain true |
| --- | --- | --- |
| Evidence | All nine killers; pure routes; reported mixed-route failures; deduplicated reachable reveal states | Killer preserved, prose supports exclusions, intended route structure retained |
| Broad versus shallow investigation | Exactly one each; 2/2/2; correct guess with weak evidence; wrong accusation | Approved breadth help; no unapproved rescue; honest account of collected proof |
| Optional evenings | None, all, first stay late, skip Day 3/stay Day 4; all 64 attend/skip combinations at logic level if practical | Mandatory work completes, no undefined state or false recollection; approved readiness rules |
| Player intent | Professional-only, consistent flirting, friendly refusal, changed mind through an explicit later choice | No invented attraction, touch, gender, promise, or biography |
| Conduct | Respect limit, honest mistake, deliberate violation, approved repair | Later intimacy and reports use actual events rather than score alone |
| Ownership | Every snack/music/gift/loan branch | Objects and preferences remain correct in reports and callbacks |
| Minigames | Win, lose, assist at zero/partial progress, withdraw, retry, reopen rules, repeated input | One completion, correct clue, correct outcome, readable feedback |
| Board game | Player, Winston, and Ica wins; withdrawal; any supported draw | Correct wager, report, and winner; usable exit |
| UI | Supported sizes; long names/lines/confessions; full notebook/notes; long card hands; history/save/gallery | No clipping, hidden controls, unreachable text, misleading labels |
| Persistence | Fresh run; save/load around new state and screens; older compatible save; restart | Correct defaults, no stale prior-run facts, no fabricated past intimacy |
| Endings | Each retained variant's conditions; representative actual-choice routes at approved thresholds; failures and alone/friendship routes | Legal attainable path, honest case state, correct privacy/access and gallery policy |
| Reference voice | Compare opening/briefing diff and changed scenes | Protected text unchanged unless specifically approved; later writing fits its voice |

Keep logic, engine, visual, and editorial evidence separate in the report. “Lint passed” does not mean a route was played; “screenshot inspected” does not mean keyboard navigation works; a manually set affection score does not prove an ending is attainable. When an engine or asset is unavailable, state precisely what remains unverified.

For each repaired bug, record a compact reproduction: starting state, route/choice sequence, old failure, expected new result, observed result, and test method. If the current game already fixes an item, mark it verified already resolved with evidence instead of reintroducing a different implementation.

## Completion and handoff

The implementation is ready for creator review when every ID has a recorded disposition, confirmed fixes have relevant checks, revised scenes pass a full branch-aware reading, and remaining creator decisions or production gaps are plainly listed. An approved deferral is a valid disposition; it is not an implemented feature. Do not describe a partial pass as all 234 items fixed.

Each progress report should contain:

- The IDs handled and what changed for the player.
- The checks actually performed and their result.
- Any exact character/design questions blocking the next related change.
- Deferred items and why they remain deferred.
- The next small batch, with its dependencies.

### Copyable starting instruction for the next model

> Read `docs/implementation_guide.md` and `docs/audit_decisions.md`, then inspect the current project and any local instructions. Implement the guide in small batches, starting with Phase 0 and the confirmed blockers in Phase 1. The creator-authored intro and Day One briefing in `game/script.rpy` are the primary writing standard: preserve their voice and do not rewrite them without specific approval. Apply the no-ai-slop skill if available, using the guide's embedded principles if it is not. Preserve existing user changes. Maintain a progress ledger mapping all A001–A234 IDs to evidence, changes, checks, questions, or explicit deferrals. Do not treat every criticism as a confirmed bug or invent character canon. Ask a few focused scenario questions from the question bank when needed, record the answers, and continue independent repairs while waiting. Test mixed and unusual routes, refusals, skipped personal scenes, assistance, reports, and endings. Begin with the source review and first bounded fixes; do not rewrite the entire game in one pass.
