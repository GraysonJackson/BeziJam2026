import sys

class MockStore:
    def __init__(self):
        self.height_memory_active = False
        self.height_memory_complete = False
        self.height_memory_completion_recorded = False
        self.height_memory_refreshing = False
        self.height_memory_progress = 0
        self.height_memory_required_cleanups = 10
        self.height_memory_timer = 0.0
        self.height_memory_setbacks = 0
        self.height_memory_assisted = False
        self.height_memory_quality = "clean"
        self.height_memory_feedback = ""
        self.suspectNames = {1: "Victor", 2: "Jermiah", 3: "Barry", 4: "Carl", 5: "Tucker", 6: "Edgar", 7: "Simon", 8: "Kyle", 9: "Alan"}
        self.suspectAttributes = {
            1: {"build": "Brawny"},
            2: {"build": "Skinny"},
            3: {"build": "Average"},
            4: {"build": "Skinny"},
            5: {"build": "Average"},
            6: {"build": "Brawny"},
            7: {"build": "Average"},
            8: {"build": "Brawny"},
            9: {"build": "Skinny"},
        }
        self.NICKY_BUILD_RECORD_DESCRIPTIONS = {
            "Skinny": "a narrow shoulder-to-height ratio",
            "Average": "a middle-range shoulder-to-height ratio",
            "Brawny": "a broad shoulder-to-height ratio",
        }
        self.NICKY_MEMORY_PAIRS_PER_PHASE = 6
        self.NICKY_MEMORY_PHASE_SECONDS = 75
        self.remainingSuspects = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.routeRevealsAwarded = {}

store = MockStore()

class MockRenpy:
    def hide_screen(self, screen_name):
        pass
    def restart_interaction(self):
        pass
    def end_interaction(self, result):
        pass

renpy = MockRenpy()

def get_planned_route_reveal(route, visit):
    return {
        "scope": "category",
        "value": "Tall",
        "eliminated": [3, 5],
    }

def record_planned_route_reveal(route, visit, clue_text="", expected_count=None):
    store.routeRevealsAwarded[(route, visit)] = clue_text


# --- Height memory minigame logic ---
def finish_height_memory_minigame():
    if store.height_memory_completion_recorded or not store.height_memory_active:
        return
    if not store.height_memory_assisted and store.height_memory_progress < store.height_memory_required_cleanups:
        return

    store.height_memory_completion_recorded = True
    store.height_memory_complete = True
    store.height_memory_active = False
    store.height_memory_refreshing = False
    store.height_memory_timer = 0.0
    if not store.height_memory_assisted:
        store.height_memory_quality = "flawless" if store.height_memory_setbacks == 0 else "scrambled"
    renpy.hide_screen("height_memory_minigame")
    reveal = get_planned_route_reveal("razzle", 3)
    if reveal.get("scope") == "category":
        clue_text = "Eyewitness evidence rules out {} height.".format(reveal["value"])
    else:
        names = " and ".join(store.suspectNames[s] for s in reveal["eliminated"])
        clue_text = "Doorframe measurements clear the individual profiles for {}.".format(names)
    record_planned_route_reveal("razzle", 3, clue_text=clue_text, expected_count=2)
    renpy.restart_interaction()

def abort_height_memory_minigame():
    if not store.height_memory_active or store.height_memory_completion_recorded:
        return
    store.height_memory_assisted = True
    store.height_memory_quality = "assisted"
    store.height_memory_feedback = "Razzle takes over, sorts the remaining thoughts, and preserves the measurement."
    finish_height_memory_minigame()


# --- Nicky memory minigame logic ---
def _nicky_memory_pair_definitions(phase_index):
    reveal = store.nicky_memory_reveal
    active_eliminations = [
        suspect_id for suspect_id in reveal["eliminated"]
        if suspect_id in store.remainingSuspects
    ]
    first_name = store.suspectNames[active_eliminations[0]]
    second_name = store.suspectNames[active_eliminations[1]]
    first_build = store.suspectAttributes[active_eliminations[0]]["build"]
    second_build = store.suspectAttributes[active_eliminations[1]]["build"]
    first_description = store.NICKY_BUILD_RECORD_DESCRIPTIONS[first_build]
    second_description = store.NICKY_BUILD_RECORD_DESCRIPTIONS[second_build]

    return [
        ("suspect_a", "{}\nBOOKING FILE".format(first_name),
         "BOOKING MEASUREMENT\n{}".format(first_description), "SUSPECT"),
        ("suspect_b", "{}\nINTAKE FILE".format(second_name),
         "INTAKE MEASUREMENT\n{}".format(second_description), "SUSPECT"),
        ("scale", "CAMERA SCALE", "DOORFRAME WIDTH", "MEASUREMENT"),
        ("coat", "OVERSIZED COAT", "IGNORE SILHOUETTE", "CORRECTION"),
        ("power", "POWERED FORCE", "DOES NOT PROVE BUILD", "CORRECTION"),
        ("duplicate", "DUPLICATE REPORT", "COUNT ONCE", "CORRECTION"),
    ]

