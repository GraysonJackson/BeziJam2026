## Madeline Visit 3: forgiving centrifuge balance and blood-band test.

define MADELINE_CENTRIFUGE_SPIN_STEP = 5
define MADELINE_CENTRIFUGE_TRIM_MIN = -2
define MADELINE_CENTRIFUGE_TRIM_MAX = 2

define MADELINE_CENTRIFUGE_TUBES = {
    "sample": {"label": "CRIME-SCENE SAMPLE", "mass": 6, "color": "#8D3027"},
    "control": {"label": "CONTROL SAMPLE", "mass": 4, "color": "#00719A"},
    "counter_red": {"label": "COUNTERWEIGHT 6", "mass": 6, "color": "#D26143"},
    "counter_blue": {"label": "COUNTERWEIGHT 4", "mass": 4, "color": "#58A88A"},
}

define MADELINE_CENTRIFUGE_SLOTS = (
    "left_top", "left_bottom", "right_top", "right_bottom",
)

default madeline_centrifuge_active = False
default madeline_centrifuge_phase = "idle"
default madeline_centrifuge_selected_tube = ""
default madeline_centrifuge_slots = {}
default madeline_centrifuge_trim = 0
default madeline_centrifuge_spin_progress = 0
default madeline_centrifuge_stability = 100
default madeline_centrifuge_attempts = 0
default madeline_centrifuge_feedback = ""
default madeline_centrifuge_reveal = {}
default madeline_centrifuge_result = {}
default madeline_centrifuge_completion_recorded = False

