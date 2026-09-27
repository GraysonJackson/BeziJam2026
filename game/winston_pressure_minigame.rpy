## Winston Visit 3: interrogation-pressure game using blackjack rules.

define WINSTON_PRESSURE_DEALER_STAND = 17
define WINSTON_PRESSURE_MAX_INTUITION = 3

default winston_pressure_active = False
default winston_pressure_phase = "idle"
default winston_pressure_targets = []
default winston_pressure_target_index = 0
default winston_pressure_reveal = {}
default winston_pressure_deck = []
default winston_pressure_player_hand = []
default winston_pressure_dealer_hand = []
default winston_pressure_feedback = ""
default winston_pressure_completed = []
default winston_pressure_attempts = 0
default winston_pressure_busts = 0
default winston_pressure_exact_twenty_ones = 0
default winston_pressure_intuition_uses = 0
default winston_pressure_assists = 0
default winston_pressure_dhampir_used = False
default winston_pressure_dhampir_total = 0
default winston_pressure_completion_recorded = False
default winston_pressure_result = {}

init python:
    def _winston_pressure_card_value(rank):
        if rank == "A":
            return 11
        if rank in ("J", "Q", "K"):
            return 10
        return int(rank)

    def winston_pressure_hand_total(hand):
        total = sum(card["value"] for card in hand)
        aces = sum(1 for card in hand if card["rank"] == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def _winston_pressure_new_deck():
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suits = ("ALIBI", "MOTIVE", "POWER", "VIBES")
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append({
                    "rank": rank,
                    "suit": suit,
                    "value": _winston_pressure_card_value(rank),
                })
        renpy.random.shuffle(deck)
        return deck

    def _winston_pressure_draw():
        if not store.winston_pressure_deck:
            store.winston_pressure_deck = _winston_pressure_new_deck()
        card = store.winston_pressure_deck[-1]
        store.winston_pressure_deck = store.winston_pressure_deck[:-1]
        return card

    def winston_pressure_current_target_id():
        index = store.winston_pressure_target_index
        if 0 <= index < len(store.winston_pressure_targets):
            return store.winston_pressure_targets[index]
        return None

    def winston_pressure_current_target_name():
        suspect_id = winston_pressure_current_target_id()
        if suspect_id is None:
            return "INTERVIEWS COMPLETE"
        return store.suspectNames[suspect_id]

    def _winston_pressure_deal_attempt():
        store.winston_pressure_deck = _winston_pressure_new_deck()
        store.winston_pressure_player_hand = [
            _winston_pressure_draw(), _winston_pressure_draw()]
        store.winston_pressure_dealer_hand = [
            _winston_pressure_draw(), _winston_pressure_draw()]
        store.winston_pressure_attempts += 1
        store.winston_pressure_phase = "playing"
        store.winston_pressure_feedback = (
            "Raise the pressure without exceeding 21. Question when the suspect is ready."
        )

    def _winston_pressure_load_target():
        if store.winston_pressure_target_index >= len(store.winston_pressure_targets):
            store.winston_pressure_phase = "result"
            store.winston_pressure_feedback = (
                "Every remaining suspect has been tested under controlled pressure."
            )
            return
        _winston_pressure_deal_attempt()

    def _winston_pressure_reset():
        store.winston_pressure_active = True
        store.winston_pressure_phase = "setup"
        store.winston_pressure_targets = list(store.remainingSuspects)
        store.winston_pressure_target_index = 0
        store.winston_pressure_reveal = get_planned_route_reveal("winston", 3)
        store.winston_pressure_deck = []
        store.winston_pressure_player_hand = []
        store.winston_pressure_dealer_hand = []
        store.winston_pressure_completed = []
        store.winston_pressure_attempts = 0
        store.winston_pressure_busts = 0
        store.winston_pressure_exact_twenty_ones = 0
        store.winston_pressure_intuition_uses = 0
        store.winston_pressure_assists = 0
        store.winston_pressure_assist_all_requested = False
        store.winston_pressure_dhampir_used = False
        store.winston_pressure_dhampir_total = 0
        store.winston_pressure_completion_recorded = False
        store.winston_pressure_result = {}
        _winston_pressure_load_target()

    def start_winston_pressure_minigame():
        """Begin the suspect queue and return when Dhampir interrupts or play ends."""
        _winston_pressure_reset()
        return renpy.call_screen("winston_pressure_minigame")

    def resume_winston_pressure_minigame():
        """Resume the existing queue after Dhampir's scripted turn."""
        if not store.winston_pressure_active:
            return None
        if getattr(store, "winston_pressure_assist_all_requested", False):
            while store.winston_pressure_target_index < len(store.winston_pressure_targets):
                _winston_pressure_complete_current(assisted=True)
            store.winston_pressure_phase = "result"
            store.winston_pressure_feedback = (
                "Winston finishes the remaining interviews and preserves every canonical result."
            )
        return renpy.call_screen("winston_pressure_minigame")

    def winston_pressure_press():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "playing"):
            return
        hand = list(store.winston_pressure_player_hand)
        hand.append(_winston_pressure_draw())
        store.winston_pressure_player_hand = hand
        total = winston_pressure_hand_total(hand)
        if total > 21:
            store.winston_pressure_busts += 1
            store.winston_pressure_phase = "bust"
            store.winston_pressure_feedback = (
                "Too much pressure. The suspect folds their arms and stops answering."
            )
        elif total == 21:
            store.winston_pressure_feedback = (
                "Exactly 21. Ask now before the moment passes."
            )
        elif total >= 17:
            store.winston_pressure_feedback = (
                "The suspect is strained but still engaged. This is a strong moment to question."
            )
        else:
            store.winston_pressure_feedback = (
                "The suspect is still comfortable. You can raise the pressure or question now."
            )
        renpy.restart_interaction()

    def winston_pressure_use_intuition():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "playing"):
            return
        if store.winston_pressure_intuition_uses >= store.WINSTON_PRESSURE_MAX_INTUITION:
            store.winston_pressure_feedback = (
                "You have exhausted your intuition reads for this session. Trust your detective gut."
            )
            renpy.restart_interaction()
            return
        total = winston_pressure_hand_total(store.winston_pressure_player_hand)
        store.winston_pressure_intuition_uses += 1
        if total <= 12:
            message = "Your intuition says they can take considerably more pressure."
        elif total <= 16:
            message = "Your intuition says they are getting close, but have not closed off yet."
        else:
            message = "Your intuition catches the edge of withdrawal. Questioning now feels safer."
        store.winston_pressure_feedback = message
        renpy.restart_interaction()

    def winston_pressure_question():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "playing"):
            return

        dealer = list(store.winston_pressure_dealer_hand)
        while winston_pressure_hand_total(dealer) < store.WINSTON_PRESSURE_DEALER_STAND:
            dealer.append(_winston_pressure_draw())
        store.winston_pressure_dealer_hand = dealer

        player_total = winston_pressure_hand_total(store.winston_pressure_player_hand)
        dealer_total = winston_pressure_hand_total(dealer)
        exact = player_total == 21
        success = exact or dealer_total > 21 or player_total > dealer_total

        if success:
            if exact:
                store.winston_pressure_exact_twenty_ones += 1
                store.winston_pressure_feedback = (
                    "Perfect pressure. The question lands before the suspect can rebuild their guard."
                )
            elif dealer_total > 21:
                store.winston_pressure_feedback = (
                    "The suspect overplays their defense and contradicts the earlier statement."
                )
            else:
                store.winston_pressure_feedback = (
                    "Your pressure holds. Winston asks the question and receives a usable answer."
                )
            store.winston_pressure_phase = "answered"
        else:
            store.winston_pressure_feedback = (
                "The suspect's defense holds at {}. The answer stays incomplete; reset and try another angle."
                .format(dealer_total)
            )
            store.winston_pressure_phase = "retry"
        renpy.restart_interaction()

    def winston_pressure_retry():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase not in ("bust", "retry")):
            return
        _winston_pressure_deal_attempt()
        store.winston_pressure_feedback = (
            "Winston changes the subject, lets the room cool, and gives you another opening."
        )
        renpy.restart_interaction()

    def _winston_pressure_complete_current(assisted=False):
        suspect_id = winston_pressure_current_target_id()
        if suspect_id is None:
            return
        completed = list(store.winston_pressure_completed)
        if suspect_id not in completed:
            completed.append(suspect_id)
        store.winston_pressure_completed = completed
        if assisted:
            store.winston_pressure_assists += 1
        store.winston_pressure_target_index += 1

    def _winston_pressure_pause_for_dhampir():
        """Pause once at the midpoint, regardless of how an interview ended."""
        midpoint = max(1, len(store.winston_pressure_targets) // 2)
        if (not store.winston_pressure_dhampir_used
                and store.winston_pressure_target_index == midpoint
                and store.winston_pressure_target_index < len(store.winston_pressure_targets)):
            store.winston_pressure_phase = "dhampir_pause"
            store.winston_pressure_feedback = "Dhampir steps forward for his turn."
            renpy.hide_screen("winston_pressure_minigame")
            renpy.end_interaction("dhampir_pause")
            return True
        return False

    def winston_pressure_next_target():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "answered"):
            return
        _winston_pressure_complete_current()

        if _winston_pressure_pause_for_dhampir():
            return

        _winston_pressure_load_target()
        renpy.restart_interaction()

    def winston_pressure_dhampir_turn():
        """Resolve Dhampir's one scripted, terrifyingly perfect turn."""
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "dhampir_pause"):
            return
        store.winston_pressure_dhampir_used = True
        store.winston_pressure_player_hand = [
            {"rank": "A", "suit": "BAD COP", "value": 11},
            {"rank": "K", "suit": "FEAR", "value": 10},
        ]
        store.winston_pressure_dealer_hand = []
        store.winston_pressure_exact_twenty_ones += 1
        store.winston_pressure_dhampir_total = 21
        _winston_pressure_complete_current()
        _winston_pressure_load_target()

    def winston_pressure_assist_current():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase not in ("playing", "bust", "retry")):
            return
        _winston_pressure_complete_current(assisted=True)
        if _winston_pressure_pause_for_dhampir():
            return
        _winston_pressure_load_target()
        store.winston_pressure_feedback = (
            "Winston takes the chair, changes tone twice, and gets the usable answer without drama."
        )
        renpy.restart_interaction()

    def winston_pressure_assist_all():
        if not store.winston_pressure_active:
            return
        midpoint = max(1, len(store.winston_pressure_targets) // 2)
        stop_index = len(store.winston_pressure_targets)
        if (not store.winston_pressure_dhampir_used
                and store.winston_pressure_target_index < midpoint):
            stop_index = midpoint

        while store.winston_pressure_target_index < stop_index:
            _winston_pressure_complete_current(assisted=True)

        if (not store.winston_pressure_dhampir_used
                and store.winston_pressure_target_index == midpoint
                and store.winston_pressure_target_index < len(store.winston_pressure_targets)):
            store.winston_pressure_phase = "dhampir_pause"
            store.winston_pressure_feedback = "Dhampir steps forward for his turn."
            renpy.hide_screen("winston_pressure_minigame")
            renpy.end_interaction("dhampir_pause")
            return

        store.winston_pressure_phase = "result"
        store.winston_pressure_feedback = (
            "Winston finishes the remaining interviews and preserves every canonical result."
        )
        renpy.restart_interaction()

    def _winston_pressure_record_result():
        if store.winston_pressure_completion_recorded:
            return False
        store.winston_pressure_completion_recorded = True

        reveal = store.winston_pressure_reveal
        cleared_names = [
            store.suspectNames[suspect_id]
            for suspect_id in reveal["eliminated"]
        ]
        clue_text = "Controlled stress interviews clear {}.".format(
            " and ".join(cleared_names))
        record_planned_route_reveal(
            "winston", 3, clue_text=clue_text, expected_count=2)

        if store.winston_pressure_assists:
            quality = "assisted"
        elif store.winston_pressure_busts == 0:
            quality = "controlled"
        elif store.winston_pressure_busts <= 2:
            quality = "recovered"
        else:
            quality = "messy"

        store.winston_pressure_result = {
            "completed": True,
            "quality": quality,
            "busts": store.winston_pressure_busts,
            "attempts": store.winston_pressure_attempts,
            "exact_twenty_ones": store.winston_pressure_exact_twenty_ones,
            "intuition_uses": store.winston_pressure_intuition_uses,
            "assists": store.winston_pressure_assists,
            "cleared_names": cleared_names,
        }
        return True

    def finish_winston_pressure_minigame():
        if (not store.winston_pressure_active
                or store.winston_pressure_phase != "result"):
            return
        if not _winston_pressure_record_result():
            return
        store.winston_pressure_active = False
        store.winston_pressure_phase = "complete"
        renpy.hide_screen("winston_pressure_minigame")
        renpy.end_interaction(True)

    def abort_winston_pressure_minigame():
        store.winston_pressure_active = False
        store.winston_pressure_phase = "aborted"
        store.winston_pressure_player_hand = []
        store.winston_pressure_dealer_hand = []
        renpy.hide_screen("winston_pressure_minigame")
        renpy.end_interaction(False)

    def validate_winston_pressure_rules():
        """Headless checks for deck shape, Visit 3 setup, and Dhampir's turn."""
        saved = {
            "killer": store.killer,
            "remaining": list(store.remainingSuspects),
            "active": store.winston_pressure_active,
            "phase": store.winston_pressure_phase,
            "targets": list(store.winston_pressure_targets),
            "target_index": store.winston_pressure_target_index,
            "reveal": dict(store.winston_pressure_reveal),
            "deck": list(store.winston_pressure_deck),
            "player_hand": list(store.winston_pressure_player_hand),
            "dealer_hand": list(store.winston_pressure_dealer_hand),
            "completed": list(store.winston_pressure_completed),
            "dhampir_used": store.winston_pressure_dhampir_used,
            "dhampir_total": store.winston_pressure_dhampir_total,
        }
        try:
            store.killer = 1
            store.remainingSuspects = [1, 3, 4, 5, 6, 7, 8, 9]
            _winston_pressure_reset()

            if len(store.winston_pressure_targets) != 8:
                raise Exception("Winston pressure test did not load eight pure-route suspects.")
            if len(store.winston_pressure_deck) != 48:
                raise Exception("Winston pressure deck did not deal four cards from 52.")
            if winston_pressure_hand_total([
                    {"rank": "A", "value": 11},
                    {"rank": "K", "value": 10}]) != 21:
                raise Exception("Winston pressure blackjack total is incorrect.")
            if winston_pressure_hand_total([
                    {"rank": "A", "value": 11},
                    {"rank": "A", "value": 11},
                    {"rank": "K", "value": 10}]) != 12:
                raise Exception("Winston pressure ace adjustment is incorrect.")

            store.winston_pressure_target_index = 4
            store.winston_pressure_phase = "dhampir_pause"
            winston_pressure_dhampir_turn()
            if (not store.winston_pressure_dhampir_used
                    or store.winston_pressure_dhampir_total != 21
                    or store.winston_pressure_target_index != 5):
                raise Exception("Dhampir's scripted pressure turn did not resolve at 21.")
        finally:
            store.killer = saved["killer"]
            store.remainingSuspects = saved["remaining"]
            store.winston_pressure_active = saved["active"]
            store.winston_pressure_phase = saved["phase"]
            store.winston_pressure_targets = saved["targets"]
            store.winston_pressure_target_index = saved["target_index"]
            store.winston_pressure_reveal = saved["reveal"]
            store.winston_pressure_deck = saved["deck"]
            store.winston_pressure_player_hand = saved["player_hand"]
            store.winston_pressure_dealer_hand = saved["dealer_hand"]
            store.winston_pressure_completed = saved["completed"]
            store.winston_pressure_dhampir_used = saved["dhampir_used"]
            store.winston_pressure_dhampir_total = saved["dhampir_total"]
