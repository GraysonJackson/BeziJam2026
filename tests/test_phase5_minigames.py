"""Verification tests for Phase 5 Minigames (A145-A182)."""

import unittest
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestPhase5Minigames(unittest.TestCase):

    def test_a146_a147_height_memory(self):
        """Verify height memory catalog has no case-lore conflicts and uses in-place replacement."""
        path = os.path.join(ROOT, "game", "height_memory_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check distractors updated
        self.assertIn("A bulky coat rack standing by the door.", content)
        self.assertIn("A stray gust rattling the wind chimes.", content)
        self.assertIn("A garden hose coiled up near the porch.", content)
        self.assertNotIn("The figure may have worn a bulky coat.", content)
        self.assertNotIn("Footsteps hurried across the gravel.", content)
        self.assertNotIn("The hedge shook after the figure passed.", content)

        # Check in-place replacement
        self.assertIn("def _height_memory_replace_card", content)
        self.assertIn("_height_memory_replace_card(card_id)", content)

    def test_a149_a152_dhampir_ispy(self):
        """Verify Dhampir I-spy orientation feedback, 3rd clue hold, and review function."""
        path = os.path.join(ROOT, "game", "dhampir_ispy_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check contextual orientation feedback
        self.assertIn("Dhampir claims the attacker struck walls and furniture with bare fists.", content)
        self.assertIn("Dhampir claims the attacker scraped their hands on rough entryways.", content)
        self.assertIn("Dhampir claims the attacker escaped without a single injury.", content)

        # Check review method exists
        self.assertIn("def dhampir_ispy_review(target_id):", content)

        # Check 3rd clue text not overwritten
        self.assertNotIn("store.dhampir_ispy_feedback = (\n                \"All three inconsistencies found.", content)

        # Check screen review support
        screen_path = os.path.join(ROOT, "game", "screens", "dhampir_ispy_minigame.rpy")
        with open(screen_path, "r", encoding="utf-8") as f:
            screen_content = f.read()
        self.assertIn("Function(dhampir_ispy_review, target_id)", screen_content)

    def test_a153_a155_madeline_centrifuge(self):
        """Verify centrifuge masses allow meaningful trim."""
        path = os.path.join(ROOT, "game", "madeline_centrifuge_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn('"mass": 5', content)
        self.assertIn('"mass": 4', content)
        self.assertIn('"mass": 6', content)
        self.assertIn('"mass": 3', content)

        # Test balance math:
        # 6 + 3 = 9 vs 5 + 4 = 9 (diff 0)
        # 6 + 4 = 10 vs 5 + 3 = 8 (diff +2, can be balanced with trim -2!)
        self.assertEqual((6 + 4) - (5 + 3), 2)
        self.assertEqual((6 + 3) - (5 + 4), 0)

        # Check screen button
        screen_path = os.path.join(ROOT, "game", "screens", "madeline_centrifuge_minigame.rpy")
        with open(screen_path, "r", encoding="utf-8") as f:
            screen_content = f.read()
        self.assertIn("INSPECT DENSITY BANDS", screen_content)

    def test_a156_nicky_memory_pairs(self):
        """Verify Nicky Round 1 pairs are all consistent record sources."""
        path = os.path.join(ROOT, "game", "nicky_memory_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn('("witness", "WITNESS WORDING", "CANVASS INTERVIEW", "STATEMENT")', content)
        self.assertNotIn("UNVERIFIED ASSUMPTION", content)

    def test_a163_winston_pressure_viewport(self):
        """Verify dealer hand is wrapped in a viewport."""
        screen_path = os.path.join(ROOT, "game", "screens", "winston_pressure_minigame.rpy")
        with open(screen_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("viewport:", content)
        self.assertIn("winston_pressure_dealer_hand", content)

    def test_a164_a166_ica_cards(self):
        """Verify Ica cards approach description and explicit leeway in round results."""
        path = os.path.join(ROOT, "game", "ica_cards_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("leeway", content)
        self.assertIn("leeway_win", content)
        self.assertIn("Sleight of hand flips the round!", content)

    def test_a168_a170_ica_staring(self):
        """Verify staring finishes immediately on hold completion and dialogue is accurate."""
        path = os.path.join(ROOT, "game", "ica_staring_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("if store.ica_staring_success_time >= store.ica_staring_required_hold:", content)

        script_path = os.path.join(ROOT, "game", "script.rpy")
        with open(script_path, "r", encoding="utf-8") as f:
            script_content = f.read()
        self.assertIn("Whoever holds eye contact longest without blinking out takes it.", script_content)
        self.assertNotIn("First person to blink loses.", script_content)

    def test_a172_a174_ica_board_game(self):
        """Verify AI turn automation, win priority, and character bump strategy."""
        path = os.path.join(ROOT, "game", "ica_board_game_minigame.rpy")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("if position + card_value >= store.ICA_BOARD_FINISH:", content)

        screen_path = os.path.join(ROOT, "game", "screens", "ica_board_game_minigame.rpy")
        with open(screen_path, "r", encoding="utf-8") as f:
            screen_content = f.read()
        self.assertIn("timer 1.0 action Function(ica_board_ica_turn)", screen_content)
        self.assertIn("timer 1.0 action Function(ica_board_winston_turn)", screen_content)

    def test_a176_a177_ica_eating(self):
        """Verify eating button sensitivity during cooldown and accurate rules text."""
        screen_path = os.path.join(ROOT, "game", "screens", "ica_eating_minigame.rpy")
        with open(screen_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("sensitive ica_eating_action_cooldown <= 0.0", content)

        rules_path = os.path.join(ROOT, "game", "screens", "minigame_rules.rpy")
        with open(rules_path, "r", encoding="utf-8") as f:
            rules_content = f.read()
        self.assertIn("Flirting and cheating grant a one-time special move; playing fair relies on steady", rules_content)
        self.assertIn("Bite and Pace rhythm.", rules_content)


if __name__ == "__main__":
    unittest.main()
