## One source of rules for the opening card and the in-game pause panel.

default minigame_paused = False

define MINIGAME_RULES = {'height': ("Razzle's Rapid Recall",
            "Keep the two anchor memories that establish the attacker's height while sorting unrelated recollections aside.",
            ['Select an unrelated memory card to file it into the background.',
             'Anchor height memories must remain on the board. Selecting one causes confusion and restores a previously filed card.',
             'When the timer expires, one filed thought returns to the board. There is no failure screen; refocus and continue.'],
            'Mouse: select a card to sort it aside. The board resolves when the key height observations are isolated.'),
 'scanner': ("Madeline's Forensic Scanner",
             "Find three room details that contradict Dhampir's projected attack path.",
             ['Inspect objects in the reconstructed room.',
              'A useful contradiction turns green. A detail already explained by the '
              'reconstruction turns gray.',
              'Calibration can point toward a useful area, and Madeline can finish the scan if you '
              'want to move on.'],
             'Mouse: inspect a labeled object, request a hint, or finish the scan.'),
 'centrifuge': ("Madeline's Centrifuge Test",
                "Load all four tubes and balance Madeline's test rotor.",
                ['Select a tube, then a slot. Select a filled slot to pick its tube up again.',
                 'The tubes weigh 5g, 4g, 6g, and 3g. Aim for 9g on each side of this simplified '
                 'rotor.',
                 'Fine trim changes the left-minus-right balance by up to 2g. The effective '
                 'balance must be zero.',
                 'A vibrating run can be unlocked and retried. After a stable spin, inspect the '
                 'bands and record the result.'],
                'Mouse: select tubes, rotor slots, trim controls, and the spin button.'),
 'memory': ("Nicky's Case-File Match",
            'Match every case-file claim to the independent record that supports or corrects it.',
            ['Turn over two cards at a time. A correct pair stays visible.',
             'There are two record sets. Finish the first to continue to the second.',
             'The timer changes to review mode when it expires; it does not erase progress or '
             'change the evidence.',
             "You may briefly reveal the board, accept Nicky's hint, or let her finish."],
            'Mouse: turn over cards and use the review controls.'),
 'blackjack': ("Winston's Controlled Pressure Test",
               'Bring your pressure close to 21 without going over, then question the suspect.',
               ['Pressure draws another card. Question stands on your current total.',
                'The suspect follows dealer rules and must stand at 17 or higher.',
                'Your 21 always succeeds, even against another 21. Other ties go to the suspect.',
                'Going over 21 overwhelms the interview and resets that suspect; it never changes '
                'the case evidence.',
                'Intuition gives 3 limited reads per session. Winston can take one interview or '
                'finish the remaining set.'],
               'Mouse: choose PRESSURE to draw or QUESTION to stand.'),
 'cards': ("Ica's High-Card Hangout",
           "Predict whether your hidden card is higher or lower than Ica's visible card and finish "
           'with the higher score.',
           ['Each correct call scores one point. An incorrect call gives the point to Ica.',
            'Once per match, a Double call makes that round worth two points to whoever wins it.',
            'Equal cards lose when playing fair; flirt/cheat leeway can turn a near miss into a '
            'win. The result explains the adjustment.',
            "Tied match points use each player's highest drawn card, then their last card. A "
            'remaining tie goes to Ica when playing fair, otherwise to you.',
            'Your approach changes the assistance you receive, but Ica responds best to staying '
            'relaxed and nonchalant.'],
           'Mouse: choose Higher, Lower, or one of the one-time Double calls.'),
 'staring': ("Ica's Staring Contest",
             "Keep your focus marker inside Ica's moving target until the eye-contact meter fills.",
             ['Your focus drifts downward. Each pulse moves it toward the target in either '
              'direction.',
              'Time inside the orange target fills the success meter; time outside it does not '
              'erase completed progress.',
              'Your chosen approach changes the target speed and size.',
              'Fill the hold meter before time runs out. The contest ends early when there is no '
              'longer enough time to finish.'],
             'Mouse: click PULSE TO REFOCUS. Keyboard: Space also pulses.'),
 'board': ('Office Pawn Race',
           'Reach or pass space 12 before Ica and Winston.',
           ['On your turn, play one of the two movement cards in your hand.',
            'Landing exactly on another pawn sends that pawn back to Start. They can do the same '
            'to you.',
            'Your chosen approach may provide a one-time movement bonus that you can toggle before '
            'playing a card.',
            "Ica and Winston take their turns automatically after a short delay."],
           'Mouse: select a movement card and toggle your bonus.'),
 'eating': ("Ica's Extremely Necessary Hot Dog Contest",
            'Clear more of your tray than Ica before the timer expires.',
            ['Take Bites to make fast progress, but every bite spends stamina.',
             'Pace Yourself to recover stamina and avoid choking incidents.',
             'Flirting and cheating grant a one-time special move; playing fair relies on steady '
             'Bite and Pace rhythm.',
             'The contest ends automatically when time runs out.'],
            'Mouse: Bite, Pace Yourself, or use the special action. Keyboard: Space bites; R '
            'paces.'),
 'prank': ('Operation: Extremely Pink Office',
           'Collect the pink paint, cross the hall, and paint all three office walls without '
           "staying in Ulysses's sight.",
           ["Orange tiles show Ulysses's current line of sight. Walls block his view.",
            'Interact with the paint and each marked wall. Completed objectives become '
            'checkpoints.',
            'If spotted, Ica returns you to the latest checkpoint; finished painting remains '
            'finished.',
            'Some approaches grant one Ica assist for the current objective.'],
           "Keyboard: Arrows or WASD move; E or Space interacts; Q uses Ica's assist. On-screen "
           'buttons also work.')}