init python:
    def _madeline_centrifuge_reset():
        store.madeline_centrifuge_active = True
        store.madeline_centrifuge_phase = "setup"
        store.madeline_centrifuge_selected_tube = ""
        store.madeline_centrifuge_slots = {
            slot_id: "" for slot_id in store.MADELINE_CENTRIFUGE_SLOTS
        }
        store.madeline_centrifuge_trim = 0
        store.madeline_centrifuge_spin_progress = 0
        store.madeline_centrifuge_stability = 100
        store.madeline_centrifuge_attempts = 0
        store.madeline_centrifuge_feedback = (
            "Place all four tubes. Keep the total mass equal on both sides of the rotor."
        )
        store.madeline_centrifuge_reveal = get_planned_route_reveal(
            "madeline", 3)
        store.madeline_centrifuge_result = {}
        store.madeline_centrifuge_completion_recorded = False

    def start_madeline_centrifuge_minigame():
        """Reset the laboratory state and open the modal centrifuge screen."""
        _madeline_centrifuge_reset()
        renpy.call_screen("madeline_centrifuge_minigame")

    def madeline_centrifuge_select_tube(item_id):
        """Select a tube, pick one up from a slot, or place it in a slot."""
        if (not store.madeline_centrifuge_active
                or store.madeline_centrifuge_phase != "setup"):
            return

        known_tubes = store.MADELINE_CENTRIFUGE_TUBES
        known_slots = store.MADELINE_CENTRIFUGE_SLOTS

        if item_id in known_tubes:
            if store.madeline_centrifuge_selected_tube == item_id:
                store.madeline_centrifuge_selected_tube = ""
            else:
                store.madeline_centrifuge_selected_tube = item_id
            store.madeline_centrifuge_feedback = (
                "Selected {}.".format(known_tubes[item_id]["label"])
            )
            renpy.restart_interaction()
            return

        if item_id not in known_slots:
            return

        slots = dict(store.madeline_centrifuge_slots)
        selected = store.madeline_centrifuge_selected_tube
        occupying = slots.get(item_id, "")

        if not selected:
            if not occupying:
                return
            slots[item_id] = ""
            store.madeline_centrifuge_selected_tube = occupying
            store.madeline_centrifuge_feedback = (
                "Removed {} from the rotor.".format(
                    known_tubes[occupying]["label"]))
        else:
            for slot_id in known_slots:
                if slots.get(slot_id) == selected:
                    slots[slot_id] = ""
            slots[item_id] = selected
            store.madeline_centrifuge_selected_tube = occupying
            store.madeline_centrifuge_feedback = (
                "Placed {}. Check the balance before spinning.".format(
                    known_tubes[selected]["label"]))

        store.madeline_centrifuge_slots = slots
        store.madeline_centrifuge_spin_progress = 0
        store.madeline_centrifuge_stability = 100
        renpy.restart_interaction()

    def _madeline_centrifuge_side_mass(side):
        total = 0
        for slot_id, tube_id in store.madeline_centrifuge_slots.items():
            if slot_id.startswith(side) and tube_id:
                total += store.MADELINE_CENTRIFUGE_TUBES[tube_id]["mass"]
        return total

    def madeline_centrifuge_effective_balance():
        left_mass = _madeline_centrifuge_side_mass("left")
        right_mass = _madeline_centrifuge_side_mass("right")
        return left_mass - right_mass + store.madeline_centrifuge_trim

    def madeline_centrifuge_balance(action_id):
        """Adjust the visible fine-balance trim or reset a failed spin."""
        if not store.madeline_centrifuge_active:
            return

        if action_id == "retry" and store.madeline_centrifuge_phase == "retry":
            store.madeline_centrifuge_phase = "setup"
            store.madeline_centrifuge_spin_progress = 0
            store.madeline_centrifuge_stability = 100
            store.madeline_centrifuge_feedback = (
                "The rotor is unlocked. Rearrange the tubes or adjust the trim."
            )
        elif store.madeline_centrifuge_phase == "setup":
            if action_id == "trim_left":
                store.madeline_centrifuge_trim = min(
                    store.MADELINE_CENTRIFUGE_TRIM_MAX,
                    store.madeline_centrifuge_trim + 1)
            elif action_id == "trim_right":
                store.madeline_centrifuge_trim = max(
                    store.MADELINE_CENTRIFUGE_TRIM_MIN,
                    store.madeline_centrifuge_trim - 1)
            elif action_id == "trim_reset":
                store.madeline_centrifuge_trim = 0
            else:
                return
            store.madeline_centrifuge_feedback = (
                "Fine trim set to {:+d}. Effective balance: {:+d}.".format(
                    store.madeline_centrifuge_trim,
                    madeline_centrifuge_effective_balance()))
        else:
            return

        renpy.restart_interaction()

    def madeline_centrifuge_start_spin():
        """Begin a short spin after all four rotor positions are occupied."""
        if (not store.madeline_centrifuge_active
                or store.madeline_centrifuge_phase != "setup"):
            return

        placed = [
            tube_id for tube_id in store.madeline_centrifuge_slots.values()
            if tube_id
        ]
        if len(placed) != len(store.MADELINE_CENTRIFUGE_SLOTS):
            store.madeline_centrifuge_feedback = (
                "Madeline: All four slots, newb. An empty rotor position is not balance."
            )
            renpy.restart_interaction()
            return

        if len(set(placed)) != len(store.MADELINE_CENTRIFUGE_TUBES):
            store.madeline_centrifuge_feedback = (
                "Madeline: You duplicated a tube. Impressive violation of matter. Reset it."
            )
            renpy.restart_interaction()
            return

        store.madeline_centrifuge_attempts += 1
        store.madeline_centrifuge_phase = "spinning"
        store.madeline_centrifuge_spin_progress = 0
        imbalance = abs(madeline_centrifuge_effective_balance())
        store.madeline_centrifuge_stability = max(0, 100 - imbalance * 22)
        store.madeline_centrifuge_feedback = "Rotor accelerating."
        renpy.restart_interaction()

    def madeline_centrifuge_tick():
        """Advance the active spin and resolve stability at the end."""
        if (not store.madeline_centrifuge_active
                or store.madeline_centrifuge_phase != "spinning"):
            return

        store.madeline_centrifuge_spin_progress = min(
            100,
            store.madeline_centrifuge_spin_progress
            + store.MADELINE_CENTRIFUGE_SPIN_STEP)

        if store.madeline_centrifuge_spin_progress >= 100:
            if madeline_centrifuge_effective_balance() == 0:
                store.madeline_centrifuge_phase = "read_pending"
                store.madeline_centrifuge_stability = 100
                store.madeline_centrifuge_feedback = (
                    "Separation complete. The bands are stable enough to read."
                )
            else:
                store.madeline_centrifuge_phase = "retry"
                store.madeline_centrifuge_feedback = (
                    "The rotor completed safely, but vibration blurred the bands. Rebalance and retry."
                )
        renpy.restart_interaction()

    def madeline_centrifuge_read_result():
        """Expose the seeded blood-type exclusion after a stable separation."""
        if (not store.madeline_centrifuge_active
                or store.madeline_centrifuge_phase != "read_pending"):
            return
        blood_type = store.madeline_centrifuge_reveal["value"]
        store.madeline_centrifuge_phase = "result"
        store.madeline_centrifuge_feedback = (
            "No type {} markers appear in the recovered trace.".format(blood_type)
        )
        renpy.restart_interaction()

    def _madeline_centrifuge_record_result(quality, completed):
        if store.madeline_centrifuge_completion_recorded:
            return False
        store.madeline_centrifuge_completion_recorded = True

        blood_type = store.madeline_centrifuge_reveal["value"]
        clue_text = (
            "The recovered blood trace excludes blood type {}."
            .format(blood_type)
        )
        record_planned_route_reveal(
            "madeline", 3, clue_text=clue_text, expected_count=2)
        store.madeline_centrifuge_result = {
            "completed": completed,
            "quality": quality,
            "attempts": store.madeline_centrifuge_attempts,
            "blood_type": blood_type,
        }
        return True

    def finish_madeline_centrifuge_minigame():
        """Record a successfully read result and return to the route."""
        if (not store.madeline_centrifuge_active
                or store.madeline_centrifuge_phase != "result"):
            return
        quality = "perfect" if store.madeline_centrifuge_attempts == 1 else "recovered"
        if not _madeline_centrifuge_record_result(quality, True):
            return
        store.madeline_centrifuge_active = False
        store.madeline_centrifuge_phase = "complete"
        renpy.hide_screen("madeline_centrifuge_minigame")
        renpy.end_interaction(True)

    def madeline_centrifuge_assist():
        """Let Madeline complete the procedure without withholding evidence."""
        if not store.madeline_centrifuge_active:
            return
        if not _madeline_centrifuge_record_result("assisted", False):
            return
        store.madeline_centrifuge_active = False
        store.madeline_centrifuge_phase = "assisted"
        renpy.hide_screen("madeline_centrifuge_minigame")
        renpy.end_interaction(True)

    def abort_madeline_centrifuge_minigame():
        """Close during an external interruption without recording evidence."""
        if not store.madeline_centrifuge_active:
            return
        store.madeline_centrifuge_active = False
        store.madeline_centrifuge_phase = "aborted"
        store.madeline_centrifuge_selected_tube = ""
        renpy.hide_screen("madeline_centrifuge_minigame")
        renpy.end_interaction(False)

