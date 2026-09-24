## Ica's first-visit card minigame.

# Every approach plays a full match. Easier tactics help with the cards, while
# matching Ica's nonchalant attitude is better for the relationship.
define ICA_CARDS_BASE_ROUNDS = 7
define ICA_CARDS_MIN_CARD = 1
define ICA_CARDS_MAX_CARD = 13

define ICA_CARDS_APPROACH_LABELS = {
    "flirt": "Flirt",
    "cheat": "Get Cheeky",
    "play_fair": "Play It Cool",
}

define ICA_CARDS_APPROACH_DESCRIPTIONS = {
    "flirt": "Keep the banter going. Ica's attention wanders, making the game a little easier.",
    "cheat": "Steal a look whenever Ica is too comfortable to guard the deck.",
    "play_fair": "No tricks, no speech, no pressure. Just play like neither of you has somewhere better to be.",
}

default ica_cards_session_active = False
default ica_cards_phase = "idle"
default ica_cards_approach = ""
default ica_cards_difficulty_reduction = 0
default ica_cards_round = 0
default ica_cards_round_count = 0
default ica_cards_player_score = 0
default ica_cards_ica_score = 0
default ica_cards_current_ica_card = 0
default ica_cards_current_player_card = 0
default ica_cards_current_action = ""
default ica_cards_current_wager = 1
default ica_cards_double_available = True
default ica_cards_round_result = ""
default ica_cards_deck = []
default ica_cards_player_cards = []
default ica_cards_ica_cards = []
default ica_cards_result = {}
default ica_cards_result_applied = False