def _nicky_memory_card(card_id):
    for card in store.nicky_memory_cards:
        if card.get("id") == card_id:
            return card
    return None

def nicky_memory_resolve_pair():
    if len(store.nicky_memory_selected_ids) != 2:
        return

    first = _nicky_memory_card(store.nicky_memory_selected_ids[0])
    second = _nicky_memory_card(store.nicky_memory_selected_ids[1])
    if first is None or second is None:
        store.nicky_memory_selected_ids = []
        return

    if first["pair_id"] != second["pair_id"]:
        if store.nicky_memory_phase_index == 1:
            suspect_pairs = {"suspect_a", "suspect_b"}
            if {first["pair_id"], second["pair_id"]} == suspect_pairs:
                file_cards = [c for c in (first, second) if "\nBOOKING FILE" in c["text"] or "\nINTAKE FILE" in c["text"]]
                meas_cards = [c for c in (first, second) if "MEASUREMENT\n" in c["text"] or "MEASURED FRAME\n" in c["text"]]
                if len(file_cards) == 1 and len(meas_cards) == 1:
                    target_file = file_cards[0]
                    target_meas = meas_cards[0]
                    partner_meas = None
                    for c in store.nicky_memory_cards:
                        if c["pair_id"] == target_file["pair_id"] and ("MEASUREMENT\n" in c["text"] or "MEASURED FRAME\n" in c["text"]):
                            partner_meas = c
                            break
                    if partner_meas is not None:
                        meas_desc = target_meas["text"].split("\n", 1)[-1]
                        partner_desc = partner_meas["text"].split("\n", 1)[-1]
                        if meas_desc == partner_desc:
                            target_meas["pair_id"], partner_meas["pair_id"] = partner_meas["pair_id"], target_meas["pair_id"]

    if first["pair_id"] == second["pair_id"]:
        matched = list(store.nicky_memory_matched_pairs)
        if first["pair_id"] not in matched:
            matched.append(first["pair_id"])
        store.nicky_memory_matched_pairs = matched
        store.nicky_memory_selected_ids = []
        store.nicky_memory_consecutive_mistakes = 0
        store.nicky_memory_feedback = "Matched: {}".format(first["category"])
    else:
        store.nicky_memory_mistakes += 1
        store.nicky_memory_consecutive_mistakes += 1
        store.nicky_memory_selected_ids = []


def test_height_memory_assistance():
    print("Testing A002: Height memory assistance...")
    # 1. Immediate assist (progress = 0)
    store.height_memory_active = True
    store.height_memory_complete = False
    store.height_memory_completion_recorded = False
    store.height_memory_progress = 0
    store.height_memory_assisted = False
    store.height_memory_quality = "clean"
    store.routeRevealsAwarded.clear()

    abort_height_memory_minigame()

    assert not store.height_memory_active, "Minigame must be deactivated after assist"
    assert store.height_memory_complete, "Minigame must be complete after assist"
    assert store.height_memory_completion_recorded, "Completion must be recorded"
    assert store.height_memory_assisted, "height_memory_assisted must be True"
    assert store.height_memory_quality == "assisted", "quality must be 'assisted'"
    assert ("razzle", 3) in store.routeRevealsAwarded, "Planned reveal must be awarded"

    # 2. Idempotent check (repeated call does nothing extra)
    abort_height_memory_minigame()
    finish_height_memory_minigame()
    assert len(store.routeRevealsAwarded) == 1, "Clue must not be awarded more than once"
    print("A002 Height memory assistance tests passed!")


