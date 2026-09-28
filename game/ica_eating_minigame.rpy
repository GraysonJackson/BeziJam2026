## Ica's fourth-visit hot dog eating contest.

define ICA_EATING_DURATION = 26.0
define ICA_EATING_TICK_INTERVAL = 0.25
define ICA_EATING_TOTAL_HOT_DOGS = 12.0
define ICA_EATING_MAX_STAMINA = 5.0
define ICA_EATING_PLAYER_PASSIVE_PROGRESS = 0.045
define ICA_EATING_ICA_PASSIVE_PROGRESS = 0.08
define ICA_EATING_STAMINA_RECOVERY = 0.055
define ICA_EATING_BITE_PROGRESS = 0.52
define ICA_EATING_BITE_DIFFICULTY_BONUS = 0.06
define ICA_EATING_BITE_STAMINA_COST = 0.9
define ICA_EATING_BASE_ACTION_COOLDOWN = 0.60
define ICA_EATING_COOLDOWN_REDUCTION = 0.05
define ICA_EATING_PACE_PROGRESS = 0.14
define ICA_EATING_PACE_STAMINA = 1.55
define ICA_EATING_PACE_COOLDOWN = 0.55
define ICA_EATING_ICA_CHEAT_PROGRESS = 0.60
define ICA_EATING_CHEAT_INTERVAL = 6.0
define ICA_EATING_CHEAT_COUNT = 3
define ICA_EATING_FLIRT_SLOWDOWN = 0.20
define ICA_EATING_FLIRT_DURATION = 5.0
define ICA_EATING_HIGH_FLIRT_DURATION = 6.5
define ICA_EATING_CHEAT_SPECIAL_PROGRESS = 1.25

define ICA_EATING_APPROACH_LABELS = {
    "play_fair": "Power Through",
    "flirt": "Make It Weird",
    "cheat": "Get Sneaky",
}

default ica_eating_session_active = False
default ica_eating_phase = "idle"
default ica_eating_approach = ""
default ica_eating_reaction = ""
default ica_eating_difficulty_reduction = 0
default ica_eating_elapsed = 0.0
default ica_eating_player_progress = 0.0
default ica_eating_ica_progress = 0.0
default ica_eating_stamina = ICA_EATING_MAX_STAMINA
default ica_eating_action_cooldown = 0.0
default ica_eating_flirt_slowdown_left = 0.0
default ica_eating_special_used = False
default ica_eating_ica_cheat_stage = 0
default ica_eating_mistakes = 0
default ica_eating_feedback = ""
default ica_eating_completion_recorded = False
default ica_eating_result_applied = False
default ica_eating_result = {}

