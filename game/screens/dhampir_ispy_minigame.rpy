## Scanner-overlay I-spy screen for Dhampir's third visit.

screen dhampir_ispy_minigame():
    modal True
    zorder 250

    add "gui/bgtile.png"
    add Solid("#102F3DDD")
    key "game_menu" action Function(dhampir_ispy_abort)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 900)

        frame:
            xysize (1500, 900)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (38, 30, 38, 30)

        text _("Madeline's Forensic Scanner") style "dhampir_ispy_title":
            xpos 0
            ypos 0
            xsize 1424

        text _("Find three details that contradict Dhampir's projected attack path.") style "dhampir_ispy_subtitle":
            xpos 0
            ypos 58
            xsize 1424

        frame:
            xpos 38
            ypos 125
            xsize 940
            ysize 615
            background Solid("#173E4BEF")
            padding (22, 22, 22, 22)

            fixed:
                frame:
                    xpos 18
                    ypos 20
                    xsize 850
                    ysize 530
                    background Solid("#D8EEE822")

                frame:
                    xpos 250
                    ypos 205
                    xsize 380
                    ysize 150
                    background Solid("#A9D6D522")

                frame:
                    xpos 35
                    ypos 455
                    xsize 790
                    ysize 10
                    background Solid("#6EB7B4AA")

                text _("SCANNER LAYER: CONTACT / WOUND OVERLAY") style "dhampir_ispy_scan_label":
                    xpos 190
                    ypos 475
                    xsize 500

                for target_id, target_label, target_x, target_y in DHAMPIR_ISPY_TARGET_LAYOUT:
                    textbutton "[dhampir_ispy_target_text(target_id, target_label)]":
                        xpos target_x
                        ypos target_y
                        xsize 125
                        ysize 76
                        text_style "dhampir_ispy_target_text"
                        background Solid(dhampir_ispy_target_color(target_id))
                        hover_background Solid("#D26143")
                        sensitive dhampir_ispy_phase == "active" and target_id not in dhampir_ispy_inspected_targets
                        action Function(dhampir_ispy_inspect, target_id)

        frame:
            xpos 1010
            ypos 125
            xsize 390
            ysize 615
            background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
            padding (28, 24, 28, 24)

            vbox:
                spacing 17
                text _("SCAN STATUS") style "dhampir_ispy_hud_heading"
                text _("Useful details: [len(dhampir_ispy_found_targets)] / [DHAMPIR_ISPY_REQUIRED_FINDS]") style "dhampir_ispy_hud_body"
                text _("False leads: [dhampir_ispy_mistakes]") style "dhampir_ispy_hud_body"
                text _("Scanner hints: [dhampir_ispy_hints_used]") style "dhampir_ispy_hud_body"

                null height 8
                text _("Inspect objects in the projected room. A useful contradiction turns green; an explained detail becomes gray.") style "dhampir_ispy_hint"

                if dhampir_ispy_phase == "active":
                    textbutton _("CALIBRATE HINT") action Function(dhampir_ispy_hint)
                elif dhampir_ispy_phase == "complete_pending":
                    text _("The reconstruction is complete.") style "dhampir_ispy_hud_body"
                    textbutton _("FINISH SCAN") action Function(finish_dhampir_ispy_minigame)

        text _("[dhampir_ispy_feedback]") style "dhampir_ispy_feedback":
            xpos 90
            ypos 770
            xsize 1320

        textbutton _("Let Madeline finish"):
            xpos 1220
            ypos 35
            action Function(dhampir_ispy_abort)

style dhampir_ispy_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 44

style dhampir_ispy_subtitle:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 24

style dhampir_ispy_scan_label:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#8DD4D0"
    size 18

style dhampir_ispy_target_text:
    is button_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#FFFFFF"
    insensitive_color "#DDE8E8"
    size 16
    bold True

style dhampir_ispy_hud_heading:
    is gui_text
    color "#D26143"
    size 28
    bold True

style dhampir_ispy_hud_body:
    is gui_text
    color "#00719A"
    size 22

style dhampir_ispy_hint:
    is gui_text
    color "#4D6570"
    size 19

style dhampir_ispy_feedback:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 26
