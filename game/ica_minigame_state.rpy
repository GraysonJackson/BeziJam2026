## Shared approach and result state for Ica's minigames.

default ica_minigame_results = {}

define ICA_DIFFICULTY_REDUCTION = {
    "play_fair": 0,
    "flirt": 1,
    "cheat": 2,
}

# Ica likes people who match her low-pressure energy more than people who try
# to impress her. Keep the legacy "play_fair" id for save compatibility, but
# present it to the player as playing it cool.
define ICA_APPROACH_RELATIONSHIP = {
    "play_fair": 2,
    "flirt": 1,
    "cheat": 0,
}

define ICA_MINIGAME_WIN_BONUS = 1

init python:
    def ica_record_minigame_result(game_id, approach_id, difficulty_reduction, won, result_tier):
        """Persist one complete Ica minigame result with a canonical modifier."""
        if approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica minigame approach: {}".format(approach_id))

        if not isinstance(won, bool):
            raise Exception("Ica minigame result must use a boolean win value.")

        canonical_reduction = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        result = {
            "approach": approach_id,
            "difficulty_reduction": canonical_reduction,
            "won": won,
            "lost": not won,
            "result_tier": result_tier,
            "completed": True,
        }

        results = dict(store.ica_minigame_results)
        results[game_id] = result
        store.ica_minigame_results = results

    def ica_relationship_change_for_result(result):
        """Favor Ica's preferred attitude, with a small bonus for winning."""
        if not result.get("completed", False):
            return 0

        approach_change = store.ICA_APPROACH_RELATIONSHIP.get(
            result.get("approach", ""), 0)
        win_bonus = store.ICA_MINIGAME_WIN_BONUS if result.get("won", False) else 0
        return approach_change + win_bonus

    def ica_clear_minigame_result(game_id):
        """Discard stale data when a new minigame session begins."""
        if game_id not in store.ica_minigame_results:
            return

        results = dict(store.ica_minigame_results)
        del results[game_id]
        store.ica_minigame_results = results
