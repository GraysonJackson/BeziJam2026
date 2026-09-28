## Local release verification; excluded from distributions in options.rpy.
testsuite release_checks:
    before testcase:
        $ main_menu = False
        $ _in_replay = False
        $ _preferences.text_cps = 0
        $ _test.timeout = 60.0
        $ release_check_done = False
        $ persistent._file_page = "1"
        $ renpy.scene(layer="screens")
        python:
            for test_screen in ("main_menu", "height_memory_minigame", "minigame_pause", "say", "choice"):
                renpy.hide_screen(test_screen)

    testcase all_catalog_ending_scenes:
        run Jump("ReleaseCheckEndings")
        advance until eval release_check_done
        assert eval len(release_checked_endings) == 42

    testcase all_confessions_preserve_text:
        python:
            for test_culprit in suspectNames:
                pages = day_seven_confession_pages(test_culprit)
                assert " ".join(pages) == day_seven_culprit_confession(test_culprit)
                assert max(map(len, pages)) <= 220

    testcase long_dialogue_layout:
        run Jump("ReleaseCheckLongDialogue")
        advance until screen "say"
        pause 0.2
        screenshot "release/long_dialogue.png"

    testcase save_slot_layout:
        $ persistent._file_page = "987654"
        $ dayWin = 4
        $ update_save_context("NickyDayTwo")
        $ renpy.save("987654-5")
        run Jump("UITestSave")
        advance until screen "save"
        assert id "save_slot_1"
        assert id "save_slot_2"
        assert id "save_slot_3"
        assert id "save_slot_4"
        assert id "save_slot_5"
        screenshot "release/save.png"

    testcase final_accusation_to_credits:
        $ killer = 1
        $ remainingSuspects = [1, 2, 3]
        $ recordedRouteReveals = {}
        $ investigationClues = []
        $ ulyssesCrossReportCompleted = False
        $ dayIca = 1
        $ dayRazz = 7
        $ dayDham = 1
        $ dayMads = 1
        $ dayNick = 1
        $ dayWinn = 1
        run Jump("DaySevenStart")
        advance until screen "choice"
        click "Defend the evidence chain."
        advance until screen "day_seven_accusation"
        click "Accuse Victor Veytovi"
        assert screen "day_seven_confirm_accusation"
        click "Confirm Accusation"
        advance until screen "day_seven_partner_choice"
        click "Celebrate with the team as friends"
        assert screen "day_seven_confirm_partner"
        click "Confirm"
        advance until screen "day_seven_credits"
        assert eval "success_alone" in persistent.daySevenEndings
        keysym "K_ESCAPE"
        assert screen "day_seven_thanks"

label ReleaseCheckEndings:
    $ release_checked_endings = []
    $ release_entries = day_seven_ending_catalog()
    $ release_entry_index = 0
    while release_entry_index < len(release_entries):
        $ release_entry = release_entries[release_entry_index]
        $ day_seven_setup_gallery_replay(release_entry["key"])
        call DaySevenCharacterEnding
        call DaySevenOutro
        $ assert daySevenRelationshipOutcome == release_entry["outcome"], release_entry["key"]
        $ release_checked_endings.append(release_entry["key"])
        $ release_entry_index += 1
    $ release_check_done = True
    pause
    return

label ReleaseCheckLongDialogue:
    scene cubicleOutline
    "You carry the cups to a metal table away from a noisy birthday party. After the final hole, the two of you sit outside with ice cream while the sun sinks behind the plastic castle. Madeline has written the score, wind conditions, and several complaints across every empty section of the scorecard."
    return
