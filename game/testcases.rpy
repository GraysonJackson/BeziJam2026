## Automated structural checks. Run with the Ren'Py SDK's `test` command.

testsuite investigation_validation:
    testcase every_six_day_route_mix:
        $ validate_investigation_routes()

    testcase winston_pressure_model:
        $ validate_winston_pressure_rules()

    testcase ulysses_evening_model:
        $ validate_ulysses_evening_model()

    testcase day_seven_model:
        $ validate_day_seven_model()

testcase ulysses_first_evening_flow:
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ investigationClues = []
    $ recordedClueKeys = []
    $ recordedRouteReveals = {}
    $ dayWin = 1
    $ dayRazz = 2
    $ dayDham = 1
    $ dayMads = 1
    $ dayNick = 1
    $ dayWinn = 1
    $ dayIca = 1
    $ spendRazz = True
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWin = False
    $ spendIca = False

    run Jump("UlyssesEvening")
    advance until screen "choice"
    click "Emphasize that Razzle slowed down for the witness."
    advance until screen "choice"
    click "Stay a little longer after the report."
    advance until screen "choice"
    click "Offer to help organize tomorrow's work."
    advance until screen "choice"
    click "Take a pineapple slice and keep working beside him."
    advance until screen "choice"
    click "Tell him the vest looks good on him."
    advance until screen "choice"

testcase ulysses_first_evening_relaxed_flow:
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ investigationClues = []
    $ recordedClueKeys = []
    $ recordedRouteReveals = {}
    $ dayWin = 1
    $ dayRazz = 2
    $ dayDham = 1
    $ dayMads = 1
    $ dayNick = 1
    $ dayWinn = 1
    $ dayIca = 1
    $ spendRazz = True
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWin = False
    $ spendIca = False

    run Jump("UlyssesEvening")
    advance until screen "choice"
    click "Say the witness gave you a name to remove."
    advance until screen "choice"
    click "Stay a little longer after the report."
    advance until screen "choice"
    click "Say the report is finished and relax in the guest chair."
    advance until screen "choice"
    click "Take another slice and ask about the photographs on his desk."
    advance until screen "choice"
    click "Ask for permission to leave."


testsuite ui_layout_smoke:
    testcase rules_card_layout:
        run Jump("UITestRulesCard")
        advance until screen "minigame_rules"
        pause 0.2
        screenshot "ui_rules_card.png"

    testcase dialogue_layout:
        run Jump("UITestDialogue")
        advance until screen "say"
        pause 0.2
        screenshot "ui_dialogue.png"

    testcase long_choice_layout:
        run Jump("UITestLongChoice")
        advance until screen "choice"
        pause 0.2
        screenshot "ui_long_choice.png"

    testcase accusation_layout:
        $ killer = 1
        $ remainingSuspects = [1, 2, 3]
        $ daySevenAccusationPage = 0
        $ daySevenPinnedSuspect = 2
        run Jump("UITestAccusation")
        advance until screen "day_seven_accusation"
        pause 0.2
        screenshot "ui_accusation.png"

    testcase save_layout:
        run Jump("UITestSave")
        advance until screen "save"
        pause 0.2
        screenshot "ui_save.png"

    testcase history_layout:
        run Jump("UITestHistory")
        advance until screen "history"
        pause 0.2
        screenshot "ui_history.png"

    testcase play_help_layout:
        run Jump("UITestHelp")
        advance until screen "help"
        click "Play"
        pause 0.2
        screenshot "ui_play_help.png"


