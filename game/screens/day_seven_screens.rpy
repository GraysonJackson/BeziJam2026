## Day Seven suspect files, romantic-choice confirmation, credits, and gallery.

screen day_seven_suspect_portrait(suspect_id, size=(260, 260)):
    frame:
        xysize size
        background Solid("#d8cfb5")
        padding (10, 10)

        fixed:
            add Solid("#302923") xysize (size[0] - 20, size[1] - 20)
            text day_seven_initials(suspect_id):
                align (0.5, 0.5)
                size 86
                color "#f3ead2"
                font "fonts/MonaspaceArgon-SemiBold.otf"


screen day_seven_profile_columns(suspect_id, compact=False):
    $ attrs = suspectAttributes[suspect_id]
    $ displayed_fields = DAY_SEVEN_PROFILE_FIELDS

    $ column_length = len(displayed_fields) // 2
    hbox:
        spacing 12

        for column in range(2):
            vbox:
                spacing 10

                for field_label, field_key in displayed_fields[column * column_length:(column + 1) * column_length]:
                    vbox:
                        xsize (300 if not compact else 220)
                        spacing 2
                        text field_label.upper():
                            size (18 if not compact else 15)
                            color "#8d3027"
                            font "fonts/MonaspaceArgon-SemiBold.otf"
                        text "[attrs[field_key]]":
                            size (25 if not compact else 19)
                            color "#251d18"
                            font "fonts/MonaspaceNeon-Regular.otf"


screen day_seven_accusation():
    modal True
    zorder 180

    $ suspects = day_seven_selectable_suspects()
    $ current_id = day_seven_current_suspect()
    $ pinned_id = daySevenPinnedSuspect
    $ show_comparison = pinned_id in suspects and pinned_id != current_id

    add Solid("#171313")
    add "debriefRoomOutline" alpha 0.16

    key "game_menu" action ShowMenu("save")
    key "K_ESCAPE" action ShowMenu("save")

    frame:
        align (0.5, 0.5)
        xysize (1760, 960)
        background Solid("#efe6cc")
        padding (34, 28)

        vbox:
            spacing 16

            hbox:
                xfill True
                text "FINAL ACCUSATION — SURVIVING FILES":
                    size 42
                    color "#8d3027"
                    font "fonts/RandoSharpie.ttf"
                text "PAGE [daySevenAccusationPage + 1] / [len(suspects)]":
                    xalign 1.0
                    size 24
                    color "#654c3c"

            viewport:
                xsize 1690
                ysize 58
                mousewheel "horizontal"
                draggable True

                hbox:
                    spacing 10
                    for suspect_id in suspects:
                        textbutton suspectNames[suspect_id]:
                            action Function(day_seven_go_to_suspect, suspect_id)
                            selected suspect_id == current_id
                            text_size 22

            null height 4

            hbox:
                spacing 30

                frame:
                    xysize ((1650 if not show_comparison else 1000), 650)
                    background Solid("#fbf5e5")
                    padding (28, 22)

                    vbox:
                        spacing 18
                        hbox:
                            spacing 22
                            use day_seven_suspect_portrait(current_id, (220, 220))
                            vbox:
                                xsize (900 if not show_comparison else 680)
                                spacing 8
                                text suspectNames[current_id]:
                                    size 50
                                    color "#251d18"
                                    font "fonts/RandoWB.ttf"
                                text "ACTIVE SUSPECT FILE":
                                    size 24
                                    color "#8d3027"
                                text "Compare this profile against the evidence notebook and your personal notes. No single dramatic trait is enough.":
                                    size 22
                                    color "#654c3c"
                                    xmaximum (900 if not show_comparison else 680)

                        use day_seven_profile_columns(current_id, compact=False)

                if show_comparison:
                    frame:
                        xysize (620, 650)
                        background Solid("#e4d8bc")
                        padding (22, 22)

                        vbox:
                            spacing 13
                            text "PINNED COMPARISON":
                                size 25
                                color "#8d3027"
                            text suspectNames[pinned_id]:
                                size 36
                                color "#251d18"
                                font "fonts/RandoWB.ttf"
                            use day_seven_suspect_portrait(pinned_id, (145, 145))
                            use day_seven_profile_columns(pinned_id, compact=True)
                            textbutton "Clear Pin":
                                action Function(day_seven_toggle_pin, pinned_id)
                                text_size 21

            hbox:
                xfill True
                spacing 12

                textbutton "Previous File":
                    action Function(day_seven_change_page, -1)
                    style "day_seven_action_button"
                    xsize 190
                textbutton "Next File":
                    action Function(day_seven_change_page, 1)
                    style "day_seven_action_button"
                    xsize 170
                textbutton ("Clear Comparison" if pinned_id == current_id else "Pin for Comparison"):
                    action Function(day_seven_toggle_pin, current_id)
                    style "day_seven_action_button"
                    xsize 275
                textbutton "Evidence Notebook":
                    action Show("suspect_notebook")
                    style "day_seven_action_button"
                    xsize 260
                textbutton "Personal Notes":
                    action Show("suspect_notepad")
                    style "day_seven_action_button"
                    xsize 230
                textbutton "Accuse [suspectNames[current_id]]":
                    action Show("day_seven_confirm_accusation", suspect_id=current_id)
                    style "day_seven_accuse_button"
                    xsize 390


    textbutton "Save / Settings":
        align (0.98, 0.985)
        style "minigame_panel_button"
        action ShowMenu("save")


