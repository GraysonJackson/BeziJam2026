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
    $ ulyssesPersonalEvenings = 0
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
    $ ulyssesPersonalEvenings = 0
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
        screenshot "round2/ui_rules_card.png"

    testcase dialogue_layout:
        run Jump("UITestDialogue")
        advance until screen "say"
        pause 0.2
        screenshot "round2/ui_dialogue.png"

    testcase long_choice_layout:
        run Jump("UITestLongChoice")
        advance until screen "choice"
        pause 0.2
        screenshot "round2/ui_long_choice.png"

    testcase accusation_layout:
        $ killer = 1
        $ remainingSuspects = [1, 2, 3]
        $ daySevenAccusationPage = 0
        $ daySevenPinnedSuspect = 2
        run Jump("UITestAccusation")
        advance until screen "day_seven_accusation"
        pause 0.2
        screenshot "round2/ui_accusation.png"

    testcase save_layout:
        run Jump("UITestSave")
        advance until screen "save"
        pause 0.2
        screenshot "round2/ui_save.png"

    testcase history_layout:
        run Jump("UITestHistory")
        advance until screen "history"
        pause 0.2
        screenshot "round2/ui_history.png"

    testcase play_help_layout:
        run Jump("UITestHelp")
        advance until screen "help"
        click "Play"
        pause 0.2
        screenshot "round2/ui_play_help.png"


testsuite minigame_ui_smoke:
    testcase height_memory_layout:
        run Jump("UITestHeightMemory")
        advance until screen "height_memory_minigame"
        pause 0.2
        screenshot "round2/ui_height_memory.png"

    testcase dhampir_ispy_layout:
        run Jump("UITestDhampirISpy")
        advance until screen "dhampir_ispy_minigame"
        pause 0.2
        screenshot "round2/ui_dhampir_ispy.png"

    testcase madeline_centrifuge_layout:
        run Jump("UITestMadelineCentrifuge")
        advance until screen "madeline_centrifuge_minigame"
        pause 0.2
        screenshot "round2/ui_madeline_centrifuge.png"

    testcase nicky_memory_layout:
        run Jump("UITestNickyMemory")
        advance until screen "nicky_memory_minigame"
        pause 0.2
        screenshot "round2/ui_nicky_memory.png"

    testcase winston_pressure_layout:
        run Jump("UITestWinstonPressure")
        advance until screen "winston_pressure_minigame"
        pause 0.2
        screenshot "round2/ui_winston_pressure.png"

    testcase ica_cards_layout:
        run Jump("UITestIcaCards")
        advance until screen "ica_cards_minigame"
        pause 0.2
        screenshot "round2/ui_ica_cards.png"

    testcase ica_staring_layout:
        run Jump("UITestIcaStaring")
        advance until screen "ica_staring_minigame"
        pause 0.2
        screenshot "round2/ui_ica_staring.png"

    testcase ica_board_layout:
        run Jump("UITestIcaBoard")
        advance until screen "ica_board_game_minigame"
        pause 0.2
        screenshot "round2/ui_ica_board.png"

    testcase ica_eating_layout:
        run Jump("UITestIcaEating")
        advance until screen "ica_eating_minigame"
        pause 0.2
        screenshot "round2/ui_ica_eating.png"

    testcase ica_prank_layout:
        run Jump("UITestIcaPrank")
        advance until screen "ica_prank_minigame"
        pause 0.2
        screenshot "round2/ui_ica_prank.png"


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
    $ main_menu = False
    $ _in_replay = False
    call screen day_seven_accusation
    return


label UITestSave:
    window hide
    $ main_menu = False
    $ _in_replay = False
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


## Round 2 interaction checks use a separate screenshot directory.
init python:
    def round2_minigame_snapshot(prefix):
        import copy
        return copy.deepcopy({key: value for key, value in vars(store).items()
            if key.startswith(prefix + "_") and isinstance(value, (str, int, float, bool, list, tuple, dict))})

