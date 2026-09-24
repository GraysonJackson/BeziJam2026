## Madeline's scanner-assisted I-spy reconstruction for Dhampir's third visit.

define DHAMPIR_ISPY_REQUIRED_FINDS = 3

define DHAMPIR_ISPY_TARGET_LAYOUT = (
    ("plaster", "CRACKED\nPLASTER", 76, 82),
    ("window", "WINDOW\nLATCH", 610, 58),
    ("lamp", "LAMP\nBASE", 345, 172),
    ("table", "TABLE\nEDGE", 550, 270),
    ("frame", "BROKEN\nFRAME", 105, 350),
    ("blood", "BLOOD\nSMEAR", 405, 420),
    ("chair", "CHAIR\nLEG", 695, 390),
    ("rug", "FOLDED\nRUG", 260, 480),
    ("door", "DOOR\nHANDLE", 785, 205),
)

define DHAMPIR_ISPY_VALID_TARGETS = {
    "Bruised Knuckles": ("plaster", "lamp", "table"),
    "Scuffed Hands": ("window", "rug", "door"),
    "None": ("frame", "blood", "chair"),
}

define DHAMPIR_ISPY_VALID_FEEDBACK = {
    "Bruised Knuckles": {
        "plaster": "The plaster mark is rounded. Madeline matches it to the lamp, not a fist.",
        "lamp": "The lamp base carries plaster dust from the wall indentation.",
        "table": "Dust along the table edge is intact. No knuckles struck it.",
    },
    "Scuffed Hands": {
        "window": "The window latch is dusty and untouched; nobody scraped a hand climbing through.",
        "rug": "The drag path stops before the rug's abrasive backing.",
        "door": "The handle has blood transfer, but no skin or friction trace from a scuffed palm.",
    },
    "None": {
        "frame": "A jagged frame edge carries a second blood source from the attacker.",
        "blood": "The smaller smear travels away from Enrico's blood pool toward the exit.",
        "chair": "A sharp chair fitting holds a tiny piece of skin that did not belong to Enrico.",
    },
}

define DHAMPIR_ISPY_DECOY_FEEDBACK = {
    "plaster": "Dhampir: Wall lost that fight, but the mark fits this path.",
    "window": "Madeline: The latch is consistent. Dhampir: Window's innocent. Probably.",
    "lamp": "Dhampir: Displaced, not useful. The lamp's just dramatic.",
    "table": "Madeline: It confirms the room's layout, not the injury pattern.",
    "frame": "Dhampir: Enrico broke that during this path. Keep looking.",
    "blood": "Madeline: That portion of the smear is already accounted for.",
    "chair": "Dhampir: It moved, but it isn't contradicting anything. Rude of it.",
    "rug": "Dhampir: Suspicious-looking rug. Completely innocent rug.",
    "door": "Madeline: The handle is consistent with the projected movement.",
}

default dhampir_ispy_active = False
default dhampir_ispy_phase = "idle"
default dhampir_ispy_excluded_injuries = ""
default dhampir_ispy_valid_targets = []
default dhampir_ispy_inspected_targets = []
default dhampir_ispy_found_targets = []
default dhampir_ispy_mistakes = 0
default dhampir_ispy_hints_used = 0
default dhampir_ispy_hint_target = ""
default dhampir_ispy_feedback = ""
default dhampir_ispy_result = {}

