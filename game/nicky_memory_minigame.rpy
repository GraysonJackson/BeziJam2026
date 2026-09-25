## Nicky Visit 3: two-round records-and-alibis memory matching game.

define NICKY_MEMORY_PHASE_SECONDS = 75
define NICKY_MEMORY_MISMATCH_DELAY = 0.85
define NICKY_MEMORY_PEEK_SECONDS = 2.0
define NICKY_MEMORY_PAIRS_PER_PHASE = 6
define NICKY_MEMORY_PHASE_NAMES = ("RECORD SOURCES", "SUSPECT PROFILES")

default nicky_memory_active = False
default nicky_memory_phase = "idle"
default nicky_memory_phase_index = 0
default nicky_memory_cards = []
default nicky_memory_selected_ids = []
default nicky_memory_matched_pairs = []
default nicky_memory_hint_card_ids = []
default nicky_memory_hint_available = False
default nicky_memory_peek_active = False
default nicky_memory_time_remaining = NICKY_MEMORY_PHASE_SECONDS
default nicky_memory_mistakes = 0
default nicky_memory_consecutive_mistakes = 0
default nicky_memory_hints_used = 0
default nicky_memory_expired_phases = 0
default nicky_memory_feedback = ""
default nicky_memory_reveal = {}
default nicky_memory_result = {}
default nicky_memory_completion_recorded = False

