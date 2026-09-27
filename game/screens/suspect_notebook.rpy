## Modal investigation notebook. Showing this screen leaves the current
## dialogue interaction in place and does not advance the script.

screen suspect_notebook():
    modal True
    zorder 200

    add Solid("#00000099")

    key "game_menu" action Hide("suspect_notebook")

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1180, 760)
        background None

        hbox:
            spacing 24

            fixed:
                xysize (570, 760)
                add "gui/notebook.png" xysize (570, 760)

                vbox:
                    xpos 70
                    ypos 65
                    xsize 430
                    spacing 12

                    text _("Suspects"):
                        xalign 0.5
                        size 42
                        color "#251d18"

                    text _("[len(remainingSuspects)] remaining"):
                        xalign 0.5
                        size 25
                        color "#654c3c"

                    null height 8

                    viewport:
                        xsize 430
                        ysize 555
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox:
                            xsize 405
                            spacing 12
                            for suspect_id in sorted(suspectNames.keys()):
                                $ s_power = suspectAttributes[suspect_id]["power"]
                                $ s_build = suspectAttributes[suspect_id]["build"]
                                $ s_height = suspectAttributes[suspect_id]["height"]
                                if suspect_id in remainingSuspects:
                                    vbox:
                                        spacing 2
                                        text suspectNames[suspect_id]:
                                            size 24
                                            bold True
                                            color "#251d18"
                                        text "[s_power] • [s_height] • [s_build]":
                                            size 18
                                            color "#654c3c"
                                else:
                                    vbox:
                                        spacing 2
                                        text "{s}[suspectNames[suspect_id]]{/s}":
                                            size 22
                                            color "#8d3027"
                                        text "{s}[s_power] • [s_height] • [s_build]{/s} (CLEARED)":
                                            size 16
                                            color "#a07065"

            fixed:
                xysize (570, 760)
                add "gui/notebook.png" xysize (570, 760)

                vbox:
                    xpos 66
                    ypos 65
                    xsize 438
                    spacing 12

                    text _("Clues"):
                        xalign 0.5
                        size 42
                        color "#251d18"

                    if investigationClues:
                        viewport:
                            xsize 438
                            ysize 555
                            mousewheel True
                            draggable True
                            scrollbars "vertical"

                            vbox:
                                xsize 405
                                spacing 22

                                for clue in investigationClues:
                                    vbox:
                                        spacing 5
                                        text "[clue['route']] - Visit [clue['visit']]":
                                            size 25
                                            color "#654c3c"
                                        text clue["text"]:
                                            size 23
                                            color "#251d18"
                                            xmaximum 390
                                        if clue.get("eliminated_names"):
                                            text "Removed: [', '.join(clue['eliminated_names'])]":
                                                size 20
                                                color "#8d3027"
                                                xmaximum 390
                
                    else:
                        text _("No clues discovered yet."):
                            xalign 0.5
                            size 25
                            color "#654c3c"

        hbox:
            xalign 1.0
            yalign 0.0
            spacing 12

            textbutton _("Write Notes"):
                action [Hide("suspect_notebook"), Show("suspect_notepad")]

            textbutton _("Close"):
                action Hide("suspect_notebook")


screen suspect_notepad():
    modal True
    zorder 200

    add Solid("#00000099")

    key "game_menu" action Hide("suspect_notepad")

    frame:
        xalign 0.5
        yalign 0.5
        xysize (700, 930)
        background None

        add "gui/notebook.png" xysize (700, 930)

        vbox:
            xpos 88
            ypos 72
            xsize 524
            spacing 14

            text _("Personal Notes"):
                xalign 0.5
                size 42
                color "#251d18"

            text _("Write anything you want to remember. These notes are stored in your save."):
                size 22
                color "#654c3c"
                xmaximum 524

            frame:
                xsize 524
                ysize 670
                background Solid("#ffffff22")
                padding (12, 12)

                viewport:
                    xsize 500
                    ysize 646
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    input:
                        value VariableInputValue("playerInvestigationNotes")
                        multiline True
                        length 4000
                        copypaste True
                        xmaximum 480
                        size 24
                        color "#251d18"

        hbox:
            xalign 1.0
            yalign 0.0
            spacing 12

            textbutton _("Evidence"):
                action [Hide("suspect_notepad"), Show("suspect_notebook")]

            textbutton _("Close"):
                action Hide("suspect_notepad")
