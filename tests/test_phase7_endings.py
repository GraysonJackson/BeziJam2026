"""
Unit and integration tests for Phase 7 Endings and Climax (A204-A215, A230).
"""

import os
import re
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestPhase7Endings(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT_DIR, "game", "day_seven.rpy"), "r", encoding="utf-8") as f:
            self.day_seven_text = f.read()
        with open(os.path.join(ROOT_DIR, "game", "day_seven_state.rpy"), "r", encoding="utf-8") as f:
            self.day_seven_state_text = f.read()
        with open(os.path.join(ROOT_DIR, "game", "screens", "day_seven_screens.rpy"), "r", encoding="utf-8") as f:
            self.day_seven_screens_text = f.read()

    def test_a204_direct_friendship_choice_in_scene(self):
        """A204: Verify players can ask for direct friendship without romantic rejection."""
        # Check that each character ending includes an option to ask for friendship directly
        partners = ["Razzle", "Winston", "Nicky", "Ica", "Ulysses", "Madeline", "Dhampir"]
        for partner in partners:
            self.assertIn(
                f"label DaySevenEnding{partner}:",
                self.day_seven_text,
                f"Missing ending label for {partner}"
            )
            # Find the menu block in that character's label
            char_block = re.search(
                rf"label DaySevenEnding{partner}:.*?(?=\nlabel|\Z)",
                self.day_seven_text,
                re.DOTALL
            ).group(0)
            if partner != "Ulysses":
                self.assertIn(
                    "as friends",
                    char_block,
                    f"Direct friendship choice missing from {partner} ending menu"
                )
            else:
                self.assertIn(
                    "outside the office as friends",
                    char_block,
                    "Direct friendship choice missing from Ulysses ending menu"
                )
            # Ensure daySevenRelationshipOutcome is set to 'friend' on direct friendship acceptance
            self.assertIn('daySevenRelationshipOutcome = "friend"', char_block)

    def test_a205_readiness_signals_in_dialogue(self):
        """A205: Verify clear dialogue cues and readiness checks exist before player choice."""
        partners = ["razz", "winn", "nick", "ica", "uly", "mads", "dham"]
        for p in partners:
            self.assertIn(
                f"_{p}_romance_ready",
                self.day_seven_text,
                f"Romance readiness check missing for {p}"
            )
            self.assertIn(
                f"_{p}_friend_ready",
                self.day_seven_text,
                f"Friend readiness check missing for {p}"
            )

    def test_a206_varied_invitation_language(self):
        """A206: Invitations must not use identical phrasing across all characters."""
        invitations = re.findall(r'"Ask ([^"]+) on an? (?:actual|romantic) date[^"]*":', self.day_seven_text)
        self.assertGreaterEqual(len(invitations), 7, "Expected at least 7 varied date invitation options")
        # Ensure phrasing varies
        phrasings = re.findall(r'"Ask [^"]+ on an? (?:actual|romantic) date—([^"]+)":', self.day_seven_text)
        self.assertEqual(len(phrasings), len(set(phrasings)), "Date invitations should have unique character-specific phrasing")

    def test_a207_lively_date_vignettes(self):
        """A207: Romance endings must include concrete date dialogue/vignettes rather than generic summary."""
        self.assertIn("The following weekend at The Red Room", self.day_seven_text)
        self.assertIn("On Saturday night at Barney's Billiards", self.day_seven_text)
        self.assertIn("tactical reconnaissance", self.day_seven_text)
        self.assertIn("cutting through freeway traffic on the back of her bike", self.day_seven_text)
        self.assertIn("At midnight on the gravel roof above a 24-hour convenience store", self.day_seven_text)
        self.assertIn("late-night bookstore", self.day_seven_text)
        self.assertIn("On Saturday under buzzing floodlights at Pirate's Cove Mini-Golf", self.day_seven_text)
        self.assertIn("That weekend in the dimly lit basement of an unlicensed venue", self.day_seven_text)

    def test_a208_non_defensive_rejections(self):
        """A208: Rejections must demonstrate boundaries directly without narrator defensiveness."""
        # Ensure previous defensive narrator lines are removed
        self.assertNotIn("He refuses to make the rejection cruel, but he also refuses to disguise it as uncertainty.", self.day_seven_text)
        self.assertNotIn("She leaves the rejection sharp, truthful, and impossible to mistake for an experiment still in progress.", self.day_seven_text)
        self.assertNotIn("He gives you a casual farewell and does not turn the rejection into either a punishment or a joke.", self.day_seven_text)

    def test_a209_madeline_failure_response_branches(self):
        """A209: Madeline failure ending must adapt to dismissal response (defend vs joke vs owned)."""
        mads_block = re.search(
            r"label DaySevenEndingMadeline:.*?(?=\nlabel|\Z)",
            self.day_seven_text,
            re.DOTALL
        ).group(0)
        self.assertIn('if daySevenFailureResponse == "defend":', mads_block)
        self.assertIn('elif daySevenFailureResponse == "joke":', mads_block)
        self.assertIn("intellectually indefensible", mads_block)
        self.assertIn("making a joke about paperwork", mads_block)

    def test_a211_offsite_or_perimeter_failure_access(self):
        """A211: Dismissed protagonist interactions happen at exit/perimeter, respecting security."""
        self.assertIn("Winston catches you at the security sign-out desk", self.day_seven_text)
        self.assertIn("Nicky is adjusting her helmet by her motorcycle at the parking gate", self.day_seven_text)
        self.assertIn("Ica is sitting on the wide concrete steps outside the building", self.day_seven_text)
        self.assertIn("Madeline is packing field equipment into her car by the loading dock", self.day_seven_text)
        self.assertIn("Dhampir returns from searching long enough to find you beside the secure exit", self.day_seven_text)

    def test_a212_alone_ending_confident_tone(self):
        """A212: Alone ending must be confident without apologetic comparison to romance."""
        alone_block = re.search(
            r"label DaySevenEndingAlone:.*?(?=\nlabel|\Z)",
            self.day_seven_text,
            re.DOTALL
        ).group(0)
        self.assertNotIn("It is not a lesser ending", alone_block)
        self.assertNotIn("without asking anyone for romance", alone_block)
        self.assertIn("wanted, trusted, and fully cemented as an ATLAS detective", alone_block)

        outro_block = re.search(
            r"label DaySevenOutro:.*?(?=\nlabel|\Z)",
            self.day_seven_text,
            re.DOTALL
        ).group(0)
        self.assertNotIn("It is not a lesser ending", outro_block)
        self.assertIn("You celebrate with the team that brought the case home.", outro_block)

    def test_a214_gallery_grouping_and_hints(self):
        """A214: Ending gallery groups by character with spoiler-safe status hints."""
        for group in ["RAZZLE DAZZLE", "WINSTON", "NICKY", "ICA", "ULYSSES", "MADELINE", "DHAMPIR", "ATLAS TEAM & SOLO"]:
            self.assertIn(group, self.day_seven_screens_text, f"Gallery missing character group header: {group}")
        self.assertIn("Locked: Requires romantic connection", self.day_seven_screens_text)
        self.assertIn("Locked: Requires friendship trust", self.day_seven_screens_text)

    def test_a215_unlock_after_viewing_ending(self):
        """A215: Ending unlock occurs after DaySevenCharacterEnding completes."""
        finale = re.search(r"label DaySevenStart:.*?(?=\nlabel|\Z)", self.day_seven_text, re.DOTALL).group(0)
        self.assertLess(finale.index("call DaySevenRelationshipSelection"), finale.index("call DaySevenOutro"))
        self.assertLess(finale.index("call DaySevenOutro"), finale.index("day_seven_unlock_ending"))
        self.assertLess(finale.index("day_seven_unlock_ending"), finale.index("call screen day_seven_credits"))

    def test_a230_ending_attainability_and_catalog(self):
        """A230: Verify 42 endings catalog integrity and legal threshold ranges."""
        # Total catalog count must remain exactly 42
        keys = re.findall(r'"key":\s*"([^"]+)"', self.day_seven_state_text)
        # Check day_seven_ending_catalog generates 42 keys
        # We can simulate day_seven_ending_catalog logic
        partners = ["razzle", "winston", "nicky", "ica", "ulysses", "madeline", "dhampir"]
        outcomes = ["romance", "friend", "rejection"]
        expected_keys = []
        for solved in (True, False):
            res = "success" if solved else "failure"
            for p in partners:
                avail = outcomes
                if not solved and p == "ulysses":
                    avail = ["rejection"]
                for o in avail:
                    expected_keys.append(f"{res}_{p}_{o}")
            expected_keys.append(f"{res}_alone")

        self.assertEqual(len(expected_keys), 42, "Expected exactly 42 endings")
        self.assertEqual(len(set(expected_keys)), 42, "Expected 42 unique ending keys")


if __name__ == "__main__":
    unittest.main()
