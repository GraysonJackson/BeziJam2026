## A consistent, readable rules card shown before every playable minigame.

screen minigame_rules(title, objective, rules, controls="", note=""):
    modal True
    zorder 300

    add Solid("#091017F2")
    add "gui/bgtile.png" alpha 0.10
    key "game_menu" action NullAction()

    frame:
        align (0.5, 0.5)
        xysize (1660, 940)
        background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
        padding (85, 60, 85, 60)

        vbox:
            xfill True
            spacing 25

            text title:
                xalign 0.5
                text_align 0.5
                size 54
                color "#D26143"
                font "fonts/RandoWB.ttf"
                xmaximum 1450

            text "HOW TO PLAY":
                xalign 0.5
                size 30
                color "#008DBF"
                bold True

            frame:
                xfill True
                background Solid("#F3E8D9EE")
                padding (48, 34)

                vbox:
                    spacing 21
                    text objective:
                        size 31
                        color "#251D18"
                        bold True
                        xmaximum 1420

                    for rule in rules:
                        hbox:
                            spacing 18
                            text "•":
                                size 29
                                color "#D26143"
                            text rule:
                                size 27
                                color "#251D18"
                                xmaximum 1320

                    if controls:
                        null height 4
                        text "CONTROLS":
                            size 24
                            color "#8D3027"
                            bold True
                        text controls:
                            size 25
                            color "#00719A"
                            xmaximum 1360

            if note:
                text note:
                    xalign 0.5
                    text_align 0.5
                    size 23
                    color "#DB8D7A"
                    xmaximum 1380

            textbutton "Start Game":
                xalign 0.5
                action Return()
                text_size 31


label RulesHeightMemory:
    call screen minigame_rules(
        "Razzle's Rapid Recall",
        "Keep the two memories that establish the attacker's height and clear the distracting thoughts.",
        [
            "Select a memory card to clear it from the board.",
            "Useful height memories must remain. Clearing one causes a setback and restores a previously cleared card.",
            "When the timer expires, one cleared distraction returns. There is no failure screen; refocus and continue.",
        ],
        "Mouse: select a card. The board resolves when enough distractions are cleared.")
    return


label RulesDhampirISpy:
    call screen minigame_rules(
        "Madeline's Forensic Scanner",
        "Find three room details that contradict Dhampir's projected attack path.",
        [
            "Inspect objects in the reconstructed room.",
            "A useful contradiction turns green. A detail already explained by the reconstruction turns gray.",
            "Calibration can point toward a useful area, and Madeline can finish the scan if you want to move on.",
        ],
        "Mouse: inspect a labeled object, request a hint, or finish the scan.")
    return


label RulesMadelineCentrifuge:
    call screen minigame_rules(
        "Madeline's Centrifuge Test",
        "Load all four tubes and make the total mass on the left match the total mass on the right.",
        [
            "Select a tube from the bank, then select a rotor slot to place it.",
            "The 6g sample must be opposed by 6g, and the 4g control must be opposed by 4g.",
            "Use fine trim only if the displayed effective balance is not zero. An unstable run can be unlocked and retried.",
            "Once the stable spin finishes, read the bands and record the result.",
        ],
        "Mouse: select tubes, rotor slots, trim controls, and the spin button.")
    return


label RulesNickyMemory:
    call screen minigame_rules(
        "Nicky's Case-File Match",
        "Match every case-file claim to the independent record that supports or corrects it.",
        [
            "Turn over two cards at a time. A correct pair stays visible.",
            "There are two record sets. Finish the first to continue to the second.",
            "The timer changes to review mode when it expires; it does not erase progress or change the evidence.",
            "You may briefly reveal the board, accept Nicky's hint, or let her finish.",
        ],
        "Mouse: turn over cards and use the review controls.")
    return


label RulesWinstonPressure:
    call screen minigame_rules(
        "Winston's Controlled Pressure Test",
        "Bring your pressure close to 21 without going over, then question the suspect.",
        [
            "Pressure draws another card. Question stands on your current total.",
            "The suspect follows dealer rules and must stand at 17 or higher.",
            "Going over 21 overwhelms the interview and resets that suspect; it never changes the seeded evidence.",
            "Intuition gives limited help. Winston can take one interview or finish the remaining set.",
        ],
        "Mouse: choose PRESSURE to draw or QUESTION to stand.")
    return


label RulesIcaCards:
    call screen minigame_rules(
        "Ica's High-Card Hangout",
        "Predict whether your hidden card is higher or lower than Ica's visible card and finish with the higher score.",
        [
            "Each correct call scores one point. An incorrect call gives the point to Ica.",
            "Once per match, a Double call makes that round worth two points to whoever wins it.",
            "Your approach changes the assistance you receive, but Ica responds best to staying relaxed and nonchalant.",
        ],
        "Mouse: choose Higher, Lower, or one of the one-time Double calls.")
    return


label RulesIcaStaring:
    call screen minigame_rules(
        "Ica's Staring Contest",
        "Keep your focus marker inside Ica's moving target until the eye-contact meter fills.",
        [
            "Your focus drifts downward. Each pulse moves it back toward the target.",
            "Time inside the orange target fills the success meter; time outside it does not erase completed progress.",
            "Your chosen approach changes the target speed and size.",
        ],
        "Mouse: click PULSE TO REFOCUS. Keyboard: Space also pulses.")
    return


label RulesIcaBoard:
    call screen minigame_rules(
        "Office Pawn Race",
        "Reach or pass space 12 before Ica and Winston.",
        [
            "On your turn, play one of the two movement cards in your hand.",
            "Landing exactly on another pawn sends that pawn back to Start. They can do the same to you.",
            "Your chosen approach may provide a one-time movement bonus that you can toggle before playing a card.",
            "Resolve Ica's and Winston's turns when prompted.",
        ],
        "Mouse: select a movement card, toggle a bonus, and resolve opponent turns.")
    return


label RulesIcaEating:
    call screen minigame_rules(
        "Ica's Extremely Necessary Hot Dog Contest",
        "Clear more of your tray than Ica before the timer expires.",
        [
            "Take Bites to make fast progress, but every bite spends stamina.",
            "Pace Yourself to recover stamina and avoid choking incidents.",
            "Your chosen approach grants one special action. Ica will also cheat during the contest.",
            "The contest ends automatically when time runs out.",
        ],
        "Mouse: Bite, Pace Yourself, or use the special action. Keyboard: Space bites; R paces.")
    return


label RulesIcaPrank:
    call screen minigame_rules(
        "Operation: Extremely Pink Office",
        "Collect the pink paint, cross the hall, and paint all three office walls without staying in Ulysses's sight.",
        [
            "Orange tiles show Ulysses's current line of sight. Walls block his view.",
            "Interact with the paint and each marked wall. Completed objectives become checkpoints.",
            "If spotted, Ica returns you to the latest checkpoint; finished painting remains finished.",
            "Some approaches grant one Ica assist for the current objective.",
        ],
        "Keyboard: Arrows or WASD move; E or Space interacts; Q uses Ica's assist. On-screen buttons also work.")
    return