init python:
    def minigame_pause(game_id):
        if game_id not in store.MINIGAME_RULES:
            raise ValueError("Unknown minigame: {}".format(game_id))
        store.minigame_paused = True
        renpy.show_screen("minigame_pause", game_id=game_id)
        renpy.restart_interaction()

    def minigame_resume():
        store.minigame_paused = False
        renpy.hide_screen("minigame_pause")
        renpy.restart_interaction()

    def minigame_leave(game_id):
        minigame_resume()
        actions = {
            "height": abort_height_memory_minigame,
            "scanner": dhampir_ispy_abort,
            "centrifuge": madeline_centrifuge_assist,
            "memory": nicky_memory_assist,
            "blackjack": winston_pressure_assist_all,
            "cards": abort_ica_cards_minigame,
            "staring": ica_staring_abort,
            "board": ica_board_withdraw,
            "eating": ica_eating_abort,
            "prank": ica_prank_abort,
        }
        actions[game_id]()

screen minigame_controls(game_id):
    key "game_menu" action Function(minigame_pause, game_id)
    key "K_ESCAPE" action Function(minigame_pause, game_id)
    textbutton "Pause / Rules":
        align (0.98, 0.985)
        style "minigame_panel_button"
        action Function(minigame_pause, game_id)

screen minigame_pause(game_id):
    modal True
    zorder 300
    use minigame_rules(game_id, paused=True)

screen minigame_rules(game_id, paused=False):
    modal True
    zorder 300
    $ title, objective, rules, controls = MINIGAME_RULES[game_id]
    $ close_rules = Function(minigame_resume) if paused else Return()

    add Solid("#091017F2")
    key "game_menu" action close_rules
    key "K_ESCAPE" action close_rules

    frame:
        align (0.5, 0.5)
        xysize (1580, 930)
        background Solid("#F3E8D9")
        padding (50, 34)

        vbox:
            spacing 20
            text ("PAUSED — " + title if paused else title):
                size 42
                color "#8D3027"
                font "fonts/RandoWB.ttf"
                xmaximum 1460
            viewport:
                xsize 1480
                ysize 620
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                vbox:
                    xsize 1400
                    spacing 22
                    text objective:
                        style "minigame_rules_body"
                        bold True
                    for rule in rules:
                        text ("• " + rule):
                            style "minigame_rules_body"
                    text controls:
                        style "minigame_rules_body"
                        color "#005673"

            hbox:
                spacing 22
                textbutton ("Resume Game" if paused else "Start Game"):
                    style "minigame_panel_button"
                    action close_rules
                if paused:
                    textbutton ("Let partner finish" if game_id in ("height", "scanner", "centrifuge", "memory", "blackjack") else "Withdraw"):
                        style "minigame_panel_button"
                        action Function(minigame_leave, game_id)
            if paused:
                text "The game is paused while you read. Escape or right-click resumes.":
                    size 23
                    color "#453B32"

style minigame_rules_body:
    font "fonts/MonaspaceNeon-Regular.otf"
    size 28
    color "#251D18"
    xmaximum 1380

style minigame_panel_button:
    background Solid("#174D60")
    hover_background Solid("#8D3027")
    padding (20, 12)

style minigame_panel_button_text:
    font "fonts/MonaspaceArgon-SemiBold.otf"
    size 25
    color "#FFFFFF"
    hover_color "#FFFFFF"

label RulesHeightMemory:
    $ minigame_paused = False
    call screen minigame_rules("height")
    return

label RulesDhampirISpy:
    $ minigame_paused = False
    call screen minigame_rules("scanner")
    return

label RulesMadelineCentrifuge:
    $ minigame_paused = False
    call screen minigame_rules("centrifuge")
    return

label RulesNickyMemory:
    $ minigame_paused = False
    call screen minigame_rules("memory")
    return

label RulesWinstonPressure:
    $ minigame_paused = False
    call screen minigame_rules("blackjack")
    return

label RulesIcaCards:
    $ minigame_paused = False
    call screen minigame_rules("cards")
    return

label RulesIcaStaring:
    $ minigame_paused = False
    call screen minigame_rules("staring")
    return

label RulesIcaBoard:
    $ minigame_paused = False
    call screen minigame_rules("board")
    return

label RulesIcaEating:
    $ minigame_paused = False
    call screen minigame_rules("eating")
    return

label RulesIcaPrank:
    $ minigame_paused = False
    call screen minigame_rules("prank")
    return

