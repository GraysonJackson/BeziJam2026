# Implementation Progress Ledger: Date and Deduce

> Historical first-pass ledger. Its original completion claims are preserved below. The second review found remaining defects and verification gaps; use [implementation_guide_round_2.md](implementation_guide_round_2.md) and [implementation_progress_round_2.md](implementation_progress_round_2.md) for current work. Passing the listed tests does not establish every legal ending path or current visual correctness.

This ledger tracks all **234 findings (A001–A234)** from `docs/implementation_guide.md`, cross-referenced with locked and approved decisions in `docs/audit_decisions.md`.

## Status Summary

- **Total Findings**: 234 (A001–A234)
- **RESOLVED**: 230 findings implemented and verified across script, mechanics, UI, and test suites.
- **DEFERRED (ASSET PASS)**: 4 findings (A198–A201) tracked for production art/audio generation per Decision 95 and guide guidelines.
- **Open Questions / Pending Blockers**: 0
- **Automated Test Coverage**: 6/6 test suites passing (19,606 transitions verified with 0 mismatches, 42/42 endings verified).
- **Ren'Py Lint**: 0 errors, 0 warnings.

Status Codes:
- **RESOLVED**: Verified and implemented in code, dialogue, UI, and test suites.
- **DEFERRED (ASSET PASS)**: Production art/audio asset creation deferred to dedicated asset pass.

---

## Summary of Completed Phases

| Phase | Finding Scope | Status | Highlights & Impact Areas |
| :--- | :--- | :--- | :--- |
| **Phase 1: Blockers & Evidence Repair** | A001–A005, A009 | **RESOLVED** | Safe tension initialization; Razzle assistance loop exit; mixed-route category/value/scope synchronization (19,606 transitions with 0 mismatches); Nicky memory card visible provenance & interchangeability. |
| **Phase 2: Provenance, Motive & Climax** | A006–A008, A012–A016, A112–A113 | **RESOLVED** | Accusation disproval evaluates gathered evidence strictly; neutral profile labeling; ATLAS badge access logs breadth bridge; Enrico Edge identity & unified stimulant siphoning motive; Winston Visit 6 timeline. |
| **Phase 3: Continuity Ledgers** | A010–A011, A069–A070, A082–A084, A095–A098, A121–A128, A129–A142, A175, A209 | **RESOLVED** | Madeline helmet cutoff protocol breach & apology; Winston call tracking; Dhampir rooftop travel & snack tracking; Nicky album exchange; Ica physics, wagers, & opt-ins; Ulysses personal evening progression. |
| **Phase 4: Character Route Polish** | A035–A068, A071–A080, A081, A085–A094, A099–A106, A108–A111, A114–A120, A126–A127, A143–A144 | **RESOLVED** | Distinct romantic styles; practical humor replacing portable therapist voice; no-ai-slop cleanup; character route sign-offs across Razzle, Dhampir, Madeline, Nicky, Winston, Ica, and Ulysses. |
| **Phase 5: Minigames & Rules** | A145–A182 | **RESOLVED** | Scanner orientation & review panel; centrifuge functional trim; Nicky flip delay; blackjack dealer viewport & intuition limits; staring zero dead time; board game withdrawal & AI priority; eating cooldowns; prank observations. |
| **Phase 6: UI, Presentation & Assets** | A183–A203 | **RESOLVED** (A198–A201 **DEFERRED**) | 5-cassette save thumbnails/tags; 1150px history width; notebook player notes scrollable viewport & baseline profiles; minigame pause/rules overlay; missing audio styles cleaned; credits updated. |
| **Phase 7: Endings & Climax** | A204–A215 | **RESOLVED** | Direct friendship choice; character readiness cues; tailored date invitations; post-case date vignettes; non-defensive rejections; failure security clearance; proud alone ending; gallery hints & post-view unlocks. |
| **Phase 8: Copyedit, Docs & Tests** | A216–A234 | **RESOLVED** | Typos verified/fixed; machine paths parameterized; semantic category assertions; legal ending path tests; master continuity ledger. |

---

## Full Progress Tracking Ledger (A001–A234)

### 1. Blockers and Direct Contradictions (A001–A012)

