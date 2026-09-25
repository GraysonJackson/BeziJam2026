## Shared approach and result state for Ica's minigames.

default ica_minigame_results = {}

define ICA_DIFFICULTY_REDUCTION = {
    "play_fair": 0,
    "flirt": 1,
    "cheat": 2,
}

define ICA_MINIGAME_WIN_BONUS = 1
define ICA_EARLY_FLIRT_THRESHOLD = 8
define ICA_WARM_FLIRT_THRESHOLD = 13
define ICA_HIGH_FLIRT_THRESHOLD = 18
define ICA_DATE_ACCEPT_THRESHOLD = 32

default ica_day_one_candy = ""
default ica_hotdog_style = ""
default ica_paint_preparation = ""

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
        """Give a small performance bonus; dialogue choices score attitude."""
        if not result.get("completed", False):
            return 0
        return store.ICA_MINIGAME_WIN_BONUS if result.get("won", False) else 0

    def ica_clear_minigame_result(game_id):
        """Discard stale data when a new minigame session begins."""
        if game_id not in store.ica_minigame_results:
            return

        results = dict(store.ica_minigame_results)
        del results[game_id]
        store.ica_minigame_results = results
