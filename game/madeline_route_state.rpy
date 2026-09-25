## Madeline route thresholds and seed-dependent forensic descriptions.

define MADELINE_WARM_THRESHOLD = 15
define MADELINE_HIGH_THRESHOLD = 27

default madeline_ice_cream_choice = ""
default madeline_prototype_watch = ""

define MADELINE_WOUND_SCENE_HINTS = {
    "Bruised Knuckles": (
        "The contact wounds overlap in a tight bare-handed pattern. Tiny bone and protein traces remain where the attacker repeatedly closed distance, the sort of exchange neither participant's hands would leave unmarked."
    ),
    "Scuffed Hands": (
        "Grit from the damaged wall appears inside two of Enrico's defensive cuts. The attack path only makes sense if the other person caught and dragged a hand along that rough surface while forcing their power through the struggle."
    ),
    "None": (
        "Every secondary wound can be explained by projected energy and displaced objects. The attacker never needed to brace, punch, or drag bare skin across anything in the room."
    ),
}

define MADELINE_ORGANIZATION_SCENE_HINTS = {
    "Clean": (
        "The remaining residue stops at several unnaturally neat boundaries. Loose grit has been removed from the places a hurried person would never think to wipe, while the useful trace survives only inside the wound itself."
    ),
    "Messy": (
        "Dust, fabric fibers, and flecks of dried blood overlap without any consistent order. Whoever handled the scene ground fresh dirt into the trace and left every accidental transfer exactly where it fell."
    ),
}

define MADELINE_POWER_RESIDUE_TEXT = {
    "Fire": (
        "The damaged proteins carry a repeating thermal signature: heat introduced from inside the contact point rather than from an ordinary flame."
    ),
    "Ice": (
        "The tissue contains uniform microfractures left by water crystallizing almost instantly, far faster than any environmental freezing could produce."
    ),
    "Light": (
        "The sample shows patterned photochemical bleaching beneath the surface, where no ordinary lamp or flash could have reached."
    ),
}