init python:
    def _nicky_memory_pair_definitions(phase_index):
        """Build six stable semantic pairs for the requested round."""
        if phase_index == 0:
            return [
                ("device", "PHONE LOCATION", "WATCH MOVEMENT", "DEVICE DATA"),
                ("camera", "TRAFFIC CAMERA", "STREET TIMESTAMP", "VIDEO"),
                ("booking", "BOOKING PHOTO", "INTAKE MEASUREMENTS", "POLICE FILE"),
                ("medical", "MEDICAL INTAKE", "OLD INJURY RECORD", "HEALTH RECORD"),
                ("property", "PROPERTY LOG", "SIGNED EVIDENCE SEAL", "CUSTODY"),
                ("witness", "WITNESS WORDING", "UNVERIFIED ASSUMPTION", "STATEMENT"),
            ]

        if phase_index != 1:
            raise Exception("Unknown Nicky memory phase: {}".format(phase_index))

        reveal = store.nicky_memory_reveal
        active_eliminations = [
            suspect_id for suspect_id in reveal["eliminated"]
            if suspect_id in store.remainingSuspects
        ]
        if len(active_eliminations) != 2:
            raise Exception(
                "Nicky memory game expected two active build eliminations, found {}."
                .format(active_eliminations))

        first_name = store.suspectNames[active_eliminations[0]]
        second_name = store.suspectNames[active_eliminations[1]]
        first_build = store.suspectAttributes[active_eliminations[0]]["build"]
        second_build = store.suspectAttributes[active_eliminations[1]]["build"]
        first_description = store.NICKY_BUILD_RECORD_DESCRIPTIONS[first_build]
        second_description = store.NICKY_BUILD_RECORD_DESCRIPTIONS[second_build]

        return [
            ("suspect_a", "{}\nBOOKING FILE".format(first_name),
             "MEASURED FRAME\n{}".format(first_description), "SUSPECT"),
            ("suspect_b", "{}\nINTAKE FILE".format(second_name),
             "MEASURED FRAME\n{}".format(second_description), "SUSPECT"),
            ("scale", "CAMERA SCALE", "DOORFRAME WIDTH", "MEASUREMENT"),
            ("coat", "OVERSIZED COAT", "IGNORE SILHOUETTE", "CORRECTION"),
            ("power", "POWERED FORCE", "DOES NOT PROVE BUILD", "CORRECTION"),
            ("duplicate", "DUPLICATE REPORT", "COUNT ONCE", "CORRECTION"),
        ]

    def _nicky_memory_build_cards(phase_index):
        cards = []
        for pair_id, left_text, right_text, category in _nicky_memory_pair_definitions(phase_index):
            cards.append({
                "id": "{}_{}_a".format(phase_index, pair_id),
                "pair_id": pair_id,
                "text": left_text,
                "category": category,
            })
            cards.append({
                "id": "{}_{}_b".format(phase_index, pair_id),
                "pair_id": pair_id,
                "text": right_text,
                "category": category,
            })
        renpy.random.shuffle(cards)
        return cards

    def _nicky_memory_cards_are_valid():
        cards = store.nicky_memory_cards
        if len(cards) != store.NICKY_MEMORY_PAIRS_PER_PHASE * 2:
            return False

        card_ids = [card.get("id") for card in cards]
        if None in card_ids or len(set(card_ids)) != len(card_ids):
            return False

        pair_counts = {}
        for card in cards:
            pair_id = card.get("pair_id")
            if not pair_id or "text" not in card:
                return False
            pair_counts[pair_id] = pair_counts.get(pair_id, 0) + 1
        return (len(pair_counts) == store.NICKY_MEMORY_PAIRS_PER_PHASE
                and all(count == 2 for count in pair_counts.values()))

    def _nicky_memory_load_phase(phase_index):
        store.nicky_memory_phase_index = phase_index
        store.nicky_memory_cards = _nicky_memory_build_cards(phase_index)
        store.nicky_memory_selected_ids = []
        store.nicky_memory_matched_pairs = []
        store.nicky_memory_hint_card_ids = []
        store.nicky_memory_hint_available = False
        store.nicky_memory_peek_active = False
        store.nicky_memory_time_remaining = store.NICKY_MEMORY_PHASE_SECONDS
        store.nicky_memory_consecutive_mistakes = 0
        store.nicky_memory_phase = "matching"
        store.nicky_memory_feedback = (
            "Flip two cards and match each record to the detail that verifies it."
            if phase_index == 0 else
            "Match the corrected suspect files to the measurements that survive review."
        )

    def _nicky_memory_reset():
        store.nicky_memory_active = True
        store.nicky_memory_reveal = get_planned_route_reveal("nicky", 3)
        store.nicky_memory_mistakes = 0
        store.nicky_memory_consecutive_mistakes = 0
        store.nicky_memory_hints_used = 0
        store.nicky_memory_expired_phases = 0
        store.nicky_memory_result = {}
        store.nicky_memory_completion_recorded = False
        _nicky_memory_load_phase(0)

    def start_nicky_memory_minigame():
        """Reset the briefing cards and open the modal matching screen."""
        _nicky_memory_reset()
        renpy.call_screen("nicky_memory_minigame")

    def _nicky_memory_card(card_id):
        for card in store.nicky_memory_cards:
            if card.get("id") == card_id:
                return card
        return None

    def nicky_memory_card_is_face_up(card_id):
        card = _nicky_memory_card(card_id)
        if card is None:
            return False
        return (
            store.nicky_memory_peek_active
            or card_id in store.nicky_memory_selected_ids
            or card_id in store.nicky_memory_hint_card_ids
            or card["pair_id"] in store.nicky_memory_matched_pairs
        )

    def nicky_memory_flip(card_id):
        """Flip one legal card and resolve after the second selection."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "matching"
                or store.nicky_memory_peek_active):
            return

        if not _nicky_memory_cards_are_valid():
            _nicky_memory_load_phase(store.nicky_memory_phase_index)
            store.nicky_memory_feedback = (
                "Nicky rebuilt a malformed set of cards. The evidence result is unchanged."
            )
            renpy.restart_interaction()
            return

        card = _nicky_memory_card(card_id)
        if card is None:
            return
        if (card_id in store.nicky_memory_selected_ids
                or card["pair_id"] in store.nicky_memory_matched_pairs
                or len(store.nicky_memory_selected_ids) >= 2):
            return

        selected = list(store.nicky_memory_selected_ids)
        selected.append(card_id)
        store.nicky_memory_selected_ids = selected
        store.nicky_memory_hint_card_ids = []

        if len(selected) == 2:
            nicky_memory_resolve_pair()
        else:
            store.nicky_memory_feedback = "One record selected. Find the corroborating card."
            renpy.restart_interaction()

    def nicky_memory_resolve_pair():
        """Keep a correct pair visible or enter a short mismatch window."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "matching"
                or len(store.nicky_memory_selected_ids) != 2):
            return

        first = _nicky_memory_card(store.nicky_memory_selected_ids[0])
        second = _nicky_memory_card(store.nicky_memory_selected_ids[1])
        if first is None or second is None:
            store.nicky_memory_selected_ids = []
            renpy.restart_interaction()
            return

        if first["pair_id"] == second["pair_id"]:
            matched = list(store.nicky_memory_matched_pairs)
            if first["pair_id"] not in matched:
                matched.append(first["pair_id"])
            store.nicky_memory_matched_pairs = matched
            store.nicky_memory_selected_ids = []
            store.nicky_memory_consecutive_mistakes = 0
            store.nicky_memory_hint_available = False
            store.nicky_memory_feedback = (
                "Matched: {}. Nicky clips the records together.".format(
                    first["category"]))

            if len(matched) >= store.NICKY_MEMORY_PAIRS_PER_PHASE:
                store.nicky_memory_phase = "phase_complete"
                store.nicky_memory_feedback = (
                    "Round complete. Every record has independent support."
                    if store.nicky_memory_phase_index == 0 else
                    "Profile review complete. The unsupported build group is isolated."
                )
        else:
            store.nicky_memory_mistakes += 1
            store.nicky_memory_consecutive_mistakes += 1
            if store.nicky_memory_consecutive_mistakes >= 3:
                store.nicky_memory_hint_available = True
                store.nicky_memory_feedback = (
                    "No match. Nicky taps two cards. 'Want a hint, rookie?'"
                )
            else:
                store.nicky_memory_feedback = (
                    "Those records do not corroborate each other. They'll flip back."
                )
            store.nicky_memory_phase = "mismatch"
        renpy.restart_interaction()

    def nicky_memory_tick():
        """Close the mismatch window and return unmatched cards face down."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "mismatch"):
            return
        store.nicky_memory_selected_ids = []
        store.nicky_memory_phase = "matching"
        renpy.restart_interaction()

    def nicky_memory_countdown_tick():
        """Run a forgiving timer that offers assistance instead of failure."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "matching"
                or store.nicky_memory_time_remaining <= 0):
            return
        store.nicky_memory_time_remaining = max(
            0, store.nicky_memory_time_remaining - 1)
        if store.nicky_memory_time_remaining == 0:
            store.nicky_memory_expired_phases += 1
            store.nicky_memory_feedback = (
                "Time's up, but the files are still here. Keep matching or let Nicky finish."
            )
        renpy.restart_interaction()

    def nicky_memory_hint():
        """Expose one unmatched pair after Nicky offers help."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "matching"
                or not store.nicky_memory_hint_available):
            return
        unresolved_pairs = [
            pair_id for pair_id in {
                card["pair_id"] for card in store.nicky_memory_cards
            }
            if pair_id not in store.nicky_memory_matched_pairs
        ]
        if not unresolved_pairs:
            return
        pair_id = sorted(unresolved_pairs)[0]
        store.nicky_memory_hint_card_ids = [
            card["id"] for card in store.nicky_memory_cards
            if card["pair_id"] == pair_id
        ]
        store.nicky_memory_hints_used += 1
        store.nicky_memory_hint_available = False
        store.nicky_memory_consecutive_mistakes = 0
        store.nicky_memory_feedback = (
            "Nicky marks one corroborating pair in yellow."
        )
        renpy.restart_interaction()

    def nicky_memory_reveal_all():
        """Accessibility peek: reveal every card briefly without a penalty."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "matching"
                or store.nicky_memory_peek_active
                or store.nicky_memory_selected_ids):
            return
        store.nicky_memory_peek_active = True
        store.nicky_memory_feedback = (
            "Accessibility preview: all records are visible briefly."
        )
        renpy.restart_interaction()

    def nicky_memory_end_peek():
        if not store.nicky_memory_active or not store.nicky_memory_peek_active:
            return
        store.nicky_memory_peek_active = False
        store.nicky_memory_feedback = "The cards return face down."
        renpy.restart_interaction()

    def nicky_memory_next_phase():
        """Advance from source matching to profiles, then expose the result."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "phase_complete"):
            return
        if store.nicky_memory_phase_index == 0:
            _nicky_memory_load_phase(1)
        else:
            store.nicky_memory_phase = "result"
            if store.nicky_memory_reveal.get("scope") == "category":
                store.nicky_memory_feedback = (
                    "The corroborated records exclude the {} build group."
                    .format(store.nicky_memory_reveal["value"]))
            else:
                store.nicky_memory_feedback = (
                    "The corrected records clear two individually measured suspect profiles."
                )
        renpy.restart_interaction()

    def _nicky_memory_record_result(quality, completed):
        if store.nicky_memory_completion_recorded:
            return False
        store.nicky_memory_completion_recorded = True

        active_eliminations = [
            suspect_id for suspect_id in store.nicky_memory_reveal["eliminated"]
            if suspect_id in store.remainingSuspects
        ]
        reveal = store.nicky_memory_reveal
        build_value = reveal["value"]
        eliminated_names = [
            store.suspectNames[suspect_id]
            for suspect_id in active_eliminations
        ]
        if reveal.get("scope") == "category":
            clue_text = (
                "Corroborated records rule out the {} build group."
                .format(build_value)
            )
        else:
            clue_text = (
                "Corroborated measurements clear the individual profiles for {}."
                .format(" and ".join(eliminated_names))
            )
        record_planned_route_reveal(
            "nicky", 3, clue_text=clue_text, expected_count=2)
        store.nicky_memory_result = {
            "completed": completed,
            "quality": quality,
            "mistakes": store.nicky_memory_mistakes,
            "hints_used": store.nicky_memory_hints_used,
            "expired_phases": store.nicky_memory_expired_phases,
            "build": build_value,
            "scope": reveal.get("scope", "category"),
            "eliminated_names": eliminated_names,
        }
        return True

    def finish_nicky_memory_minigame():
        """Record the completed build finding exactly once and return."""
        if (not store.nicky_memory_active
                or store.nicky_memory_phase != "result"):
            return
        if (store.nicky_memory_mistakes == 0
                and store.nicky_memory_hints_used == 0
                and store.nicky_memory_expired_phases == 0):
            quality = "perfect"
        elif store.nicky_memory_mistakes <= 4:
            quality = "steady"
        else:
            quality = "recovered"
        if not _nicky_memory_record_result(quality, True):
            return
        store.nicky_memory_active = False
        store.nicky_memory_phase = "complete"
        renpy.hide_screen("nicky_memory_minigame")
        renpy.end_interaction(True)

    def nicky_memory_assist():
        """Let Nicky finish without withholding the canonical clue."""
        if not store.nicky_memory_active:
            return
        if not _nicky_memory_record_result("assisted", False):
            return
        store.nicky_memory_active = False
        store.nicky_memory_phase = "assisted"
        renpy.hide_screen("nicky_memory_minigame")
        renpy.end_interaction(True)

    def abort_nicky_memory_minigame():
        """Close an interrupted session without recording its clue."""
        if not store.nicky_memory_active:
            return
        store.nicky_memory_active = False
        store.nicky_memory_phase = "aborted"
        store.nicky_memory_selected_ids = []
        store.nicky_memory_hint_card_ids = []
        store.nicky_memory_peek_active = False
        renpy.hide_screen("nicky_memory_minigame")
        renpy.end_interaction(False)
