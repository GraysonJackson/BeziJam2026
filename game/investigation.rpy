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
    1: {"blood_type": "A", "power": "Fire", "height": "Short", "unique_drop": "Missing Hair", "unique_id": "Mole", "organization": "Clean", "build": "Brawny", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "Calculated"},
    2: {"blood_type": "B", "power": "Ice", "height": "Average", "unique_drop": "Missing Tooth", "unique_id": "Glasses", "organization": "Messy", "build": "Skinny", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "Panicked"},
    3: {"blood_type": "A", "power": "Ice", "height": "Tall", "unique_drop": "Ear Chunk", "unique_id": "Missing Arm", "organization": "Clean", "build": "Average", "injuries": "None", "hair": "Blonde", "temperament": "Calm", "kill_reaction": "None"},
    4: {"blood_type": "O", "power": "Ice", "height": "Average", "unique_drop": "Missing Hair", "unique_id": "Scar", "organization": "Clean", "build": "Skinny", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "None"},
    5: {"blood_type": "O", "power": "Fire", "height": "Tall", "unique_drop": "Missing Tooth", "unique_id": "Birthmark", "organization": "Messy", "build": "Average", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "Calculated"},
    6: {"blood_type": "B", "power": "Fire", "height": "Short", "unique_drop": "Ear Chunk", "unique_id": "Tattoos", "organization": "Messy", "build": "Brawny", "injuries": "None", "hair": "Blonde", "temperament": "Passionate", "kill_reaction": "Panicked"},
    7: {"blood_type": "A", "power": "Light", "height": "Short", "unique_drop": "Missing Hair", "unique_id": "Piercings", "organization": "Clean", "build": "Average", "injuries": "Bruised Knuckles", "hair": "Brown", "temperament": "Calm", "kill_reaction": "Panicked"},
    8: {"blood_type": "O", "power": "Light", "height": "Average", "unique_drop": "Missing Tooth", "unique_id": "Eye Patch", "organization": "Messy", "build": "Brawny", "injuries": "Scuffed Hands", "hair": "Black", "temperament": "Passionate", "kill_reaction": "None"},
    9: {"blood_type": "B", "power": "Light", "height": "Tall", "unique_drop": "Ear Chunk", "unique_id": "Vitiligo", "organization": "Clean", "build": "Skinny", "injuries": "None", "hair": "Blonde", "temperament": "Nervous", "kill_reaction": "Calculated"},
}

## Shared one-person clearing used by routes whose first evidence visit clears
## a single suspect. This is keyed by the selected killer and is not owned by
## any one character route.
define singleEliminationByKiller = {
    1: 2,
    2: 5,
    3: 1,
    4: 7,
    5: 4,
    6: 9,
    7: 8,
    8: 3,
    9: 6,
}

define razzleFocusedRoutePlan = {
    1: {"height": "Average"},
    2: {"height": "Tall"},
    3: {"height": "Short"},
    4: {"height": "Short"},
    5: {"height": "Average"},
    6: {"height": "Tall"},
    7: {"height": "Average"},
    8: {"height": "Tall"},
    9: {"height": "Short"},
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

## All five evidence characters live here. For unwritten visits, the cycle
## selects a ruled-out attribute value that never contains the saved killer.
## The exact number removed can differ outside Razzle because the source
## attribute groups are not all balanced 3/3/3.
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
            1: {"kind": "single", "eliminations": singleEliminationByKiller, "template": "Fingerprint analysis clears {suspect}."},
            3: {"kind": "attribute", "attribute": "blood_type", "cycle": {"A": "B", "B": "O", "O": "A"}, "template": "Lab evidence rules out blood type {value}."},
            6: {"kind": "attribute", "attribute": "power", "cycle": {"Fire": "Ice", "Ice": "Light", "Light": "Fire"}, "template": "Lab evidence rules out the {value} power type."},
        },
    },
    "winston": {
        "name": "Winston",
        "visits": {
            1: {"kind": "single", "eliminations": singleEliminationByKiller, "template": "The interrogation clears {suspect}."},
            3: {"kind": "attribute", "attribute": "temperament", "cycle": {"Calm": "Passionate", "Passionate": "Calm", "Nervous": "Passionate"}, "template": "Behavioral evidence rules out the {value} temperament group."},
            6: {"kind": "attribute", "attribute": "kill_reaction", "cycle": {"Panicked": "Calculated", "Calculated": "None", "None": "Panicked"}, "template": "The interrogation rules out the {value} killing-reaction group."},
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
            1: {"kind": "single", "eliminations": singleEliminationByKiller, "template": "Alibi verification clears {suspect}."},
            3: {"kind": "attribute", "attribute": "build", "cycle": {"Brawny": "Skinny", "Skinny": "Average", "Average": "Brawny"}, "template": "The records rule out the {value} build group."},
            6: {"kind": "attribute", "attribute": "organization", "cycle": {"Clean": "Messy", "Messy": "Clean"}, "template": "The records rule out the {value} organization group."},
        },
    },
}