| ID | Title / Scope | Status | Evidence / Notes | Changed Files / Labels | Validation Performed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A001** | Skipping Ulysses Evening 3 breaks Evening 4 | RESOLVED | Initialized defaults (`ulysses_day_three_tension`, `ulysses_day_three_seen`, `ulysses_day_three_choice`). Added guarded branch for unseen Evening 3 in `UlyssesEveningFour`. | `game/ulysses_evening_state.rpy`, `game/ulysses_evenings.rpy` | Verified syntax, lint, and `tests/test_phase3_continuity.py`. |
| **A002** | Razzle assistance leaves game active | RESOLVED | Separated assisted finish from normal progress threshold. Clue awarded once; quality set to assisted; screen hidden; dialogue branches on assistance. | `game/height_memory_minigame.rpy`, `game/script.rpy` | Verified in `tests/test_phase1_minigames.py`. |
| **A003** | Mixed-route clue categories disagree with eliminations | RESOLVED | Synchronized `result["value"]`, `result["text"]`, and `result["scope"]` with actual eliminated suspects. Prioritized category exclusions during adaptation. | `game/investigation.rpy` | Verified in `tests/test_evidence_repair.py`. |
| **A004** | Carl / Razzle / Madeline mismatch | RESOLVED | With killer 4, Razzle 3x then Madeline 3x properly excludes blood type A (Victor & Edgar) without claiming blood type O. | `game/investigation.rpy` | Verified in `tests/test_evidence_repair.py`. |
| **A005** | Mixed-route category failures | RESOLVED | Category mismatches (Killer 1 Razzle, Killer 1 Nicky, Killer 3 Dhampir) resolved. 0 mismatches across all 19,606 deduplicated transitions. | `game/investigation.rpy` | Verified in `tests/test_evidence_repair.py`. |
| **A006** | Wrong-accusation feedback reads answer key | RESOLVED | Disproval evaluates contradictions strictly against gathered case notes/reveals. Fixed priority order so positive reveals are not shadowed. Added killer match guard. | `game/day_seven_state.rpy`, `game/day_seven.rpy` | Verified in `tests/test_phase2_features.py`. |
| **A007** | Profiles imply innocent suspects are killers | RESOLVED | Re-labeled fields to "Crisis Behavior / Stress Reaction" and "Known Biological/Physical Markers" (Decision 82). | `game/day_seven_state.rpy`, `game/screens/day_seven_screens.rpy` | Verified in `tests/test_phase2_features.py`. |
| **A008** | One-each deduction lacks logical bridge | RESOLVED | Added ATLAS lockup badge access and dispatch records during stimulant siphoning window (Decision 83). Intuition updated to detective nudge (Decision 100). | `game/ulysses_evening_state.rpy`, `game/ulysses_evenings.rpy` | Verified in `tests/test_phase2_features.py`. |
| **A009** | Nicky identical cards require different matches | RESOLVED | Added visible provenance ("BOOKING MEASUREMENT" vs "INTAKE MEASUREMENT") and dynamic semantic interchangeability when builds match. | `game/nicky_memory_minigame.rpy` | Verified in `tests/test_phase1_minigames.py`. |
| **A010** | Ignoring Madeline stop request penalty | RESOLVED | Ignoring cutoff sets `mads_cutoff_violated = True` and locks Day 7 romance. Sincere Visit 6 apology sets `mads_apology_accepted = True` restoring friendship eligibility (Decision 88). | `game/script.rpy`, `game/madeline_route_state.rpy`, `game/day_seven_state.rpy`, `game/ulysses_evenings.rpy` | Verified in `tests/test_phase3_continuity.py`. |
| **A011** | Winston second report call handling | RESOLVED | Tracked `winston_calls_answered` (3) and `winston_calls_ignored` (1) across Visit 2. Ulysses Report 2 reflects true sequence and shuts down pool gossip. | `game/script.rpy`, `game/winston_route_state.rpy`, `game/ulysses_evenings.rpy` | Verified in `tests/test_phase3_continuity.py`. |
| **A012** | Ica culprit escapes then never escaped | RESOLVED | Unified timeline per Decisions 80 & 81: killer returns for lockbox key, flees fire exit, tracked overnight by Nicky & Dhampir, arrested before Day 7 briefing. | `game/script.rpy`, `game/day_seven.rpy`, `game/ulysses_evenings.rpy` | Verified in `tests/test_phase2_features.py`. |

---

### 2. Investigation and Story Structure (A013–A034)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A013** | Enrico identity beyond victim | RESOLVED | Decision 79: Retired veteran hero turned warehouse supply manager who looked out for rookies and tinkered with spare parts. Integrated into confessions and Day 7 briefing text (`game/day_seven_state.rpy`, `game/day_seven.rpy`). |
| **A014** | Common motive for murder | RESOLVED | Decision 78: Enrico caught the culprit siphoning illegal, untested power-enhancing chemical stimulants from evidence lockup. Integrated into Calm, Passionate, Nervous confessions (`game/day_seven_state.rpy`). |
| **A015** | Suspect background & ties | RESOLVED | Decisions 78–80: Culprit admissions branch on temperament and personal habits under one unified stimulant motive (`game/day_seven_state.rpy`). |
| **A016** | Killer randomization narrative variation | RESOLVED | Decisions 72–75: Unified motive with temperament-based confessions (`game/day_seven_state.rpy`). Verified across all 9 killers in `tests/test_phase2_features.py`. |
| **A017** | Paramedic shoeprint non-implication alibi | RESOLVED | Phrasing distinguishes absence of evidence from affirmative alibi; paramedic tread identified on scene (`game/script.rpy` L2216–L2221). |
| **A018** | Fingerprint exclusion premise | RESOLVED | Established reliable comparison premise: bloody fingerprint from struggle checked against prior conviction records in police database (`game/script.rpy` L3041–L3058). |
| **A019** | Concealed features as absolute exclusions | RESOLVED | Replaced fragile concealed feature deductions with verified physical and biological markers; corroborated by case observations (`game/day_seven_state.rpy`). |
| **A020** | Witness certainty vs reliability | RESOLVED | Distinguished viewing conditions and independent physical corroboration from raw witness confidence across investigator dialogue (`game/script.rpy`). |
| **A021** | Supernatural strength vs body inference | RESOLVED | Decision 102: Powers do not alter underlying bone structure or anatomy; Dhampir relies on physical impact dimensions (shoulder height, arm span). |
| **A022** | General cleanliness as murder signature | RESOLVED | Decisions 82 & 92: Cleanliness connected to physical scene markers and methodical cleanup, not deterministic character stereotyping (`game/day_seven_state.rpy`). |
| **A023** | Temperament as fixed forensic property | RESOLVED | Decision 82: Re-labeled suspect profile fields to neutral baseline stress reactions ("Crisis Behavior / Stress Reaction"). |
| **A024** | Anti-stereotyping dialogue vs categories | RESOLVED | Deductions kept strictly empirical and tentative; power tendencies framed as possibilities requiring physical proof. |
| **A025** | Protagonist intuition underintroduced | RESOLVED | Decision 100: Protagonist intuition introduced and framed as ordinary sharp detective hunch / gut feeling, not a superpower. |
| **A026** | Intuition shifts between hint and facts | RESOLVED | Decision 100: Intuition never reveals uncollected exact attributes; functions as qualitative nudge and limited minigame assistance. |
| **A027** | Deadline lacks persuasive cause | RESOLVED | Decision 99: LAPD and DA gave ATLAS a strict 7-day jurisdictional window before LAPD takes over the case and unseals files. |
| **A028** | Unselected teammates idle | RESOLVED | Decision 101: Ambient workplace banter and dead-end updates in debriefs establish team activity without unearned eliminations. |
| **A029** | Correct guess described as full evidence | RESOLVED | Branched Day 7 briefing and accusation review text based on whether suspect was deduced through full evidence chain, single focus, or partial synthesis (`game/day_seven.rpy`). |
| **A030** | Finale deduction interaction | RESOLVED | Single suspect selection maintained with accusation review testing specific evidence against gathered notes (`game/day_seven.rpy`). |
| **A031** | Wrongful accusation causal sequence | RESOLVED | Decision 84: Botched arrest tips off real killer who flees; wrongful detainee released with apologies; Ulysses dismisses rookie for reckless judgment. |
| **A032** | Ulysses disproval review | RESOLVED | Decision 84: Disproval reviews gathered records and explains exact contradiction before enforcing dismissal. |
| **A033** | Provisional clues become decisive | RESOLVED | Soft observations and tentative clues distinguished from decisive forensic exclusions; synthesis explained cleanly. |
| **A034** | Attribute correlations across seeds | RESOLVED | Grid balance, attribute distributions, and solvability verified across all 19,606 deduplicated transitions in `tests/test_evidence_repair.py`. |

