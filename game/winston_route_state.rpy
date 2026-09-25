## Winston route thresholds, remembered choices, and seeded scene descriptions.

define WINSTON_FRIENDLY_THRESHOLD = 8
define WINSTON_WARM_THRESHOLD = 18
define WINSTON_HIGH_THRESHOLD = 32

default winston_day_one_role = ""
default winston_day_one_takeout = ""
default winston_day_two_order = ""
default winston_day_two_pool = ""
default winston_day_two_calls = ""
default winston_day_two_exit = ""
default winston_day_four_interview = ""
default winston_day_four_takeout = ""
default winston_day_five_role = ""
default winston_day_five_care = ""
default winston_day_five_cleanup = ""
default winston_day_six_sequence_attempts = 0

define WINSTON_DAY_ONE_LIES = {
    1: "attending an underground boxing match under a false name",
    2: "spending the night replacing a neighbor's window before anyone learned who broke it",
    3: "losing several hours and considerably more money in an illegal card room",
    4: "helping an ex move furniture after insisting they no longer spoke",
    5: "sleeping in the stockroom of a closed restaurant after being thrown out of a party",
    6: "performing in a terrible local band under an even worse stage name",
    7: "waiting outside a veterinary clinic with an injured stray animal",
    8: "trying to retrieve a pawned family keepsake without admitting it had been pawned",
    9: "meeting a reporter who promised to keep the conversation off the record",
}

define WINSTON_ORGANIZATION_INTERVIEW_HINTS = {
    "Clean": (
        "The witness remembers the figure stopping to straighten what had been disturbed. "
        "Even under pressure, they kept their sleeves clear of the dirty surfaces and wiped "
        "one mark that nobody else had noticed."
    ),
    "Messy": (
        "The witness remembers the figure treating the room like cleanliness had never been "
        "invented. Dust transferred to their clothes, loose debris stayed underfoot, and they "
        "never once checked what they were tracking behind them."
    ),
}

define WINSTON_HAND_INTERVIEW_HINTS = {
    "Bruised Knuckles": (
        "While demonstrating the remembered posture, the witness closes one fist and indicates "
        "dark swelling across the knuckles. Winston's dart pauses against the board for half a beat."
    ),
    "Scuffed Hands": (
        "The witness drags one palm across the edge of the desk, then remembers the figure repeatedly "
        "flexing a hand as though grit had torn the skin. Winston stops smiling for half a beat."
    ),
    "None": (
        "The witness demonstrates open, steady hands without favoring either one. Nothing in the "
        "motion suggests bruising, torn skin, or pain. Winston watches without commenting."
    ),
}

define WINSTON_REACTION_RECONSTRUCTION = {
    "Panicked": (
        "The first sound is a sharp collision with the cabinet. A hurried attempt to move something "
        "ends halfway through, followed by uneven footsteps racing for the exit."
    ),
    "Calculated": (
        "The footsteps circle the room once. A drawer opens, one object is deliberately moved, and "
        "the exit follows at a measured pace only after the room has been checked."
    ),
    "None": (
        "The footsteps never change pace. There is no pause beside Enrico and no frantic search of "
        "the room—only an ordinary walk to the door, as if nothing meaningful had happened."
    ),
}

define WINSTON_REACTION_SEQUENCE_LABELS = {
    "Panicked": [
        "A hard collision breaks the silence.",
        "An attempted cleanup is abandoned.",
        "Uneven footsteps hurry for the exit.",
    ],
    "Calculated": [
        "The room is checked in a deliberate circuit.",
        "A specific object is handled and repositioned.",
        "The killer leaves at a controlled pace.",
    ],
    "None": [
        "The killer crosses the room without slowing.",
        "Nothing is checked, cleaned, or disturbed deliberately.",
        "The departure sounds completely ordinary.",
    ],
}

define WINSTON_REACTION_DISPLAY = {
    "Panicked": "Panicked",
    "Calculated": "Calculated",
    "None": "No Visible Reaction",
}
