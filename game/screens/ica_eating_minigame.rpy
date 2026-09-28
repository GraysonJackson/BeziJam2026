## Hot dog race UI for Ica's fourth visit.

screen ica_eating_minigame():
    modal True
    zorder 250

    add "gui/bgtile.png"
    add Solid("#172C3CCC")
    key "K_SPACE" action Function(ica_eating_action, "bite")
    key "K_r" action Function(ica_eating_action, "pace")

    if ica_eating_phase == "active":
        if not minigame_paused:
            timer ICA_EATING_TICK_INTERVAL repeat True action Function(ica_eating_tick)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 900)

        frame:
            xysize (1500, 900)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (50, 38, 50, 38)

        text _("Ica's Extremely Necessary Hot Dog Contest") style "ica_eating_title":
            ypos 0
            xsize 1400

        text _("Approach: [ica_eating_approach_label(ica_eating_approach)]") style "ica_eating_status":
            ypos 64
            xsize 1400

        frame:
            xpos 90
            ypos 145
            xsize 600
            ysize 270
            background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
            padding (32, 24, 32, 24)

            vbox:
                spacing 18
                text _("YOU") style "ica_eating_contestant"
                text _("Tray cleared: [ica_eating_player_progress:.1f] / [ICA_EATING_TOTAL_HOT_DOGS:.0f]") style "ica_eating_meter_label"
                bar:
                    value StaticValue(ica_eating_player_progress, ICA_EATING_TOTAL_HOT_DOGS)
                    xsize 536
                    ysize 34
                text _("Stamina") style "ica_eating_meter_label"
                bar:
                    value StaticValue(ica_eating_stamina, ICA_EATING_MAX_STAMINA)
                    xsize 536
                    ysize 24

        frame:
            xpos 810
            ypos 145
            xsize 600
            ysize 270
            background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
            padding (32, 24, 32, 24)

            vbox:
                spacing 18
                text _("ICA") style "ica_eating_contestant"
                text _("Tray cleared: [ica_eating_ica_progress:.1f] / [ICA_EATING_TOTAL_HOT_DOGS:.0f]") style "ica_eating_meter_label"
                bar:
                    value StaticValue(ica_eating_ica_progress, ICA_EATING_TOTAL_HOT_DOGS)
                    xsize 536
                    ysize 34
                if ica_eating_flirt_slowdown_left > 0.0:
                    text _("Distracted for [ica_eating_flirt_slowdown_left:.1f]s") style "ica_eating_flirt_status"
                else:
                    text _("Total cheats witnessed (incl. pre-game): [ica_eating_ica_cheat_stage + 1]") size 22 style "ica_eating_meter_label"

        text _("[ica_eating_feedback]") style "ica_eating_feedback":
            ypos 455
            xsize 1260

        text _("Time: [max(0, int(ICA_EATING_DURATION - ica_eating_elapsed))]s   |   Choking incidents: [ica_eating_mistakes]") style "ica_eating_status":
            ypos 535
            xsize 1300

        bar:
            value StaticValue(ica_eating_elapsed, ICA_EATING_DURATION)
            xpos 220
            ypos 580
            xsize 1060
            ysize 22

        if ica_eating_action_cooldown > 0.0:
            text _("Recovering breath... ([ica_eating_action_cooldown:.1f]s)") style "ica_eating_status":
                ypos 615
                xsize 1300

        hbox:
            xpos 205
            ypos 650
            spacing 35

            textbutton (_("TAKE A BITE\n(-0.9 Stamina)") if ica_eating_stamina >= ICA_EATING_BITE_STAMINA_COST else _("TAKE A BITE\n(Low Stamina - Choke Risk!)")):
                xsize 350
                ysize 82
                text_text_align 0.5
                text_size 20
                sensitive ica_eating_action_cooldown <= 0.0
                action Function(ica_eating_action, "bite")

            textbutton _("PACE YOURSELF\n(+1.5 Stamina)"):
                xsize 350
                ysize 82
                text_text_align 0.5
                text_size 20
                sensitive ica_eating_action_cooldown <= 0.0
                action Function(ica_eating_action, "pace")

            if ica_eating_approach == "flirt":
                textbutton _("LEAN IN\n(Distract Ica)"):
                    xsize 350
                    ysize 82
                    text_text_align 0.5
                    text_size 20
                    sensitive not ica_eating_special_used and ica_eating_action_cooldown <= 0.0
                    action Function(ica_eating_action, "special")
            elif ica_eating_approach == "cheat":
                textbutton _("PALM ONE\n(+1.25 Progress)"):
                    xsize 350
                    ysize 82
                    text_text_align 0.5
                    text_size 20
                    sensitive not ica_eating_special_used and ica_eating_action_cooldown <= 0.0
                    action Function(ica_eating_action, "special")
            else:
                frame:
                    xsize 350
                    ysize 82
                    background Solid("#243846")
                    text _("PURE RHYTHM\n(No Tricks)") style "ica_eating_no_tricks":
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

        textbutton _("Withdraw"):
            xpos 1280
            ypos 35
            action Function(ica_eating_abort)

    use minigame_controls("eating")


style ica_eating_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 46

style ica_eating_status:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 25

style ica_eating_contestant:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 38
    bold True

style ica_eating_meter_label:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 26

style ica_eating_flirt_status:
    is ica_eating_meter_label
    color "#D26143"

style ica_eating_feedback:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 29

style ica_eating_hint:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 21

style ica_eating_no_tricks:
    is gui_text
    color "#FFFFFF"
    size 24
    bold True
