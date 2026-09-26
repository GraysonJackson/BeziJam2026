## Day Seven accusation, relationship, ending-gallery, and replay state.

define DAY_SEVEN_PARTNERS = [
    ("razzle", "Razzle Dazzle", "razz"),
    ("winston", "Winston", "winn"),
    ("nicky", "Nicky", "nick"),
    ("ica", "Ica", "ica"),
    ("ulysses", "Ulysses", "uly"),
    ("madeline", "Madeline", "mads"),
    ("dhampir", "Dhampir", "dhamp"),
]

## These are calibrated against the maximum points available in each route.
## "Hard" means less room for incompatible answers, never perfection.
define DAY_SEVEN_ROMANCE_THRESHOLDS = {
    "razzle": 20,
    "winston": 20,
    "nicky": 25,
    "ica": 24,
    "ulysses": 30,
    "madeline": 30,
    "dhampir": 30,
}

define DAY_SEVEN_FRIEND_THRESHOLDS = {
    "razzle": 9,
    "winston": 9,
    "nicky": 10,
    "ica": 9,
    "ulysses": 18,
    "madeline": 11,
    "dhampir": 11,
}

## Relationship endings also require time together. Scores decide how those
## visits went; visit counts prevent one unusually strong afternoon from
## standing in for an arc.
define DAY_SEVEN_MIN_ROMANCE_VISITS = {
    "razzle": 3,
    "winston": 3,
    "nicky": 4,
    "ica": 4,
    "ulysses": 0,
    "madeline": 5,
    "dhampir": 5,
}
define DAY_SEVEN_MIN_FRIEND_VISITS = 2

define DAY_SEVEN_PROFILE_FIELDS = [
    ("Blood Type", "blood_type"),
    ("Rh Factor", "rh_factor"),
    ("Power", "power"),
    ("Height", "height"),
    ("Trace Left at Scene", "unique_drop"),
    ("Identifying Feature", "unique_id"),
    ("Personal Habits", "organization"),
    ("Build", "build"),
    ("Hand Injuries", "injuries"),
    ("Hair Color", "hair"),
    ("Temperament", "temperament"),
    ("Reaction After Killing", "kill_reaction"),
]

default daySevenSelectedSuspect = 0
default daySevenAccusationPage = 0
default daySevenPinnedSuspect = 0
default daySevenCaseSolved = False
default daySevenCaseModifierApplied = False
default daySevenChosenPartner = ""
default daySevenRelationshipOutcome = ""
default daySevenEndingKey = ""
default daySevenReplayMode = False
default daySevenReplayKey = ""
default daySevenIcaSpecial = False
default daySevenRelationshipSnapshot = {}
default daySevenBriefingResponse = ""

default persistent.daySevenEndings = {}

