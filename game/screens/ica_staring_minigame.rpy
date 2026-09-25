## Modal approach picker and fishing-bar-style Ica staring contest.

screen ica_staring_minigame():
    modal True
    zorder 250

    add "gui/bgtile.png"
    add Solid("#172C3C66")
    key "game_menu" action Function(ica_staring_abort)

    if ica_staring_phase == "active":
        timer ICA_STARING_TICK_INTERVAL repeat True action Function(ica_staring_tick)
        key "K_SPACE" action Function(ica_staring_click)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 900)

        frame:
            xysize (1500, 900)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (50, 38, 50, 38)

        if ica_staring_phase == "approach":
            vbox:
                xalign 0.5
                yalign 0.5
                xsize 1260
                spacing 18

                text _("Ica's Staring Contest") style "ica_staring_title"
                text _("Choose how you want to play.") style "ica_staring_body"

                hbox:
                    xalign 0.5
                    spacing 35

                    frame:
                        xsize 375
                        ysize 250
                        background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                        padding (24, 22, 24, 20)
                        vbox:
                            spacing 12
                            textbutton _("Play It Cool") action Function(ica_staring_choose_approach, "play_fair")
                            text _("No tricks or performance. Face Ica straight on with no difficulty reduction.") style "ica_staring_hint"

                    frame:
                        xsize 375
                        ysize 250
                        background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                        padding (24, 22, 24, 20)
                        vbox:
                            spacing 12
                            textbutton _("Flirt") action Function(ica_staring_choose_approach, "flirt")
                            text _("Keep eye contact while teasing her with distracting banter. Small difficulty reduction.") style "ica_staring_hint"

                    frame:
                        xsize 375
                        ysize 250
                        background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                        padding (24, 22, 24, 20)
                        vbox:
                            spacing 12
                            textbutton _("Get Cheeky") action Function(ica_staring_choose_approach, "cheat")
                            text _("Use Ica's reflection to steal blinks. Large difficulty reduction.") style "ica_staring_hint"

                textbutton _("Back out") action Function(ica_staring_abort):
                    xalign 0.5

        elif ica_staring_phase == "active":
            text _("Ica's Staring Contest") style "ica_staring_title":
                ypos 2
                xsize 1400

            text _("Approach: [ica_staring_approach_label(ica_staring_approach)]   |   Difficulty reduction: [ica_staring_difficulty_reduction]") style "ica_staring_status":
                ypos 70
                xsize 1400

            frame:
                xpos 625
                ypos 210
                xsize 250
                ysize 530
                background Solid("#243846")
                padding (0, 0, 0, 0)

            frame:
                xpos 646
                ypos 230
                xsize 208
                ysize 490
                background Solid("#DCE3D8")
                padding (0, 0, 0, 0)

            frame:
                xpos 630
                ypos (ICA_STARING_TRACK_TOP + int((ICA_STARING_NORMALIZED_MAX - ica_staring_target_position) * ICA_STARING_TRACK_HEIGHT) - int(ica_staring_target_half_size * ICA_STARING_TRACK_HEIGHT))
                xsize 240
                ysize max(52, int(ica_staring_target_half_size * 2 * ICA_STARING_TRACK_HEIGHT))
                background Solid("#D8784F")
                padding (6, 4, 6, 4)
                text _("ICA'S TARGET"):
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color "#FFFFFF"
                    bold True

            frame:
                xpos 630
                ypos (ICA_STARING_TRACK_TOP + int((ICA_STARING_NORMALIZED_MAX - ica_staring_player_position) * ICA_STARING_TRACK_HEIGHT) - 18)
                xsize 240
                ysize 36
                background Solid("#157A9A")
                padding (4, 2, 4, 2)
                text _("YOU"):
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color "#FFFFFF"
                    bold True

            text _("TARGET"):
                xpos 370
                ypos 330
                xsize 220
                size 24
                color "#D8784F"
                text_align 1.0

            text _("YOUR FOCUS"):
                xpos 370
                ypos 390
                xsize 220
                size 24
                color "#157A9A"
                text_align 1.0

            text _("[ica_staring_feedback]") style "ica_staring_feedback":
                ypos 760
                xsize 1300

            text _("Eye contact: [int(ica_staring_success_time)] / [ica_staring_required_hold]s   |   Contest: [int(ica_staring_elapsed)] / [int(ICA_STARING_DURATION)]s") style "ica_staring_status":
                ypos 690
                xsize 1300

            bar:
                value StaticValue(ica_staring_success_time, ica_staring_required_hold)
                xpos 245
                ypos 730
                xsize 1010
                ysize 20

            textbutton _("CLICK / PULSE TO REFOCUS"):
                xpos 505
                ypos 800
                xsize 490
                ysize 65
                action Function(ica_staring_click)

            textbutton _("Withdraw"):
                xpos 1280
                ypos 45
                action Function(ica_staring_abort)

style ica_staring_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 48

style ica_staring_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 29

style ica_staring_hint:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 22

style ica_staring_status:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 25

style ica_staring_feedback:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 30
