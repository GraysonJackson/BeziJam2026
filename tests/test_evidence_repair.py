import sys

suspectNames = {
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

suspectAttributes = {
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

singleEliminationByKiller = {1: 3, 2: 1, 3: 2, 4: 5, 5: 6, 6: 4, 7: 9, 8: 7, 9: 8}
razzleFocusedRoutePlan = {1: {"height": "Tall"}, 2: {"height": "Short"}, 3: {"height": "Average"}, 4: {"height": "Tall"}, 5: {"height": "Short"}, 6: {"height": "Average"}, 7: {"height": "Tall"}, 8: {"height": "Short"}, 9: {"height": "Average"}}
dhampirDayOneEliminationByKiller = {1: 2, 2: 3, 3: 1, 4: 5, 5: 6, 6: 4, 7: 8, 8: 9, 9: 7}
madelineDayOneEliminationByKiller = {1: 2, 2: 5, 3: 8, 4: 9, 5: 4, 6: 7, 7: 1, 8: 3, 9: 6}
madelineFocusedRoutePlan = {1: {"blood_type": "B"}, 2: {"blood_type": "O"}, 3: {"blood_type": "O"}, 4: {"blood_type": "O"}, 5: {"blood_type": "B"}, 6: {"blood_type": "B"}, 7: {"blood_type": "A"}, 8: {"blood_type": "A"}, 9: {"blood_type": "A"}}
nickyDayOneEliminationByKiller = {1: 2, 2: 5, 3: 4, 4: 7, 5: 4, 6: 9, 7: 9, 8: 3, 9: 3}
nickyFocusedRoutePlan = {1: {"build": "Skinny"}, 2: {"build": "Average"}, 3: {"build": "Skinny"}, 4: {"build": "Average"}, 5: {"build": "Skinny"}, 6: {"build": "Skinny"}, 7: {"build": "Skinny"}, 8: {"build": "Average"}, 9: {"build": "Average"}}
winstonDayOneEliminationByKiller = {1: 2, 2: 5, 3: 1, 4: 7, 5: 4, 6: 9, 7: 8, 8: 5, 9: 6}
winstonDayThreeEliminationsByKiller = {1: [3, 6], 2: [1, 8], 3: [2, 7], 4: [1, 2], 5: [2, 7], 6: [1, 8], 7: [1, 5], 8: [1, 2], 9: [3, 8]}
investigationRouteSalts = {"razzle": 1, "madeline": 3, "winston": 5, "dhampir": 7, "nicky": 9}

investigationRoutes = {
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

def _investigation_priority(route_id, killer_id, preferred_ids):
    priority = []
    for suspect_id in preferred_ids:
        if suspect_id != killer_id and suspect_id not in priority:
            priority.append(suspect_id)

    salt = investigationRouteSalts.get(route_id, 0)
    rotated = list(sorted(suspectNames.keys()))
    offset = (killer_id + salt) % len(rotated)
    rotated = rotated[offset:] + rotated[:offset]
    for suspect_id in rotated:
        if suspect_id != killer_id and suspect_id not in priority:
            priority.append(suspect_id)
    return priority

def _adapt_early_reveal_original(route_id, visit, killer_id, active_suspects,
                        preferred_ids, attribute=None, preferred_value=None):
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
                value = suspectAttributes[suspect_id][attribute]
                if (value != suspectAttributes[killer_id][attribute]
                        and value not in candidate_values):
                    candidate_values.append(value)

            for value in candidate_values:
                same_value = [
                    suspect_id for suspect_id in priority
                    if (suspect_id in active
                        and suspect_id not in chosen
                        and suspectAttributes[suspect_id][attribute] == value)
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

def get_planned_route_reveal_original(route_id, visit, killer_id, active_suspects):
    route = investigationRoutes.get(route_id)
    reveal = route["visits"][visit]
    kind = reveal["kind"]

    if kind == "single":
        suspect_id = reveal["eliminations"][killer_id]
        eliminated_ids = _adapt_early_reveal_original(
            route_id, visit, killer_id, active_suspects, [suspect_id])
        suspect_id = eliminated_ids[0]
        value = suspectAttributes[suspect_id]["unique_id"]
        clue_text = reveal["template"].format(
            suspect=suspectNames[suspect_id], value=value)
    elif kind == "focused_pair":
        attribute = reveal["attribute"]
        preferred_ids = list(reveal["eliminations"][killer_id])
        eliminated_ids = _adapt_early_reveal_original(
            route_id, visit, killer_id, active_suspects, preferred_ids, attribute=attribute)
        value = "Individual profiles"
        suspect_text = " and ".join(
            suspectNames[suspect_id] for suspect_id in eliminated_ids)
        clue_text = reveal["template"].format(
            suspects=suspect_text, value=value)
    else:
        attribute = reveal["attribute"]
        if kind == "retain_killer_attribute":
            value = suspectAttributes[killer_id][attribute]
            eliminated_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] != value
            ])
        elif kind == "razzle_attribute":
            value = razzleFocusedRoutePlan[killer_id][attribute]
            preferred_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] == value
            ])
            eliminated_ids = _adapt_early_reveal_original(
                route_id, visit, killer_id, active_suspects,
                preferred_ids, attribute=attribute, preferred_value=value)
        elif kind == "madeline_attribute":
            value = madelineFocusedRoutePlan[killer_id][attribute]
            preferred_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] == value
            ])
            eliminated_ids = _adapt_early_reveal_original(
                route_id, visit, killer_id, active_suspects,
                preferred_ids, attribute=attribute, preferred_value=value)
        elif kind == "nicky_attribute":
            value = nickyFocusedRoutePlan[killer_id][attribute]
            preferred_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] == value
            ])
            eliminated_ids = _adapt_early_reveal_original(
                route_id, visit, killer_id, active_suspects,
                preferred_ids, attribute=attribute, preferred_value=value)
        else:
            killer_value = suspectAttributes[killer_id][attribute]
            value = reveal["cycle"][killer_value]
            preferred_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] == value
            ])
            eliminated_ids = _adapt_early_reveal_original(
                route_id, visit, killer_id, active_suspects,
                preferred_ids, attribute=attribute, preferred_value=value)
        clue_text = reveal["template"].format(value=value)

    result = {
        "route_id": route_id,
        "visit": visit,
        "text": clue_text,
        "value": value,
        "eliminated": eliminated_ids,
    }

    if visit == 3:
        attribute = reveal.get("attribute")
        selected_values = set(
            suspectAttributes[suspect_id][attribute]
            for suspect_id in eliminated_ids
        ) if attribute else set()
        if len(selected_values) == 1:
            selected_value = list(selected_values)[0]
            active_with_value = set(
                suspect_id for suspect_id in active_suspects
                if (suspect_id != killer_id
                    and suspectAttributes[suspect_id][attribute] == selected_value)
            )
            category_complete = active_with_value == set(eliminated_ids)
        else:
            category_complete = False
        result["scope"] = "category" if category_complete else "individual"
        result["selected_values"] = sorted(selected_values)
    else:
        result["scope"] = "single" if visit == 1 else "category"

    return result