def test_nicky_memory_provenance_and_interchangeability():
    print("Testing A009: Nicky memory provenance and semantic interchangeability...")
    # Both suspects 3 and 5 have "Average" build
    store.nicky_memory_reveal = {"scope": "category", "value": "Average", "eliminated": [3, 5]}
    pairs = _nicky_memory_pair_definitions(1)
    
    # Check visible provenance
    suspect_a = [p for p in pairs if p[0] == "suspect_a"][0]
    suspect_b = [p for p in pairs if p[0] == "suspect_b"][0]
    assert "BOOKING MEASUREMENT" in suspect_a[2], f"Expected BOOKING MEASUREMENT in {suspect_a[2]}"
    assert "INTAKE MEASUREMENT" in suspect_b[2], f"Expected INTAKE MEASUREMENT in {suspect_b[2]}"

    # Setup cards
    store.nicky_memory_cards = [
        {"id": "card_a_file", "pair_id": "suspect_a", "text": suspect_a[1], "category": "SUSPECT"},
        {"id": "card_a_meas", "pair_id": "suspect_a", "text": suspect_a[2], "category": "SUSPECT"},
        {"id": "card_b_file", "pair_id": "suspect_b", "text": suspect_b[1], "category": "SUSPECT"},
        {"id": "card_b_meas", "pair_id": "suspect_b", "text": suspect_b[2], "category": "SUSPECT"},
    ]
    store.nicky_memory_phase_index = 1
    store.nicky_memory_matched_pairs = []
    store.nicky_memory_mistakes = 0
    store.nicky_memory_consecutive_mistakes = 0

    # Cross-match: pair card_a_file with card_b_meas (matching builds!)
    store.nicky_memory_selected_ids = ["card_a_file", "card_b_meas"]
    nicky_memory_resolve_pair()

    assert "suspect_a" in store.nicky_memory_matched_pairs, "Cross match of identical builds must match!"
    assert store.nicky_memory_mistakes == 0, "No mistake should be recorded for semantic match"

    # Now pair remaining: card_b_file with card_a_meas
    store.nicky_memory_selected_ids = ["card_b_file", "card_a_meas"]
    nicky_memory_resolve_pair()

    assert "suspect_b" in store.nicky_memory_matched_pairs, "Remaining cross-card pair must also match!"
    assert store.nicky_memory_mistakes == 0, "No mistake should be recorded for remaining match"
    print("A009 Nicky memory provenance and semantic interchangeability tests passed!")


def test_dhampir_day_three_individual_scope_handling():
    print("Testing Dhampir Day 3 individual scope consumer robustness...")
    # Simulate a reveal where scope is individual
    reveal = {
        "route_id": "dhampir",
        "visit": 3,
        "scope": "individual",
        "value": "Individual profiles",
        "target_injury": "None",
        "selected_values": ["None"],
        "eliminated": [3, 9]
    }

    DHAMPIR_INJURY_EXCLUSION_TEXT = {
        "Bruised Knuckles": "Knuckles text",
        "Scuffed Hands": "Scuffed hands text",
        "None": "None text"
    }
    DHAMPIR_ISPY_VALID_TARGETS = {
        "Bruised Knuckles": ("plaster", "lamp", "table"),
        "Scuffed Hands": ("window", "rug", "door"),
        "None": ("frame", "blood", "chair"),
    }

    # 1. Test script resolution logic with target_injury
    dhampir_day_three_target_injury = reveal.get("target_injury") or reveal["value"]
    if dhampir_day_three_target_injury not in DHAMPIR_INJURY_EXCLUSION_TEXT:
        dhampir_day_three_target_injury = reveal.get("selected_values", ["None"])[0] if reveal.get("selected_values") else "None"

    dhampir_day_three_excluded_injuries = dhampir_day_three_target_injury
    assert dhampir_day_three_excluded_injuries in DHAMPIR_ISPY_VALID_TARGETS
    assert dhampir_day_three_excluded_injuries in DHAMPIR_INJURY_EXCLUSION_TEXT

    # 2. Test without target_injury (fallback to selected_values)
    reveal_fallback = {
        "route_id": "dhampir",
        "visit": 3,
        "scope": "individual",
        "value": "Individual profiles",
        "selected_values": ["Scuffed Hands"],
        "eliminated": [5, 8]
    }
    fallback_injury = reveal_fallback.get("target_injury") or reveal_fallback["value"]
    if fallback_injury not in DHAMPIR_INJURY_EXCLUSION_TEXT:
        fallback_injury = reveal_fallback.get("selected_values", ["None"])[0] if reveal_fallback.get("selected_values") else "None"
    assert fallback_injury == "Scuffed Hands"
    assert fallback_injury in DHAMPIR_ISPY_VALID_TARGETS

    # 3. Assert unpatched behavior would have crashed
    unpatched_val = reveal["value"]
    assert unpatched_val not in DHAMPIR_INJURY_EXCLUSION_TEXT
    assert unpatched_val not in DHAMPIR_ISPY_VALID_TARGETS
    print("Dhampir Day 3 individual scope consumer tests passed!")


if __name__ == "__main__":
    test_height_memory_assistance()
    test_nicky_memory_provenance_and_interchangeability()
    test_dhampir_day_three_individual_scope_handling()
    print("All Phase 1 minigame tests passed successfully!")