init python:
    def ica_eating_approach_label(approach_id):
        """Return the UI label for the approach already chosen in dialogue."""
        return store.ICA_EATING_APPROACH_LABELS.get(approach_id, "Unknown")

    def _ica_eating_clamp(value, low, high):
        return max(low, min(high, value))

    def _ica_eating_reset_state(approach_id, reaction_id):
        if approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica eating-contest approach: {}".format(approach_id))
        if reaction_id not in ("match_cheat", "flirt_back", "call_out"):
            raise Exception("Unknown Ica eating-contest reaction: {}".format(reaction_id))

        store.ica_eating_session_active = True
        store.ica_eating_phase = "active"
        store.ica_eating_approach = approach_id
        store.ica_eating_reaction = reaction_id
        store.ica_eating_difficulty_reduction = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        store.ica_eating_elapsed = 0.0
        store.ica_eating_player_progress = 0.0
        store.ica_eating_ica_progress = store.ICA_EATING_ICA_CHEAT_PROGRESS
        store.ica_eating_stamina = store.ICA_EATING_MAX_STAMINA
        store.ica_eating_action_cooldown = 0.0
        store.ica_eating_flirt_slowdown_left = 0.0
        store.ica_eating_special_used = False
        store.ica_eating_ica_cheat_stage = 0
        store.ica_eating_mistakes = 0
        store.ica_eating_completion_recorded = False
        store.ica_eating_result_applied = False
        store.ica_eating_result = {}

        if reaction_id == "match_cheat":
            store.ica_eating_feedback = "Ica caught your discarded hot dog with gravity and floated it back. Fine. Eat the rest."
        elif reaction_id == "flirt_back":
            extra_disappeared = 2 if store.ica >= store.ICA_HIGH_FLIRT_THRESHOLD else 3
            store.ica_eating_ica_progress += extra_disappeared * 0.35
            store.ica_eating_feedback = "The ketchup move landed. Unfortunately, Ica used the opening to cheat more."
        else:
            store.ica_eating_feedback = "The trash can is now mysteriously immovable. Proving anything can wait."

    def start_ica_eating_minigame(approach_id, reaction_id):
        """Start after both story choices, without asking for either choice again."""
        store.ica_clear_minigame_result("eating")
        _ica_eating_reset_state(approach_id, reaction_id)
        push_minigame_music()
        renpy.call_screen("ica_eating_minigame")

    def ica_eating_action(action_id):
        """Handle deliberate bites, recovery, and each approach's one special move."""
        if not store.ica_eating_session_active or store.ica_eating_phase != "active":
            return
        if store.ica_eating_action_cooldown > 0.0:
            return

        if action_id == "bite":
            if store.ica_eating_stamina < store.ICA_EATING_BITE_STAMINA_COST:
                store.ica_eating_mistakes += 1
                store.ica_eating_action_cooldown = 0.8
                store.ica_eating_feedback = "Too fast. You nearly inhale one whole and lose your rhythm."
            else:
                progress = (store.ICA_EATING_BITE_PROGRESS
                            + store.ICA_EATING_BITE_DIFFICULTY_BONUS
                            * store.ica_eating_difficulty_reduction)
                store.ica_eating_player_progress = _ica_eating_clamp(
                    store.ica_eating_player_progress + progress,
                    0.0,
                    store.ICA_EATING_TOTAL_HOT_DOGS)
                store.ica_eating_stamina = _ica_eating_clamp(
                    store.ica_eating_stamina - store.ICA_EATING_BITE_STAMINA_COST,
                    0.0,
                    store.ICA_EATING_MAX_STAMINA)
                store.ica_eating_action_cooldown = max(
                    0.35,
                    store.ICA_EATING_BASE_ACTION_COOLDOWN
                    - store.ICA_EATING_COOLDOWN_REDUCTION
                    * store.ica_eating_difficulty_reduction)
                store.ica_eating_feedback = "Terrible. Keep eating."

        elif action_id == "pace":
            store.ica_eating_player_progress = _ica_eating_clamp(
                store.ica_eating_player_progress + store.ICA_EATING_PACE_PROGRESS,
                0.0,
                store.ICA_EATING_TOTAL_HOT_DOGS)
            store.ica_eating_stamina = _ica_eating_clamp(
                store.ica_eating_stamina + store.ICA_EATING_PACE_STAMINA,
                0.0,
                store.ICA_EATING_MAX_STAMINA)
            store.ica_eating_action_cooldown = store.ICA_EATING_PACE_COOLDOWN
            store.ica_eating_feedback = "You breathe. Ica calls that cowardice with her mouth full."

        elif action_id == "special":
            if store.ica_eating_special_used or store.ica_eating_approach == "play_fair":
                return
            store.ica_eating_special_used = True

            if store.ica_eating_approach == "flirt":
                duration = (store.ICA_EATING_HIGH_FLIRT_DURATION
                            if store.ica >= store.ICA_HIGH_FLIRT_THRESHOLD
                            else store.ICA_EATING_FLIRT_DURATION)
                store.ica_eating_flirt_slowdown_left = duration
                store.ica_eating_feedback = "Ica stops chewing just long enough to decide whether that was smooth."
            else:
                store.ica_eating_player_progress = _ica_eating_clamp(
                    store.ica_eating_player_progress + store.ICA_EATING_CHEAT_SPECIAL_PROGRESS,
                    0.0,
                    store.ICA_EATING_TOTAL_HOT_DOGS)
                store.ica_eating_feedback = "You palm a hot dog. Ica sees it and respects the lack of effort."
            store.ica_eating_action_cooldown = 0.75

        else:
            raise Exception("Unknown Ica eating-contest action: {}".format(action_id))

        if store.ica_eating_player_progress >= store.ICA_EATING_TOTAL_HOT_DOGS:
            ica_eating_finish()
            return
        renpy.restart_interaction()

    def ica_eating_tick():
        """Advance both contestants and guarantee a result when the timer expires."""
        if (not store.ica_eating_session_active
                or store.ica_eating_phase != "active"
                or store.ica_eating_completion_recorded
                or getattr(store, "minigame_paused", False)):
            return

        tick = store.ICA_EATING_TICK_INTERVAL
        store.ica_eating_elapsed = min(
            store.ICA_EATING_DURATION,
            store.ica_eating_elapsed + tick)
        store.ica_eating_action_cooldown = max(
            0.0, store.ica_eating_action_cooldown - tick)
        store.ica_eating_flirt_slowdown_left = max(
            0.0, store.ica_eating_flirt_slowdown_left - tick)
        store.ica_eating_stamina = _ica_eating_clamp(
            store.ica_eating_stamina + store.ICA_EATING_STAMINA_RECOVERY,
            0.0,
            store.ICA_EATING_MAX_STAMINA)

        store.ica_eating_player_progress = _ica_eating_clamp(
            store.ica_eating_player_progress + store.ICA_EATING_PLAYER_PASSIVE_PROGRESS,
            0.0,
            store.ICA_EATING_TOTAL_HOT_DOGS)

        ica_rate = store.ICA_EATING_ICA_PASSIVE_PROGRESS
        if store.ica_eating_flirt_slowdown_left > 0.0:
            ica_rate *= store.ICA_EATING_FLIRT_SLOWDOWN
        store.ica_eating_ica_progress = _ica_eating_clamp(
            store.ica_eating_ica_progress + ica_rate,
            0.0,
            store.ICA_EATING_TOTAL_HOT_DOGS)

        next_cheat_time = ((store.ica_eating_ica_cheat_stage + 1)
                           * store.ICA_EATING_CHEAT_INTERVAL)
        if (store.ica_eating_ica_cheat_stage < store.ICA_EATING_CHEAT_COUNT
                and store.ica_eating_elapsed >= next_cheat_time):
            store.ica_eating_ica_cheat_stage += 1
            store.ica_eating_ica_progress = _ica_eating_clamp(
                store.ica_eating_ica_progress + store.ICA_EATING_ICA_CHEAT_PROGRESS,
                0.0,
                store.ICA_EATING_TOTAL_HOT_DOGS)
            store.ica_eating_feedback = "Another hot dog slips under the desk. Ica does not break eye contact."

        if (store.ica_eating_elapsed >= store.ICA_EATING_DURATION
                or store.ica_eating_ica_progress >= store.ICA_EATING_TOTAL_HOT_DOGS):
            ica_eating_finish()
            return
        renpy.restart_interaction()

    def ica_eating_finish():
        """Record one result and return to the surrounding Day 4 scene."""
        if (not store.ica_eating_session_active
                or store.ica_eating_phase != "active"
                or store.ica_eating_completion_recorded):
            return

        won = store.ica_eating_player_progress > store.ica_eating_ica_progress
        result_tier = "win" if won else "loss"
        store.ica_record_minigame_result(
            "eating",
            store.ica_eating_approach,
            store.ica_eating_difficulty_reduction,
            won,
            result_tier)
        store.ica_eating_result = store.ica_minigame_results.get("eating", {})
        store.ica_eating_completion_recorded = True
        store.ica_eating_phase = "complete"
        store.ica_eating_session_active = False
        pop_minigame_music()
        renpy.hide_screen("ica_eating_minigame")
        renpy.end_interaction(True)

    def ica_eating_abort():
        """Return to the scene without manufacturing a contest result."""
        if not store.ica_eating_session_active:
            return
        store.ica_eating_phase = "aborted"
        store.ica_eating_session_active = False
        store.ica_eating_feedback = ""
        pop_minigame_music()
        renpy.hide_screen("ica_eating_minigame")
        renpy.end_interaction(True)

    def ica_eating_apply_relationship_result():
        """Apply only the shared win bonus; dialogue already scores attitude."""
        result = store.ica_minigame_results.get("eating", {})
        if not result.get("completed", False) or store.ica_eating_result_applied:
            return False

        store.ica += store.ica_relationship_change_for_result(result)
        store.ica_eating_result_applied = True
        return True
