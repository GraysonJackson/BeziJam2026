## Razzle route thresholds. Minor activity choices now carry small relationship
## changes, so the route gates expect sustained compatibility across the week.

define RAZZLE_EARLY_THRESHOLD = 6
define RAZZLE_WARM_THRESHOLD = 16
define RAZZLE_HIGH_THRESHOLD = 30
define RAZZLE_DATE_ACCEPT_THRESHOLD = 40

default razzle_day_two_pizza = ""
default razzle_day_two_detour = ""

define RAZZLE_UNIQUE_ID_WITNESS_TEXT = {
    "Mole": "They definitely didn't have a mole on their face.",
    "Glasses": "They definitely weren't wearing glasses.",
    "Missing Arm": "They had both arms. I would remember otherwise.",
    "Scar": "I never saw a visible scar anywhere on their face.",
    "Birthmark": "There wasn't a visible birthmark on their face or neck.",
    "Tattoos": "I didn't see any visible tattoos.",
    "Piercings": "They weren't wearing any visible piercings.",
    "Eye Patch": "They definitely weren't wearing an eye patch.",
    "Vitiligo": "I didn't see any patches of vitiligo on the skin that was visible.",
}

## These are deliberately phrased as witness observations rather than formal
## database labels. They distinguish the three suspects left by Visit 6 hair
## evidence without entering either detail into the notebook.
define RAZZLE_BUILD_SCENE_HINTS = {
    "Brawny": "When the bundle slipped, their coat pulled tight across the shoulders. Even without what they were carrying, they looked solid through the upper body.",
    "Average": "When the bundle shifted, their coat settled normally again. They weren't especially broad or especially slight once I could separate them from what they carried.",
    "Skinny": "When the bundle slipped, I saw how loosely the coat hung from their shoulders. The thing in their arms was what made them look broad.",
}

define RAZZLE_REACTION_SCENE_HINTS = {
    "Calculated": {
        "action": "The figure stops beneath the grocery awning, checks both ends of the street, and wipes the place where their sleeve brushed the wall before continuing.",
        "razzle": "That isn't somebody just running. They stop, check, clean up, then pick the quietest direction. They're thinking through every move.",
    },
    "Panicked": {
        "action": "The figure clips a sidewalk sign, recoils from the noise, and breaks into an uneven run without looking back at what they struck.",
        "razzle": "Whoa. They are losing it. No plan, no cleanup—just bounce off something and keep going before their brain catches up.",
    },
    "None": {
        "action": "The figure keeps the same unhurried pace past the wall, never checking behind them and never changing course when a car turns onto the block.",
        "razzle": "They just walk away. No rush, no checking over a shoulder, nothing. Like leaving that house didn't shake them at all.",
    },
}