def run_enumeration(get_reveal_fn):
    route_ids = tuple(sorted(investigationRoutes.keys()))
    choice_ids = route_ids + ("ica",)
    expected_by_visit = {1: 1, 3: 2, 6: 3}
    mismatches = []
    total_transitions = 0

    for killer_id in suspectNames:
        initial_visits = tuple([0 for _ in route_ids])
        states = {(initial_visits, tuple(sorted(suspectNames.keys())))}

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
                            total_transitions += 1
                            reveal = get_reveal_fn(
                                choice_id,
                                visit,
                                killer_id,
                                active_suspects=next_active,
                            )
                            removed = [
                                s for s in reveal["eliminated"]
                                if s in next_active
                            ]
                            
                            # Check category / value truthfulness:
                            if visit == 3 and choice_id != "winston":
                                attr = investigationRoutes[choice_id]["visits"][visit]["attribute"]
                                # What are the actual attributes of the removed suspects?
                                removed_attrs = [suspectAttributes[s][attr] for s in removed]
                                if reveal.get("scope") == "category":
                                    # Claim: category reveal["value"] is excluded
                                    # Therefore, every removed suspect MUST have this value
                                    # AND no other active suspect (other than killer) has this value!
                                    claimed_val = reveal["value"]
                                    if any(a != claimed_val for a in removed_attrs):
                                        mismatches.append({
                                            "killer": killer_id,
                                            "route": choice_id,
                                            "day": day_index + 1,
                                            "claimed_val": claimed_val,
                                            "removed_attrs": removed_attrs,
                                            "active": sorted(next_active),
                                            "removed": removed,
                                        })
                                    # Also check if any active suspect with claimed_val was NOT removed
                                    active_with_val = [s for s in next_active if s != killer_id and suspectAttributes[s][attr] == claimed_val]
                                    if set(active_with_val) != set(removed):
                                        mismatches.append({
                                            "killer": killer_id,
                                            "route": choice_id,
                                            "day": day_index + 1,
                                            "reason": "claimed category not fully removed",
                                            "claimed_val": claimed_val,
                                            "active_with_val": active_with_val,
                                            "removed": removed,
                                        })
                            next_active.difference_update(removed)

                    next_states.add((
                        tuple(visits[route_id] for route_id in route_ids),
                        tuple(sorted(next_active)),
                    ))
            states = next_states

    return total_transitions, mismatches

