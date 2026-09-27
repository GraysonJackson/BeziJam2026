import sys
import re

# Mock Ren'Py store environment
class Store:
    def __init__(self):
        self.killer = 0
        self.remainingSuspects = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.investigationClues = []
        self.recordedClueKeys = []
        self.recordedRouteReveals = {}
        self.ulyssesCrossReportCompleted = False
        self.daySevenIcaSpecial = False

store = Store()
sys.modules['renpy'] = Store()
sys.modules['renpy.store'] = store

# Import suspect data
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

DAY_SEVEN_PROFILE_FIELDS = [
    ("Blood Type", "blood_type"),
    ("Rh Factor", "rh_factor"),
    ("Power", "power"),
    ("Height", "height"),
    ("Known Biological/Physical Markers", "unique_drop"),
    ("Identifying Feature", "unique_id"),
    ("Personal Habits", "organization"),
    ("Build", "build"),
    ("Hand Injuries", "injuries"),
    ("Hair Color", "hair"),
    ("Temperament", "temperament"),
    ("Crisis Behavior / Stress Reaction", "kill_reaction"),
]

store.suspectNames = suspectNames
store.suspectAttributes = suspectAttributes
store.DAY_SEVEN_PROFILE_FIELDS = DAY_SEVEN_PROFILE_FIELDS

import textwrap