default killer = 0
default remainingSuspects = [1, 2, 3, 4, 5, 6, 7, 8, 9]
default investigationClues = []
default recordedClueKeys = []
default playerInvestigationNotes = ""

init python:
    def initialize_investigation():
        """Choose one killer for a new game or a migrated pre-model save."""
        if store.killer not in store.suspectNames:
            store.killer = renpy.random.randint(1, 9)

        if config.developer:
            validate_investigation_routes()

    def validate_investigation_routes():
        """Fail early if a planned route can eliminate its generated killer."""
        for route_id in store.investigationRoutes:
            for killer_id in store.suspectNames:
                active = set(store.suspectNames.keys())
                counts = []

                for visit in sorted(store.investigationRoutes[route_id]["visits"]):
                    reveal = get_planned_route_reveal(route_id, visit, killer_id)
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

                if route_id == "dhampir" and counts != [8, 6, 3]:
                    raise Exception("Dhampir killer {} produced counts {}, not 8/6/3.".format(
                        killer_id, counts))

    def get_planned_route_reveal(route_id, visit, killer_id=None):
        """Resolve one route/visit into a killer-safe clue and suspect list."""
        if killer_id is None:
            killer_id = store.killer

        route = store.investigationRoutes.get(route_id)
        if route is None or visit not in route["visits"]:
            raise Exception("Unknown investigation reveal: {} visit {}".format(route_id, visit))

        reveal = route["visits"][visit]
        kind = reveal["kind"]

        if kind == "single":
            suspect_id = reveal["eliminations"][killer_id]
            eliminated_ids = [suspect_id]
            value = store.suspectAttributes[suspect_id]["unique_id"]
            clue_text = reveal["template"].format(
                suspect=store.suspectNames[suspect_id], value=value)
        else:
            attribute = reveal["attribute"]
            if kind == "retain_killer_attribute":
                value = store.suspectAttributes[killer_id][attribute]
                eliminated_ids = sorted([
                    suspect_id for suspect_id, attributes in store.suspectAttributes.items()
                    if attributes[attribute] != value
                ])
            elif kind == "razzle_attribute":
                value = store.razzleFocusedRoutePlan[killer_id][attribute]
                eliminated_ids = sorted([
                    suspect_id for suspect_id, attributes in store.suspectAttributes.items()
                    if attributes[attribute] == value
                ])
            else:
                killer_value = store.suspectAttributes[killer_id][attribute]
                value = reveal["cycle"][killer_value]
                eliminated_ids = sorted([
                    suspect_id for suspect_id, attributes in store.suspectAttributes.items()
                    if attributes[attribute] == value
                ])
            clue_text = reveal["template"].format(value=value)

        if killer_id in eliminated_ids:
            raise Exception("Planned reveal {} visit {} eliminates killer {}.".format(
                route_id, visit, killer_id))

        return {
            "route_id": route_id,
            "route": route["name"],
            "visit": visit,
            "text": clue_text,
            "value": value,
            "eliminated": eliminated_ids,
        }

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
        return record_investigation_clue(
            "{}_visit_{}".format(route_id, visit),
            reveal["route"],
            visit,
            clue_text or reveal["text"],
            reveal["eliminated"],
            expected_count=expected_count,
        )