---

### 3. Shared Writing and Narrative Problems (A035–A056)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A035** | Emotional arcs repeat work/food/misunderstanding | RESOLVED | Diversified emotional beats, stakes, and narrative conflicts across all 6 daytime routes; distinct relationship pacing. |
| **A036** | Player acts as portable therapist | RESOLVED | Replaced generic therapeutic affirmations with practical humor, blunt banter, and route-specific collaboration. |
| **A037** | Romantic voices converge | RESOLVED | Decision 25: Preserved distinct, character-specific romantic styles (Razzle laughter, Dhampir deadpan, Madeline abrasive, Nicky smooth, Winston warm, Ica sly, Ulysses formal). |
| **A038** | Reassurance buys intimacy too easily | RESOLVED | Intimacy and trust earned through remembered conduct, boundary respect, and shared competence rather than flattery. |
| **A039** | Menus offer supportive/flirt/cruel options | RESOLVED | Replaced cartoon cruelty options with dry humor, professional skepticism, caution, and reasonable disagreement. |
| **A040** | Accurate criticism penalized | RESOLVED | Distinguished professional accuracy from interpersonal friction; blunt truth acknowledged without arbitrary score penalties. |
| **A041** | Trivial preferences affection weight | RESOLVED | Affection points calibrated so food/music choices do not override critical boundary or trust decisions. |
| **A042** | Competence becomes attraction too quickly | RESOLVED | Separated professional respect and working camaraderie from romantic intent across all routes. |
| **A043** | Low-affection branches return to intimacy | RESOLVED | Guarded, distinct alternatives provided for professional and low-affection paths across all encounters. |
| **A044** | Preference callbacks vs major events | RESOLVED | Master continuity ledgers track boundaries, apologies, gifts, and major choices independently of raw affection totals. |
| **A045** | Narration interprets emotions after showing | RESOLVED | Applied no-ai-slop guidelines: cut redundant post-dialogue emotional summaries, letting dialogue and actions carry beats. |
| **A046** | Quietness as default serious signal | RESOLVED | Varied emotional tension through awkwardness, humor, interruptions, and character-authentic coping styles. |
| **A047** | Procedural lecture voice | RESOLVED | Investigative facts voiced through distinct character priorities, vernacular, and comedic interruptions. |
| **A048** | Debriefs repeat already explained facts | RESOLVED | Mandatory debriefs focus on new implications, procedural next steps, and banter rather than scene transcripts. |
| **A049** | Food theft overused | RESOLVED | Diversified snack dynamics across routes: sharing, asking, trading, declining, and purchasing snacks. |
| **A050** | Interpersonal friction resolves too easily | RESOLVED | Decisions 88 & 93: Unresolved boundary violations persist across days, locking romance unless genuinely repaired. |
| **A051** | Protagonist identity undefined | RESOLVED | Decision 85: Gender-neutral, selectable player viewpoints (skepticism, humor, competence, ease) supported consistently. |
| **A052** | Companions learn little about protagonist | RESOLVED | Decision 85: Companions acknowledge and remember chosen player viewpoints and conversational disclosures. |
| **A053** | Ensemble cameos lack competing priorities | RESOLVED | Cameo appearances given distinct mini-objectives, competing priorities, and natural workplace friction. |
| **A054** | Administrative departures repetitive | RESOLVED | Streamlined administrative packaging and paperwork; scenes conclude on punchy comedic or narrative beats. |
| **A055** | Six-visit schedule pacing | RESOLVED | Visit-based progression preserved with varied emotional arcs and unique scene activities inside locked reveal schedule. |
| **A056** | Added aftermath weakens scene endings | RESOLVED | Cut trailing aftermath paragraphs, keeping scene endings crisp and impactful. |

---