def extract_rpy_python(rpy_path):
    lines = []
    in_python = False
    with open(rpy_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("init python:"):
                in_python = True
                continue
            elif in_python:
                if line.strip() and not line.startswith(" ") and not line.startswith("\t"):
                    in_python = False
                else:
                    lines.append(line)
    return textwrap.dedent("".join(lines))

# Load day_seven_state
d7_code = extract_rpy_python("game/day_seven_state.rpy")
d7_ns = {
    "store": store,
    "DAY_SEVEN_PROFILE_FIELDS": DAY_SEVEN_PROFILE_FIELDS,
}
exec(compile(d7_code, "game/day_seven_state.rpy", "exec"), d7_ns)

day_seven_culprit_confession = d7_ns["day_seven_culprit_confession"]
day_seven_mismatch_info = d7_ns["day_seven_mismatch_info"]
day_seven_mismatch_text = d7_ns["day_seven_mismatch_text"]

# Load ulysses_evening_state
uly_code = extract_rpy_python("game/ulysses_evening_state.rpy")
uly_ns = {
    "store": store,
}
exec(compile(uly_code, "game/ulysses_evening_state.rpy", "exec"), uly_ns)

ulysses_candidate_profile_text = uly_ns["ulysses_candidate_profile_text"]
ulysses_intuition_hint_text = uly_ns["ulysses_intuition_hint_text"]
record_ulysses_cross_report_reveal = uly_ns["record_ulysses_cross_report_reveal"]


def test_a007_profile_fields():
    print("Testing A007: Suspect profile field re-labeling...")
    # Check definition in game/day_seven_state.rpy
    with open("game/day_seven_state.rpy", "r", encoding="utf-8") as f:
        d7_raw = f.read()

    assert '("Known Biological/Physical Markers", "unique_drop")' in d7_raw
    assert '("Crisis Behavior / Stress Reaction", "kill_reaction")' in d7_raw
    assert "Reaction After Killing" not in d7_raw
    assert "Trace Left at Scene" not in d7_raw
    print("A007 tests passed!")


def test_a006_accusation_mismatch():
    print("Testing A006: Accusation mismatch based on gathered evidence...")
    store.killer = 1  # Victor Veytovi
    
    # Subtest 0: Killer correctly matches
    info_killer = day_seven_mismatch_info(1)
    assert info_killer["kind"] == "matches", f"Expected matches for killer, got {info_killer['kind']}"

    # Subtest 1: Suspect was explicitly eliminated in a gathered clue
    store.investigationClues = [
        {
            "key": "madeline_visit_3",
            "route": "Madeline",
            "visit": 3,
            "text": "Lab evidence rules out blood type B.",
            "eliminated": [2, 4, 7],
            "eliminated_names": ["Jermiah Jones", "Carl Creek", "Simon Streep"],
        }
    ]
    store.recordedRouteReveals = {}
    store.ulyssesCrossReportCompleted = False

    # Choose Jermiah Jones (eliminated)
    info = day_seven_mismatch_info(2)
    assert info["kind"] == "already_eliminated", f"Expected already_eliminated, got {info['kind']}"
    assert "Lab evidence rules out blood type B" in info["text"]
    assert "Jermiah Jones was already ruled out" in info["text"]

    # Subtest 2: Suspect contradicts recorded positive reveal (Visit 6)
    # IN REAL GAMEPLAY, BOTH investigationClues AND recordedRouteReveals ARE PRESENT!
    store.investigationClues = [
        {
            "key": "razzle_visit_6",
            "route": "Razzle",
            "visit": 6,
            "text": "Eyewitness evidence identifies Brown hair.",
            "eliminated": [2, 3, 5, 6, 8, 9],
        }
    ]
    store.recordedRouteReveals = {
        "razzle_visit_6": {
            "route": "Razzle",
            "visit": 6,
            "attribute": "hair",
            "value": "Brown",
            "eliminated": [2, 3, 5, 6, 8, 9],
        }
    }
    # Choose Edgar Ebbington (Blonde hair)
    info = day_seven_mismatch_info(6)
    assert info["kind"] == "contradicts_gathered", f"Expected contradicts_gathered, got {info['kind']}"
    assert "Hair Color as Brown" in info["text"]
    assert "Edgar Ebbington's file lists Hair Color as Blonde" in info["text"]
    # Check that ungathered attributes (like Mole/Vitiligo) are NOT leaked
    assert "Mole" not in info["text"]
    assert "Vitiligo" not in info["text"]

    # Subtest 3: Suspect survived gathered clues, but is innocent (insufficient evidence)
    store.investigationClues = []
    store.recordedRouteReveals = {}
    # Choose Tucker Thompson (5) - innocent, but player has gathered 0 clues against him
    info = day_seven_mismatch_info(5)
    assert info["kind"] == "insufficient_evidence", f"Expected insufficient_evidence, got {info['kind']}"
    assert "does not isolate Tucker Thompson" in info["text"]
    assert "unsupported guess" in info["text"]
    # Verify no hidden attributes are cited
    for key in suspectAttributes[store.killer]:
        val = suspectAttributes[store.killer][key]
        assert f"points to {val}" not in info["text"]

    # Subtest 4: Cross-report contradiction
    store.ulyssesCrossReportCompleted = True
    info = day_seven_mismatch_info(3)
    assert info["kind"] == "contradicts_cross_report"
    assert "cross-report badge analysis" in info["text"]
    assert "Evidence Storage C" in info["text"]

    # Subtest 5: Comprehensive matrix across all 9 killers
    for k_id in range(1, 10):
        store.killer = k_id
        assert day_seven_mismatch_info(k_id)["kind"] == "matches"
        # Test an unsupported guess on an innocent suspect
        innocents = [s for s in range(1, 10) if s != k_id]
        store.investigationClues = []
        store.recordedRouteReveals = {}
        store.ulyssesCrossReportCompleted = False
        info_guess = day_seven_mismatch_info(innocents[0])
        assert info_guess["kind"] == "insufficient_evidence"

    print("A006 tests passed!")


def test_a008_ulysses_one_each_deduction():
    print("Testing A008: One-each breadth deduction using badge access logs...")
    for killer_id in range(1, 10):
        store.killer = killer_id
        other_suspects = [s for s in range(1, 10) if s != killer_id][:3]
        store.remainingSuspects = [killer_id] + other_suspects
        
        profile_text = ulysses_candidate_profile_text()
        # Verify killer has lockup access
        killer_name = suspectNames[killer_id]
        assert f"{killer_name} — Log: ATLAS Lockup Badge Reader — 21:14 (Access Granted: Evidence Storage C)" in profile_text
        
        # Verify none of the other 3 suspects have Evidence Storage C access
        for s in other_suspects:
            s_name = suspectNames[s]
            assert f"{s_name} — Log: ATLAS Lockup Badge Reader" not in profile_text
            assert "Evidence Storage C" not in profile_text.split(f"{s_name} — Log:")[1].split("•")[0]

        # Test intuition hint text
        hint = ulysses_intuition_hint_text()
        assert "lockup security logs" in hint
        assert "siphoned stimulants" in hint
        assert "Evidence Storage C" in hint
        # Must not leak raw build/organization/reaction attributes
        for raw_attr in ["Brawny", "Skinny", "Messy", "Calculated", "Panicked"]:
            assert f" {raw_attr.lower()} " not in f" {hint.lower()} "

    print("A008 tests passed!")


def test_a013_a016_confessions():
    print("Testing A013–A016: Confession motive and Enrico's identity...")
    for killer_id in range(1, 10):
        confession = day_seven_culprit_confession(killer_id)
        assert "stimulant" in confession.lower(), f"Confession for killer {killer_id} missing stimulant motive"
        assert "enrico" in confession.lower(), f"Confession for killer {killer_id} missing Enrico"
        # Check veteran hero / warehouse supply context
        assert ("warehouse supply" in confession.lower() or "thirty years" in confession.lower() or "supplies" in confession.lower())
    print("A013–A016 tests passed!")


def test_a012_ica_timeline_and_text():
    print("Testing A012: Ica Visit 6 and Day 7 custody timeline text...")
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()

    # Check IcaDaySix for fire exit, lockbox key, and overnight pursuit
    assert "bolts through the emergency fire exit" in script_text, "Missing fire exit escape in IcaDaySix"
    assert "lockbox key" in script_text, "Missing lockbox key in IcaDaySix"
    assert "rail yard" in script_text, "Missing rail yard flight vector in IcaDaySix"

    # Check day_seven.rpy
    with open("game/day_seven.rpy", "r", encoding="utf-8") as f:
        d7_text = f.read()

    assert "Dhampir and my LAPD patrol tracked them across four rooftops overnight" in d7_text
    assert "hospital check-in logs during the murder" in d7_text
    print("A012 tests passed!")


def test_a112_a113_winston_day_six():
    print("Testing A112–A113: Winston Visit 6 deduction prompt and visible data...")
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()

    # Verify timeline figures are displayed
    assert "21:28 — Neighbor connects emergency call" in script_text, "Missing 21:28 timestamp in WinstonDaySix"
    assert "21:31 — Second witness on sidewalk" in script_text, "Missing 21:31 timestamp in WinstonDaySix"
    assert "21:35 — LAPD patrol unit arrives" in script_text, "Missing 21:35 timestamp in WinstonDaySix"
    assert "exact three-minute window" in script_text, "Missing 3-minute window in WinstonDaySix"

    # Verify prompt aligns with sequence options
    assert "Which post-crime behavior matches the timeline?" in script_text
    print("A112–A113 tests passed!")


if __name__ == "__main__":
    test_a007_profile_fields()
    test_a006_accusation_mismatch()
    test_a008_ulysses_one_each_deduction()
    test_a013_a016_confessions()
    test_a012_ica_timeline_and_text()
    test_a112_a113_winston_day_six()
    print("\nALL PHASE 2 TESTS PASSED SUCCESSFULLY!")