init python:
    def ica_cards_approach_label(approach_id):
        return store.ICA_CARDS_APPROACH_LABELS.get(approach_id, "Unknown")

    def ica_cards_approach_description(approach_id):
        return store.ICA_CARDS_APPROACH_DESCRIPTIONS.get(approach_id, "Choose how you want to approach the game.")

    def _ica_cards_reset_state():
        store.ica_cards_session_active = True
        store.ica_cards_phase = "approach"
        store.ica_cards_approach = ""
        store.ica_cards_difficulty_reduction = 0
        store.ica_cards_round = 0
        store.ica_cards_round_count = 0
        store.ica_cards_player_score = 0
        store.ica_cards_ica_score = 0
        store.ica_cards_current_ica_card = 0
        store.ica_cards_current_player_card = 0
        store.ica_cards_current_action = ""
        store.ica_cards_current_wager = 1
        store.ica_cards_double_available = True
        store.ica_cards_round_result = ""
        store.ica_cards_deck = []
        store.ica_cards_player_cards = []
        store.ica_cards_ica_cards = []
        store.ica_cards_result_applied = False
        store.ica_cards_result = {}

    def start_ica_cards_minigame(approach_id=None):
        """Start a fresh session, optionally using a choice made in dialogue."""
        store.ica_clear_minigame_result("cards")
        _ica_cards_reset_state()
        if approach_id is not None:
            ica_cards_choose_approach(approach_id)
        renpy.call_screen("ica_cards_minigame")

    def _ica_cards_build_deck():
        deck = []
        for card_value in range(store.ICA_CARDS_MIN_CARD, store.ICA_CARDS_MAX_CARD + 1):
            deck.extend([card_value, card_value, card_value, card_value])
        renpy.random.shuffle(deck)
        return deck

    def _ica_cards_deck_is_valid(deck):
        if not isinstance(deck, list) or len(deck) < 1:
            return False
        return all(isinstance(card, int) and store.ICA_CARDS_MIN_CARD <= card <= store.ICA_CARDS_MAX_CARD for card in deck)

    def ica_cards_choose_approach(approach_id):
        """Apply the canonical approach modifier and deal the opening card."""
        if not store.ica_cards_session_active:
            return
        if approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica cards approach: {}".format(approach_id))
        if store.ica_cards_phase != "approach":
            return

        store.ica_cards_approach = approach_id
        store.ica_cards_difficulty_reduction = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        store.ica_cards_round_count = store.ICA_CARDS_BASE_ROUNDS
        store.ica_cards_round = 1
        store.ica_cards_deck = _ica_cards_build_deck()
        store.ica_cards_player_cards = []
        store.ica_cards_ica_cards = []
        store.ica_cards_player_score = 0
        store.ica_cards_ica_score = 0
        store.ica_cards_phase = "play"
        ica_cards_draw()

    def ica_cards_draw():
        """Deal one visible Ica card and prepare one hidden player draw."""
        if not store.ica_cards_session_active:
            return
        if store.ica_cards_phase not in ("play", "feedback"):
            return
        if store.ica_cards_round > store.ica_cards_round_count:
            return

        if not _ica_cards_deck_is_valid(store.ica_cards_deck):
            store.ica_cards_deck = _ica_cards_build_deck()

        if len(store.ica_cards_deck) < 2:
            store.ica_cards_deck = _ica_cards_build_deck()

        store.ica_cards_current_ica_card = store.ica_cards_deck.pop()
        store.ica_cards_current_player_card = 0
        store.ica_cards_current_action = ""
        store.ica_cards_current_wager = 1
        store.ica_cards_round_result = ""
        store.ica_cards_phase = "play"

    def _ica_cards_resolve_round(action_id, player_card, ica_card):
        reduction = store.ica_cards_difficulty_reduction
        prediction = action_id.replace("double_", "")

        if player_card == ica_card:
            return reduction > 0
        if prediction == "higher":
            return player_card + reduction > ica_card
        if prediction == "lower":
            return player_card - reduction < ica_card
        return False

    def ica_cards_choose(action):
        """Resolve a normal or doubled higher/lower call once per round."""
        if not store.ica_cards_session_active:
            return
        if action not in ("higher", "lower", "double_higher", "double_lower"):
            raise Exception("Unknown Ica cards action: {}".format(action))
        if store.ica_cards_phase != "play":
            return
        if store.ica_cards_current_ica_card == 0:
            return
        if action.startswith("double_") and not store.ica_cards_double_available:
            return

        if not _ica_cards_deck_is_valid(store.ica_cards_deck):
            store.ica_cards_deck = _ica_cards_build_deck()

        store.ica_cards_current_action = action
        store.ica_cards_current_wager = 2 if action.startswith("double_") else 1
        if store.ica_cards_current_wager == 2:
            store.ica_cards_double_available = False
        store.ica_cards_current_player_card = store.ica_cards_deck.pop()
        store.ica_cards_player_cards = store.ica_cards_player_cards + [
            store.ica_cards_current_player_card]
        store.ica_cards_ica_cards = store.ica_cards_ica_cards + [
            store.ica_cards_current_ica_card]

        player_won_round = _ica_cards_resolve_round(
            action,
            store.ica_cards_current_player_card,
            store.ica_cards_current_ica_card)

        if player_won_round:
            store.ica_cards_player_score += store.ica_cards_current_wager
            if store.ica_cards_current_wager == 2:
                store.ica_cards_round_result = "Your double call lands. Ica barely sits up, which is as close as she gets to panic."
            elif store.ica_cards_approach == "flirt":
                store.ica_cards_round_result = "You take the round. Ica critiques your flirting instead of admitting it distracted her."
            elif store.ica_cards_approach == "cheat":
                store.ica_cards_round_result = "You take the round. Ica glances at your hand like she knows exactly what you did."
            else:
                store.ica_cards_round_result = "You take the round. Neither of you puts in the effort to celebrate."
        else:
            store.ica_cards_ica_score += store.ica_cards_current_wager
            if store.ica_cards_current_wager == 2:
                store.ica_cards_round_result = "The double call misses. Ica steals two points and will never let you forget it."
            elif store.ica_cards_approach == "flirt":
                store.ica_cards_round_result = "Ica takes the round and calls your banter a respectable consolation prize."
            elif store.ica_cards_approach == "cheat":
                store.ica_cards_round_result = "Ica takes the round. Apparently cheating still requires effort."
            else:
                store.ica_cards_round_result = "Ica takes the round and gives you the smallest possible victory nod."

        store.ica_cards_phase = "feedback"

    def ica_cards_next_round():
        """Advance from feedback or expose the finalization control."""
        if not store.ica_cards_session_active:
            return
        if store.ica_cards_phase != "feedback":
            return
        if store.ica_cards_round >= store.ica_cards_round_count:
            store.ica_cards_phase = "complete_pending"
            return

        store.ica_cards_round += 1
        ica_cards_draw()

    def _ica_cards_tiebreaker_won():
        player_cards = store.ica_cards_player_cards
        ica_cards = store.ica_cards_ica_cards
        player_high = max(player_cards) if player_cards else 0
        ica_high = max(ica_cards) if ica_cards else 0

        if player_high != ica_high:
            return player_high > ica_high
        if player_cards and ica_cards and player_cards[-1] != ica_cards[-1]:
            return player_cards[-1] > ica_cards[-1]
        return store.ica_cards_difficulty_reduction > 0

    def finish_ica_cards_minigame():
        """Finalize once, persist a definite result, and close the modal."""
        if not store.ica_cards_session_active:
            return
        if store.ica_cards_phase != "complete_pending":
            return
        if store.ica_cards_result_applied:
            return

        if store.ica_cards_player_score > store.ica_cards_ica_score:
            won = True
            result_tier = "win"
        elif store.ica_cards_player_score < store.ica_cards_ica_score:
            won = False
            result_tier = "loss"
        else:
            won = _ica_cards_tiebreaker_won()
            result_tier = "tiebreaker_win" if won else "tiebreaker_loss"

        store.ica_record_minigame_result(
            "cards",
            store.ica_cards_approach,
            store.ica_cards_difficulty_reduction,
            won,
            result_tier)

        completed_result = store.ica_minigame_results.get("cards", {})
        relationship_change = store.ica_relationship_change_for_result(completed_result)
        store.ica = store.ica + relationship_change
        store.ica_cards_result_applied = True
        store.ica_cards_phase = "complete"
        store.ica_cards_session_active = False
        renpy.hide_screen("ica_cards_minigame")
        renpy.end_interaction(True)

    def abort_ica_cards_minigame():
        """Close an unfinished session without writing a result record."""
        if not store.ica_cards_session_active:
            return
        store.ica_cards_phase = "aborted"
        store.ica_cards_session_active = False
        renpy.hide_screen("ica_cards_minigame")
        renpy.end_interaction(True)

    def ica_cards_result_text():
        if store.ica_cards_player_score > store.ica_cards_ica_score:
            return "You win the match on points."
        if store.ica_cards_player_score < store.ica_cards_ica_score:
            return "Ica wins the match on points."
        return "The points are tied, so the high-card tiebreaker decides it."

    def ica_cards_card_name(card_value):
        names = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K",
        }
        return names.get(card_value, str(card_value)) if card_value else "?"