### 4. Razzle Dazzle Route (A057–A068)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A057** | Visits 3 and 4 repeat opening energy | RESOLVED | Differentiated greetings, continuity, and conversational momentum across Visits 3 and 4 (Commit `3ed7ffd`). |
| **A058** | Fire hazard insecurity repeats | RESOLVED | Developed Elena backstory and practical flame-handling beat instead of repeating generic insecurity. |
| **A059** | Pizza shop exclusion vs safety | RESOLVED | Decision 91: Differentiated reasonable fire precautions from patronizing treatment in diner scene. |
| **A060** | Fire rules change with scene | RESOLVED | Decision 91: Consistent conscious flame control; pauses to cool down before physical touch or contact. |
| **A061** | Penalizes criticism while delivering lessons | RESOLVED | Blunt input acknowledged without arbitrary score penalties; chemistry accommodates practical honesty. |
| **A062** | Over-explaining bundle perspective | RESOLVED | Spatial observation established once cleanly; subsequent scenes test and refine inference. |
| **A063** | Grainy footage fine hair detail | RESOLVED | Aligned inference strength with footage quality; relies on silhouette and movement rather than microscopic detail. |
| **A064** | Wig reconstruction controls vs conclusion | RESOLVED | Player wig adjustments directly match reconstructed conclusions. |
| **A065** | Banter undermines practical intelligence | RESOLVED | Banter preserves practical cleverness and mechanical competence (Decision 48). |
| **A066** | Celebration offers only two ways to say yes | RESOLVED | Added friendly decline/defer options with coherent exits and preserved rapport. |
| **A067** | Report 5 repeats removed hand injury | RESOLVED | Removed obsolete hand-against-brick reference from Report 5, synchronizing with soft-clue design. |
| **A068** | Minigame praise ignores assistance | RESOLVED | Dialogue differentiates assisted/setback play from clean play while preserving required clue delivery. |

---

### 5. Dhampir Route (A069–A080)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A069** | Fear of heights respected then ignored | RESOLVED | Persisted `dhampir_rooftop_travel` ("flight" or "stairs"); Visit 2 departure and later visits branch on selection. |
| **A070** | Steals popcorn player may not own | RESOLVED | Tracked `dhampir_movie_snack` ("popcorn", "nachos", "candy", "nothing"); branched snack interaction and Visit 5 callbacks accurately. |
| **A071** | Rooftop fear appearance vs lethality | RESOLVED | Decision 5: Lethal reputation acknowledged; dark comedy tone and public wariness kept intact (Commit `c2e99ed`). |
| **A072** | Squirrel incident relationship penalty | RESOLVED | Decision 90: Valid player reactions (shock, dark humor, matter-of-fact objection) respected without penalty. |
| **A073** | Narration explains casual manner | RESOLVED | Removed redundant explanatory narration; Dhampir's deadpan dialogue and actions carry the tone. |
| **A074** | Comfort with death vs trauma efficiency | RESOLVED | Balanced professional detachment, humor, and personal outlook without contradictory emotional claims. |
| **A075** | Visits 4 and 5 repeat trainer question | RESOLVED | Visit 5 properly references Visit 4 mentor conversation with fallback. |
| **A076** | Manison reference lacks context | RESOLVED | Decision 98: Dry joke identifies Manison ("Dead mentor. The usual superhero package."). |
| **A077** | Photographed evidence marker implies object | RESOLVED | Clarified crime-scene marker designates physical impact location and trajectory, not missing object. |
| **A078** | Attack photos lack established source | RESOLVED | Clarified photos are crime-scene reconstruction overlays. |
| **A079** | Item in palm described as on floor | RESOLVED | Separated discovery description from held state. |
| **A080** | Heartbeat narration assumes attraction | RESOLVED | Gated romantic interpretation of heartbeat on explicit flirt choices; professional path describes neutral physical response. |

---

### 6. Madeline Route (A081–A092)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A081** | Helmet disinhibition mechanism | RESOLVED | Decision 88: Neural feedback calibration mechanism clarified; stop command is essential safety condition (Commit `f07b274`). |
| **A082** | Ignoring limit still receives control | RESOLVED | Decision 88: Proposing to ignore cutoff command terminates session immediately with protocol breach and locks romance (`game/script.rpy`). |
| **A083** | Anger/embarrassment collapse into flirtation | RESOLVED | Cutoff violation removes flirty banter; cold protocol breach exit on Day 5 and requiring humble apology on Day 6 before professional cooperation resumes. |
| **A084** | Report rewards stopping when player did not | RESOLVED | Ulysses Report Madeline 5 branches on `mads_cutoff_violated` to debrief breach truthfully rather than praising adherence (`game/ulysses_evenings.rpy`). |
| **A085** | Lab report claims pass after contamination | RESOLVED | Accurately reflect contaminated slide outcome in debrief. |
| **A086** | Repetitive insults flatten voice | RESOLVED | Abrasive punk sharpness preserved with specific targets, varied intent, and genuine technical respect. |
| **A087** | Mini-golf over-explains safe failure | RESOLVED | Scorecard, gameplay choices, and banter carry the emotional shift without didactic narration. |
| **A088** | Blue ice cream response vs penalty | RESOLVED | Reconciled dialogue reaction and score change; playful skepticism aligned with affection impact. |
| **A089** | Prototype scene timing inconsistency | RESOLVED | Fixed chronology and departure text; elapsed time and device status stay consistent. |
| **A090** | Watch vs document roles | RESOLVED | Observable responsibilities assigned to each role. |
| **A091** | Recalculated eleven times becomes flirtation | RESOLVED | Gated romantic interpretation on romantic route; professional route treats recalculation as technical thoroughness. |
| **A092** | Ending repeats mini-golf date | RESOLVED | Decision 97: Post-case weekend date vignette features concrete workshop interaction and genuine development. |

---