def _adapt_early_reveal_fixed(route_id, visit, killer_id, active_suspects,
                             preferred_ids, attribute=None, preferred_value=None):
    expected = 1 if visit == 1 else 2
    active = set(active_suspects)
    active.discard(killer_id)
    preferred_active = [
        suspect_id for suspect_id in preferred_ids
        if suspect_id in active
    ]

    # If preferred active innocents can satisfy expected:
    # But wait: if attribute is given, we also prefer complete category exclusions if possible!
    if len(preferred_active) >= expected:
        # Check if eliminating preferred_active[:expected] completes the category or if there are leftover active suspects with preferred_value
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
                val = suspectAttributes[suspect_id][attribute]
                if (val != suspectAttributes[killer_id][attribute]
                        and val not in candidate_values):
                    candidate_values.append(val)

            # First priority: is there a candidate value that has EXACTLY expected active innocents?
            # If so, choosing all of them makes a clean category exclusion!
            found_exact = False
            for val in candidate_values:
                val_active = [
                    s for s in priority
                    if s in active and suspectAttributes[s][attribute] == val
                ]
                if len(val_active) == expected:
                    chosen = val_active
                    found_exact = True
                    break

            if not found_exact:
                # Second priority: any candidate value with >= expected active innocents?
                for val in candidate_values:
                    val_active = [
                        s for s in priority
                        if s in active and suspectAttributes[s][attribute] == val
                    ]
                    if len(val_active) >= expected:
                        chosen = val_active[:expected]
                        found_exact = True
                        break

            if not found_exact:
                # Fallback: fill across values
                for val in candidate_values:
                    same_value = [
                        s for s in priority
                        if (s in active
                            and s not in chosen
                            and suspectAttributes[s][attribute] == val)
                    ]
                    for s in same_value:
                        chosen.append(s)
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

