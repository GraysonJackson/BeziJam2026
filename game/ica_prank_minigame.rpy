## Ica's fifth-visit office-painting stealth game.

define ICA_PRANK_GRID_WIDTH = 12
define ICA_PRANK_GRID_HEIGHT = 7
define ICA_PRANK_PATROL_INTERVAL = 0.75
define ICA_PRANK_CAUGHT_DELAY = 1.1
define ICA_PRANK_SIGHT_RANGE = 2
define ICA_PRANK_START = (1, 5)
define ICA_PRANK_PAINT_TILE = (2, 1)
define ICA_PRANK_DESK_TILE = (1, 5)
define ICA_PRANK_DOOR_TILE = (6, 3)
define ICA_PRANK_OFFICE_ENTRY = (8, 3)
define ICA_PRANK_WALL_TARGETS = ((9, 1), (10, 3), (9, 5))
define ICA_PRANK_BLOCKED_TILES = (
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
    (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
    (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6),
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5),
    (3, 2), (4, 2), (2, 4), (3, 4),
    (9, 2), (9, 4),
)
define ICA_PRANK_PATROL = (
    (5, 1, "down"),
    (5, 2, "down"),
    (5, 3, "down"),
    (5, 4, "down"),
    (5, 5, "right"),
    (6, 5, "up"),
    (6, 4, "up"),
    (6, 3, "up"),
    (6, 2, "up"),
    (6, 1, "left"),
)
define ICA_PRANK_FACING_VECTORS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}
define ICA_PRANK_FACING_ARROWS = {
    "up": "UP",
    "down": "DOWN",
    "left": "LEFT",
    "right": "RIGHT",
}
define ICA_PRANK_APPROACH_LABELS = {
    "play_fair": "Just Paint",
    "flirt": "Make It Weird",
    "cheat": "Get It Over With",
}

default ica_prank_session_active = False
default ica_prank_phase = "idle"
default ica_prank_approach = ""
default ica_prank_difficulty_reduction = 0
default ica_prank_player_position = ICA_PRANK_START
default ica_prank_ulysses_position = (5, 1)
default ica_prank_ulysses_facing = "down"
default ica_prank_patrol_index = 0
default ica_prank_sight_cells = []
default ica_prank_objective = "pickup"
default ica_prank_has_paint = False
default ica_prank_painted_targets = []
default ica_prank_checkpoint_position = ICA_PRANK_START
default ica_prank_checkpoint_objective = "pickup"
default ica_prank_checkpoint_has_paint = False
default ica_prank_checkpoint_painted_targets = []
default ica_prank_assist_available = False
default ica_prank_patrol_pause_ticks = 0
default ica_prank_safe_ticks = 0
default ica_prank_caught_count = 0
default ica_prank_feedback = ""
default ica_prank_completion_recorded = False
default ica_prank_result_applied = False
default ica_prank_result = {}

