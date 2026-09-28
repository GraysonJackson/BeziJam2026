## Ica and Winston's three-player pawn-race hangout.
define ICA_BOARD_FINISH = 12
define ICA_BOARD_CARD_VALUES = (1, 2, 3, 4)
define ICA_BOARD_CARDS_PER_VALUE = 1

default ica_board_session_active = False
default ica_board_phase = "idle"
default ica_board_approach = ""
default ica_board_movement_bonus = 0
default ica_board_bonus_available = False
default ica_board_spend_bonus_next_move = False
default ica_board_player_position = 0
default ica_board_ica_position = 0
default ica_board_winston_position = 0
default ica_board_player_deck = []
default ica_board_player_discard = []
default ica_board_player_hand = []
default ica_board_ica_deck = []
default ica_board_ica_discard = []
default ica_board_ica_hand = []
default ica_board_winston_deck = []
default ica_board_winston_discard = []
default ica_board_winston_hand = []
default ica_board_turn_number = 1
default ica_board_feedback = ""
default ica_board_pending_won = False
default ica_board_winner = ""
default ica_board_result_applied = False

init python:
    def _ica_board_new_deck():
        deck = []
        for card_value in store.ICA_BOARD_CARD_VALUES:
            deck.extend([card_value] * store.ICA_BOARD_CARDS_PER_VALUE)
        renpy.random.shuffle(deck)
        return deck

    def _ica_board_draw_player_card():
        if not store.ica_board_player_deck:
            store.ica_board_player_deck = list(store.ica_board_player_discard)
            store.ica_board_player_discard = []
            renpy.random.shuffle(store.ica_board_player_deck)
        return store.ica_board_player_deck.pop()

    def _ica_board_draw_ica_card():
        if not store.ica_board_ica_deck:
            store.ica_board_ica_deck = list(store.ica_board_ica_discard)
            store.ica_board_ica_discard = []
            renpy.random.shuffle(store.ica_board_ica_deck)
        return store.ica_board_ica_deck.pop()

    def _ica_board_draw_winston_card():
        if not store.ica_board_winston_deck:
            store.ica_board_winston_deck = list(store.ica_board_winston_discard)
            store.ica_board_winston_discard = []
            renpy.random.shuffle(store.ica_board_winston_deck)
        return store.ica_board_winston_deck.pop()

    def _ica_board_deal_initial_hands():
        store.ica_board_player_deck = _ica_board_new_deck()
        store.ica_board_player_discard = []
        store.ica_board_player_hand = []
        store.ica_board_ica_deck = _ica_board_new_deck()
        store.ica_board_ica_discard = []
        store.ica_board_ica_hand = []
        store.ica_board_winston_deck = _ica_board_new_deck()
        store.ica_board_winston_discard = []
        store.ica_board_winston_hand = []

        for _ in range(2):
            store.ica_board_player_hand.append(_ica_board_draw_player_card())
            store.ica_board_ica_hand.append(_ica_board_draw_ica_card())
            store.ica_board_winston_hand.append(_ica_board_draw_winston_card())

    def _ica_board_refill_player_hand():
        while len(store.ica_board_player_hand) < 2:
            store.ica_board_player_hand.append(_ica_board_draw_player_card())

    def _ica_board_refill_ica_hand():
        while len(store.ica_board_ica_hand) < 2:
            store.ica_board_ica_hand.append(_ica_board_draw_ica_card())

    def _ica_board_refill_winston_hand():
        while len(store.ica_board_winston_hand) < 2:
            store.ica_board_winston_hand.append(_ica_board_draw_winston_card())

    def _ica_board_choose_ai_card(pawn_id, hand):
        """Prefer winning move first, then character-specific strategic bump."""
        if not hand:
            return None

        if pawn_id == "ica":
            position = store.ica_board_ica_position
        elif pawn_id == "winston":
            position = store.ica_board_winston_position
        else:
            raise Exception("Unknown Ica board-game AI pawn: {}".format(pawn_id))

        # 1. Winning move takes absolute priority
        for card_value in sorted(hand, reverse=True):
            if position + card_value >= store.ICA_BOARD_FINISH:
                return card_value

        # 2. Personality-specific bump strategy
        if pawn_id == "winston":
            leader_pos = max(store.ica_board_player_position, store.ica_board_ica_position)
            for card_value in sorted(hand, reverse=True):
                destination = position + card_value
                if destination == leader_pos and destination > 0:
                    return card_value
            for card_value in sorted(hand, reverse=True):
                destination = position + card_value
                if destination in (store.ica_board_player_position, store.ica_board_ica_position) and destination > 0:
                    return card_value
        elif pawn_id == "ica":
            for card_value in sorted(hand, reverse=True):
                destination = position + card_value
                if destination == store.ica_board_winston_position and destination > 0:
                    return card_value
            for card_value in sorted(hand, reverse=True):
                destination = position + card_value
                if destination in (store.ica_board_player_position, store.ica_board_winston_position) and destination > 0:
                    return card_value

        return max(hand)

    def start_ica_board_game_minigame(approach_id=None):
        """Reset the three-player race and use the scene's chosen approach."""
        store.ica_clear_minigame_result("board")
        store.ica_board_session_active = True
        store.ica_board_phase = "approach"
        store.ica_board_approach = ""
        store.ica_board_movement_bonus = 0
        store.ica_board_bonus_available = False
        store.ica_board_spend_bonus_next_move = False
        store.ica_board_player_position = 0
        store.ica_board_ica_position = 0
        store.ica_board_winston_position = 0
        store.ica_board_player_deck = []
        store.ica_board_player_discard = []
        store.ica_board_player_hand = []
        store.ica_board_ica_deck = []
        store.ica_board_ica_discard = []
        store.ica_board_ica_hand = []
        store.ica_board_winston_deck = []
        store.ica_board_winston_discard = []
        store.ica_board_winston_hand = []
        store.ica_board_turn_number = 1
        store.ica_board_feedback = ""
        store.ica_board_pending_won = False
        store.ica_board_winner = ""
        store.ica_board_result_applied = False
        if approach_id is not None:
            ica_board_choose_approach(approach_id)
        push_minigame_music()
        renpy.call_screen("ica_board_game_minigame")

    def ica_board_choose_approach(approach_id):
        """Validate the shared approach and start the first player turn."""
        if not store.ica_board_session_active or store.ica_board_phase != "approach":
            return
        if not isinstance(approach_id, str) or approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica board-game approach: {}".format(approach_id))

        store.ica_board_approach = approach_id
        store.ica_board_movement_bonus = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        store.ica_board_bonus_available = True
        store.ica_board_spend_bonus_next_move = False
        _ica_board_deal_initial_hands()
        store.ica_board_phase = "player_turn"
        store.ica_board_feedback = "Choose one of your two movement cards."

    def ica_board_toggle_bonus():
        """Toggle whether the available approach bonus is spent on this move."""
        if not store.ica_board_session_active or store.ica_board_phase != "player_turn":
            return
        if not store.ica_board_bonus_available or store.ica_board_movement_bonus <= 0:
            return
        store.ica_board_spend_bonus_next_move = not store.ica_board_spend_bonus_next_move

    def ica_board_choose_card(card_id):
        """Play one card from the visible hand and resolve the player's landing."""
        if not store.ica_board_session_active or store.ica_board_phase != "player_turn":
            return
        if type(card_id) is not int or card_id not in store.ICA_BOARD_CARD_VALUES:
            raise Exception("Unknown Ica board-game card: {}".format(card_id))
        if card_id not in store.ica_board_player_hand:
            return

        store.ica_board_player_hand.remove(card_id)
        store.ica_board_player_discard.append(card_id)
        _ica_board_refill_player_hand()

        movement = card_id
        if store.ica_board_spend_bonus_next_move and store.ica_board_bonus_available:
            movement += store.ica_board_movement_bonus
            store.ica_board_bonus_available = False
            store.ica_board_spend_bonus_next_move = False

        store.ica_board_feedback = "You play a {}-space card{}.".format(
            card_id,
            " with your +{}-space bonus".format(store.ica_board_movement_bonus)
            if movement > card_id else "")
        ica_board_resolve_landing("player", movement)

    def ica_board_ica_turn():
        """Play Ica's bump-first turn, then hand play to Winston."""
        if not store.ica_board_session_active or store.ica_board_phase != "ica_turn":
            return
        if not store.ica_board_ica_hand:
            _ica_board_refill_ica_hand()

        card_value = _ica_board_choose_ai_card("ica", store.ica_board_ica_hand)
        store.ica_board_ica_hand.remove(card_value)
        store.ica_board_ica_discard.append(card_value)
        _ica_board_refill_ica_hand()
        store.ica_board_feedback += " Ica plays a {}-space card.".format(card_value)

        ica_board_resolve_landing("ica", card_value)
        if store.ica_board_phase == "ica_turn":
            store.ica_board_phase = "winston_turn"

    def ica_board_winston_turn():
        """Play Winston's enthusiastic bump-first turn and start a new round."""
        if not store.ica_board_session_active or store.ica_board_phase != "winston_turn":
            return
        if not store.ica_board_winston_hand:
            _ica_board_refill_winston_hand()

        card_value = _ica_board_choose_ai_card(
            "winston", store.ica_board_winston_hand)
        store.ica_board_winston_hand.remove(card_value)
        store.ica_board_winston_discard.append(card_value)
        _ica_board_refill_winston_hand()
        store.ica_board_feedback += " Winston slams down a {}-space card.".format(
            card_value)

        ica_board_resolve_landing("winston", card_value)
        if store.ica_board_phase == "winston_turn":
            store.ica_board_phase = "player_turn"
            store.ica_board_turn_number += 1

    def ica_board_resolve_landing(pawn_id, move_amount):
        """Clamp a move, resolve a bump, then settle any finish in turn order."""
        if not store.ica_board_session_active:
            return
        if pawn_id not in ("player", "ica", "winston"):
            raise Exception("Unknown Ica board-game pawn: {}".format(pawn_id))
        expected_phase = {
            "player": "player_turn",
            "ica": "ica_turn",
            "winston": "winston_turn",
        }[pawn_id]
        if store.ica_board_phase != expected_phase:
            return

        move_amount = max(0, int(move_amount))
        if pawn_id == "player":
            old_position = max(0, min(store.ICA_BOARD_FINISH, int(store.ica_board_player_position)))
            destination = min(store.ICA_BOARD_FINISH, old_position + move_amount)
            store.ica_board_player_position = destination
        elif pawn_id == "ica":
            old_position = max(0, min(store.ICA_BOARD_FINISH, int(store.ica_board_ica_position)))
            destination = min(store.ICA_BOARD_FINISH, old_position + move_amount)
            store.ica_board_ica_position = destination
        else:
            old_position = max(0, min(store.ICA_BOARD_FINISH, int(store.ica_board_winston_position)))
            destination = min(store.ICA_BOARD_FINISH, old_position + move_amount)
            store.ica_board_winston_position = destination

        if destination < store.ICA_BOARD_FINISH:
            opponents = (
                ("player", "You"),
                ("ica", "Ica"),
                ("winston", "Winston"),
            )
            for opponent_id, opponent_name in opponents:
                if opponent_id == pawn_id:
                    continue
                position_name = "ica_board_{}_position".format(opponent_id)
                if getattr(store, position_name) == destination:
                    setattr(store, position_name, 0)
                    actor_name = {
                        "player": "You",
                        "ica": "Ica",
                        "winston": "Winston",
                    }[pawn_id]
                    store.ica_board_feedback += " {} bump{} {} back to start.".format(
                        actor_name,
                        "" if pawn_id == "player" else "s",
                        opponent_name)

        if destination >= store.ICA_BOARD_FINISH:
            store.ica_board_winner = pawn_id
            store.ica_board_pending_won = pawn_id == "player"
            store.ica_board_phase = "complete_pending"
            winner_name = {
                "player": "You",
                "ica": "Ica",
                "winston": "Winston",
            }[pawn_id]
            store.ica_board_feedback += " {} reach{} the finish first!".format(
                winner_name,
                "" if pawn_id == "player" else "es")
        elif pawn_id == "player":
            store.ica_board_phase = "ica_turn"

    def ica_board_withdraw():
        """Allow player to withdraw from the race and let AI battle."""
        if not store.ica_board_session_active or store.ica_board_phase == "complete":
            return
        store.ica_board_winner = "withdrawn"
        store.ica_board_pending_won = False
        store.ica_board_feedback = "You step back from the board to let Ica and Winston battle for supremacy."
        store.ica_board_phase = "complete_pending"
        renpy.restart_interaction()

    def finish_ica_board_game_minigame():
        """Record the settled race exactly once and close the modal screen."""
        if not store.ica_board_session_active:
            return
        if store.ica_board_phase != "complete_pending" or store.ica_board_result_applied:
            return

        result_tier = (
            "win" if store.ica_board_pending_won
            else "loss_{}".format(store.ica_board_winner))
        store.ica_record_minigame_result(
            "board",
            store.ica_board_approach,
            store.ica_board_movement_bonus,
            store.ica_board_pending_won,
            result_tier)
        store.ica_board_result_applied = True
        store.ica_board_phase = "complete"
        store.ica_board_session_active = False
        pop_minigame_music()
        renpy.hide_screen("ica_board_game_minigame")
        renpy.end_interaction(True)