style day_seven_action_button:
    ysize 58
    background Solid("#e4d8bc")
    hover_background Solid("#f6d7c7")
    selected_background Solid("#d9c8a7")
    padding (14, 8)

style day_seven_action_button_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 21
    color "#00719a"
    hover_color "#d26143"
    font "fonts/MonaspaceNeon-Regular.otf"

style day_seven_accuse_button is day_seven_action_button:
    background Solid("#8d3027")
    hover_background Solid("#d26143")

style day_seven_accuse_button_text is day_seven_action_button_text:
    color "#fff4df"
    hover_color "#ffffff"


screen day_seven_confirm_accusation(suspect_id):
    modal True
    zorder 260
    key "game_menu" action Hide("day_seven_confirm_accusation")
    key "K_ESCAPE" action Hide("day_seven_confirm_accusation")

    add Solid("#000000b8")

    frame:
        align (0.5, 0.5)
        xysize (880, 760)
        background Solid("#efe6cc")
        padding (38, 34)

        vbox:
            align (0.5, 0.5)
            xsize 790
            spacing 22

            text "PROPOSED CULPRIT":
                xalign 0.5
                size 35
                color "#8d3027"
                font "fonts/RandoSharpie.ttf"
            use day_seven_suspect_portrait(suspect_id, (240, 240))
            text suspectNames[suspect_id]:
                xalign 0.5
                size 50
                color "#251d18"
                font "fonts/RandoWB.ttf"
            text "Formally accuse [suspectNames[suspect_id]] of murdering Enrico Edge?":
                xalign 0.5
                text_align 0.5
                size 28
                color "#251d18"
                xmaximum 700
            text "This decision is final for this playthrough.":
                xalign 0.5
                size 22
                color "#8d3027"

            hbox:
                xalign 0.5
                spacing 35
                textbutton "Review Again":
                    action Hide("day_seven_confirm_accusation")
                textbutton "Confirm Accusation":
                    action [Hide("day_seven_confirm_accusation"), Return(suspect_id)]


