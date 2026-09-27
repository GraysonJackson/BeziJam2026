## Investigation state and reusable suspect-clue helpers.

define suspectNames = {
    1: "Victor Veytovi",
    2: "Jermiah Jones",
    3: "Barry Baxter",
    4: "Carl Creek",
    5: "Tucker Thompson",
    6: "Edgar Ebbington",
    7: "Simon Streep",
    8: "Kyle Kallus",
    9: "Alan Ashmore",
}

## Stable source-of-truth attributes used by every evidence route. The
## normalized "Scuffed Hands" value intentionally groups Tucker with the
## matching workbook category without changing the source workbook typo.
define suspectAttributes = {
    1: {"blood_type": "A", "rh_factor": "+", "power": "Fire", "height": "Short", "unique_drop": "Missing Hair", "unique_id": "Mole", "organization": "Clean", "build": "Brawny", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "Calculated"},
    2: {"blood_type": "B", "rh_factor": "+", "power": "Ice", "height": "Average", "unique_drop": "Missing Tooth", "unique_id": "Glasses", "organization": "Messy", "build": "Skinny", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "Panicked"},
    3: {"blood_type": "A", "rh_factor": "-", "power": "Ice", "height": "Tall", "unique_drop": "Ear Chunk", "unique_id": "Missing Arm", "organization": "Clean", "build": "Average", "injuries": "None", "hair": "Blonde", "temperament": "Calm", "kill_reaction": "None"},
    4: {"blood_type": "B", "rh_factor": "-", "power": "Ice", "height": "Average", "unique_drop": "Missing Hair", "unique_id": "Scar", "organization": "Clean", "build": "Skinny", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "None"},
    5: {"blood_type": "O", "rh_factor": "+", "power": "Fire", "height": "Tall", "unique_drop": "Missing Tooth", "unique_id": "Birthmark", "organization": "Messy", "build": "Average", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "Calculated"},
    6: {"blood_type": "A", "rh_factor": "+", "power": "Fire", "height": "Short", "unique_drop": "Ear Chunk", "unique_id": "Tattoos", "organization": "Messy", "build": "Brawny", "injuries": "None", "hair": "Blonde", "temperament": "Passionate", "kill_reaction": "Panicked"},
    7: {"blood_type": "B", "rh_factor": "-", "power": "Light", "height": "Short", "unique_drop": "Missing Hair", "unique_id": "Piercings", "organization": "Clean", "build": "Average", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "Panicked"},
    8: {"blood_type": "O", "rh_factor": "-", "power": "Light", "height": "Average", "unique_drop": "Missing Tooth", "unique_id": "Eye Patch", "organization": "Messy", "build": "Brawny", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "None"},
    9: {"blood_type": "O", "rh_factor": "+", "power": "Light", "height": "Tall", "unique_drop": "Ear Chunk", "unique_id": "Vitiligo", "organization": "Clean", "build": "Skinny", "injuries": "None", "hair": "Blonde", "temperament": "Nervous", "kill_reaction": "Calculated"},
}

## Shared one-person clearing used by routes whose first evidence visit clears
## a single suspect. This is keyed by the selected killer and is not owned by
## any one character route.
define singleEliminationByKiller = {
    1: 3,
    2: 1,
    3: 2,
    4: 5,
    5: 6,
    6: 4,
    7: 9,
    8: 7,
    9: 8,
}

define razzleFocusedRoutePlan = {
    1: {"height": "Tall"},
    2: {"height": "Short"},
    3: {"height": "Average"},
    4: {"height": "Tall"},
    5: {"height": "Short"},
    6: {"height": "Average"},
    7: {"height": "Tall"},
    8: {"height": "Short"},
    9: {"height": "Average"},
}

## Dhampir's first scene result is selected so that his third visit removes
## exactly two additional suspects from the planned injury group. This keeps
## his focused route at 9 -> 8 -> 6 before the positive visit-six evidence.
define dhampirDayOneEliminationByKiller = {
    1: 2,
    2: 3,
    3: 1,
    4: 5,
    5: 6,
    6: 4,
    7: 8,
    8: 9,
    9: 7,
}

