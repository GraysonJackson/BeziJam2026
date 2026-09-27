## Ica's second-visit staring contest minigame.

define ICA_STARING_DURATION = 24.0
define ICA_STARING_TICK_INTERVAL = 0.15
define ICA_STARING_TRACK_MIN = 0.08
define ICA_STARING_TRACK_MAX = 0.92
define ICA_STARING_CLICK_IMPULSE = 0.18
define ICA_STARING_BASE_TARGET_SPEED = 0.24
define ICA_STARING_BASE_DECAY_SPEED = 0.20
define ICA_STARING_BASE_TARGET_HALF_SIZE = 0.105
define ICA_STARING_BASE_REQUIRED_HOLD = 8.0
define ICA_STARING_CENTER_POSITION = 0.5
define ICA_STARING_NORMALIZED_MAX = 1.0
define ICA_STARING_INITIAL_TARGET_MIN = 0.38
define ICA_STARING_INITIAL_TARGET_SPAN = 0.24
define ICA_STARING_TARGET_SPEED_REDUCTION = 0.045
define ICA_STARING_MIN_TARGET_SPEED = 0.12
define ICA_STARING_DECAY_REDUCTION = 0.045
define ICA_STARING_MIN_DECAY_SPEED = 0.08
define ICA_STARING_TARGET_SIZE_INCREASE = 0.025
define ICA_STARING_MAX_TARGET_HALF_SIZE = 0.17
define ICA_STARING_REQUIRED_HOLD_REDUCTION = 0.75
define ICA_STARING_MIN_REQUIRED_HOLD = 6.5
define ICA_STARING_FORWARD_DIRECTION = 1.0
define ICA_STARING_REVERSE_DIRECTION = -1.0
define ICA_STARING_TRACK_TOP = 260
define ICA_STARING_TRACK_HEIGHT = 420

define ICA_STARING_APPROACH_LABELS = {
    "flirt": "Flirt",
    "cheat": "Get Cheeky",
    "play_fair": "Play It Cool",
}

define ICA_STARING_APPROACH_DESCRIPTIONS = {
    "flirt": "Keep eye contact and tease Ica with distracting banter. The target slows and your focus holds longer.",
    "cheat": "Watch Ica in the dark monitor so you can steal blinks. The target slows further and the eye-contact zone widens.",
    "play_fair": "No tricks and no big performance. Just settle in and meet Ica's stare.",
}

default ica_staring_session_active = False
default ica_staring_phase = "idle"
default ica_staring_approach = ""
default ica_staring_difficulty_reduction = 0
default ica_staring_elapsed = 0.0
default ica_staring_player_position = ICA_STARING_CENTER_POSITION
default ica_staring_target_position = ICA_STARING_CENTER_POSITION
default ica_staring_target_direction = ICA_STARING_FORWARD_DIRECTION
default ica_staring_target_speed = ICA_STARING_BASE_TARGET_SPEED
default ica_staring_decay_speed = ICA_STARING_BASE_DECAY_SPEED
default ica_staring_target_half_size = ICA_STARING_BASE_TARGET_HALF_SIZE
default ica_staring_required_hold = ICA_STARING_BASE_REQUIRED_HOLD
default ica_staring_success_time = 0.0
default ica_staring_miss_time = 0.0
default ica_staring_feedback = ""
default ica_staring_completion_recorded = False
default ica_staring_result_applied = False

default ica_staring_result = {}