testsuite minigame_ui_smoke:
    testcase height_memory_layout:
        run Jump("UITestHeightMemory")
        advance until screen "height_memory_minigame"
        pause 0.2
        screenshot "ui_height_memory.png"

    testcase dhampir_ispy_layout:
        run Jump("UITestDhampirISpy")
        advance until screen "dhampir_ispy_minigame"
        pause 0.2
        screenshot "ui_dhampir_ispy.png"

    testcase madeline_centrifuge_layout:
        run Jump("UITestMadelineCentrifuge")
        advance until screen "madeline_centrifuge_minigame"
        pause 0.2
        screenshot "ui_madeline_centrifuge.png"

    testcase nicky_memory_layout:
        run Jump("UITestNickyMemory")
        advance until screen "nicky_memory_minigame"
        pause 0.2
        screenshot "ui_nicky_memory.png"

    testcase winston_pressure_layout:
        run Jump("UITestWinstonPressure")
        advance until screen "winston_pressure_minigame"
        pause 0.2
        screenshot "ui_winston_pressure.png"

    testcase ica_cards_layout:
        run Jump("UITestIcaCards")
        advance until screen "ica_cards_minigame"
        pause 0.2
        screenshot "ui_ica_cards.png"

    testcase ica_staring_layout:
        run Jump("UITestIcaStaring")
        advance until screen "ica_staring_minigame"
        pause 0.2
        screenshot "ui_ica_staring.png"

    testcase ica_board_layout:
        run Jump("UITestIcaBoard")
        advance until screen "ica_board_game_minigame"
        pause 0.2
        screenshot "ui_ica_board.png"

    testcase ica_eating_layout:
        run Jump("UITestIcaEating")
        advance until screen "ica_eating_minigame"
        pause 0.2
        screenshot "ui_ica_eating.png"

    testcase ica_prank_layout:
        run Jump("UITestIcaPrank")
        advance until screen "ica_prank_minigame"
        pause 0.2
        screenshot "ui_ica_prank.png"


label UITestRulesCard:
    window hide
    call RulesWinstonPressure from _call_RulesWinstonPressure_1
    return


label UITestDialogue:
    window hide
    $ _preferences.text_cps = 0
    u "This is a deliberately long line used to verify that dialogue remains inside the readable textbox area, wraps cleanly, and never disappears beyond the right edge of a sixteen-by-nine display."
    return


label UITestLongChoice:
    window hide
    menu:
        "Review the witness statement and compare it against the physical timeline.":
            return
        "Check the laboratory findings before drawing a conclusion.":
            return
        "Compare the suspect profiles against your personal notes.":
            return
        "Ask whether the behavioral clue agrees with the formal evidence.":
            return
        "Re-read the scene report for details that were not formally logged.":
            return
        "Verify the chain of custody one final time.":
            return
        "Look for contradictions between two surviving profiles.":
            return
        "Use intuition only as a direction, not as proof.":
            return
        "Return to the complete evidence chain.":
            return


label UITestAccusation:
    window hide
    call screen day_seven_accusation
    return


label UITestSave:
    window hide
    call screen save
    return


label UITestHistory:
    python:
        _history_list[:] = []
        for speaker, dialogue, color in [
            ("Razzle Dazzle", "This entry is deliberately long because the log needs to wrap character dialogue while keeping a long speaker name legible inside the notebook margins.", "#5C9D54"),
            ("Ulysses", "The report can wait until you have finished that sentence. I am not going anywhere.", "#4C6B9C"),
            (None, "For once, the office settles into an easy silence.", "#b87160"),
        ]:
            entry = renpy.character.HistoryEntry()
            entry.who = speaker
            entry.what = dialogue
            entry.who_args = {"color": color}
            entry.what_args = {}
            _history_list.append(entry)
    window hide
    call screen history
    return


label UITestHelp:
    window hide
    call screen help
    return


label UITestHeightMemory:
    window hide
    $ renpy.random.seed(20260925)
    $ start_height_memory_minigame()
    pause
    return


label UITestDhampirISpy:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ start_dhampir_ispy_minigame("Bruised Knuckles")
    return


label UITestMadelineCentrifuge:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ recordedRouteReveals = {}
    $ start_madeline_centrifuge_minigame()
    return


label UITestNickyMemory:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ recordedRouteReveals = {}
    $ start_nicky_memory_minigame()
    return


label UITestWinstonPressure:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ recordedRouteReveals = {}
    $ start_winston_pressure_minigame()
    return


label UITestIcaCards:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ start_ica_cards_minigame("play_fair")
    return


label UITestIcaStaring:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ start_ica_staring_minigame("play_fair")
    return


label UITestIcaBoard:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ start_ica_board_game_minigame("play_fair")
    return


label UITestIcaEating:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ start_ica_eating_minigame("play_fair", "call_out")
    return


label UITestIcaPrank:
    window hide
    $ renpy.hide_screen("height_memory_minigame")
    $ renpy.random.seed(20260925)
    $ start_ica_prank_minigame("play_fair")
    return