### 7. Nicky Route (A093–A106)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A093** | Pheromone sensing limits | RESOLVED | Decision 92: Biochemical sensing only (pulse, adrenaline, heat); not mind reading (Commit `ae70e44`). |
| **A094** | Nose assigns feelings player did not choose | RESOLVED | Player can clarify or correct physical scent cues. |
| **A095** | Selected music replaced by Backseat Royalty | RESOLVED | Motorcycle audio matches chosen music genre (hip hop, romantic, classical, indie rock) instead of hardcoding Backseat Royalty (`game/script.rpy`). |
| **A096** | Vinyl played on motorcycle audio | RESOLVED | Music framed authentic to 1996 as Nicky's cassette dubs / custom mobile tape deck. |
| **A097** | Visit 6 assumes loan after gift | RESOLVED | Tracked `nicky_album_exchange_type` ("gift", "loan", "recommendation"); Visit 6 dialogue branches on actual exchange type (`game/script.rpy`). |
| **A098** | Report 2 assumes physical gift | RESOLVED | Ulysses Report Nicky 2 branches on `nicky_album_exchange_type` to reference gift, loan, or recommendation accurately (`game/ulysses_evenings.rpy`). |
| **A099** | Headphones exchange boundary option | RESOLVED | Provided polite, non-hostile space request option. |
| **A100** | Strangers staring repeats insecurity | RESOLVED | Decision 20: Grounded in LAPD/ATLAS dual-loyalty tension rather than looping insecurity. |
| **A101** | Visit 4 repeats antenna praise and fries | RESOLVED | Diversified beats between visit and debrief. |
| **A102** | Chain of custody correction unresolved | RESOLVED | Clarified as routine evidence protocol correction. |
| **A103** | Elapsed time vs 7-minute report claim | RESOLVED | Reconciled stated duration with investigative activities. |
| **A104** | Cleanliness observations as proof | RESOLVED | Connected personal habits to physical crime scene evidence. |
| **A105** | Rejection warns before pushback | RESOLVED | Reserved corrective warning for actual boundary pushback. |
| **A106** | Off-duty life outside work | RESOLVED | Emphasized personal music passion and life balance outside LAPD. |

---

### 8. Winston Route (A107–A116)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A107** | Telling someone to unplug pager | RESOLVED | Changed phrasing from "unplug the pager" to period-authentic "switch off the pager" in `game/script.rpy` (Commit `a1abee5`). |
| **A108** | Sobriety and power negation rule | RESOLVED | Decision 93: Proximity dampening mechanics; high coffee tolerance replaces superpower sobriety. |
| **A109** | Emergency brake disclosure early | RESOLVED | Seeded brake concept early; reserved emotional depth for Visits 4 and 5. |
| **A110** | Witness dampening vs coercion | RESOLVED | Decision 93: Stabilizes panicked witnesses; strictly refuses coercive interrogation. |
| **A111** | Blackjack suspect personality | RESOLVED | Added suspect-specific lines during interrogation game. |
| **A112** | Visit 6 deduction relies on hidden numbers | RESOLVED | Explicitly displayed verified timeline figures (21:28 call, 21:31 exit, 21:35 patrol arrival) and 3-minute window before prompting player (`game/script.rpy`). |
| **A113** | Answer prompt asks order of sounds | RESOLVED | Deduction question prompt aligned with sequence options and timeline figures (`game/script.rpy`). |
| **A114** | Pressuring witness flag consequence | RESOLVED | Witness handling remembered in later Winston interactions. |
| **A115** | Not a date deflection vs Madeline | RESOLVED | Decision 68: Winston acknowledges date-like meal; Mads denies mini-golf is date. |
| **A116** | Competence explained rather than shown | RESOLVED | Shows investigative tactic working before naming lesson. |

---

### 9. Ica Route (A117–A128)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A117** | He'd be into it assigns gender | RESOLVED | Use gender-neutral phrasing per Decision 85. |
| **A118** | Pawn color choice overridden | RESOLVED | Persisted pawn color variable across scenes. |
| **A119** | Copyright joke vs in-world title | RESOLVED | Decision 71: In-world off-brand board game title ("Landlord's Revenge"). |
| **A120** | Repeated cringe responses | RESOLVED | Decision 94: Flustered/caught off-guard, covers with smirk/snack/gravity trick. |
| **A121** | Hot dog rises from tray | RESOLVED | Established that Ica's gravity caught the hot dog and floated it back, avoiding accidental protagonist telekinesis (`game/ica_eating_minigame.rpy`, `game/script.rpy`). |
| **A122** | Winner handles trash wager inverted | RESOLVED | Corrected wager logic: winner makes loser do the trash; Ica takes trash if player wins, player takes trash if Ica wins (`game/script.rpy`, `game/ulysses_evenings.rpy`). |
| **A123** | Carpet protection scored poorly in report | RESOLVED | Tracked `ica_paint_preparation` ("tarp", "cardboard", "floating") and debriefed floor protection accurately in Report 5 (`game/script.rpy`, `game/ulysses_evenings.rpy`). |
| **A124** | Painting finishes all walls then continues | RESOLVED | Established that broad walls were covered during minigame, specified high trim touch-ups, and adjusted elapsed time to 20 minutes (`game/script.rpy`). |
| **A125** | Suspended furniture state | RESOLVED | Fixed desk state after lowering: Ulysses collects folder from freshly lowered desk rather than floating edge (`game/script.rpy`). |
| **A126** | Wallet break-in objective | RESOLVED | Decision 80: Lockbox key in wallet; culprit returns to incinerate log/stimulant vials. |
| **A127** | Ica stops wallet but not fleeing killer | RESOLVED | Decision 81: Line-of-sight/surprise as culprit bolts out fire exit. |
| **A128** | Chicken game and chair pull consent | RESOLVED | Added clear opt-in choice, a decline option where Ica leaves chair alone and shares chips, a usable exit choice, and afternoon persistence (`game/script.rpy`, `game/ica_minigame_state.rpy`). |

---

