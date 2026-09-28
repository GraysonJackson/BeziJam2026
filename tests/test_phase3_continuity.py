"""
Phase 3 Continuity Ledger and Consequential State Tracking Test Suite
Verifies:
- A010 & A082–A084: Madeline cutoff consequence, lockouts, apology, debrief, Visit 6 tone gating, and Day 7 friend branch
- A011: Winston Visit 2 call tracking, pager continuity, and debrief privacy
- A069 & A070: Dhampir rooftop travel, snack choice (nachos), retaliation & callbacks
- A095–A098: Nicky album exchange type, departure music, debrief & callbacks
- A121–A128: Ica physical consistency, wager resolution, carpet protection, painting elapsed time, lowered desk, chicken game opt-in/exit
- A129–A142, A216, A222: Ulysses evening sequencing by personal evenings, coma disclosure gate, handholding & near-kiss boundary gates, repeat visit count, 13yo photo fix, stray Freddy token fix, typo fixes
"""

import sys
import os
import textwrap

# Mock Ren'Py store environment
class Store:
    def __init__(self):
        self.killer = 1
        self.remainingSuspects = [1, 2, 3, 4]
        self.investigationClues = []
        self.recordedClueKeys = []
        self.recordedRouteReveals = {}
        self.dayWin = 1
        self.daySevenChosenPartner = ""
        self.daySevenCaseSolved = True
        self.madsRomanceEligible = True
        self.mads_cutoff_violated = False
        self.mads_apology_accepted = False
        self.winston_calls_answered = 0
        self.winston_calls_ignored = 0
        self.winston_day_two_calls = ""
        self.dhampir_rooftop_travel = "flight"
        self.dhampir_movie_snack = ""
        self.nicky_album_exchange_type = ""
        self.ica_paint_preparation = ""
        self.ica_chicken_opted_in = False
        self.ica_chicken_backed_down = False
        self.ulyssesPersonalEvenings = 0
        self.ulyssesEveningsCompleted = 0
        self.ulyssesRomanceInterest = 0
        self.ulyssesBoundaryViolation = False
        self.ulyssesBoundaryApology = False
        self.dayRazz = 6
        self.dayDham = 6
        self.dayMads = 6
        self.dayNick = 6
        self.dayWinn = 6
        self.dayIca = 6
        self.dayWin_count = 6
        self.daySevenIcaSpecial = False
        self.ulyssesCrossReportCompleted = False
        self.suspectNames = {
            1: "Victor Veytovi", 2: "Jermiah Jones", 3: "Barry Baxter",
            4: "Carl Creek", 5: "Tucker Thompson", 6: "Edgar Ebbington",
            7: "Simon Streep", 8: "Kyle Kallus", 9: "Alan Ashmore",
        }
        self.suspectAttributes = {
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
        self.DAY_SEVEN_PARTNERS = [
            ("razzle", "Razzle Dazzle", "razz"),
            ("dhampir", "Dhampir", "dhamp"),
            ("madeline", "Madeline", "mads"),
            ("nicky", "Nicky", "nick"),
            ("winston", "Winston", "winn"),
            ("ica", "Ica", "ica"),
            ("ulysses", "Ulysses", "uly"),
        ]
        self.DAY_SEVEN_ROMANCE_THRESHOLDS = {
            "razzle": 30, "dhampir": 30, "madeline": 30,
            "nicky": 30, "winston": 30, "ica": 32, "ulysses": 30,
        }
        self.DAY_SEVEN_FRIEND_THRESHOLDS = {
            "razzle": 18, "dhampir": 18, "madeline": 18,
            "nicky": 18, "winston": 18, "ica": 18, "ulysses": 18,
        }
        self.DAY_SEVEN_MIN_ROMANCE_VISITS = {
            "razzle": 5, "dhampir": 5, "madeline": 5,
            "nicky": 5, "winston": 5, "ica": 5, "ulysses": 0,
        }
        self.DAY_SEVEN_MIN_FRIEND_VISITS = 2
        self.ULYSSES_DATE_ACCEPT_THRESHOLD = 8
        self.ULYSSES_DATE_MIN_PERSONAL_EVENINGS = 5
        self.ULYSSES_ROUTE_DATA = {
            "razzle": ("Razzle Dazzle", "Razzle", "dayRazz"),
            "dhampir": ("Dhampir", "Dhampir", "dayDham"),
            "madeline": ("Madeline", "Madeline", "dayMads"),
            "nicky": ("Nicky", "Nicky", "dayNick"),
            "winston": ("Winston", "Winston", "dayWinn"),
            "ica": ("Ica", "Ica", "dayIca"),
        }
        self.DAY_SEVEN_PROFILE_FIELDS = [
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
        self.mads = 35
        self.uly = 35
        self.razz = 35
        self.dhamp = 35
        self.nick = 35
        self.winn = 35
        self.ica = 35

    def ulysses_completed_visits(self, route_id):
        data = self.ULYSSES_ROUTE_DATA.get(route_id)
        if data is None:
            return 0
        return max(0, int(getattr(self, data[2])) - 1)

store = Store()
sys.modules['renpy'] = store
sys.modules['renpy.store'] = store

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

class MockRenpy:
    @staticmethod
    def has_label(label):
        return True
    @staticmethod
    def restart_interaction():
        pass
    @staticmethod
    def save_persistent():
        pass
    @staticmethod
    def log(msg):
        pass

mock_renpy = MockRenpy()
sys.modules['renpy'] = mock_renpy

# Load actual day_seven_state.rpy implementation
d7_code = extract_rpy_python("game/day_seven_state.rpy")
d7_ns = {"store": store, "renpy": mock_renpy}
exec(compile(d7_code, "game/day_seven_state.rpy", "exec"), d7_ns)

day_seven_relationship_outcome = d7_ns["day_seven_relationship_outcome"]
day_seven_set_score = d7_ns["day_seven_set_score"]
validate_day_seven_model = d7_ns["validate_day_seven_model"]


def test_a010_a082_a084_madeline_cutoff():
    print("Testing A010 & A082–A084: Madeline helmet cutoff consequence...")
    # Check default state in madeline_route_state.rpy
    with open("game/madeline_route_state.rpy", "r", encoding="utf-8") as f:
        mads_state_text = f.read()
    assert "default mads_cutoff_violated = False" in mads_state_text
    assert "default madsRomanceEligible = True" in mads_state_text
    assert "default mads_apology_accepted = False" in mads_state_text

    # Outcome logic checks using actual day_seven_state.rpy logic:
    # 1. Normal high score -> romance
    store.madsRomanceEligible = True
    store.mads_cutoff_violated = False
    store.mads_apology_accepted = False
    day_seven_set_score("madeline", 35)
    assert day_seven_relationship_outcome("madeline", True) == "romance"

    # Normal medium score -> friend
    day_seven_set_score("madeline", 20)
    assert day_seven_relationship_outcome("madeline", True) == "friend"

    # Normal low score -> rejection
    day_seven_set_score("madeline", 10)
    assert day_seven_relationship_outcome("madeline", True) == "rejection"

    # 2. Cutoff violated, no apology -> rejection (even with high score)
    store.madsRomanceEligible = False
    store.mads_cutoff_violated = True
    store.mads_apology_accepted = False
    day_seven_set_score("madeline", 35)
    assert day_seven_relationship_outcome("madeline", True) == "rejection"

    # 3. Cutoff violated, apology accepted -> friend (romance locked out even with 35 score)
    store.madsRomanceEligible = False
    store.mads_cutoff_violated = True
    store.mads_apology_accepted = True
    day_seven_set_score("madeline", 35)
    assert day_seven_relationship_outcome("madeline", True) == "friend"

    # Cutoff violated, apology accepted, but low score -> rejection
    day_seven_set_score("madeline", 10)
    assert day_seven_relationship_outcome("madeline", True) == "rejection"

    # Script checks:
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()

    # Visit 5 cutoff abort
    assert "$ mads_cutoff_violated = True" in script_text
    assert "$ madsRomanceEligible = False" in script_text
    assert "mads_cutoff_violated:" in script_text
    assert "Personal time is terminated." in script_text
    assert "Calibration aborted." in script_text and "stricken from the record." in script_text
    assert "jump endOfDay" in script_text

    # Visit 6 apology option and tone gating
    assert "Yesterday you ignored a cutoff order while I was strapped into a feedback machine" in script_text
    assert "$ mads_apology_accepted = True" in script_text
    assert "The bitter chill breaks into a focused, professional truce." in script_text
    assert "observation chair" in script_text
    assert "don't make a sound." in script_text or "don't speak" in script_text

    # Verify no flirty slip during Visit 6 procedure when cutoff violated
    assert "if not mads_cutoff_violated:" in script_text
    assert "elif mads_apology_accepted:" in script_text
    assert "The seals hold. Load the cartridges and keep your hands off the panel." in script_text
    assert "Don't flatter yourself with conversation. Touch the cartridges." in script_text
    assert "Replication is standard procedure. Don't narrate my own protocol to me." in script_text

    # Ulysses report check
    with open("game/ulysses_evenings.rpy", "r", encoding="utf-8") as f:
        ulysses_text = f.read()
    assert "if mads_cutoff_violated:" in ulysses_text
    assert "The automatic timer triggered because you ignored her verbal stop command." in ulysses_text
    assert "Acknowledge the protocol breach directly without excuses." in ulysses_text

    # Day 7 friend ending check in day_seven.rpy
    with open("game/day_seven.rpy", "r", encoding="utf-8") as f:
        day_seven_text = f.read()
    assert 'if getattr(store, "mads_cutoff_violated", False):' in day_seven_text
    assert "No. Not romantically. We settled that yesterday." in day_seven_text
    assert "keeping the boundary firm without holding yesterday's breach over you." in day_seven_text

    # Run engine self-validation test in day_seven_state.rpy
    assert validate_day_seven_model() is True
    print("A010 & A082–A084 tests passed!")


def test_a011_winston_calls():
    print("Testing A011: Winston Visit 2 call tracking & debrief...")
    with open("game/winston_route_state.rpy", "r", encoding="utf-8") as f:
        winn_state_text = f.read()
    assert "default winston_calls_answered = 0" in winn_state_text
    assert "default winston_calls_ignored = 0" in winn_state_text

    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()
    assert "$ winston_calls_answered = 3" in script_text
    assert "$ winston_calls_ignored = 1" in script_text
    assert "switch off the pager" in script_text
    assert "unplug the pager" not in script_text
    assert 'if winston_day_two_calls == "screened":' in script_text

    with open("game/ulysses_evenings.rpy", "r", encoding="utf-8") as f:
        ulysses_text = f.read()
    assert "[winston_calls_answered]" in ulysses_text
    assert "He answered none of the calls" not in ulysses_text
    assert "Report that he answered three minor workplace crises before ignoring the fourth." in ulysses_text
    assert "Report his private confession about feeling like an emergency brake." in ulysses_text
    assert "Winston's private doubts about his role are between him and the people he trusts. They are not report material. Stick to the operational debrief." in ulysses_text
    print("A011 tests passed!")


def test_a069_a070_dhampir_continuity():
    print("Testing A069 & A070: Dhampir rooftop travel and snack tracking...")
    with open("game/dhampir_route_state.rpy", "r", encoding="utf-8") as f:
        dham_state_text = f.read()
    assert 'default dhampir_rooftop_travel = "flight"' in dham_state_text
    assert 'default dhampir_movie_snack = ""' in dham_state_text

    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()
    assert '$ dhampir_movie_snack = "nachos"' in script_text
    assert '$ dhampir_rooftop_travel = "flight"' in script_text
    assert '$ dhampir_rooftop_travel = "stairs"' in script_text
    assert 'if dhampir_rooftop_travel == "stairs":' in script_text
    assert 'dhampir_movie_snack == "nachos"' in script_text
    assert "He swipes a nacho dripping with cheese in retaliation." in script_text
    assert "He nudges your sneaker and playfully reclaims the shared armrest in retaliation." in script_text
    assert "We'll risk the movie theater nachos again." in script_text
    print("A069 & A070 tests passed!")


def test_a095_a098_nicky_album():
    print("Testing A095–A098: Nicky album exchange type and departure...")
    with open("game/nicky_route_state.rpy", "r", encoding="utf-8") as f:
        nick_state_text = f.read()
    assert 'default nicky_album_exchange_type = ""' in nick_state_text

    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()
    assert '$ nicky_album_exchange_type = "gift"' in script_text
    assert '$ nicky_album_exchange_type = "loan"' in script_text
    assert '$ nicky_album_exchange_type = "recommendation"' in script_text
    assert 'if nicky_day_two_music == "hiphop":' in script_text
    assert 'elif nicky_day_two_music == "romantic":' in script_text
    assert 'elif nicky_day_two_music == "classical":' in script_text
    assert 'if nicky_album_exchange_type == "loan":' in script_text

    with open("game/ulysses_evenings.rpy", "r", encoding="utf-8") as f:
        ulysses_text = f.read()
    assert 'if nicky_album_exchange_type == "gift":' in ulysses_text
    assert 'elif nicky_album_exchange_type == "loan":' in ulysses_text
    assert 'Say she gave you an album that proved she listened.' in ulysses_text
    assert 'Say she trusted you enough to lend you her own tape.' in ulysses_text
    assert 'Mention the listening homework she scribbled on the receipt.' in ulysses_text
    print("A095–A098 tests passed!")


def test_a121_a128_ica_continuity():
    print("Testing A121–A128: Ica physical consistency, wagers, and chicken opt-in...")
    with open("game/ica_eating_minigame.rpy", "r", encoding="utf-8") as f:
        eating_text = f.read()
    assert "Ica caught your discarded hot dog with gravity and floated it back" in eating_text

    with open("game/script.rpy", "r", encoding="utf-8") as f:
        script_text = f.read()

    # A122 Wager
    assert "Mostly I'm annoyed that I lost the bet and actually have to throw this shit away" in script_text
    assert "Bet's a bet, freshie. You're taking out the trash." in script_text
    # A124 Painting elapsed time & touch up
    assert "only the high trim and missed corners remain to touch up" in script_text
    assert "Within twenty minutes, the remaining patches are blended" in script_text
    # A125 Lowered desk
    assert "Ulysses collects one folder from his freshly lowered desk and leaves." in script_text
    assert "floating edge of his desk" not in script_text

    # A128 Chicken opt-in & exit
    assert "$ ica_chicken_opted_in = False" in script_text
    assert "$ ica_chicken_opted_in = True" in script_text
    assert "$ ica_chicken_backed_down = True" in script_text
    assert 'if not ica_chicken_opted_in:' in script_text
    assert "Suit yourself. Less work for me anyway." in script_text
    assert "zero games of chicken" in script_text

    # Ulysses reports 4 and 5
    with open("game/ulysses_evenings.rpy", "r", encoding="utf-8") as f:
        ulysses_text = f.read()
    assert "ica_paint_preparation" in ulysses_text
    assert "Ica being forced to throw away her own trash is an unprecedented achievement in this building." in ulysses_text
    assert "At least you taped down a drop cloth. The floor survived your artistic impulses." in ulysses_text
    assert "Cardboard beneath the cans did not protect the floor from roller splatter, recruit." in ulysses_text
    print("A121–A128 tests passed!")


def test_a129_a142_a216_ulysses():
    print("Testing A129–A142, A216, A222: Ulysses personal evenings, boundary gates, and copy fixes...")
    with open("game/ulysses_evenings.rpy", "r", encoding="utf-8") as f:
        ulysses_text = f.read()

    # A129 Personal evening dispatch by ulyssesPersonalEvenings
    assert "if ulyssesPersonalEvenings == 1:" in ulysses_text
    assert "call UlyssesEveningOne" in ulysses_text
    assert "elif ulyssesPersonalEvenings == 2:" in ulysses_text
    assert "call UlyssesEveningTwo" in ulysses_text
    assert "elif ulyssesPersonalEvenings == 3:" in ulysses_text
    assert "call UlyssesEveningThree" in ulysses_text
    assert "elif ulyssesPersonalEvenings == 4:" in ulysses_text
    assert "call UlyssesEveningFour" in ulysses_text

    # A137 repeat visit comment based on ulysses_today_count
    assert "if ulysses_today_count == 2:" in ulysses_text
    assert "elif ulysses_today_count == 3:" in ulysses_text
    assert "elif ulysses_today_count == 4:" in ulysses_text
    assert "elif ulysses_today_count == 5:" in ulysses_text

    # A216 stray Freddy removed
    assert "vest and button-up Freddy" not in ulysses_text
    assert "leaving the vest and button-up, and rolls each sleeve once." in ulysses_text

    # A222 passtime -> pastime typo
    assert "passtime" not in ulysses_text
    assert "ask him to choose a pastime." in ulysses_text

    # did'nt -> didn't typo
    assert "did'nt" not in ulysses_text
    assert "She didn't blame me for what happened." in ulysses_text

    # A142 romance points on 13yo photo
    assert "You look cute in the photograph." not in ulysses_text
    assert "You were remarkably stubborn in that photo. You carry it better now." in ulysses_text
    assert "A compliment directed at the present is considerably harder to deflect." in ulysses_text

    # A130 & A131 coma disclosure gate in UlyssesEveningFour
    assert 'if ulyssesBoundaryViolation and not ulyssesBoundaryApology:' in ulysses_text
    assert 'elif ulysses_day_three_choice == "learned_boundary":' in ulysses_text

    # A132 handholding gate in UlyssesEveningFive
    assert '"Turn your hand palm-up beside his." if not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):' in ulysses_text

    # A133 UlyssesEveningSix apology, closeness gating, and romance gate
    assert 'if ulyssesBoundaryViolation and not ulyssesBoundaryApology:' in ulysses_text
    assert 'Apologize for treating his survival like another clue.' in ulysses_text
    assert '"Tell him these evenings became the best part of the week." if ulyssesPersonalEvenings >= 3 and not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):' in ulysses_text
    assert '"Step close and straighten his tie." if not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):' in ulysses_text
    assert "ulysses_romance_eligible = (" in ulysses_text
    assert "not (ulyssesBoundaryViolation and not ulyssesBoundaryApology)" in ulysses_text
    assert "ulyssesPersonalEvenings >= ULYSSES_DATE_MIN_PERSONAL_EVENINGS" in ulysses_text

    # DaySeven romance gate in day_seven_state.rpy using real day_seven_relationship_outcome
    store.ulyssesRomanceInterest = 10
    store.ulyssesPersonalEvenings = 5
    store.ulyssesBoundaryViolation = True
    store.ulyssesBoundaryApology = False
    day_seven_set_score("ulysses", 35)
    assert day_seven_relationship_outcome("ulysses", True) == "friend"

    # Apologized restores romance eligibility
    store.ulyssesBoundaryApology = True
    assert day_seven_relationship_outcome("ulysses", True) == "romance"

    # Under 5 personal evenings locks out romance
    store.ulyssesPersonalEvenings = 4
    assert day_seven_relationship_outcome("ulysses", True) == "friend"

    # Failed case rejects
    assert day_seven_relationship_outcome("ulysses", False) == "rejection"
    print("A129–A142, A216, A222 tests passed!")


if __name__ == "__main__":
    test_a010_a082_a084_madeline_cutoff()
    test_a011_winston_calls()
    test_a069_a070_dhampir_continuity()
    test_a095_a098_nicky_album()
    test_a121_a128_ica_continuity()
    test_a129_a142_a216_ulysses()
    print("\nALL PHASE 3 CONTINUITY TESTS PASSED SUCCESSFULLY!")