init python:
    def ica_prank_approach_label(approach_id):
        return store.ICA_PRANK_APPROACH_LABELS.get(approach_id, "Unknown")

    def _ica_prank_is_in_bounds(position):
        x, y = position
        return (0 <= x < store.ICA_PRANK_GRID_WIDTH
                and 0 <= y < store.ICA_PRANK_GRID_HEIGHT)

    def _ica_prank_is_walkable(position):
        return (_ica_prank_is_in_bounds(position)
                and position not in store.ICA_PRANK_BLOCKED_TILES)

    def _ica_prank_update_ulysses():
        patrol_length = len(store.ICA_PRANK_PATROL)
        if patrol_length <= 0:
            raise Exception("Ica prank patrol cannot be empty.")
        store.ica_prank_patrol_index = max(
            0, min(patrol_length - 1, store.ica_prank_patrol_index))
        x, y, facing = store.ICA_PRANK_PATROL[store.ica_prank_patrol_index]
        store.ica_prank_ulysses_position = (x, y)
        store.ica_prank_ulysses_facing = facing
        _ica_prank_update_sight()

    def _ica_prank_update_sight():
        facing_vector = store.ICA_PRANK_FACING_VECTORS.get(
            store.ica_prank_ulysses_facing, (0, 1))
        sight = []
        start_x, start_y = store.ica_prank_ulysses_position
        for distance in range(1, store.ICA_PRANK_SIGHT_RANGE + 1):
            cell = (start_x + facing_vector[0] * distance,
                    start_y + facing_vector[1] * distance)
            if not _ica_prank_is_in_bounds(cell) or cell in store.ICA_PRANK_BLOCKED_TILES:
                break
            sight.append(cell)
        store.ica_prank_sight_cells = sight

    def _ica_prank_reset_state(approach_id):
        if approach_id not in store.ICA_DIFFICULTY_REDUCTION:
            raise Exception("Unknown Ica prank approach: {}".format(approach_id))

        store.ica_prank_session_active = True
        store.ica_prank_phase = "active"
        store.ica_prank_approach = approach_id
        store.ica_prank_difficulty_reduction = store.ICA_DIFFICULTY_REDUCTION[approach_id]
        store.ica_prank_player_position = store.ICA_PRANK_START
        store.ica_prank_patrol_index = 0
        store.ica_prank_objective = "pickup"
        store.ica_prank_has_paint = False
        store.ica_prank_painted_targets = []
        store.ica_prank_patrol_pause_ticks = 0
        store.ica_prank_safe_ticks = 0
        store.ica_prank_caught_count = 0
        store.ica_prank_feedback = "Get the paint, then cross the hall when Ulysses looks away."
        store.ica_prank_completion_recorded = False
        store.ica_prank_result_applied = False
        store.ica_prank_result = {}
        _ica_prank_update_ulysses()
        ica_prank_set_checkpoint(restart=False)

    def start_ica_prank_minigame(approach_id):
        """Use the approach selected in dialogue and open the stealth map."""
        store.ica_clear_minigame_result("prank")
        _ica_prank_reset_state(approach_id)
        renpy.call_screen("ica_prank_minigame")

    def ica_prank_set_checkpoint(restart=True):
        """Capture completed objectives so being spotted never erases progress."""
        store.ica_prank_checkpoint_position = store.ica_prank_player_position
        store.ica_prank_checkpoint_objective = store.ica_prank_objective
        store.ica_prank_checkpoint_has_paint = store.ica_prank_has_paint
        store.ica_prank_checkpoint_painted_targets = list(store.ica_prank_painted_targets)
        store.ica_prank_assist_available = store.ica_prank_approach != "play_fair"
        store.ica_prank_patrol_pause_ticks = 0
        store.ica_prank_safe_ticks = 0
        if restart:
            renpy.restart_interaction()

    def _ica_prank_trigger_detection():
        if store.ica_prank_phase != "active":
            return False
        if store.ica_prank_safe_ticks > 0:
            return False
        if (store.ica_prank_player_position == store.ica_prank_ulysses_position
                or store.ica_prank_player_position in store.ica_prank_sight_cells):
            store.ica_prank_phase = "caught"
            store.ica_prank_caught_count += 1
            store.ica_prank_feedback = "Caught. Ica yanks you back with gravity before Ulysses gets a good look."
            renpy.restart_interaction()
            return True
        return False

    def ica_prank_reset_to_checkpoint():
        """Resume the current objective after the caught overlay."""
        if not store.ica_prank_session_active or store.ica_prank_phase != "caught":
            return
        store.ica_prank_player_position = store.ica_prank_checkpoint_position
        store.ica_prank_objective = store.ica_prank_checkpoint_objective
        store.ica_prank_has_paint = store.ica_prank_checkpoint_has_paint
        store.ica_prank_painted_targets = list(
            store.ica_prank_checkpoint_painted_targets)
        store.ica_prank_patrol_index = 0
        store.ica_prank_patrol_pause_ticks = 0
        store.ica_prank_safe_ticks = 0
        store.ica_prank_assist_available = store.ica_prank_approach != "play_fair"
        store.ica_prank_phase = "active"
        store.ica_prank_feedback = "Back to the last safe point. Ulysses starts the same patrol again."
        _ica_prank_update_ulysses()
        renpy.restart_interaction()

    def ica_prank_move(dx, dy):
        """Move exactly one cardinal tile when the destination is walkable."""
        if not store.ica_prank_session_active or store.ica_prank_phase != "active":
            return
        if abs(dx) + abs(dy) != 1:
            raise Exception("Ica prank movement must be one cardinal tile.")

        current_x, current_y = store.ica_prank_player_position
        destination = (current_x + dx, current_y + dy)
        if not _ica_prank_is_walkable(destination):
            store.ica_prank_feedback = "Blocked. Even Ica isn't moving the walls for this."
            renpy.restart_interaction()
            return

        store.ica_prank_player_position = destination
        if store.ica_prank_safe_ticks <= 0:
            _ica_prank_trigger_detection()
        renpy.restart_interaction()

    def ica_prank_tick():
        """Advance Ulysses' deterministic patrol and check his visible tiles."""
        if not store.ica_prank_session_active or store.ica_prank_phase != "active" or getattr(store, "minigame_paused", False):
            return

        if store.ica_prank_safe_ticks > 0:
            store.ica_prank_safe_ticks -= 1

        if store.ica_prank_patrol_pause_ticks > 0:
            store.ica_prank_patrol_pause_ticks -= 1
            store.ica_prank_feedback = "Ica keeps Ulysses occupied. Move."
        else:
            store.ica_prank_patrol_index = (
                store.ica_prank_patrol_index + 1) % len(store.ICA_PRANK_PATROL)
            _ica_prank_update_ulysses()

        if store.ica_prank_safe_ticks <= 0:
            _ica_prank_trigger_detection()
        renpy.restart_interaction()

    def ica_prank_use_assist():
        """Use the one Ica-assisted opening available on the current objective leg."""
        if (not store.ica_prank_session_active
                or store.ica_prank_phase != "active"
                or not store.ica_prank_assist_available):
            return

        store.ica_prank_assist_available = False
        if store.ica_prank_approach == "flirt":
            store.ica_prank_patrol_pause_ticks = 2
            store.ica_prank_feedback = "Ica calls out something distracting. Ulysses stops to reconsider his life."
        elif store.ica_prank_approach == "cheat":
            store.ica_prank_safe_ticks = 2
            store.ica_prank_feedback = "Ica bends the light around you with floating office junk. You're briefly covered."
        renpy.restart_interaction()

    def ica_prank_interact():
        """Pick up paint, enter the office, or paint the current wall marker."""
        if not store.ica_prank_session_active or store.ica_prank_phase != "active":
            return

        position = store.ica_prank_player_position
        if store.ica_prank_objective == "pickup" and position == store.ICA_PRANK_PAINT_TILE:
            store.ica_prank_has_paint = True
            store.ica_prank_objective = "enter_office"
            store.ica_prank_feedback = "Paint acquired. Reach the PINK DOOR marker and interact."
            ica_prank_set_checkpoint(restart=False)

        elif store.ica_prank_objective == "enter_office" and position == store.ICA_PRANK_DOOR_TILE:
            if not store.ica_prank_has_paint:
                store.ica_prank_feedback = "You need the paint first."
            else:
                store.ica_prank_player_position = store.ICA_PRANK_OFFICE_ENTRY
                store.ica_prank_objective = "paint_walls"
                store.ica_prank_feedback = "Inside. Paint all three PINK WALL markers before he opens the door."
                ica_prank_set_checkpoint(restart=False)

        elif (store.ica_prank_objective == "paint_walls"
                and position in store.ICA_PRANK_WALL_TARGETS
                and position not in store.ica_prank_painted_targets):
            painted = list(store.ica_prank_painted_targets)
            painted.append(position)
            store.ica_prank_painted_targets = painted
            remaining = len(store.ICA_PRANK_WALL_TARGETS) - len(painted)
            if remaining <= 0:
                finish_ica_prank_minigame()
                return
            store.ica_prank_feedback = "Wall section painted. {} left.".format(remaining)
            ica_prank_set_checkpoint(restart=False)

        else:
            store.ica_prank_feedback = "Nothing useful to do on this tile."

        renpy.restart_interaction()

    def ica_prank_objective_text():
        if store.ica_prank_objective == "pickup":
            return "Pick up the pink paint."
        if store.ica_prank_objective == "enter_office":
            return "Cross the hall and interact at PINK DOOR."
        if store.ica_prank_objective == "paint_walls":
            remaining = (len(store.ICA_PRANK_WALL_TARGETS)
                         - len(store.ica_prank_painted_targets))
            return "Paint the marked wall sections ({} left).".format(remaining)
        return "Prank complete."

    def ica_prank_cell_background(x, y):
        position = (x, y)
        if position in store.ICA_PRANK_BLOCKED_TILES:
            return "#2D3540"
        if position in store.ica_prank_sight_cells and store.ica_prank_phase == "active":
            return "#E58B73"
        if x >= 8:
            return "#F3CADB"
        if x >= 5:
            return "#D7D0C2"
        return "#E7E3D8"

    def ica_prank_cell_label(x, y):
        position = (x, y)
        if position == store.ica_prank_player_position:
            return "YOU"
        if position == store.ica_prank_ulysses_position:
            return "ULY\n{}".format(
                store.ICA_PRANK_FACING_ARROWS.get(store.ica_prank_ulysses_facing, ""))
        if position in store.ICA_PRANK_BLOCKED_TILES:
            return ""
        if position == store.ICA_PRANK_PAINT_TILE and not store.ica_prank_has_paint:
            return "PAINT"
        if position == store.ICA_PRANK_DOOR_TILE:
            return "PINK\nDOOR"
        if position in store.ICA_PRANK_WALL_TARGETS:
            return "DONE" if position in store.ica_prank_painted_targets else "PINK\nWALL"
        if position == store.ICA_PRANK_DESK_TILE:
            return "ICA"
        return ""

    def finish_ica_prank_minigame():
        """Record the completed office prank once and return to Day 5 dialogue."""
        if (not store.ica_prank_session_active
                or store.ica_prank_phase != "active"
                or store.ica_prank_completion_recorded):
            return
        if len(store.ica_prank_painted_targets) < len(store.ICA_PRANK_WALL_TARGETS):
            return

        store.ica_record_minigame_result(
            "prank",
            store.ica_prank_approach,
            store.ica_prank_difficulty_reduction,
            True,
            "success")
        store.ica_prank_result = store.ica_minigame_results.get("prank", {})
        store.ica_prank_completion_recorded = True
        store.ica_prank_phase = "complete"
        store.ica_prank_session_active = False
        renpy.hide_screen("ica_prank_minigame")
        renpy.end_interaction(True)

    def ica_prank_abort():
        """Leave the map without recording a false success."""
        if not store.ica_prank_session_active:
            return
        store.ica_prank_phase = "aborted"
        store.ica_prank_session_active = False
        renpy.hide_screen("ica_prank_minigame")
        renpy.end_interaction(True)

    def ica_prank_apply_relationship_result():
        """Add only the shared completion bonus; dialogue already scores approach."""
        result = store.ica_minigame_results.get("prank", {})
        if not result.get("completed", False) or store.ica_prank_result_applied:
            return False
        store.ica += store.ica_relationship_change_for_result(result)
        store.ica_prank_result_applied = True
        return True