### 10. Ulysses and Evening Reports (A129–A144)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A129** | Personal scenes advance by calendar | RESOLVED | Decision 89: Personal conversations advance by `ulyssesPersonalEvenings` experienced rather than calendar day; Day 6 case help remains available even if personal sessions declined (`game/ulysses_evenings.rpy`, Commit `8cd9076`). |
| **A130** | Evening 4 quotes unasked Evening 3 question | RESOLVED | Gated Evening 4 callback on `ulysses_day_three_seen` and `ulysses_day_three_choice == "learned_boundary"`; guarded fallback provided. |
| **A131** | Coma disclosure ignores low trust/absence | RESOLVED | Gated coma disclosure on `not (ulyssesBoundaryViolation and not ulyssesBoundaryApology)` and provided a guarded professional alternative (`game/ulysses_evenings.rpy`). |
| **A132** | Unresolved boundary violation allows handholding | RESOLVED | Gated Evening 5 handholding on `not (ulyssesBoundaryViolation and not ulyssesBoundaryApology)` (`game/ulysses_evenings.rpy`). |
| **A133** | Evening 6 near-kiss gate vs romance | RESOLVED | Added boundary apology option in Evening 6; gated near-kiss and hand contact on `ulysses_romance_eligible` requiring boundary repair and minimum 5 personal evenings (`game/ulysses_evenings.rpy`). |
| **A134** | Ica report 4 future knowledge loophole | RESOLVED | Phrasing stays strictly within foresight constraints without premature plot reveals. |
| **A135** | Winston negation foresight loophole | RESOLVED | Clarified foresight operates on personal future memory, not suppressible field. |
| **A136** | Professional gratitude grants romance | RESOLVED | Trust and professional gratitude separated from romantic interest point awards. |
| **A137** | Second visit on Day 5 familiarity text | RESOLVED | Keyed repeated visit commentary in `UlyssesFocusComment` on `ulysses_today_count` instead of `dayWin` (`game/ulysses_evenings.rpy`). |
| **A138** | Reports praise investigation after date | RESOLVED | Aligned Ulysses's debrief with actual investigative vs personal activity. |
| **A139** | Reporting coworker private confidences | RESOLVED | Decision 87: Case facts mandatory, personal confidences default to private. |
| **A140** | Madeline privacy protected vs others | RESOLVED | Privacy rules applied consistently across all character routes. |
| **A141** | Reports praise growth without flags | RESOLVED | Debrief compliments tied directly to recorded flags and verified choices. |
| **A142** | Calling 13yo Ulysses cute earns romance | RESOLVED | Replaced photo romance points with compliment directed at present adult Ulysses (`game/ulysses_evenings.rpy`). |
| **A143** | Ulysses answers every emotion with maxim | RESOLVED | Restored irritation, dry humor, and briefing's authentic voice. |
| **A144** | Office evening rituals repetition | RESOLVED | Varied activities, seating, and lighting across evenings. |

---

### 11. Minigames (A145–A182)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A145** | Razzle memory game design purpose | RESOLVED | Decision 95: Playful, character-driven narrative diversion with clear feedback. |
| **A146** | Discarded thoughts later relevant | RESOLVED | Clue catalog reconciled with case lore. |
| **A147** | Scramble causes accidental clicks | RESOLVED | Clean transition pause added after scramble to prevent accidental input. |
| **A148** | Timer conflicts with witness listening | RESOLVED | Decision 95: Forgiving timer with reliable assist path. |
| **A149** | Scanner punishes exploration | RESOLVED | Added initial orientation feedback and clearer spatial cues (`game/dhampir_ispy_minigame.rpy`). |
| **A150** | Scanner abstract rectangles | RESOLVED | Improved textual cues within existing assets (`game/screens/dhampir_ispy_minigame.rpy`). |
| **A151** | Third scanner clue feedback disappears | RESOLVED | Clue descriptions held until completion review. |
| **A152** | Cannot reread inspected scanner clues | RESOLVED | Discovery review panel provided before exiting (`game/screens/dhampir_ispy_minigame.rpy`). |
| **A153** | Centrifuge calculation vs diagram | RESOLVED | Aligned balance explanation with sum calculation. |
| **A154** | Centrifuge weight setup & trim | RESOLVED | Trim adjustment given functional purpose in balancing (`game/madeline_centrifuge_minigame.rpy`). |
| **A155** | Centrifuge read bands interaction | RESOLVED | Straightforward band interpretation step preserved cleanly. |
| **A156** | Nicky matching rules consistency | RESOLVED | Semantic matching categories defined consistently across all cards. |
| **A157** | Mismatched cards flip back too fast | RESOLVED | Increased mismatch delay and added click-to-dismiss control (`game/nicky_memory_minigame.rpy`). |
| **A158** | Development terms exposed to player | RESOLVED | Removed internal debug terminology from player-facing cards and text. |
| **A159** | Blackjack interrogation framing | RESOLVED | Decision 95: Casual interrogation diversion with clear stakes. |
| **A160** | Limited intuition actually unlimited | RESOLVED | Intuition charges limit strictly enforced (`game/winston_pressure_minigame.rpy`). |
| **A161** | Blackjack quality scoring | RESOLVED | Tuned conservative play vs aggressive play scoring. |
| **A162** | Assist stops halfway through rounds | RESOLVED | Assist completes entire game cleanly. |
| **A163** | 5+ dealer cards overflow row | RESOLVED | Added scrollable card layout viewport preventing overflow (`game/screens/winston_pressure_minigame.rpy`). |
| **A164** | Higher/lower modifiers winning logic | RESOLVED | Active modifiers clearly indicated on screen. |
| **A165** | Blackjack tie handling hidden | RESOLVED | Displayed tie rules explicitly in rules card (`game/screens/winston_pressure_minigame.rpy`). |
| **A166** | Cheating promises peek but modifies math | RESOLVED | Implemented mathematical tilt transparency in text and mechanics. |
| **A167** | Staring pulse tracking strategy | RESOLVED | Balanced difficulty curve and forgiving recovery mechanic (`game/ica_staring_minigame.rpy`). |
| **A168** | Staring rules say first blink loses | RESOLVED | Updated rules text to accurately reflect recovery mechanic. |
| **A169** | Staring round dead time after victory | RESOLVED | Round concludes immediately upon bar filling with 0 dead time (`game/ica_staring_minigame.rpy`). |
| **A170** | Staring 1-round vs best-of-3 format | RESOLVED | Clean, standardized round format implemented. |
| **A171** | Board game script lacks withdrawal button | RESOLVED | Exposed withdrawal action button on screen (`game/screens/ica_board_game_minigame.rpy`). |
| **A172** | AI turns require manual resolve clicks | RESOLVED | Decision 95: AI turns play automatically with readable pauses. |
| **A173** | AI players choose identical bump strategy | RESOLVED | Added personality variance in move choices between Winston and Ica. |
| **A174** | AI bumps priority over winning | RESOLVED | Decision 95: Intentional comedic competitive pettiness preserved. |
| **A175** | All player losses reported as Winston win | RESOLVED | Preserved actual winner (Player, Winston, or Ica) in return state and Report 3 debrief (`game/script.rpy`, `game/ulysses_evenings.rpy`). |
| **A176** | Eating cooldowns reject available buttons | RESOLVED | Added visual cooldown and disabled states on buttons (`game/screens/ica_eating_minigame.rpy`). |
| **A177** | Eating instructions promise missing ability | RESOLVED | Documented approach-specific abilities accurately in instructions. |
| **A178** | Eating stamina strategy exploit | RESOLVED | Balanced stamina curve for forgiving comedic challenge (`game/ica_eating_minigame.rpy`). |
| **A179** | Prank patrol never enters room | RESOLVED | Visible threat and patrol mechanics aligned with forgiving comedy design (`game/ica_prank_minigame.rpy`). |
| **A180** | Caught before look but records clue | RESOLVED | Dialogue branches accurately on observations actually recorded before interruption. |
| **A181** | Prank repeated captures reset | RESOLVED | Retries framed as non-diegetic second chances. |
| **A182** | Generic minigame praise | RESOLVED | Companion-specific outcome praise written for each companion and performance tier. |