init python:
    def _dhampir_ispy_reset(excluded_injuries):
        if excluded_injuries not in store.DHAMPIR_ISPY_VALID_TARGETS:
            raise Exception("Unknown Dhampir I-spy injury group: {}".format(
                excluded_injuries))

        store.dhampir_ispy_active = True
        store.dhampir_ispy_phase = "active"
        store.dhampir_ispy_excluded_injuries = excluded_injuries
        store.dhampir_ispy_valid_targets = list(
            store.DHAMPIR_ISPY_VALID_TARGETS[excluded_injuries])
        store.dhampir_ispy_inspected_targets = []
        store.dhampir_ispy_found_targets = []
        store.dhampir_ispy_mistakes = 0
        store.dhampir_ispy_hints_used = 0
        store.dhampir_ispy_hint_target = ""
        store.dhampir_ispy_feedback = (
            "Inspect the room and find three details that do not fit Dhampir's current reconstruction.")
        store.dhampir_ispy_result = {}

    def start_dhampir_ispy_minigame(excluded_injuries):
        """Reset the scanner scene and open its modal inspection screen."""
        _dhampir_ispy_reset(excluded_injuries)
        renpy.call_screen("dhampir_ispy_minigame")

    def dhampir_ispy_inspect(target_id):
        """Inspect one scene object and record a useful find or a harmless mistake."""
        if not store.dhampir_ispy_active or store.dhampir_ispy_phase != "active":
            return
        known_targets = [item[0] for item in store.DHAMPIR_ISPY_TARGET_LAYOUT]
        if target_id not in known_targets:
            raise Exception("Unknown Dhampir I-spy target: {}".format(target_id))
        if target_id in store.dhampir_ispy_inspected_targets:
            return

        inspected = list(store.dhampir_ispy_inspected_targets)
        inspected.append(target_id)
        store.dhampir_ispy_inspected_targets = inspected
        store.dhampir_ispy_hint_target = ""

        if target_id in store.dhampir_ispy_valid_targets:
            found = list(store.dhampir_ispy_found_targets)
            found.append(target_id)
            store.dhampir_ispy_found_targets = found
            store.dhampir_ispy_feedback = (
                store.DHAMPIR_ISPY_VALID_FEEDBACK[
                    store.dhampir_ispy_excluded_injuries][target_id])
        else:
            store.dhampir_ispy_mistakes += 1
            store.dhampir_ispy_feedback = store.DHAMPIR_ISPY_DECOY_FEEDBACK[target_id]

        if len(store.dhampir_ispy_found_targets) >= store.DHAMPIR_ISPY_REQUIRED_FINDS:
            store.dhampir_ispy_phase = "complete_pending"
            store.dhampir_ispy_feedback = (
                "All three inconsistencies found. Madeline can combine the scanner layers.")
        renpy.restart_interaction()

    def dhampir_ispy_hint():
        """Highlight one unresolved useful object without blocking completion."""
        if not store.dhampir_ispy_active or store.dhampir_ispy_phase != "active":
            return
        remaining = [
            target_id for target_id in store.dhampir_ispy_valid_targets
            if target_id not in store.dhampir_ispy_found_targets
        ]
        if not remaining:
            return
        store.dhampir_ispy_hints_used += 1
        store.dhampir_ispy_hint_target = remaining[0]
        store.dhampir_ispy_feedback = (
            "Madeline narrows the scanner field. One useful object is now highlighted.")
        renpy.restart_interaction()

    def dhampir_ispy_target_color(target_id):
        if target_id in store.dhampir_ispy_found_targets:
            return "#58A88A"
        if (target_id in store.dhampir_ispy_inspected_targets
                and target_id not in store.dhampir_ispy_valid_targets):
            return "#596B78"
        if target_id == store.dhampir_ispy_hint_target:
            return "#D7A84C"
        return "#274E5D"

    def dhampir_ispy_target_text(target_id, base_label):
        if target_id in store.dhampir_ispy_found_targets:
            return base_label + "\nFOUND"
        if target_id in store.dhampir_ispy_inspected_targets:
            return base_label + "\nCLEARED"
        return base_label

    def finish_dhampir_ispy_minigame():
        """Record performance and return to the guaranteed evidence scene."""
        if (not store.dhampir_ispy_active
                or store.dhampir_ispy_phase != "complete_pending"):
            return

        if store.dhampir_ispy_mistakes == 0 and store.dhampir_ispy_hints_used == 0:
            quality = "perfect"
        elif store.dhampir_ispy_mistakes <= 2:
            quality = "careful"
        else:
            quality = "messy"

        store.dhampir_ispy_result = {
            "completed": True,
            "quality": quality,
            "mistakes": store.dhampir_ispy_mistakes,
            "hints_used": store.dhampir_ispy_hints_used,
            "found": list(store.dhampir_ispy_found_targets),
        }
        store.dhampir_ispy_phase = "complete"
        store.dhampir_ispy_active = False
        renpy.hide_screen("dhampir_ispy_minigame")
        renpy.end_interaction(True)

    def dhampir_ispy_abort():
        """Let Madeline finish the scan without withholding the route evidence."""
        if not store.dhampir_ispy_active:
            return
        store.dhampir_ispy_result = {
            "completed": False,
            "quality": "assisted",
            "mistakes": store.dhampir_ispy_mistakes,
            "hints_used": store.dhampir_ispy_hints_used,
            "found": list(store.dhampir_ispy_found_targets),
        }
        store.dhampir_ispy_phase = "aborted"
        store.dhampir_ispy_active = False
        renpy.hide_screen("dhampir_ispy_minigame")
        renpy.end_interaction(True)