## Madeline's fingerprint target is chosen from the blood-type group her
## third visit will exclude. The fingerprint clears one member first, so the
## blood test removes exactly two more while preserving the killer's complete
## three-person power group for the positive Visit 6 result.
define madelineDayOneEliminationByKiller = {
    1: 2,
    2: 5,
    3: 8,
    4: 9,
    5: 4,
    6: 7,
    7: 1,
    8: 3,
    9: 6,
}

define madelineFocusedRoutePlan = {
    1: {"blood_type": "B"},
    2: {"blood_type": "O"},
    3: {"blood_type": "O"},
    4: {"blood_type": "O"},
    5: {"blood_type": "B"},
    6: {"blood_type": "B"},
    7: {"blood_type": "A"},
    8: {"blood_type": "A"},
    9: {"blood_type": "A"},
}

## Nicky's alibi target is drawn from the build group her third visit will
## exclude. The focused build values also leave an even three-versus-three
## hygiene split for her final profile, guaranteeing 9 -> 8 -> 6 -> 3.
define nickyDayOneEliminationByKiller = {
    1: 2,
    2: 5,
    3: 4,
    4: 7,
    5: 4,
    6: 9,
    7: 9,
    8: 3,
    9: 3,
}

define nickyFocusedRoutePlan = {
    1: {"build": "Skinny"},
    2: {"build": "Average"},
    3: {"build": "Skinny"},
    4: {"build": "Average"},
    5: {"build": "Skinny"},
    6: {"build": "Skinny"},
    7: {"build": "Skinny"},
    8: {"build": "Average"},
    9: {"build": "Average"},
}

## Winston's interrogation route clears one person through a concrete lie on
## Visit 1, then clears two individually tested people through the pressure
## exercise on Visit 3.  All three early clears sit outside the killer's
## reaction trio so Visit 6 can positively retain exactly three suspects.
define winstonDayOneEliminationByKiller = {
    1: 2,
    2: 5,
    3: 1,
    4: 7,
    5: 4,
    6: 9,
    7: 8,
    8: 5,
    9: 6,
}

define winstonDayThreeEliminationsByKiller = {
    1: [3, 6],
    2: [1, 8],
    3: [2, 7],
    4: [1, 2],
    5: [2, 7],
    6: [1, 8],
    7: [1, 5],
    8: [1, 2],
    9: [3, 8],
}

## Stable route salts make mixed-route fallback selections deterministic.
## Authored results always remain first in the priority order; these values
## matter only when an earlier investigator has already cleared that person.
define investigationRouteSalts = {
    "razzle": 1,
    "madeline": 3,
    "winston": 5,
    "dhampir": 7,
    "nicky": 9,
}