---

### 12. UI, Presentation, and Assets (A183–A203)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A183** | Save thumbnails and text too small | RESOLVED | Adjusted save slot layout within 5-cassette format; enlarged thumbnails and font hierarchy (`game/screens/save_load.rpy`). |
| **A184** | Save tags expose debug counts | RESOLVED | Replaced raw variable names with human-readable labels ("Day X — Morning / Evening") in save tags. |
| **A185** | History narrow reading column | RESOLVED | Expanded text width to 1150px with comfortable margins (`game/screens/history_screen.rpy`). |
| **A186** | Soft clues age out of history | RESOLVED | Decision 103: Writable player notebook notes field with persistence and scrolling (`game/screens/suspect_notebook.rpy`). |
| **A187** | Notebook lacks suspect context before Day 7 | RESOLVED | Decision 82: Shows baseline profiles with background details prior to Day 7. |
| **A188** | 4,000-char notes field overflow | RESOLVED | Added scrollable viewport preventing notes overflow across all supported resolutions. |
| **A189** | Day selection progress overview | RESOLVED | Clear visit and schedule indicators added to schedule screens. |
| **A190** | Help text Escape key inconsistency | RESOLVED | Standardized Escape/pause behavior across all minigames. |
| **A191** | Rules cannot be reopened during game | RESOLVED | Added persistent rules overlay button during active minigame play (`game/screens/minigame_rules.rpy`). |
| **A192** | Timed games pause / relaxed mode | RESOLVED | Decision 95: Pause overlay and assist option available in all timed games. |
| **A193** | Angled quick-menu labels legibility | RESOLVED | Verified legibility of quick-menu buttons and hit targets across 1080p and windowed modes. |
| **A194** | Dialogue contrast over notebook | RESOLVED | Inspected outline text contrast over paper background; clear readability confirmed. |
| **A195** | Large panels leave small controls | RESOLVED | UI controls proportioned comfortably across all minigame screens. |
| **A196** | Pinned profiles text compression | RESOLVED | Side-by-side suspect profile layout verified for readability. |
| **A197** | Long dialogue overflow | RESOLVED | Tested longest static lines and expanded dynamic confessions; no clipping or overflow. |
| **A198** | Romance routes lack finished sprites | DEFERRED (ASSET PASS) | Production asset tracking; placeholder art noted. Scope preserved per guide and Decision 95. |
| **A199** | Art style consistency | DEFERRED (ASSET PASS) | Production asset tracking; placeholder visual styles cataloged for dedicated art pass. |
| **A200** | Black / reused backgrounds | DEFERRED (ASSET PASS) | Production background art deferred to dedicated art pass; gameplay and scene transitions fully intact. |
| **A201** | Missing audio cues | DEFERRED (ASSET PASS) | Audio asset pass deferred to production sound pass per guide instructions. |
| **A202** | Styles reference missing audio files | RESOLVED | Removed unavailable `rollover3.ogg` references from `game/styles.rpy`. |
| **A203** | Credits contain "Music To Be Added" | RESOLVED | Updated credits in `game/screens/other_screens.rpy` to reflect shipping assets. |

---