init python:
    def ica_staring_approach_label(approach_id):
        """Return the display label for a canonical Ica approach ID."""
        return store.ICA_STARING_APPROACH_LABELS.get(approach_id, "Unknown")

    def ica_staring_approach_description(approach_id):
        """Return concise contest flavor for a canonical Ica approach ID."""
        return store.ICA_STARING_APPROACH_DESCRIPTIONS.get(
            approach_id, "Choose how you want to approach the contest.")

    def _ica_staring_clamp(position):
        return max(store.ICA_STARING_TRACK_MIN,
                   min(store.ICA_STARING_TRACK_MAX, position))

    def _ica_staring_position_is_valid(position):
        return (isinstance(position, (int, float))
                and store.ICA_STARING_TRACK_MIN <= position <= store.ICA_STARING_TRACK_MAX)

    def _ica_staring_reset_state():
        store.ica_staring_session_active = True
        store.ica_staring_phase = "approach"
        store.ica_staring_approach = ""
        store.ica_staring_difficulty_reduction = 0
        store.ica_staring_elapsed = 0.0
        store.ica_staring_player_position = store.ICA_STARING_CENTER_POSITION
        store.ica_staring_target_position = store.ICA_STARING_CENTER_POSITION
        store.ica_staring_target_direction = store.ICA_STARING_FORWARD_DIRECTION
        store.ica_staring_target_speed = store.ICA_STARING_BASE_TARGET_SPEED
        store.ica_staring_decay_speed = store.ICA_STARING_BASE_DECAY_SPEED
        store.ica_staring_target_half_size = store.ICA_STARING_BASE_TARGET_HALF_SIZE
        store.ica_staring_required_hold = store.ICA_STARING_BASE_REQUIRED_HOLD
        store.ica_staring_success_time = 0.0
        store.ica_staring_miss_time = 0.0
        store.ica_staring_feedback = "Choose your approach."
        store.ica_staring_completion_recorded = False
        store.ica_staring_result_applied = False
        store.ica_staring_result = {}

    def start_ica_staring_minigame(approach_id=None):
        """Reset the contest, optionally using a choice made in dialogue."""
        store.ica_clear_minigame_result("staring")
        _ica_staring_reset_state()
        if approach_id is not None:
            ica_staring_choose_approach(approach_id, restart=False)
        renpy.call_screen("ica_staring_minigame")

    def ica_staring_choose_approach(approach_id, restart=True):
        """Apply the canonical approach modifier and begin the timed contest."""
        if not store.ica_staring_session_active or store.ica_staring_phase != "approach":
            return
        if approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica staring approach: {}".format(approach_id))

        reduction = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        store.ica_staring_approach = approach_id
        store.ica_staring_difficulty_reduction = reduction
        store.ica_staring_target_speed = max(
            store.ICA_STARING_MIN_TARGET_SPEED,
            store.ICA_STARING_BASE_TARGET_SPEED - (store.ICA_STARING_TARGET_SPEED_REDUCTION * reduction))
        store.ica_staring_decay_speed = max(
            store.ICA_STARING_MIN_DECAY_SPEED,
            store.ICA_STARING_BASE_DECAY_SPEED - (store.ICA_STARING_DECAY_REDUCTION * reduction))
        store.ica_staring_target_half_size = min(
            store.ICA_STARING_MAX_TARGET_HALF_SIZE,
            store.ICA_STARING_BASE_TARGET_HALF_SIZE + (store.ICA_STARING_TARGET_SIZE_INCREASE * reduction))
        store.ica_staring_required_hold = max(
            store.ICA_STARING_MIN_REQUIRED_HOLD,
            store.ICA_STARING_BASE_REQUIRED_HOLD - (store.ICA_STARING_REQUIRED_HOLD_REDUCTION * reduction))
        store.ica_staring_elapsed = 0.0
        store.ica_staring_success_time = 0.0
        store.ica_staring_miss_time = 0.0
        store.ica_staring_player_position = store.ICA_STARING_CENTER_POSITION
        store.ica_staring_target_position = (
            store.ICA_STARING_INITIAL_TARGET_MIN
            + (renpy.random.random() * store.ICA_STARING_INITIAL_TARGET_SPAN))
        store.ica_staring_target_direction = (
            store.ICA_STARING_FORWARD_DIRECTION
            if renpy.random.random() >= store.ICA_STARING_CENTER_POSITION
            else store.ICA_STARING_REVERSE_DIRECTION)
        store.ica_staring_feedback = "Keep your eyes on the target."
        store.ica_staring_phase = "active"
        if restart:
            renpy.restart_interaction()

    def ica_staring_click():
        """Pulse the player marker toward Ica's moving eye-contact target."""
        if not store.ica_staring_session_active or store.ica_staring_phase != "active":
            return
        if not _ica_staring_position_is_valid(store.ica_staring_target_position):
            store.ica_staring_target_position = store.ICA_STARING_CENTER_POSITION
        if not _ica_staring_position_is_valid(store.ica_staring_player_position):
            store.ica_staring_player_position = store.ICA_STARING_CENTER_POSITION

        distance = store.ica_staring_target_position - store.ica_staring_player_position
        impulse = min(abs(distance), store.ICA_STARING_CLICK_IMPULSE)
        if distance > 0:
            store.ica_staring_player_position += impulse
        elif distance < 0:
            store.ica_staring_player_position -= impulse
        store.ica_staring_player_position = _ica_staring_clamp(
            store.ica_staring_player_position)
        store.ica_staring_feedback = "Refocus—hold that stare."
        renpy.restart_interaction()

    def ica_staring_tick():
        """Advance target movement, focus decay, overlap progress, and duration."""
        if not store.ica_staring_session_active or store.ica_staring_phase != "active":
            return
        if store.ica_staring_completion_recorded or getattr(store, "minigame_paused", False):
            return

        if not _ica_staring_position_is_valid(store.ica_staring_target_position):
            store.ica_staring_target_position = store.ICA_STARING_CENTER_POSITION
            store.ica_staring_target_direction = store.ICA_STARING_FORWARD_DIRECTION
        if not _ica_staring_position_is_valid(store.ica_staring_player_position):
            store.ica_staring_player_position = store.ICA_STARING_CENTER_POSITION
        if store.ica_staring_target_direction not in (
                store.ICA_STARING_REVERSE_DIRECTION,
                store.ICA_STARING_FORWARD_DIRECTION):
            store.ica_staring_target_direction = store.ICA_STARING_FORWARD_DIRECTION

        next_target = (store.ica_staring_target_position
                       + store.ica_staring_target_direction
                       * store.ica_staring_target_speed
                       * store.ICA_STARING_TICK_INTERVAL)
        if next_target >= store.ICA_STARING_TRACK_MAX:
            next_target = store.ICA_STARING_TRACK_MAX
            store.ica_staring_target_direction = store.ICA_STARING_REVERSE_DIRECTION
        elif next_target <= store.ICA_STARING_TRACK_MIN:
            next_target = store.ICA_STARING_TRACK_MIN
            store.ica_staring_target_direction = store.ICA_STARING_FORWARD_DIRECTION
        store.ica_staring_target_position = _ica_staring_clamp(next_target)

        store.ica_staring_player_position = _ica_staring_clamp(
            store.ica_staring_player_position
            - (store.ica_staring_decay_speed * store.ICA_STARING_TICK_INTERVAL))
        store.ica_staring_elapsed = min(
            store.ICA_STARING_DURATION,
            store.ica_staring_elapsed + store.ICA_STARING_TICK_INTERVAL)

        if abs(store.ica_staring_player_position - store.ica_staring_target_position) <= store.ica_staring_target_half_size:
            store.ica_staring_success_time += store.ICA_STARING_TICK_INTERVAL
            store.ica_staring_feedback = "Locked in. Don't blink."
        else:
            store.ica_staring_miss_time += store.ICA_STARING_TICK_INTERVAL
            store.ica_staring_feedback = "Blink! Catch the target again."

        if store.ica_staring_success_time >= store.ica_staring_required_hold:
            ica_staring_finish()
            return

        remaining_duration = store.ICA_STARING_DURATION - store.ica_staring_elapsed
        remaining_needed = store.ica_staring_required_hold - store.ica_staring_success_time
        if remaining_duration < remaining_needed:
            ica_staring_finish()
            return

        if store.ica_staring_elapsed >= store.ICA_STARING_DURATION:
            ica_staring_finish()
            return

        renpy.restart_interaction()

    def ica_staring_finish():
        """Record one definite contest outcome, stop updates, and close the screen."""
        if (not store.ica_staring_session_active
                or store.ica_staring_phase != "active"
                or store.ica_staring_completion_recorded):
            return

        won = store.ica_staring_success_time >= store.ica_staring_required_hold
        result_tier = "win" if won else "loss"
        store.ica_record_minigame_result(
            "staring",
            store.ica_staring_approach,
            store.ica_staring_difficulty_reduction,
            won,
            result_tier)
        store.ica_staring_result = store.ica_minigame_results.get("staring", {})
        store.ica_staring_completion_recorded = True
        store.ica_staring_phase = "complete"
        store.ica_staring_session_active = False
        renpy.hide_screen("ica_staring_minigame")
        renpy.end_interaction(True)

    def ica_staring_abort():
        """Close an unfinished contest without writing a completed result."""
        if not store.ica_staring_session_active:
            return
        store.ica_staring_phase = "aborted"
        store.ica_staring_session_active = False
        store.ica_staring_elapsed = 0.0
        store.ica_staring_feedback = ""
        renpy.hide_screen("ica_staring_minigame")
        renpy.end_interaction(True)

    def ica_staring_apply_relationship_result():
        """Apply the completed contest's Ica relationship change at most once."""
        result = store.ica_minigame_results.get("staring", {})
        if not result.get("completed", False) or store.ica_staring_result_applied:
            return False

        relationship_change = store.ica_relationship_change_for_result(result)
        store.ica += relationship_change
        store.ica_staring_result_applied = True
        return True
