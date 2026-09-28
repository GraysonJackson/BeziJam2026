## Modal investigation notebook. Showing this screen leaves the current
## dialogue interaction in place and does not advance the script.

screen suspect_notebook():
    modal True
    zorder 200

    add Solid("#00000099")

    key "game_menu" action Hide("suspect_notebook")
    key "K_ESCAPE" action Hide("suspect_notebook")

    # Outer container holding top action bar and two-page notebook
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14

        # Action buttons bar cleanly aligned to the right edge of notebook
        hbox:
            xalign 1.0
            spacing 12

            textbutton _("Write Notes"):
                style "notebook_nav_button"
                action [Hide("suspect_notebook"), Show("suspect_notepad")]

            textbutton _("Close"):
                style "notebook_close_button"
                action Hide("suspect_notebook")

        # Two-page notebook view
        hbox:
            spacing 24

            # Page 1: Suspects
            fixed:
                xysize (570, 760)
                add "gui/notebook.png" xysize (570, 760)

                vbox:
                    xpos 70
                    ypos 60
                    xsize 430
                    spacing 8

                    text _("Suspects"):
                        xalign 0.5
                        size 38
                        color "#251d18"

                    text _("[len(remainingSuspects)] remaining"):
                        xalign 0.5
                        size 22
                        color "#654c3c"

                    null height 6

                    viewport:
                        xsize 430
                        ysize 560
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox:
                            xsize 385
                            spacing 10
                            for suspect_id in sorted(suspectNames.keys()):
                                $ s_power = suspectAttributes[suspect_id]["power"]
                                $ s_build = suspectAttributes[suspect_id]["build"]
                                $ s_height = suspectAttributes[suspect_id]["height"]
                                if suspect_id in remainingSuspects:
                                    # Active suspect card with [ACTIVE] badge
                                    frame:
                                        style "suspect_card_active"
                                        vbox:
                                            spacing 2
                                            hbox:
                                                xfill True
                                                text suspectNames[suspect_id]:
                                                    size 21
                                                    bold True
                                                    color "#251d18"
                                                    xmaximum 285
                                                text _("[[ACTIVE]]"):
                                                    xalign 1.0
                                                    style "notebook_badge_active"
                                            text "[s_power] • [s_height] • [s_build]":
                                                size 16
                                                color "#00719a"
                                                xmaximum 365
                                else:
                                    # Cleared suspect card with [CLEARED] badge
                                    frame:
                                        style "suspect_card_cleared"
                                        vbox:
                                            spacing 2
                                            hbox:
                                                xfill True
                                                text "{s}[suspectNames[suspect_id]]{/s}":
                                                    size 20
                                                    color "#8d3027"
                                                    xmaximum 275
                                                text _("[[CLEARED]]"):
                                                    xalign 1.0
                                                    style "notebook_badge_cleared"
                                            text "{s}[s_power] • [s_height] • [s_build]{/s}":
                                                size 15
                                                color "#a07065"
                                                xmaximum 365

            # Page 2: Clues
            fixed:
                xysize (570, 760)
                add "gui/notebook.png" xysize (570, 760)

                vbox:
                    xpos 70
                    ypos 60
                    xsize 430
                    spacing 8

                    text _("Clues"):
                        xalign 0.5
                        size 38
                        color "#251d18"

                    null height 6

                    if investigationClues:
                        viewport:
                            xsize 430
                            ysize 560
                            mousewheel True
                            draggable True
                            scrollbars "vertical"

                            vbox:
                                xsize 385
                                spacing 14

                                for clue in investigationClues:
                                    frame:
                                        style "clue_card"
                                        vbox:
                                            spacing 4
                                            text "[clue['route']] - Visit [clue['visit']]":
                                                size 20
                                                font "fonts/MonaspaceArgon-SemiBold.otf"
                                                color "#174D60"
                                                xmaximum 365
                                            text clue["text"]:
                                                size 18
                                                color "#251d18"
                                                xmaximum 365
                                            if clue.get("eliminated_names"):
                                                text "Removed: [', '.join(clue['eliminated_names'])]":
                                                    size 16
                                                    color "#8d3027"
                                                    xmaximum 365
                    else:
                        fixed:
                            xsize 430
                            ysize 560
                            text _("No clues discovered yet."):
                                xalign 0.5
                                yalign 0.4
                                size 22
                                italic True
                                color "#654c3c"


screen suspect_notepad():
    modal True
    zorder 200

    add Solid("#00000099")

    key "game_menu" action Hide("suspect_notepad")
    key "K_ESCAPE" action Hide("suspect_notepad")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14

        # Action buttons bar aligned to notepad
        hbox:
            xalign 1.0
            spacing 12

            textbutton _("Evidence"):
                style "notebook_nav_button"
                action [Hide("suspect_notepad"), Show("suspect_notebook")]

            textbutton _("Close"):
                style "notebook_close_button"
                action Hide("suspect_notepad")

        fixed:
            xysize (700, 920)
            add "gui/notebook.png" xysize (700, 920)

            vbox:
                xpos 85
                ypos 60
                xsize 530
                spacing 12

                text _("Personal Notes"):
                    xalign 0.5
                    size 38
                    color "#251d18"

                fixed:
                    xsize 530
                    ysize 35
                    text _("Write anything you want to remember. Stored in your save."):
                        xalign 0.0
                        yalign 0.5
                        size 18
                        color "#654c3c"
                        xmaximum 410
                    text "[len(playerInvestigationNotes)]/4000":
                        xalign 1.0
                        yalign 0.5
                        size 17
                        color "#8d3027"

                frame:
                    xsize 530
                    ysize 670
                    background Solid("#ffffff33")
                    padding (12, 12)

                    viewport:
                        xsize 506
                        ysize 646
                        scrollbars "vertical"
                        mousewheel True

                        input:
                            value VariableInputValue("playerInvestigationNotes")
                            multiline True
                            length 4000
                            copypaste True
                            xmaximum 460
                            size 22
                            color "#251d18"


## Notebook UI Styles ###########################################################

style notebook_nav_button:
    background Solid("#174D60")
    hover_background Solid("#008DBF")
    padding (18, 9)

style notebook_nav_button_text:
    font "fonts/MonaspaceArgon-SemiBold.otf"
    size 20
    color "#FFFFFF"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style notebook_close_button:
    background Solid("#8D3027")
    hover_background Solid("#D26143")
    padding (18, 9)

style notebook_close_button_text:
    font "fonts/MonaspaceArgon-SemiBold.otf"
    size 20
    color "#FFFFFF"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style suspect_card_active:
    background Solid("#174D600F")
    padding (10, 8)
    xfill True

style suspect_card_cleared:
    background Solid("#8D30270D")
    padding (10, 8)
    xfill True

style clue_card:
    background Solid("#FAF6EEAA")
    padding (10, 8)
    xfill True

style notebook_badge_active:
    font "fonts/MonaspaceArgon-SemiBold.otf"
    size 14
    color "#174D60"
    bold True

style notebook_badge_cleared:
    font "fonts/MonaspaceArgon-SemiBold.otf"
    size 14
    color "#8D3027"
    bold True