testsuite round2_interactions:
    before testcase:
        $ minigame_paused = False
        python:
            for _r2_screen in ("height_memory_minigame", "dhampir_ispy_minigame", "madeline_centrifuge_minigame", "nicky_memory_minigame", "winston_pressure_minigame", "ica_cards_minigame", "ica_staring_minigame", "ica_board_game_minigame", "ica_eating_minigame", "ica_prank_minigame", "minigame_pause"):
                renpy.hide_screen(_r2_screen)

    testcase height_memory_pause_resume:
        run Jump("UITestHeightMemory")
        advance until screen "height_memory_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("height_memory")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("height_memory") == _r2_frozen
        screenshot "round2/pause_height_memory.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "height_memory_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "height_memory_minigame"

    testcase dhampir_ispy_pause_resume:
        run Jump("UITestDhampirISpy")
        advance until screen "dhampir_ispy_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("dhampir_ispy")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("dhampir_ispy") == _r2_frozen
        screenshot "round2/pause_dhampir_ispy.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "dhampir_ispy_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "dhampir_ispy_minigame"

    testcase madeline_centrifuge_pause_resume:
        run Jump("UITestMadelineCentrifuge")
        advance until screen "madeline_centrifuge_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("madeline_centrifuge")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("madeline_centrifuge") == _r2_frozen
        screenshot "round2/pause_madeline_centrifuge.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "madeline_centrifuge_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "madeline_centrifuge_minigame"

    testcase nicky_memory_pause_resume:
        run Jump("UITestNickyMemory")
        advance until screen "nicky_memory_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("nicky_memory")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("nicky_memory") == _r2_frozen
        screenshot "round2/pause_nicky_memory.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "nicky_memory_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "nicky_memory_minigame"

    testcase winston_pressure_pause_resume:
        run Jump("UITestWinstonPressure")
        advance until screen "winston_pressure_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("winston_pressure")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("winston_pressure") == _r2_frozen
        screenshot "round2/pause_winston_pressure.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "winston_pressure_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "winston_pressure_minigame"

    testcase ica_cards_pause_resume:
        run Jump("UITestIcaCards")
        advance until screen "ica_cards_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("ica_cards")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("ica_cards") == _r2_frozen
        screenshot "round2/pause_ica_cards.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "ica_cards_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "ica_cards_minigame"

    testcase ica_staring_pause_resume:
        run Jump("UITestIcaStaring")
        advance until screen "ica_staring_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("ica_staring")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("ica_staring") == _r2_frozen
        screenshot "round2/pause_ica_staring.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "ica_staring_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "ica_staring_minigame"

    testcase ica_board_pause_resume:
        run Jump("UITestIcaBoard")
        advance until screen "ica_board_game_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("ica_board")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("ica_board") == _r2_frozen
        screenshot "round2/pause_ica_board.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "ica_board_game_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "ica_board_game_minigame"

    testcase ica_eating_pause_resume:
        run Jump("UITestIcaEating")
        advance until screen "ica_eating_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("ica_eating")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("ica_eating") == _r2_frozen
        screenshot "round2/pause_ica_eating.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "ica_eating_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "ica_eating_minigame"

    testcase ica_prank_pause_resume:
        run Jump("UITestIcaPrank")
        advance until screen "ica_prank_minigame"
        click "Pause / Rules"
        assert screen "minigame_pause"
        assert eval minigame_paused
        $ _r2_frozen = round2_minigame_snapshot("ica_prank")
        keysym "K_SPACE"
        keysym "K_RIGHT"
        pause 1.2
        assert eval round2_minigame_snapshot("ica_prank") == _r2_frozen
        screenshot "round2/pause_ica_prank.png"
        click "Resume Game"
        assert eval not minigame_paused
        assert screen "ica_prank_minigame"
        keysym "K_ESCAPE"
        assert screen "minigame_pause"
        keysym "K_ESCAPE"
        assert eval not minigame_paused
        assert screen "ica_prank_minigame"

    testcase accusation_menu_and_cancel:
        $ main_menu = False
        $ _in_replay = False
        $ killer = 1
        $ remainingSuspects = list(suspectNames.keys())
        run Jump("UITestAccusation")
        advance until screen "day_seven_accusation"
        click "Save / Settings"
        assert screen "save"
        keysym "K_ESCAPE"
        assert screen "day_seven_accusation"
        $ renpy.show_screen("day_seven_confirm_accusation", suspect_id=1)
        assert screen "day_seven_confirm_accusation"
        keysym "K_ESCAPE"
        assert eval not renpy.get_screen("day_seven_confirm_accusation")
        assert screen "day_seven_accusation"

    testcase stored_save_context:
        $ dayWin = 4
        $ update_save_context("NickyDayTwo")
        $ renpy.save("release-check-5")
        $ dayWin = 6
        $ update_save_context("IcaDaySix")
        assert eval renpy.slot_json("release-check-5")["case_context"] == "Day 4\nNicky · Visit 2"
        run Jump("UITestSave")
        advance until screen "save"
        screenshot "round2/save_context.png"


testsuite accessibility_and_menu_checks:
    testcase dyslexic_font_toggle:
        $ set_dyslexic_font(True)
        assert eval _preferences.font_transform == "opendyslexic"
        assert eval persistent.dyslexic_font is True
        $ set_dyslexic_font(False)
        assert eval _preferences.font_transform is None
        assert eval persistent.dyslexic_font is False

    testcase accessibility_screen_flow:
        $ main_menu = True
        $ renpy.show_screen("accessibility_prefs")
        assert screen "accessibility_prefs"
        click "OpenDyslexic"
        assert eval _preferences.font_transform == "opendyslexic"
        assert eval persistent.dyslexic_font is True
        click "Default"
        assert eval _preferences.font_transform is None
        assert eval persistent.dyslexic_font is False
        $ renpy.hide_screen("accessibility_prefs")

    testcase main_menu_screen_flow:
        $ main_menu = True
        $ renpy.show_screen("main_menu")
        assert screen "main_menu"
        pause 0.5
        assert eval renpy.get_screen("main_menu") is not None
        $ renpy.hide_screen("main_menu")