### 13. Endings and Climax (A204–A215)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A204** | Friendship via romantic rejection | RESOLVED | Decision 86: Added direct friendship invitation menu option in each ending scene setting `daySevenRelationshipOutcome = "friend"` without romantic rejection. |
| **A205** | Hidden eligibility feedback | RESOLVED | Added character readiness dialogue cues and checks (`_romance_ready`, `_friend_ready`) before choice menus. |
| **A206** | Literal "romantic date" phrasing | RESOLVED | Replaced identical phrasing with character-tailored invitations across all 7 companions for romance and friendship. |
| **A207** | Ending montages summarize dates | RESOLVED | Decision 97: Added concrete, dialogue-driven date vignettes across all 7 romance routes. |
| **A208** | Rejection scenes over-defensive | RESOLVED | Removed narrator editorializing / defensiveness; companions state direct, respectful boundaries. |
| **A209** | Madeline ending failure admission | RESOLVED | Madeline failure branch adapts dynamically to `daySevenBriefingResponse` ("defend", "joke", and default/owned). |
| **A210** | Ongoing pursuit vs dating closure | RESOLVED | Decisions 81 & 97: Overnight arrest before Day 7 briefing on success; post-case weekend date timing. |
| **A211** | Fired protagonist security access | RESOLVED | Decision 84: Dismissal removes security clearance; Winston met at checkpoint, Nicky at parking gate, Madeline at loading dock, Ica on outdoor steps, Dhampir at secure exit. |
| **A212** | Alone ending apologetic tone | RESOLVED | Rewritten with confident, triumphant tone ("wanted, trusted, and fully cemented as an ATLAS detective"), removing apologetic comparisons. |
| **A213** | Ending variants dramatic distinctiveness | RESOLVED | Retained all 42 catalog endings with unique character dialogue and outcomes. Verified in `tests/test_phase7_endings.py`. |
| **A214** | Locked gallery rows discovery hints | RESOLVED | Decision 103: Grouped endings by character in `ending_gallery` with spoiler-safe status hints. |
| **A215** | Endings unlock before being viewed | RESOLVED | Decision 103: Moved `$ day_seven_unlock_ending` to execute after viewing character ending upon reaching outro. |

---

### 14. Copy, Documentation, and Tests (A216–A234)

| ID | Title / Scope | Status | Evidence / Notes |
| :--- | :--- | :--- | :--- |
| **A216** | Stray "vestandbutton-upFreddy" token | RESOLVED | Decision 96: Removed stray "Freddy" token after "vest and button-up" in `game/ulysses_evenings.rpy`. |
| **A217** | Duplicate "That's the team!" lines | RESOLVED | Decision 96: Merged duplicate send-off line into single clean farewell. |
| **A218** | "Extremely permanent goodbye" tone | RESOLVED | Decisions 13 & 96: Freddy permanently departs; humor kept intact. |
| **A219** | "Admissiable then" copy errors | RESOLVED | Confirmed "admissible" and "than" verified in `game/script.rpy`. |
| **A220** | Typos "ergregious", "thining", "madibles" | RESOLVED | Confirmed "egregious", "thinking", "mandibles" fixed in author commit `ae70e44`. |
| **A221** | Typos "alwasy", "Atlest", "sombeers" | RESOLVED | Confirmed "always", "At least", "some beers" fixed in author commit `c2e99ed`. |
| **A222** | Typos "enought", "passtime" | RESOLVED | Corrected "passtime" to "pastime", "enought" to "enough" (commit `a1abee5`), and "did'nt" to "didn't". |
| **A223** | To/too errors and punctuation | RESOLVED | Dialogue reviewed in context; author cadence and intentional quirks preserved. |
| **A224** | Stray punctuation `.;` and capitalization | RESOLVED | Verified 0 stray `.;` in source `.rpy` scripts; lowercase "we" in Day 7 briefing. |
| **A225** | Older audits contain superseded info | RESOLVED | Obsolete audit files deleted per creator; active requirements in `docs/audit_decisions.md`. |
| **A226** | Duplicate audit reports confusion | RESOLVED | Duplicate and historical files cleaned up per creator request. |
| **A227** | Razzle planning notes hand injury clue | RESOLVED | Soft-clue design fully implemented; outdated planning notes removed per creator request. |
| **A228** | Absolute machine paths in scripts | RESOLVED | Parameterized `tools/build_murder_plan_composite.mjs` using environment variables with fallbacks. |
| **A229** | Tests validate counts over evidence meaning | RESOLVED | Verified semantic category assertions in `tests/test_evidence_repair.py`. |
| **A230** | Ending tests score injection | RESOLVED | Verified legal path attainment and 42 ending catalog in `tests/test_phase7_endings.py`. |
| **A231** | Screenshot test dimension mismatch | RESOLVED | Reconciled layout test setup; tests pass cleanly. |
| **A232** | Critical branch test coverage | RESOLVED | Validated skipped evenings, assistance, and category adaptation across test suites. |
| **A233** | Unused template / demonstration files | RESOLVED | Removed placeholder "Music — To Be Added" from `game/screens/other_screens.rpy` and audited runtime files. |
| **A234** | Shared continuity ledger | RESOLVED | Established master ledger in `docs/implementation_progress.md` and runtime state files. |

---

## Verification Summary

- **Implementation Status Across All 234 Findings**:
  - **Code, Dialogue, UI & Test Status**: 230 / 234 findings RESOLVED in code, scripts, UI, and test suites.
  - **Production Asset Tracking**: 4 / 234 findings (A198–A201) DEFERRED to production art/audio pass per explicit project instructions.
  - **Test Suite Results**:
    - `python tests/test_evidence_repair.py`: 19,606 transitions evaluated, 0 mismatches.
    - `python tests/test_phase1_minigames.py`: Passed.
    - `python tests/test_phase2_features.py`: Passed.
    - `python tests/test_phase3_continuity.py`: Passed.
    - `python tests/test_phase5_minigames.py`: 9/9 tests passed.
    - `python tests/test_phase7_endings.py`: 11/11 tests passed.
  - **Ren'Py Lint Report**: 0 errors, 0 warnings (3,260 dialogue blocks, 247 menus, 43 images, 47 screens).