screen day_seven_partner_choice():
    modal True
    zorder 180

    add Solid("#171313")
    add "debriefRoomOutline" alpha 0.16
    key "game_menu" action ShowMenu("save")
    key "K_ESCAPE" action ShowMenu("save")

    frame:
        align (0.5, 0.5)
        xysize (1180, 940)
        background Solid("#efe6cc")
        padding (55, 42)

        vbox:
            xfill True
            spacing 15

            text "ONE FINAL CHOICE":
                xalign 0.5
                size 48
                color "#8d3027"
                font "fonts/RandoSharpie.ttf"
            text "You may speak with one person before the night ends. You cannot ask someone else if they decline.":
                xalign 0.5
                text_align 0.5
                size 25
                color "#251d18"
                xmaximum 980

            null height 12

            for partner_id, partner_name, _score_var in DAY_SEVEN_PARTNERS:
                textbutton "Spend time with [partner_name]":
                    xalign 0.5
                    xsize 850
                    action Show(
                        "day_seven_confirm_partner",
                        partner_id=partner_id,
                        partner_name=partner_name)

            null height 8

            textbutton ("Celebrate with the team as friends" if daySevenCaseSolved else "Leave without talking to anyone"):
                xalign 0.5
                xsize 850
                action Show(
                    "day_seven_confirm_partner",
                    partner_id="",
                    partner_name="no one")


    textbutton "Save / Settings":
        align (0.98, 0.985)
        style "minigame_panel_button"
        action ShowMenu("save")


screen day_seven_confirm_partner(partner_id, partner_name):
    modal True
    zorder 260
    key "game_menu" action Hide("day_seven_confirm_partner")
    key "K_ESCAPE" action Hide("day_seven_confirm_partner")

    add Solid("#000000b8")

    frame:
        align (0.5, 0.5)
        xysize (820, 430)
        background Solid("#efe6cc")
        padding (44, 36)

        vbox:
            align (0.5, 0.5)
            xsize 720
            spacing 26

            if partner_id:
                text "Spend time with [partner_name] before the night ends?":
                    xalign 0.5
                    text_align 0.5
                    size 34
                    color "#251d18"
            else:
                text ("End the night with the team?" if daySevenCaseSolved else "Leave without speaking to anyone?"):
                    xalign 0.5
                    text_align 0.5
                    size 34
                    color "#251d18"

            text "This choice is final.":
                xalign 0.5
                size 22
                color "#8d3027"

            hbox:
                xalign 0.5
                spacing 36
                textbutton "Go Back":
                    action Hide("day_seven_confirm_partner")
                textbutton "Confirm":
                    action [Hide("day_seven_confirm_partner"), Return(partner_id)]


screen ending_gallery():
    tag menu

    use game_menu(_("Endings"))

    $ unlocked = persistent.daySevenEndings or {}
    $ catalog = day_seven_ending_catalog()

    viewport:
        xpos 90
        ypos 145
        xsize 1080
        ysize 820
        mousewheel True
        draggable True
        pagekeys True
        scrollbars "vertical"

        vbox:
            xsize 1010
            spacing 15

            text "ENDING GALLERY — [len(unlocked)] / [len(catalog)]":
                size 42
                color "#E47751"
                font "fonts/RandoSharpie.ttf"

            text "Unlocked endings can be replayed. Gallery replays return here and do not replay the credits.":
                size 22
                color "#DB8D7A"
                xmaximum 1000

            for group_id, group_name in [
                    ("razzle", "RAZZLE DAZZLE"),
                    ("winston", "WINSTON"),
                    ("nicky", "NICKY"),
                    ("ica", "ICA"),
                    ("ulysses", "ULYSSES"),
                    ("madeline", "MADELINE"),
                    ("dhampir", "DHAMPIR"),
                    ("", "ATLAS TEAM & SOLO")]:
                $ group_entries = [e for e in catalog if e["partner"] == group_id]
                $ group_unlocked = [e for e in group_entries if e["key"] in unlocked]

                null height 8
                text "[group_name] — ([len(group_unlocked)]/[len(group_entries)])":
                    size 26
                    color "#E47751"
                    font "fonts/RandoSharpie.ttf"

                for entry in group_entries:
                    if entry["key"] in unlocked:
                        textbutton entry["title"]:
                            xsize 920
                            text_size 23
                            action Replay(
                                "DaySevenGalleryReplay",
                                scope={"daySevenGalleryReplayKey": entry["key"]},
                                locked=False)
                    else:
                        $ status_label = "Solved" if entry["solved"] else "Unclosed"
                        if entry["partner"] == "":
                            $ hint_text = ("Team Celebration — Case " + status_label) if entry["solved"] else ("Solo Departure — Case " + status_label)
                        elif entry["outcome"] == "romance":
                            $ hint_text = entry["title"].split(" — ")[0] + " — Romance — Case " + status_label + " (Locked: Requires romantic connection)"
                        elif entry["outcome"] == "friend":
                            $ hint_text = entry["title"].split(" — ")[0] + " — Friendship — Case " + status_label + " (Locked: Requires friendship trust)"
                        else:
                            $ hint_text = entry["title"].split(" — ")[0] + " — Professional Distance — Case " + status_label + " (Locked)"

                        frame:
                            xsize 920
                            background Solid("#2a2323aa")
                            padding (18, 12)
                            text "[hint_text]":
                                size 20
                                color "#9b8d84"