def get_planned_route_reveal_fixed(route_id, visit, killer_id, active_suspects):
    route = investigationRoutes.get(route_id)
    reveal = route["visits"][visit]
    kind = reveal["kind"]

    if kind == "single":
        suspect_id = reveal["eliminations"][killer_id]
        eliminated_ids = _adapt_early_reveal_fixed(
            route_id, visit, killer_id, active_suspects, [suspect_id])
        suspect_id = eliminated_ids[0]
        value = suspectAttributes[suspect_id]["unique_id"]
        clue_text = reveal["template"].format(
            suspect=suspectNames[suspect_id], value=value)
    elif kind == "focused_pair":
        attribute = reveal["attribute"]
        preferred_ids = list(reveal["eliminations"][killer_id])
        eliminated_ids = _adapt_early_reveal_fixed(
            route_id, visit, killer_id, active_suspects, preferred_ids, attribute=attribute)
        value = "Individual profiles"
        suspect_text = " and ".join(
            suspectNames[suspect_id] for suspect_id in eliminated_ids)
        clue_text = reveal["template"].format(
            suspects=suspect_text, value=value)
    else:
        attribute = reveal["attribute"]
        if kind == "retain_killer_attribute":
            value = suspectAttributes[killer_id][attribute]
            eliminated_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] != value
            ])
            clue_text = reveal["template"].format(value=value)
        else:
            if kind == "razzle_attribute":
                orig_val = razzleFocusedRoutePlan[killer_id][attribute]
            elif kind == "madeline_attribute":
                orig_val = madelineFocusedRoutePlan[killer_id][attribute]
            elif kind == "nicky_attribute":
                orig_val = nickyFocusedRoutePlan[killer_id][attribute]
            else:
                killer_value = suspectAttributes[killer_id][attribute]
                orig_val = reveal["cycle"][killer_value]

            preferred_ids = sorted([
                suspect_id for suspect_id, attributes in suspectAttributes.items()
                if attributes[attribute] == orig_val
            ])
            eliminated_ids = _adapt_early_reveal_fixed(
                route_id, visit, killer_id, active_suspects,
                preferred_ids, attribute=attribute, preferred_value=orig_val)

            # Determine actual eliminated category / value
            selected_values = set(
                suspectAttributes[suspect_id][attribute]
                for suspect_id in eliminated_ids
            )
            if len(selected_values) == 1:
                selected_val = list(selected_values)[0]
                active_with_val = set(
                    s for s in active_suspects
                    if s != killer_id and suspectAttributes[s][attribute] == selected_val
                )
                category_complete = active_with_val == set(eliminated_ids)
            else:
                category_complete = False

            if category_complete:
                value = selected_val
                clue_text = reveal["template"].format(value=value)
            else:
                value = "Individual profiles"
                names = " and ".join(suspectNames[s] for s in eliminated_ids)
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

    result = {
        "route_id": route_id,
        "visit": visit,
        "text": clue_text,
        "value": value,
        "eliminated": eliminated_ids,
    }

    if visit == 3:
        attribute = reveal.get("attribute")
        selected_values = set(
            suspectAttributes[suspect_id][attribute]
            for suspect_id in eliminated_ids
        ) if attribute else set()
        if len(selected_values) == 1 and kind != "focused_pair":
            selected_value = list(selected_values)[0]
            active_with_value = set(
                suspect_id for suspect_id in active_suspects
                if (suspect_id != killer_id
                    and suspectAttributes[suspect_id][attribute] == selected_value)
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

total_transitions_fixed, mismatches_fixed = run_enumeration(get_planned_route_reveal_fixed)
print(f"Total deduplicated transitions evaluated (fixed): {total_transitions_fixed}")
print(f"Total mismatches found in fixed: {len(mismatches_fixed)}")
assert len(mismatches_fixed) == 0, f"Expected 0 mismatches, found {len(mismatches_fixed)}"

# Case 1 (A004): Killer 4, Razzle 3 then Madeline 3
# Visit sequence: razzle 1, razzle 2, razzle 3, madeline 1, madeline 2, madeline 3
active = set(suspectNames.keys())
r1 = get_planned_route_reveal_fixed("razzle", 1, 4, active)
active.difference_update(r1["eliminated"])
r3 = get_planned_route_reveal_fixed("razzle", 3, 4, active)
active.difference_update(r3["eliminated"])
m1 = get_planned_route_reveal_fixed("madeline", 1, 4, active)
active.difference_update(m1["eliminated"])
m3 = get_planned_route_reveal_fixed("madeline", 3, 4, active)
print(f"A004 check: m3 value={m3['value']}, scope={m3['scope']}, text={m3['text']}, eliminated={m3['eliminated']}")
assert m3["value"] == "A", f"Expected value 'A', got {m3['value']}"
assert m3["scope"] == "category", f"Expected scope 'category', got {m3['scope']}"
assert m3["eliminated"] == [1, 6], f"Expected [1, 6], got {m3['eliminated']}"
assert "rules out blood type A" in m3["text"]

# Case 2 (A005): Killer 1, Nicky/Dhampir/Madeline/Razzle/Razzle/Razzle
active = set(suspectNames.keys())
n1 = get_planned_route_reveal_fixed("nicky", 1, 1, active)
active.difference_update(n1["eliminated"])
d1 = get_planned_route_reveal_fixed("dhampir", 1, 1, active)
active.difference_update(d1["eliminated"])
m1 = get_planned_route_reveal_fixed("madeline", 1, 1, active)
active.difference_update(m1["eliminated"])
# Razzle 1 (day 4)
r1 = get_planned_route_reveal_fixed("razzle", 1, 1, active)
active.difference_update(r1["eliminated"])
# Razzle 2 (day 5, no evidence)
# Razzle 3 (day 6)
r3 = get_planned_route_reveal_fixed("razzle", 3, 1, active)
print(f"A005 check 1: r3 value={r3['value']}, scope={r3['scope']}, text={r3['text']}, eliminated={r3['eliminated']}")
assert r3["value"] != "Tall" or [suspectAttributes[s]["height"] for s in r3["eliminated"]] == ["Tall", "Tall"]
for s in r3["eliminated"]:
    if r3["scope"] == "category":
        assert suspectAttributes[s]["height"] == r3["value"]

# Case 3 (A005): Killer 1, Madeline/Dhampir/Nicky/Nicky/Razzle/Nicky
active = set(suspectNames.keys())
m1 = get_planned_route_reveal_fixed("madeline", 1, 1, active)
active.difference_update(m1["eliminated"])
d1 = get_planned_route_reveal_fixed("dhampir", 1, 1, active)
active.difference_update(d1["eliminated"])
n1 = get_planned_route_reveal_fixed("nicky", 1, 1, active)
active.difference_update(n1["eliminated"])
# Nicky 2 (day 4, no evidence)
# Razzle 1 (day 5)
r1 = get_planned_route_reveal_fixed("razzle", 1, 1, active)
active.difference_update(r1["eliminated"])
# Nicky 3 (day 6)
n3 = get_planned_route_reveal_fixed("nicky", 3, 1, active)
print(f"A005 check 2: n3 value={n3['value']}, scope={n3['scope']}, text={n3['text']}, eliminated={n3['eliminated']}")
for s in n3["eliminated"]:
    if n3["scope"] == "category":
        assert suspectAttributes[s]["build"] == n3["value"]

# Case 4 (A005): Killer 3, Winston 3 times, Dhampir 3 times
active = set(suspectNames.keys())
w1 = get_planned_route_reveal_fixed("winston", 1, 3, active)
active.difference_update(w1["eliminated"])
# Winston 2
w3 = get_planned_route_reveal_fixed("winston", 3, 3, active)
active.difference_update(w3["eliminated"])
d1 = get_planned_route_reveal_fixed("dhampir", 1, 3, active)
active.difference_update(d1["eliminated"])
# Dhampir 2
d3 = get_planned_route_reveal_fixed("dhampir", 3, 3, active)
print(f"A005 check 3: d3 value={d3['value']}, scope={d3['scope']}, text={d3['text']}, eliminated={d3['eliminated']}")
assert d3["value"] == "Scuffed Hands"
assert d3["scope"] == "category"
assert d3["eliminated"] == [5, 8]
assert "Scuffed Hands" in d3["text"]

# Case 5 (Dhampir individual scope consumer check):
# Killer 1, path: ('dhampir', 'dhampir', 'madeline', 'dhampir')
active = set(suspectNames.keys())
d1 = get_planned_route_reveal_fixed("dhampir", 1, 1, active)
active.difference_update(d1["eliminated"])
# Dhampir 2 (no eliminations)
m1 = get_planned_route_reveal_fixed("madeline", 1, 1, active)
active.difference_update(m1["eliminated"])
# Dhampir 3
d3_ind = get_planned_route_reveal_fixed("dhampir", 3, 1, active)
print(f"Dhampir individual check: d3 value={d3_ind['value']}, scope={d3_ind['scope']}, target_injury={d3_ind['target_injury']}, eliminated={d3_ind['eliminated']}")
assert d3_ind["scope"] == "individual"
assert d3_ind["value"] == "Individual profiles"
assert d3_ind["target_injury"] in ("Bruised Knuckles", "Scuffed Hands", "None")
assert d3_ind["eliminated"] == [3, 9]
assert "individual wound profiles" in d3_ind["text"]

print("All regression checks passed successfully!")