init python:
    def day_seven_partner_data(partner_id):
        for item in store.DAY_SEVEN_PARTNERS:
            if item[0] == partner_id:
                return item
        return None

    def day_seven_partner_name(partner_id):
        data = day_seven_partner_data(partner_id)
        return data[1] if data else ""

    def day_seven_score(partner_id):
        data = day_seven_partner_data(partner_id)
        if not data:
            return 0
        return int(getattr(store, data[2], 0))

    def day_seven_set_score(partner_id, value):
        data = day_seven_partner_data(partner_id)
        if data:
            setattr(store, data[2], int(value))

    def day_seven_prepare():
        if store.killer not in store.suspectNames:
            store.initialize_investigation()
        store.daySevenSelectedSuspect = 0
        store.daySevenAccusationPage = 0
        store.daySevenPinnedSuspect = 0
        store.daySevenCaseSolved = False
        store.daySevenCaseModifierApplied = False
        store.daySevenChosenPartner = ""
        store.daySevenRelationshipOutcome = ""
        store.daySevenEndingKey = ""
        store.daySevenReplayMode = False
        store.daySevenReplayKey = ""
        store.daySevenIcaSpecial = store.dayIca >= 7
        store.daySevenBriefingResponse = ""
        store.daySevenRelationshipSnapshot = {
            partner_id: day_seven_score(partner_id)
            for partner_id, _name, _score_var in store.DAY_SEVEN_PARTNERS
        }
        if store.daySevenIcaSpecial:
            # Ica's sixth visit produces direct identification and physical
            # evidence, so the formal screen still appears with one valid file.
            store.remainingSuspects = [store.killer]
        day_seven_selectable_suspects()

    def day_seven_selectable_suspects():
        """Return a safe accusation list without exposing eliminated suspects."""
        valid_ids = set(store.suspectNames.keys())
        if store.killer not in valid_ids:
            store.initialize_investigation()
        survivors = sorted(set(
            suspect_id for suspect_id in store.remainingSuspects
            if suspect_id in valid_ids
        ))
        if store.killer not in survivors:
            survivors.append(store.killer)
            survivors.sort()
            store.remainingSuspects = list(survivors)
            renpy.log("Day Seven repaired a suspect list that omitted the seeded culprit.")
        if not survivors:
            survivors = [store.killer]
            store.remainingSuspects = list(survivors)
        return survivors

    def day_seven_current_suspect():
        suspects = day_seven_selectable_suspects()
        if not suspects:
            return store.killer
        page = max(0, min(int(store.daySevenAccusationPage), len(suspects) - 1))
        store.daySevenAccusationPage = page
        return suspects[page]

    def day_seven_change_page(delta):
        suspects = day_seven_selectable_suspects()
        if not suspects:
            return
        store.daySevenAccusationPage = (
            int(store.daySevenAccusationPage) + int(delta)) % len(suspects)
        renpy.restart_interaction()

    def day_seven_go_to_suspect(suspect_id):
        suspects = day_seven_selectable_suspects()
        if suspect_id in suspects:
            store.daySevenAccusationPage = suspects.index(suspect_id)
            renpy.restart_interaction()

    def day_seven_toggle_pin(suspect_id):
        if store.daySevenPinnedSuspect == suspect_id:
            store.daySevenPinnedSuspect = 0
        else:
            store.daySevenPinnedSuspect = suspect_id
        renpy.restart_interaction()

    def day_seven_initials(suspect_id):
        return "".join(part[0] for part in store.suspectNames[suspect_id].split()[:2]).upper()

    def day_seven_add_ica_evidence():
        if not store.daySevenIcaSpecial:
            return
        clue_key = "ica_day_seven_wallet"
        if clue_key in store.recordedClueKeys:
            return
        clue_text = (
            "{} was caught attempting to destroy Enrico Edge's bloodstained wallet."
            .format(store.suspectNames[store.killer])
        )
        clue = {
            "key": clue_key,
            "route": "Ica",
            "visit": 7,
            "text": clue_text,
            "eliminated": [],
            "eliminated_names": [],
        }
        clues = list(store.investigationClues)
        clues.append(clue)
        store.investigationClues = clues
        keys = list(store.recordedClueKeys)
        keys.append(clue_key)
        store.recordedClueKeys = keys

    def day_seven_apply_case_modifier(solved):
        if store.daySevenCaseModifierApplied:
            return
        change = 1 if solved else -1
        for partner_id, _name, _score_var in store.DAY_SEVEN_PARTNERS:
            day_seven_set_score(partner_id, day_seven_score(partner_id) + change)
        store.daySevenCaseModifierApplied = True

    def day_seven_relationship_outcome(partner_id, solved=None):
        if solved is None:
            solved = store.daySevenCaseSolved
        if partner_id == "ulysses" and not solved:
            return "rejection"

        score = day_seven_score(partner_id)
        if partner_id == "ulysses":
            visits = int(store.ulyssesPersonalEvenings)
        else:
            visits = int(store.ulysses_completed_visits(partner_id))
        romance_allowed = True
        if partner_id == "ulysses":
            romance_allowed = (
                not store.ulyssesBoundaryViolation
                or store.ulyssesBoundaryApology
            )
            romance_allowed = (
                romance_allowed
                and store.ulyssesRomanceInterest >= store.ULYSSES_DATE_ACCEPT_THRESHOLD
                and store.ulyssesPersonalEvenings >= store.ULYSSES_DATE_MIN_PERSONAL_EVENINGS
            )

        if (romance_allowed
                and (partner_id == "ulysses"
                     or visits >= store.DAY_SEVEN_MIN_ROMANCE_VISITS[partner_id])
                and score >= store.DAY_SEVEN_ROMANCE_THRESHOLDS[partner_id]):
            return "romance"
        if ((partner_id == "ulysses" or visits >= store.DAY_SEVEN_MIN_FRIEND_VISITS)
                and score >= store.DAY_SEVEN_FRIEND_THRESHOLDS[partner_id]):
            return "friend"
        return "rejection"

    def day_seven_culprit_confession(suspect_id):
        attrs = store.suspectAttributes[suspect_id]
        temperament = attrs.get("temperament", "Calm")
        reaction = attrs.get("kill_reaction", "None")
        organization = attrs.get("organization", "Messy")

        temperament_lines = {
            "Calm": "I knew exactly what Enrico would do once he discovered what I had done. He was going to expose me, so I decided he would not leave that room.",
            "Passionate": "Enrico discovered what I had done and said he would expose me. I lost my temper. By the time I understood how far it had gone, he was dead.",
            "Nervous": "Enrico discovered what I had done. He said he would expose me, and I panicked. I kept thinking I could still stop everything from collapsing.",
        }
        reaction_lines = {
            "Calculated": "Afterward, I forced myself to slow down, clean what I could, and leave as though nothing had changed.",
            "Panicked": "Afterward, I rushed. I hit things, missed things, and left before I had any idea what I had exposed.",
            "None": "Afterward, I simply left. I thought behaving normally would make the room look less connected to me.",
        }
        organization_lines = {
            "Clean": "I removed every trace I recognized. I was certain the pieces I missed would never be enough on their own.",
            "Messy": "I trusted the disorder to bury whatever I missed. I thought you would keep chasing pieces that looked unrelated.",
        }
        return "{} {} {}".format(
            temperament_lines.get(temperament, temperament_lines["Calm"]),
            reaction_lines.get(reaction, reaction_lines["None"]),
            organization_lines.get(organization, organization_lines["Messy"]),
        )

    def day_seven_favorite_investigator():
        counts = store.ulysses_visit_counts()
        if not counts:
            return ""
        highest = max(counts.values())
        leaders = [key for key, value in counts.items() if value == highest and value > 0]
        return leaders[0] if len(leaders) == 1 else ""

    def day_seven_mismatch_text(selected_id):
        chosen = store.suspectAttributes[selected_id]
        actual = store.suspectAttributes[store.killer]
        priority = [
            "unique_id", "blood_type", "rh_factor", "height", "build",
            "injuries", "power", "organization", "kill_reaction",
            "unique_drop", "hair", "temperament",
        ]
        labels = dict((key, label) for label, key in store.DAY_SEVEN_PROFILE_FIELDS)
        for key in priority:
            if chosen.get(key) != actual.get(key):
                return (
                    "{}'s file lists {} as {}, while the combined evidence points to {}."
                    .format(
                        store.suspectNames[selected_id],
                        labels.get(key, key),
                        chosen.get(key),
                        actual.get(key),
                    )
                )
        return "The selected file cannot account for the complete evidence chain."

    def day_seven_ending_key(solved, partner_id, outcome):
        result = "success" if solved else "failure"
        if not partner_id:
            return "{}_alone".format(result)
        return "{}_{}_{}".format(result, partner_id, outcome)

    def day_seven_ending_catalog():
        entries = []
        outcomes = ("romance", "friend", "rejection")
        outcome_names = {
            "romance": "Romance",
            "friend": "Friendship",
            "rejection": "Rejection",
        }
        for solved, result_id, result_title in (
                (True, "success", "Case Solved"),
                (False, "failure", "Case Unclosed")):
            for partner_id, partner_name, _score_var in store.DAY_SEVEN_PARTNERS:
                available = outcomes
                if not solved and partner_id == "ulysses":
                    available = ("rejection",)
                for outcome in available:
                    key = day_seven_ending_key(solved, partner_id, outcome)
                    entries.append({
                        "key": key,
                        "solved": solved,
                        "partner": partner_id,
                        "outcome": outcome,
                        "title": "{} — {} — {}".format(
                            partner_name, outcome_names[outcome], result_title),
                    })
            entries.append({
                "key": "{}_alone".format(result_id),
                "solved": solved,
                "partner": "",
                "outcome": "alone",
                "title": ("Part of the Team" if solved else "Case Unclosed"),
            })
        return entries

    def day_seven_catalog_entry(key):
        for entry in day_seven_ending_catalog():
            if entry["key"] == key:
                return entry
        return None

    def day_seven_unlock_ending(key):
        entry = day_seven_catalog_entry(key)
        if entry is None:
            raise Exception("Unknown Day Seven ending key: {}".format(key))
        unlocked = dict(persistent.daySevenEndings or {})
        unlocked[key] = {
            "killer": int(store.killer),
            "ica_special": bool(store.daySevenIcaSpecial),
        }
        persistent.daySevenEndings = unlocked
        renpy.save_persistent()

    def day_seven_setup_gallery_replay(key):
        entry = day_seven_catalog_entry(key)
        if entry is None:
            raise Exception("Cannot replay unknown ending: {}".format(key))
        metadata = (persistent.daySevenEndings or {}).get(key, {})
        store.daySevenReplayMode = True
        store.daySevenReplayKey = key
        store.daySevenCaseSolved = bool(entry["solved"])
        store.daySevenChosenPartner = entry["partner"]
        store.daySevenRelationshipOutcome = entry["outcome"]
        store.daySevenIcaSpecial = bool(metadata.get("ica_special", False))
        replay_killer = int(metadata.get("killer", 1))
        if replay_killer in store.suspectNames:
            store.killer = replay_killer

    def validate_day_seven_model():
        catalog = day_seven_ending_catalog()
        keys = [entry["key"] for entry in catalog]
        if len(catalog) != 42 or len(set(keys)) != 42:
            raise Exception("Day Seven gallery must contain 42 unique reachable endings.")
        if "failure_ulysses_romance" in keys or "failure_ulysses_friend" in keys:
            raise Exception("Impossible Ulysses failure outcomes entered the gallery.")
        required_labels = [
            "DaySevenStart", "DaySevenSuccess", "DaySevenFailure",
            "DaySevenEndingAlone", "DaySevenGalleryReplay",
        ] + [
            "DaySevenEnding{}".format(partner_id.title())
            for partner_id, _partner_name, _score_var in store.DAY_SEVEN_PARTNERS
        ]
        for label in required_labels:
            if not renpy.has_label(label):
                raise Exception("Day Seven is missing label {}.".format(label))
        for partner_id, _name, _score_var in store.DAY_SEVEN_PARTNERS:
            if partner_id not in store.DAY_SEVEN_ROMANCE_THRESHOLDS:
                raise Exception("Missing romance threshold for {}.".format(partner_id))
            if partner_id not in store.DAY_SEVEN_FRIEND_THRESHOLDS:
                raise Exception("Missing friendship threshold for {}.".format(partner_id))
            if (store.DAY_SEVEN_FRIEND_THRESHOLDS[partner_id]
                    >= store.DAY_SEVEN_ROMANCE_THRESHOLDS[partner_id]):
                raise Exception("Friend threshold must be below romance for {}.".format(partner_id))
        for suspect_id in store.suspectNames:
            for _label, key in store.DAY_SEVEN_PROFILE_FIELDS:
                if key not in store.suspectAttributes[suspect_id]:
                    raise Exception("Suspect {} is missing {}.".format(suspect_id, key))

        # Every seeded culprit can be the sole valid accusation, and the three
        # relationship bands remain reachable at their exact boundaries.
        original_killer = store.killer
        original_remaining = list(store.remainingSuspects)
        original_scores = {
            partner_id: day_seven_score(partner_id)
            for partner_id, _name, _score_var in store.DAY_SEVEN_PARTNERS
        }
        original_boundary = store.ulyssesBoundaryViolation
        original_apology = store.ulyssesBoundaryApology
        original_ulysses_romance = store.ulyssesRomanceInterest
        original_ulysses_personal = store.ulyssesPersonalEvenings
        original_visit_counters = {
            route_id: int(getattr(store, data[2]))
            for route_id, data in store.ULYSSES_ROUTE_DATA.items()
        }
        try:
            store.ulyssesRomanceInterest = store.ULYSSES_DATE_ACCEPT_THRESHOLD
            store.ulyssesPersonalEvenings = store.ULYSSES_DATE_MIN_PERSONAL_EVENINGS
            for route_id, data in store.ULYSSES_ROUTE_DATA.items():
                setattr(
                    store,
                    data[2],
                    store.DAY_SEVEN_MIN_ROMANCE_VISITS[route_id] + 1,
                )
            for suspect_id in store.suspectNames:
                store.killer = suspect_id
                store.remainingSuspects = [suspect_id]
                if day_seven_selectable_suspects() != [suspect_id]:
                    raise Exception("Seeded culprit {} cannot be accused.".format(suspect_id))

            for partner_id, _name, _score_var in store.DAY_SEVEN_PARTNERS:
                friend_at = store.DAY_SEVEN_FRIEND_THRESHOLDS[partner_id]
                romance_at = store.DAY_SEVEN_ROMANCE_THRESHOLDS[partner_id]
                day_seven_set_score(partner_id, friend_at - 1)
                if day_seven_relationship_outcome(partner_id, True) != "rejection":
                    raise Exception("{} rejection boundary is invalid.".format(partner_id))
                day_seven_set_score(partner_id, friend_at)
                if day_seven_relationship_outcome(partner_id, True) != "friend":
                    raise Exception("{} friendship boundary is invalid.".format(partner_id))
                day_seven_set_score(partner_id, romance_at)
                if day_seven_relationship_outcome(partner_id, True) != "romance":
                    raise Exception("{} romance boundary is invalid.".format(partner_id))

            if day_seven_relationship_outcome("ulysses", False) != "rejection":
                raise Exception("Ulysses must reject the player after a failed case.")
            store.ulyssesBoundaryViolation = True
            store.ulyssesBoundaryApology = False
            day_seven_set_score("ulysses", store.DAY_SEVEN_ROMANCE_THRESHOLDS["ulysses"])
            if day_seven_relationship_outcome("ulysses", True) == "romance":
                raise Exception("An unresolved Ulysses boundary violation allowed romance.")
        finally:
            store.killer = original_killer
            store.remainingSuspects = original_remaining
            store.ulyssesBoundaryViolation = original_boundary
            store.ulyssesBoundaryApology = original_apology
            store.ulyssesRomanceInterest = original_ulysses_romance
            store.ulyssesPersonalEvenings = original_ulysses_personal
            for route_id, value in original_visit_counters.items():
                setattr(store, store.ULYSSES_ROUTE_DATA[route_id][2], value)
            for partner_id, value in original_scores.items():
                day_seven_set_score(partner_id, value)
        return True
