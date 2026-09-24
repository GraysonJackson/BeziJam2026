## Narrative data shared across Dhampir's six investigation visits.

define DHAMPIR_WARM_THRESHOLD = 6
define DHAMPIR_HIGH_THRESHOLD = 11

## Enrico's cause of death varies with the saved killer seed. None of these
## descriptions identifies the attacker's elemental power category.
define DHAMPIR_MURDER_CAUSES = {
    1: "a crushing strike to the chest followed by a narrow puncture through the heart",
    2: "a slim blade driven upward beneath the ribs at extremely close range",
    3: "a close-range gunshot delivered at the end of a brief struggle",
    4: "a cord pulled tight from behind until his neck fractured",
    5: "a shard of broken glass driven into the side of his throat",
    6: "the back of his skull being driven into the stone edge of the fireplace",
    7: "a short hunting bolt fired from inside the room",
    8: "his neck being broken after he was forced hard against the wall",
    9: "a thin metal spike pushed precisely between two ribs",
}

## These are intentionally descriptive rather than notebook clues. The player
## must recognize the post-killing behavior without the game naming its label.
define DHAMPIR_REACTION_SCENE_HINTS = {
    "Panicked": (
        "A side table was overturned after Enrico fell. A bloody palm struck the wrong door, "
        "and three different drawers were opened without anything being taken."
    ),
    "Calculated": (
        "Four obvious contact points were wiped after Enrico fell. The weapon was moved, "
        "the door was pulled nearly shut, and one clean route out of the room was preserved."
    ),
    "None": (
        "Nothing in the room moved after Enrico fell. The departing footprints keep the same "
        "spacing all the way to the door, without a pause to clean, search, or look back."
    ),
}

## Day 5 supplies the second unlogged hint. Each final three-person drop group
## now contains one suspect of every build, so this observation is meaningful.
define DHAMPIR_BUILD_SCENE_HINTS = {
    "Brawny": (
        "The deepest damage came from direct body force. There was no useful leverage and no "
        "long windup; whoever made it could put serious weight behind a short movement."
    ),
    "Average": (
        "The angles require ordinary reach and a balanced stance. The attacker used both body "
        "weight and technique, without relying entirely on either one."
    ),
    "Skinny": (
        "The narrow approach and improvised leverage did most of the work. A heavier attacker "
        "would have left broader impact marks, while this person avoided fighting barehanded."
    ),
}

define DHAMPIR_INJURY_EXCLUSION_TEXT = {
    "Bruised Knuckles": (
        "The scanner finds no bare-fist transfer anywhere in the struggle. The suspects whose "
        "knuckles were freshly bruised could not have received those injuries here."
    ),
    "Scuffed Hands": (
        "Every abrasive surface is clean at hand height. The suspects with freshly scuffed palms "
        "and fingers did not receive those marks inside Enrico's house."
    ),
    "None": (
        "A sharp edge beside the broken frame carries a second blood trace. The attacker could "
        "not have left this room without a fresh injury on at least one hand."
    ),
}

define DHAMPIR_DROP_EVIDENCE_TEXT = {
    "Missing Hair": (
        "a torn clump of hair wedged behind the baseboard, with enough tissue attached to show "
        "that it was ripped out during the struggle"
    ),
    "Missing Tooth": (
        "a chipped human tooth lodged behind the radiator, driven there hard enough to crack "
        "the paint beneath it"
    ),
    "Ear Chunk": (
        "a small dried piece of ear tissue caught beneath an exposed floorboard nail"
    ),
}
