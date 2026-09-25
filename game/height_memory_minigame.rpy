## Razzle Visit 3: forgiving witness-memory cleanup minigame.

# Give players time to read the thought cards before each board scramble.
define height_memory_time_limit = 12.0
define height_memory_max_visible_distractors = 6
define height_memory_required_cleanups = 10
define height_memory_catalog = (
    {"id": "height_shadow", "text": "A long shadow crossed the porch.", "category": "important", "protected": True},
    {"id": "height_doorway", "text": "The doorway swallowed most of the silhouette.", "category": "important", "protected": True},
    {"id": "distractor_cat", "text": "A cat wearing a tiny detective hat.", "category": "distractor", "protected": False},
    {"id": "distractor_pizza", "text": "The smell of suspiciously cold pizza.", "category": "distractor", "protected": False},
    {"id": "distractor_lawn", "text": "Three extremely judgmental lawn gnomes.", "category": "distractor", "protected": False},
    {"id": "distractor_siren", "text": "A siren that definitely was not relevant.", "category": "distractor", "protected": False},
    {"id": "distractor_hat", "text": "A hat floating away in the breeze.", "category": "distractor", "protected": False},
    {"id": "distractor_mail", "text": "The neighbor's overdue mail pile.", "category": "distractor", "protected": False},
    {"id": "distractor_bird", "text": "A bird with a very loud opinion.", "category": "distractor", "protected": False},
    {"id": "distractor_socks", "text": "One glove, two socks, zero answers.", "category": "distractor", "protected": False},
    {"id": "distractor_coat", "text": "The figure may have worn a bulky coat.", "category": "distractor", "protected": False},
    {"id": "distractor_footsteps", "text": "Footsteps hurried across the gravel.", "category": "distractor", "protected": False},
    {"id": "distractor_portrait", "text": "A crooked family portrait hung inside.", "category": "distractor", "protected": False},
    {"id": "distractor_bush", "text": "The hedge shook after the figure passed.", "category": "distractor", "protected": False},
)

default height_memory_active = False
default height_memory_complete = False
default height_memory_completion_recorded = False
default height_memory_refreshing = False
default height_memory_progress = 0
default height_memory_timer = 0.0
default height_memory_setbacks = 0
default height_memory_feedback = ""
default height_memory_cleared = []
default height_memory_board = []

