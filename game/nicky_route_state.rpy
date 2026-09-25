## Nicky route thresholds and seed-dependent physical evidence descriptions.

define NICKY_FRIENDLY_THRESHOLD = 7
define NICKY_WARM_THRESHOLD = 15
define NICKY_HIGH_THRESHOLD = 30

default nicky_day_two_route = ""
default nicky_day_two_music = ""
default nicky_day_two_order = ""
default nicky_day_five_break_mood = ""

define NICKY_BUILD_RECORD_DESCRIPTIONS = {
    "Skinny": "a narrow shoulder-to-height ratio",
    "Average": "a middle-range shoulder-to-height ratio",
    "Brawny": "a broad shoulder-to-height ratio",
}

define NICKY_WOUND_SCENE_HINTS = {
    "Bruised Knuckles": (
        "One enlarged photograph shows a compact blood transfer surrounded by repeated impact marks. The pattern begins at bare-hand height and stops where someone pulled away from the wall."
    ),
    "Scuffed Hands": (
        "Grit and a second blood source streak along the broken window edge. The transfer runs in the direction of someone catching an exposed palm and dragging it free."
    ),
    "None": (
        "The reconstructed path accounts for every transfer through clothing, projected force, or displaced furniture. Nothing indicates that the attacker struck or braced with bare hands."
    ),
}

define NICKY_BLOOD_REACTION_TEXT = {
    "A+": (
        "The Anti-A well clouds immediately. Anti-B remains clear. A slower reaction appears in the Anti-D control."
    ),
    "A-": (
        "The Anti-A well clouds immediately. Anti-B and the Anti-D control remain clear."
    ),
    "B+": (
        "The Anti-B well clouds immediately. Anti-A remains clear. A slower reaction appears in the Anti-D control."
    ),
    "B-": (
        "The Anti-B well clouds immediately. Anti-A and the Anti-D control remain clear."
    ),
    "O+": (
        "The Anti-A and Anti-B wells remain clear. Only the Anti-D control develops a reaction."
    ),
    "O-": (
        "The Anti-A, Anti-B, and Anti-D wells all remain clear."
    ),
}

define NICKY_HYGIENE_PROFILE_TEXT = {
    "Clean": (
        "The attacker washed immediately and repeatedly. Diluted antiseptic remains beneath the dried blood, and the selective wiping follows the same meticulous grooming habits visible throughout the lawful interview and booking records."
    ),
    "Messy": (
        "Old dirt, skin oil, and fresh scene debris overlap in the recovered trace. The same disregard for personal cleanliness appears consistently throughout the lawful interview and booking records."
    ),
}