## All five evidence characters live here. Generic cycle visits select a
## ruled-out attribute value that never contains the saved killer. Razzle,
## Madeline, and Dhampir use focused mappings where their route structure
## requires exact elimination counts.
define investigationRoutes = {
    "razzle": {
        "name": "Razzle Dazzle",
        "visits": {
            1: {"kind": "single", "eliminations": singleEliminationByKiller, "template": "Eyewitness evidence clears {suspect}."},
            3: {"kind": "razzle_attribute", "attribute": "height", "template": "Eyewitness evidence rules out {value} height."},
            6: {"kind": "retain_killer_attribute", "attribute": "hair", "template": "Eyewitness evidence identifies {value} hair."},
        },
    },
    "madeline": {
        "name": "Madeline",
        "visits": {
            1: {"kind": "single", "eliminations": madelineDayOneEliminationByKiller, "template": "Fingerprint analysis clears {suspect}."},
            3: {"kind": "madeline_attribute", "attribute": "blood_type", "template": "Lab evidence rules out blood type {value}."},
            6: {"kind": "retain_killer_attribute", "attribute": "power", "template": "Lab evidence identifies the {value} power category."},
        },
    },
    "winston": {
        "name": "Winston",
        "visits": {
            1: {"kind": "single", "eliminations": winstonDayOneEliminationByKiller, "template": "The interrogation clears {suspect}."},
            3: {"kind": "focused_pair", "attribute": "temperament", "eliminations": winstonDayThreeEliminationsByKiller, "template": "Controlled stress interviews clear {suspects}."},
            6: {"kind": "retain_killer_attribute", "attribute": "kill_reaction", "template": "Corroborated testimony identifies the killer's reaction as {value}."},
        },
    },
    "dhampir": {
        "name": "Dhampir",
        "visits": {
            1: {"kind": "single", "eliminations": dhampirDayOneEliminationByKiller, "template": "Crime-scene evidence clears {suspect}."},
            3: {"kind": "attribute", "attribute": "injuries", "cycle": {"Bruised Knuckles": "Scuffed Hands", "Scuffed Hands": "None", "None": "Bruised Knuckles"}, "template": "The wound comparison rules out suspects with {value}."},
            6: {"kind": "retain_killer_attribute", "attribute": "unique_drop", "template": "Recovered physical evidence identifies the {value} group."},
        },
    },
    "nicky": {
        "name": "Nicky",
        "visits": {
            1: {"kind": "single", "eliminations": nickyDayOneEliminationByKiller, "template": "Alibi verification clears {suspect}."},
            3: {"kind": "nicky_attribute", "attribute": "build", "template": "Corroborated records rule out the {value} build group."},
            6: {"kind": "retain_killer_attribute", "attribute": "organization", "template": "The behavioral profile identifies the attacker as {value}."},
        },
    },
}

default killer = 0
default remainingSuspects = [1, 2, 3, 4, 5, 6, 7, 8, 9]
default investigationClues = []
default recordedClueKeys = []
default recordedRouteReveals = {}
default playerInvestigationNotes = ""