init python:
    def _height_memory_card(card_id):
        """Return a catalog card by stable ID, or None for an unknown ID."""
        for card in store.height_memory_catalog:
            if card["id"] == card_id:
                return card
        return None

    def _height_memory_board_is_valid():
        """Check whether the current board still contains its protected evidence."""
        if not store.height_memory_board:
            return False

        seen_ids = set()
        protected_count = 0
        for card in store.height_memory_board:
            if not isinstance(card, dict):
                return False
            card_id = card.get("id")
            catalog_card = _height_memory_card(card_id)
            if catalog_card is None or card_id in seen_ids:
                return False
            if card_id in store.height_memory_cleared:
                return False
            if card.get("protected") != catalog_card["protected"]:
                return False
            if "position" not in card:
                return False
            if card["protected"]:
                protected_count += 1
            seen_ids.add(card_id)

        return protected_count == 2

    def _height_memory_build_board():
        """Build a safe board from uncleared catalog cards."""
        distractors = [
            dict(card) for card in store.height_memory_catalog
            if not card["protected"] and card["id"] not in store.height_memory_cleared
        ]
        renpy.random.shuffle(distractors)
        visible_distractors = distractors[:store.height_memory_max_visible_distractors]
        board = visible_distractors + [
            dict(card) for card in store.height_memory_catalog if card["protected"]
        ]
        renpy.random.shuffle(board)

        for position, card in enumerate(board):
            card["position"] = position

        return board

    def _height_memory_undo_cleanup():
        """Undo one earlier cleanup while leaving the puzzle fully recoverable."""
        if not store.height_memory_cleared:
            return False

        store.height_memory_cleared = store.height_memory_cleared[:-1]
        store.height_memory_progress = max(0, store.height_memory_progress - 1)
        return True

    def _height_memory_refresh_feedback():
        """Repair malformed board state without changing cleanup progress."""
        store.height_memory_board = _height_memory_build_board()
        store.height_memory_timer = 0.0

    # Public API: initialize a fresh board and open the modal interaction.
    def start_height_memory_minigame():
        """Start a new Razzle witness-memory cleanup session."""
        store.height_memory_active = True
        store.height_memory_complete = False
        store.height_memory_completion_recorded = False
        store.height_memory_refreshing = False
        store.height_memory_progress = 0
        store.height_memory_timer = 0.0
        store.height_memory_setbacks = 0
        store.height_memory_feedback = "Clear the irrelevant thoughts. Keep the useful memories."
        store.height_memory_cleared = []
        store.height_memory_board = []
        _height_memory_refresh_feedback()
        renpy.show_screen("height_memory_minigame")
        renpy.restart_interaction()

    # Public API: resolve one thought-card click without changing route truth.
    def height_memory_click(card_id):
        """Clear a distractor or trigger a harmless protected-memory setback."""
        if (not store.height_memory_active or store.height_memory_complete
                or store.height_memory_refreshing):
            return

        if not _height_memory_board_is_valid():
            reshuffle_height_memory_board()
            return

        card = _height_memory_card(card_id)
        board_ids = [board_card.get("id") for board_card in store.height_memory_board]
        if card is None or card_id not in board_ids:
            return

        store.height_memory_refreshing = True
        should_finish = False
        try:
            if card["protected"]:
                store.height_memory_setbacks += 1
                lost_progress = _height_memory_undo_cleanup()
                if lost_progress:
                    store.height_memory_feedback = (
                        "Razzle: That was a height anchor! One cleared thought just came back."
                    )
                else:
                    store.height_memory_feedback = (
                        "Razzle: That was a height anchor! At least there was no progress to lose."
                    )
                reshuffle_height_memory_board()
            elif card_id not in store.height_memory_cleared:
                store.height_memory_cleared = store.height_memory_cleared + [card_id]
                store.height_memory_progress += 1
                store.height_memory_feedback = (
                    "Razzle: Excellent! That thought was pure eyewitness confetti."
                )
                if store.height_memory_progress >= store.height_memory_required_cleanups:
                    should_finish = True
                else:
                    reshuffle_height_memory_board()
        finally:
            store.height_memory_refreshing = False

        if should_finish:
            finish_height_memory_minigame()
        else:
            renpy.restart_interaction()

    # Public API: advance the pressure timer used by the modal screen.
    def height_memory_tick():
        """Refresh the distractors when the light timer expires."""
        if (not store.height_memory_active or store.height_memory_complete
                or store.height_memory_refreshing):
            return

        store.height_memory_timer += 0.5
        if store.height_memory_timer >= store.height_memory_time_limit:
            store.height_memory_setbacks += 1
            lost_progress = _height_memory_undo_cleanup()
            if lost_progress:
                store.height_memory_feedback = (
                    "Too slow—the thoughts scrambled and one distraction returned."
                )
            else:
                store.height_memory_feedback = (
                    "Too slow—the thoughts scrambled, but you had no progress to lose."
                )
            reshuffle_height_memory_board()

        renpy.restart_interaction()

    # Public API: preserve evidence and progress while rebuilding the board.
    def reshuffle_height_memory_board():
        """Reorder/replenish distractors without touching protected evidence."""
        if not store.height_memory_active or store.height_memory_complete:
            return

        store.height_memory_refreshing = True
        try:
            _height_memory_refresh_feedback()
            if not _height_memory_board_is_valid():
                _height_memory_refresh_feedback()
        finally:
            store.height_memory_refreshing = False
        renpy.restart_interaction()

    # Public API: award the planned killer-safe height clue exactly once.
    def finish_height_memory_minigame():
        """Close the board and record Razzle's planned Visit 3 reveal."""
        if (store.height_memory_completion_recorded or not store.height_memory_active
                or store.height_memory_progress < store.height_memory_required_cleanups):
            return

        store.height_memory_completion_recorded = True
        store.height_memory_complete = True
        store.height_memory_active = False
        store.height_memory_refreshing = False
        store.height_memory_timer = 0.0
        renpy.hide_screen("height_memory_minigame")
        reveal = get_planned_route_reveal("razzle", 3)
        if reveal.get("scope") == "category":
            clue_text = "Eyewitness evidence rules out {} height.".format(
                reveal["value"])
        else:
            names = " and ".join(
                store.suspectNames[suspect_id]
                for suspect_id in reveal["eliminated"])
            clue_text = (
                "Doorframe measurements clear the individual profiles for {}."
                .format(names)
            )
        record_planned_route_reveal(
            "razzle", 3, clue_text=clue_text, expected_count=2)
        renpy.restart_interaction()

    # Public API: safely close the screen for menu/scene interruption handling.
    def abort_height_memory_minigame():
        """Close the board without recording a clue; the scene can reopen it."""
        store.height_memory_active = False
        store.height_memory_refreshing = False
        store.height_memory_timer = 0.0
        store.height_memory_board = []
        store.height_memory_feedback = ""
        renpy.hide_screen("height_memory_minigame")
        renpy.restart_interaction()