transform day_seven_credit_scroll:
    xpos 0.5
    xanchor 0.5
    ypos 1080
    linear 48.0 ypos -3800


screen day_seven_credits():
    modal True
    zorder 300

    add Solid("#090809")
    timer 48.0 action Return()
    key "dismiss" action Return()
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    vbox at day_seven_credit_scroll:
        xsize 1400
        spacing 40

        text "DATE AND DEDUCE":
            xalign 0.5
            size 78
            color "#E47751"
            font "fonts/RandoWB.ttf"
        text "A D&D Spinoff!":
            xalign 0.5
            size 42
            color "#008DBF"

        null height 100

        text "CREATED BY":
            xalign 0.5
            size 42
            color "#E47751"
            font "fonts/RandoSharpie.ttf"

        text "Grayson (\"TriUnity\") Jackson\nCode and Writing":
            xalign 0.5
            text_align 0.5
            size 34
            color "#f0d9cf"
        text "Haven (\"Rabbit\") Herring\nBackground Art":
            xalign 0.5
            text_align 0.5
            size 34
            color "#f0d9cf"
        text "AB (\"PoeBeau\") Manness\nCharacter Art":
            xalign 0.5
            text_align 0.5
            size 34
            color "#f0d9cf"

        null height 100

        text "SPECIAL THANKS":
            xalign 0.5
            size 42
            color "#E47751"
            font "fonts/RandoSharpie.ttf"
        text "Adyn\nAvagail\nBraden\nChristian\nEvan\nGeoff\nHarlowe\nJace\nRose\nRowan":
            xalign 0.5
            text_align 0.5
            size 31
            color "#f0d9cf"

        null height 80

        text "MUSIC":
            xalign 0.5
            size 42
            color "#E47751"
            font "fonts/RandoSharpie.ttf"
        text "Music by JDSherbert\nMinigame Music Pack & Nostalgia Music Pack\nhttps://jdsherbert.itch.io":
            xalign 0.5
            text_align 0.5
            size 31
            color "#f0d9cf"

        null height 80

        text "ASSET AND TOOL CREDITS":
            xalign 0.5
            size 42
            color "#E47751"
            font "fonts/RandoSharpie.ttf"
        text "Madi Wander\nFenik\nBeau Maher\nMonaspace\nRen'Py":
            xalign 0.5
            text_align 0.5
            size 31
            color "#f0d9cf"

        null height 450

    textbutton "Skip Credits":
        align (0.96, 0.94)
        action Return()
        text_size 24


screen day_seven_thanks():
    modal True
    zorder 310

    add Solid("#090809")
    timer 8.0 action MainMenu(confirm=False)
    key "dismiss" action MainMenu(confirm=False)
    key "game_menu" action MainMenu(confirm=False)

    vbox:
        align (0.5, 0.5)
        spacing 35
        text "Thank you for playing!":
            xalign 0.5
            size 72
            color "#E47751"
            font "fonts/RandoWB.ttf"
        textbutton "Return to Main Menu":
            xalign 0.5
            action MainMenu(confirm=False)
            text_size 28