init python:
    def initialize_investigation():
        """Choose one killer for a new game or a migrated pre-model save."""
        if store.killer not in store.suspectNames:
            store.killer = renpy.random.randint(1, 9)

        if config.developer:
            validate_investigation_routes()

    def validate_investigation_routes():
        """Validate pure routes and every legal six-day mixed-route state."""
        for route_id in store.investigationRoutes:
            for killer_id in store.suspectNames:
                active = set(store.suspectNames.keys())
                counts = []

                for visit in sorted(store.investigationRoutes[route_id]["visits"]):
                    reveal = get_planned_route_reveal(
                        route_id, visit, killer_id, active_suspects=active)
                    if killer_id in reveal["eliminated"]:
                        raise Exception("{} visit {} eliminates killer {}.".format(
                            route_id, visit, killer_id))

                    active.difference_update(reveal["eliminated"])
                    counts.append(len(active))

                if route_id == "razzle":
                    if counts[:2] != [8, 6]:
                        raise Exception("Razzle killer {} produced early counts {}, not 8/6.".format(
                            killer_id, counts[:2]))

                    killer_hair = store.suspectAttributes[killer_id]["hair"]
                    wrong_hair = [
                        suspect_id for suspect_id in active
                        if store.suspectAttributes[suspect_id]["hair"] != killer_hair
                    ]
                    if wrong_hair:
                        raise Exception(
                            "Razzle killer {} left non-matching hair suspects {}.".format(
                                killer_id, wrong_hair))

                if route_id in ("madeline", "winston", "dhampir", "nicky") and counts != [8, 6, 3]:
                    raise Exception("{} killer {} produced counts {}, not 8/6/3.".format(
                        store.investigationRoutes[route_id]["name"], killer_id, counts))

                if route_id == "madeline":
                    killer_power = store.suspectAttributes[killer_id]["power"]
                    wrong_power = [
                        suspect_id for suspect_id in active
                        if store.suspectAttributes[suspect_id]["power"] != killer_power
                    ]
                    if wrong_power:
                        raise Exception(
                            "Madeline killer {} left wrong-power suspects {}.".format(
                                killer_id, wrong_power))

                    soft_pairs = [
                        (
                            store.suspectAttributes[suspect_id]["injuries"],
                            store.suspectAttributes[suspect_id]["organization"],
                        )
                        for suspect_id in active
                    ]
                    if len(set(soft_pairs)) != len(soft_pairs):
                        raise Exception(
                            "Madeline killer {} has duplicate wound/organization hints {}."
                            .format(killer_id, soft_pairs))

                if route_id == "nicky":
                    killer_hygiene = store.suspectAttributes[killer_id]["organization"]
                    wrong_hygiene = [
                        suspect_id for suspect_id in active
                        if store.suspectAttributes[suspect_id]["organization"] != killer_hygiene
                    ]
                    if wrong_hygiene:
                        raise Exception(
                            "Nicky killer {} left wrong-hygiene suspects {}.".format(
                                killer_id, wrong_hygiene))

                    soft_profiles = [
                        (
                            store.suspectAttributes[suspect_id]["injuries"],
                            store.suspectAttributes[suspect_id]["blood_type"],
                            store.suspectAttributes[suspect_id]["rh_factor"],
                        )
                        for suspect_id in active
                    ]
                    if len(set(soft_profiles)) != len(soft_profiles):
                        raise Exception(
                            "Nicky killer {} has duplicate wound/blood hints {}."
                            .format(killer_id, soft_profiles))

                if route_id == "winston":
                    killer_reaction = store.suspectAttributes[killer_id]["kill_reaction"]
                    wrong_reaction = [
                        suspect_id for suspect_id in active
                        if store.suspectAttributes[suspect_id]["kill_reaction"] != killer_reaction
                    ]
                    if wrong_reaction:
                        raise Exception(
                            "Winston killer {} left wrong-reaction suspects {}."
                            .format(killer_id, wrong_reaction))

        validate_mixed_investigation_routes()

    def validate_mixed_investigation_routes():
        """Explore every reachable six-day evidence state without brute-force duplication."""
        route_ids = tuple(sorted(store.investigationRoutes.keys()))
        choice_ids = route_ids + ("ica",)
        expected_by_visit = {1: 1, 3: 2, 6: 3}

        for killer_id in store.suspectNames:
            initial_visits = tuple([0 for route_id in route_ids])
            states = {(initial_visits, tuple(sorted(store.suspectNames.keys())))}

            for day_index in range(6):
                next_states = set()
                for visit_tuple, active_tuple in states:
                    active = set(active_tuple)
                    for choice_id in choice_ids:
                        visits = dict(zip(route_ids, visit_tuple))
                        next_active = set(active)

                        if choice_id != "ica":
                            visits[choice_id] += 1
                            visit = visits[choice_id]
                            if visit in expected_by_visit:
                                reveal = get_planned_route_reveal(
                                    choice_id,
                                    visit,
                                    killer_id,
                                    active_suspects=next_active,
                                )
                                removed = [
                                    suspect_id for suspect_id in reveal["eliminated"]
                                    if suspect_id in next_active
                                ]
                                expected = expected_by_visit[visit]
                                if len(removed) != expected:
                                    raise Exception(
                                        "Mixed route day {} killer {} {} visit {} removed {}; expected {}."
                                        .format(day_index + 1, killer_id, choice_id,
                                                visit, removed, expected))
                                if killer_id in removed:
                                    raise Exception(
                                        "Mixed route {} visit {} eliminated killer {}."
                                        .format(choice_id, visit, killer_id))
                                next_active.difference_update(removed)

                        next_states.add((
                            tuple(visits[route_id] for route_id in route_ids),
                            tuple(sorted(next_active)),
                        ))
                states = next_states

            for visit_tuple, active_tuple in states:
                if all(visit == 1 for visit in visit_tuple):
                    if len(active_tuple) != 4 or killer_id not in active_tuple:
                        raise Exception(
                            "One-each strategy for killer {} left {}, not four including the killer."
                            .format(killer_id, active_tuple))

    def _investigation_priority(route_id, killer_id, preferred_ids):
        """Return a stable killer-safe priority list led by authored targets."""
        priority = []
        for suspect_id in preferred_ids:
            if suspect_id != killer_id and suspect_id not in priority:
                priority.append(suspect_id)

        salt = store.investigationRouteSalts.get(route_id, 0)
        rotated = list(sorted(store.suspectNames.keys()))
        offset = (killer_id + salt) % len(rotated)
        rotated = rotated[offset:] + rotated[:offset]
        for suspect_id in rotated:
            if suspect_id != killer_id and suspect_id not in priority:
                priority.append(suspect_id)
        return priority

    def _adapt_early_reveal(route_id, visit, killer_id, active_suspects,
                            preferred_ids, attribute=None, preferred_value=None):
        """Choose unused innocents while preserving authored pure-route results."""
        expected = 1 if visit == 1 else 2
        active = set(active_suspects)
        active.discard(killer_id)
        preferred_active = [
            suspect_id for suspect_id in preferred_ids
            if suspect_id in active
        ]

        if len(preferred_active) >= expected:
            chosen = preferred_active[:expected]
        else:
            chosen = list(preferred_active)
            priority = _investigation_priority(
                route_id, killer_id, preferred_ids)

            if attribute:
                candidate_values = []
                if preferred_value is not None:
                    candidate_values.append(preferred_value)
                for suspect_id in priority:
                    val = store.suspectAttributes[suspect_id][attribute]
                    if (val != store.suspectAttributes[killer_id][attribute]
                            and val not in candidate_values):
                        candidate_values.append(val)

                # First priority: find a candidate value with EXACTLY expected active innocents to complete category
                found_exact = False
                for val in candidate_values:
                    val_active = [
                        s for s in priority
                        if s in active and store.suspectAttributes[s][attribute] == val
                    ]
                    if len(val_active) == expected:
                        chosen = val_active
                        found_exact = True
                        break

                if not found_exact:
                    # Second priority: any candidate value with >= expected active innocents
                    for val in candidate_values:
                        val_active = [
                            s for s in priority
                            if s in active and store.suspectAttributes[s][attribute] == val
                        ]
                        if len(val_active) >= expected:
                            chosen = val_active[:expected]
                            found_exact = True
                            break

                if not found_exact:
                    for val in candidate_values:
                        same_value = [
                            suspect_id for suspect_id in priority
                            if (suspect_id in active
                                and suspect_id not in chosen
                                and store.suspectAttributes[suspect_id][attribute] == val)
                        ]
                        for suspect_id in same_value:
                            chosen.append(suspect_id)
                            if len(chosen) == expected:
                                break
                        if len(chosen) == expected:
                            break

            if len(chosen) < expected:
                for suspect_id in priority:
                    if suspect_id in active and suspect_id not in chosen:
                        chosen.append(suspect_id)
                        if len(chosen) == expected:
                            break

        if len(chosen) != expected:
            raise Exception(
                "Could not adapt {} visit {} for killer {} from active {}."
                .format(route_id, visit, killer_id, sorted(active_suspects)))
        return sorted(chosen)

    def get_planned_route_reveal(route_id, visit, killer_id=None,
                                 active_suspects=None):
        """Resolve one route/visit into a killer-safe clue and suspect list."""
        clue_key = "{}_visit_{}".format(route_id, visit)
        use_saved_state = killer_id is None and active_suspects is None
        if use_saved_state and clue_key in store.recordedRouteReveals:
            return dict(store.recordedRouteReveals[clue_key])

        if killer_id is None:
            killer_id = store.killer
        if active_suspects is None:
            active_suspects = set(store.remainingSuspects)
        else:
            active_suspects = set(active_suspects)

        route = store.investigationRoutes.get(route_id)
        if route is None or visit not in route["visits"]:
            raise Exception("Unknown investigation reveal: {} visit {}".format(route_id, visit))

        reveal = route["visits"][visit]
        kind = reveal["kind"]

        if kind == "single":
            suspect_id = reveal["eliminations"][killer_id]
            eliminated_ids = _adapt_early_reveal(
                route_id, visit, killer_id, active_suspects, [suspect_id])
            suspect_id = eliminated_ids[0]
            value = store.suspectAttributes[suspect_id]["unique_id"]
            clue_text = reveal["template"].format(
                suspect=store.suspectNames[suspect_id], value=value)
        elif kind == "focused_pair":
            attribute = reveal["attribute"]
            preferred_ids = list(reveal["eliminations"][killer_id])
            eliminated_ids = _adapt_early_reveal(
                route_id,
                visit,
                killer_id,
                active_suspects,
                preferred_ids,
                attribute=attribute,
            )
            value = "Individual profiles"
            suspect_text = " and ".join(
                store.suspectNames[suspect_id] for suspect_id in eliminated_ids)
            clue_text = reveal["template"].format(
                suspects=suspect_text, value=value)
        else:
            attribute = reveal["attribute"]
            if kind == "retain_killer_attribute":
                value = store.suspectAttributes[killer_id][attribute]
                eliminated_ids = sorted([
                    suspect_id for suspect_id, attributes in store.suspectAttributes.items()
                    if attributes[attribute] != value
                ])
                clue_text = reveal["template"].format(value=value)
            else:
                if kind == "razzle_attribute":
                    orig_val = store.razzleFocusedRoutePlan[killer_id][attribute]
                elif kind == "madeline_attribute":
                    orig_val = store.madelineFocusedRoutePlan[killer_id][attribute]
                elif kind == "nicky_attribute":
                    orig_val = store.nickyFocusedRoutePlan[killer_id][attribute]
                else:
                    killer_value = store.suspectAttributes[killer_id][attribute]
                    orig_val = reveal["cycle"][killer_value]

                preferred_ids = sorted([
                    suspect_id for suspect_id, attributes in store.suspectAttributes.items()
                    if attributes[attribute] == orig_val
                ])
                eliminated_ids = _adapt_early_reveal(
                    route_id, visit, killer_id, active_suspects,
                    preferred_ids, attribute=attribute,
                    preferred_value=orig_val)

                # Determine actual eliminated category / value
                selected_values = set(
                    store.suspectAttributes[suspect_id][attribute]
                    for suspect_id in eliminated_ids
                )
                if len(selected_values) == 1:
                    selected_val = list(selected_values)[0]
                    active_with_val = set(
                        s for s in active_suspects
                        if s != killer_id and store.suspectAttributes[s][attribute] == selected_val
                    )
                    category_complete = active_with_val == set(eliminated_ids)
                else:
                    category_complete = False

                if category_complete:
                    value = selected_val
                    clue_text = reveal["template"].format(value=value)
                else:
                    value = "Individual profiles"
                    names = " and ".join(store.suspectNames[s] for s in eliminated_ids)
                    if route_id == "razzle":
                        clue_text = "Doorframe measurements clear the individual profiles for {}.".format(names)
                    elif route_id == "madeline":
                        clue_text = "Separated blood markers clear the individual reference profiles for {}.".format(names)
                    elif route_id == "dhampir":
                        clue_text = "The reconstruction clears the individual wound profiles for {}.".format(names)
                    elif route_id == "nicky":
                        clue_text = "Corroborated measurements clear the individual profiles for {}.".format(names)
                    else:
                        clue_text = "Analysis clears the individual profiles for {}.".format(names)

        if visit in (1, 3):
            preferred_set = set(preferred_ids if kind != "single" else [reveal["eliminations"][killer_id]])
            adaptive = not set(eliminated_ids).issubset(preferred_set)
        else:
            adaptive = False

        if killer_id in eliminated_ids:
            raise Exception("Planned reveal {} visit {} eliminates killer {}.".format(
                route_id, visit, killer_id))

        result = {
            "route_id": route_id,
            "route": route["name"],
            "visit": visit,
            "text": clue_text,
            "value": value,
            "eliminated": eliminated_ids,
            "adaptive": adaptive,
            "details": [
                {
                    "id": suspect_id,
                    "name": store.suspectNames[suspect_id],
                    "attributes": store.suspectAttributes[suspect_id],
                }
                for suspect_id in eliminated_ids
            ],
        }

        if visit == 3:
            attribute = reveal.get("attribute")
            selected_values = set(
                store.suspectAttributes[suspect_id][attribute]
                for suspect_id in eliminated_ids
            ) if attribute else set()
            if len(selected_values) == 1 and kind != "focused_pair":
                selected_value = list(selected_values)[0]
                active_with_value = set(
                    suspect_id for suspect_id in active_suspects
                    if (suspect_id != killer_id
                        and store.suspectAttributes[suspect_id][attribute] == selected_value)
                )
                category_complete = active_with_value == set(eliminated_ids)
            else:
                category_complete = False
            result["scope"] = "category" if category_complete else "individual"
            result["selected_values"] = sorted(selected_values)
            result["value"] = value
            result["text"] = clue_text
            target_val = list(selected_values)[0] if selected_values else (orig_val if "orig_val" in locals() else value)
            result["target_value"] = target_val
            result["target_injury"] = target_val if route_id == "dhampir" else None
            result["target_height"] = target_val if route_id == "razzle" else None
            result["target_blood_type"] = target_val if route_id == "madeline" else None
            result["target_build"] = target_val if route_id == "nicky" else None
        else:
            result["scope"] = "single" if visit == 1 else "category"

        return result

    def record_investigation_clue(clue_key, route, visit, clue_text, eliminated_ids, expected_count=None):
        """Record one clue and remove its suspects exactly once."""
        if clue_key in store.recordedClueKeys:
            return 0

        current = list(store.remainingSuspects)
        removed = []

        for suspect_id in eliminated_ids:
            if suspect_id == store.killer:
                message = "Clue {} attempted to eliminate the killer.".format(clue_key)
                if config.developer:
                    raise Exception(message)
                renpy.log(message)
                continue

            if suspect_id in current:
                current.remove(suspect_id)
                removed.append(suspect_id)

        if expected_count is not None and len(removed) != expected_count:
            message = "Clue {} removed {} suspects; expected {}.".format(
                clue_key, len(removed), expected_count)
            if config.developer:
                raise Exception(message)
            renpy.log(message)

        store.remainingSuspects = current
        store.investigationClues = store.investigationClues + [{
            "key": clue_key,
            "route": route,
            "visit": visit,
            "text": clue_text,
            "eliminated": removed,
            "eliminated_names": [store.suspectNames[suspect_id] for suspect_id in removed],
        }]
        store.recordedClueKeys = store.recordedClueKeys + [clue_key]

        return len(removed)

    def record_planned_route_reveal(route_id, visit, clue_text=None,
                                    expected_count=None):
        """Calculate, apply, and log a route reveal without duplicating IDs."""
        reveal = get_planned_route_reveal(route_id, visit)
        clue_key = "{}_visit_{}".format(route_id, visit)
        removed_count = record_investigation_clue(
            clue_key,
            reveal["route"],
            visit,
            clue_text or reveal["text"],
            reveal["eliminated"],
            expected_count=expected_count,
        )
        if clue_key not in store.recordedRouteReveals:
            saved_reveals = dict(store.recordedRouteReveals)
            saved_reveals[clue_key] = dict(reveal)
            store.recordedRouteReveals = saved_reveals
        return removed_count
