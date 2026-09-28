"""Exercise the game's real Python definitions, without duplicating its rules.

These are source-level tests. Ren'Py interaction tests live in game/testcases.rpy.
"""
import ast
import codeop
import re
import textwrap
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]


def load_rpy(path, namespace, names=None):
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines(True)
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith(("define ", "default ")):
            code = line.split(" ", 1)[1]
            while codeop.compile_command(code) is None:
                index += 1
                code += lines[index]
            target = ast.parse(code).body[0].targets[0]
            name = target.id if isinstance(target, ast.Name) else None
            if names is None or name in names:
                exec(compile(code, path, "exec"), namespace)
                if name:
                    setattr(namespace["store"], name, namespace[name])
        elif re.match(r"init(?: -?\d+)? python:", line) and names is None:
            block = []
            index += 1
            while index < len(lines) and (not lines[index].strip() or lines[index].startswith("    ")):
                block.append(lines[index])
                index += 1
            pre_keys = set(namespace.keys())
            exec(compile(textwrap.dedent("".join(block)), path, "exec"), namespace)
            for k in set(namespace.keys()) - pre_keys:
                if "store" in namespace and not hasattr(namespace["store"], k):
                    setattr(namespace["store"], k, namespace[k])
            continue
        index += 1


class RoundTwoTests(unittest.TestCase):
    def setUp(self):
        self.store = SimpleNamespace()
        self.persistent = SimpleNamespace(daySevenEndings={})
        self.ns = {
            "store": self.store, "persistent": self.persistent,
            "renpy": Mock(), "config": SimpleNamespace(label_callbacks=[], save_json_callbacks=[]),
        }

    def load_endings(self):
        load_rpy("game/day_seven_state.rpy", self.ns)
        load_rpy("game/investigation.rpy", self.ns)
        self.store.suspectNames = self.ns["suspectNames"]
        self.store.suspectAttributes = self.ns["suspectAttributes"]
        self.store.killer = 1
        self.store.mads_cutoff_violated = False
        self.store.mads_apology_accepted = False

    def test_real_catalog_and_legacy_replay(self):
        self.load_endings()
        entries = self.ns["day_seven_ending_catalog"]()
        self.assertEqual(42, len({e["key"] for e in entries}))
        for entry in entries:
            key = entry["key"]
            self.persistent.daySevenEndings[key] = {"killer": 2}
            self.ns["day_seven_setup_gallery_replay"](key)
            self.assertEqual(entry["outcome"], self.store.daySevenRelationshipOutcome)
            self.assertEqual(entry["solved"], self.store.daySevenCaseSolved)
            self.assertEqual(2, self.store.killer)
            if entry["outcome"] == "friend":
                self.assertEqual("friend", self.store.daySevenRelationshipIntent)

    def test_replay_preserves_ask_and_boundary_without_unlocking(self):
        self.load_endings()
        self.store.daySevenRelationshipIntent = "romance"
        self.store.daySevenFailureResponse = "joke"
        self.store.mads_cutoff_violated = True
        self.store.mads_apology_accepted = True
        key = "failure_madeline_friend"
        self.ns["day_seven_unlock_ending"](key)
        original = dict(self.persistent.daySevenEndings[key])
        self.store.daySevenRelationshipIntent = "friend"
        self.ns["day_seven_setup_gallery_replay"](key)
        self.assertEqual("romance", self.store.daySevenRelationshipIntent)
        self.assertEqual("joke", self.store.daySevenFailureResponse)
        self.assertTrue(self.store.mads_cutoff_violated)
        self.store.killer = 9
        self.ns["day_seven_unlock_ending"](key)
        self.assertEqual(original, self.persistent.daySevenEndings[key])
        self.ns["renpy"].save_persistent.assert_called_once()

    def test_missing_evidence_is_not_a_contradiction(self):
        self.load_endings()
        self.store.recordedRouteReveals = {}
        self.store.investigationClues = []
        fn = self.ns["day_seven_mismatch_info"]
        self.assertEqual("insufficient_evidence", fn(2)["kind"])
        self.store.recordedRouteReveals["razzle_6"] = {
            "visit": 6, "attribute": "hair", "value": self.store.suspectAttributes[1]["hair"]}
        self.assertEqual("contradicts_gathered", fn(2)["kind"])

    def test_pause_resume_does_not_end_the_call_screen(self):
        load_rpy("game/screens/minigame_rules.rpy", self.ns)
        for game in self.store.MINIGAME_RULES:
            self.ns["minigame_pause"](game)
            self.assertTrue(self.store.minigame_paused)
            self.ns["minigame_resume"]()
            self.assertFalse(self.store.minigame_paused)
        self.ns["renpy"].end_interaction.assert_not_called()

    def test_metadata_captures_calendar_and_visit_independently(self):
        load_rpy("game/save_context.rpy", self.ns)
        self.store.dayWin = 6
        self.ns["update_save_context"]("RazzleDayTwo")
        saved = {}
        self.ns["case_save_metadata"](saved)
        self.ns["update_save_context"]("IcaDaySix")
        self.assertEqual("Day 6\nRazzle Dazzle · Visit 2", saved["case_context"])
        self.ns["update_save_context"]("DaySevenStart")
        self.store.dayWin = 7
        current = {}
        self.ns["case_save_metadata"](current)
        self.assertEqual("Day 7\nFinal accusation", current["case_context"])

    def test_ica_board_ai_priority_and_withdrawal(self):
        self.ns["push_minigame_music"] = Mock()
        self.ns["pop_minigame_music"] = Mock()
        load_rpy("game/ica_minigame_state.rpy", self.ns)
        load_rpy("game/ica_board_game_minigame.rpy", self.ns)

        # AI win priority: even if card 2 bumps opponent at pos 10, card 4 wins at finish (12)
        self.store.ica_board_ica_position = 8
        self.store.ica_board_player_position = 10
        self.store.ica_board_winston_position = 0
        ai_card = self.ns["_ica_board_choose_ai_card"]("ica", [2, 4])
        self.assertEqual(4, ai_card)

        # AI bump strategy when winning is not possible
        self.store.ica_board_ica_position = 2
        self.store.ica_board_winston_position = 4
        self.store.ica_board_player_position = 0
        ai_card = self.ns["_ica_board_choose_ai_card"]("ica", [1, 2])
        self.assertEqual(2, ai_card)

        # Withdrawal
        self.ns["start_ica_board_game_minigame"]("play_fair")
        self.ns["ica_board_withdraw"]()
        self.assertEqual("withdrawn", self.store.ica_board_winner)
        self.assertFalse(self.store.ica_board_pending_won)
        self.assertEqual("complete_pending", self.store.ica_board_phase)
        self.ns["finish_ica_board_game_minigame"]()
        self.assertTrue(self.store.ica_board_result_applied)
        result = self.store.ica_minigame_results.get("board", {})
        self.assertFalse(result.get("won"))
        self.assertEqual("loss_withdrawn", result.get("result_tier"))

    def test_ica_prank_checkpoint_consistency(self):
        self.ns["push_minigame_music"] = Mock()
        self.ns["pop_minigame_music"] = Mock()
        load_rpy("game/ica_minigame_state.rpy", self.ns)
        load_rpy("game/ica_prank_minigame.rpy", self.ns)

        self.ns["_ica_prank_reset_state"]("cheat")
        self.assertEqual("pickup", self.store.ica_prank_objective)
        self.assertFalse(self.store.ica_prank_has_paint)

        # Simulate getting paint and painting target
        self.store.ica_prank_player_position = self.store.ICA_PRANK_PAINT_TILE
        self.store.ica_prank_has_paint = True
        self.store.ica_prank_objective = "paint"
        self.store.ica_prank_painted_targets = [(9, 1)]
        self.ns["ica_prank_set_checkpoint"](restart=False)

        # Simulate moving into sight and getting caught
        self.store.ica_prank_player_position = self.store.ica_prank_ulysses_position
        self.assertTrue(self.ns["_ica_prank_trigger_detection"]())
        self.assertEqual(1, self.store.ica_prank_caught_count)
        self.assertEqual("caught", self.store.ica_prank_phase)

        # Reset to checkpoint preserves paint, painted targets, objective, and caught count
        self.ns["ica_prank_reset_to_checkpoint"]()
        self.assertEqual("active", self.store.ica_prank_phase)
        self.assertEqual(self.store.ICA_PRANK_PAINT_TILE, self.store.ica_prank_player_position)
        self.assertTrue(self.store.ica_prank_has_paint)
        self.assertEqual("paint", self.store.ica_prank_objective)
        self.assertEqual([(9, 1)], self.store.ica_prank_painted_targets)
        self.assertEqual(1, self.store.ica_prank_caught_count)

    def test_nicky_matching_semantic_equivalence_and_completion(self):
        load_rpy("game/investigation.rpy", self.ns)
        load_rpy("game/nicky_route_state.rpy", self.ns)
        load_rpy("game/nicky_memory_minigame.rpy", self.ns)

        # Setup Phase 1 with two suspects sharing the same build
        self.store.remainingSuspects = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.store.suspectNames = self.ns["suspectNames"]
        self.store.suspectAttributes = self.ns["suspectAttributes"]
        self.store.nicky_memory_reveal = {
            "scope": "category",
            "value": "Average",
            "eliminated": [3, 5],
        }
        # Force both to have Average build in suspectAttributes
        self.store.suspectAttributes[3]["build"] = "Average"
        self.store.suspectAttributes[5]["build"] = "Average"

        self.store.nicky_memory_active = True
        self.ns["_nicky_memory_load_phase"](1)
        self.assertEqual(6, len(self.ns["_nicky_memory_pair_definitions"](1)))

        cards = self.store.nicky_memory_cards
        card_a_file = next(c for c in cards if c["pair_id"] == "suspect_a" and "\nBOOKING FILE" in c["text"])
        card_b_meas = next(c for c in cards if c["pair_id"] == "suspect_b" and "INTAKE MEASUREMENT\n" in c["text"])

        # Cross match should succeed because both have the same build description
        self.store.nicky_memory_selected_ids = [card_a_file["id"], card_b_meas["id"]]
        self.ns["nicky_memory_resolve_pair"]()
        self.assertIn("suspect_a", self.store.nicky_memory_matched_pairs)
        self.assertEqual(0, self.store.nicky_memory_mistakes)

        # The remaining cross pair should now match under suspect_b
        card_b_file = next(c for c in cards if c["pair_id"] == "suspect_b" and "\nINTAKE FILE" in c["text"])
        card_a_meas = next(c for c in cards if c["id"] != card_b_meas["id"] and ("MEASUREMENT\n" in c["text"] or "MEASURED FRAME\n" in c["text"]))
        self.store.nicky_memory_selected_ids = [card_b_file["id"], card_a_meas["id"]]
        self.ns["nicky_memory_resolve_pair"]()
        self.assertIn("suspect_b", self.store.nicky_memory_matched_pairs)
        self.assertEqual(0, self.store.nicky_memory_mistakes)


if __name__ == "__main__":
    unittest.main()

