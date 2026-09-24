## Top-down stealth map for Ica's fifth visit.

screen ica_prank_minigame():
    modal True
    zorder 250

    add "gui/bgtile.png"
    add Solid("#172C3C99")
    key "game_menu" action Function(ica_prank_abort)

    if ica_prank_phase == "active":
        timer ICA_PRANK_PATROL_INTERVAL repeat True action Function(ica_prank_tick)
        key "K_UP" action Function(ica_prank_move, 0, -1)
        key "K_DOWN" action Function(ica_prank_move, 0, 1)
        key "K_LEFT" action Function(ica_prank_move, -1, 0)
        key "K_RIGHT" action Function(ica_prank_move, 1, 0)
        key "K_w" action Function(ica_prank_move, 0, -1)
        key "K_s" action Function(ica_prank_move, 0, 1)
        key "K_a" action Function(ica_prank_move, -1, 0)
        key "K_d" action Function(ica_prank_move, 1, 0)
        key "K_e" action Function(ica_prank_interact)
        key "K_SPACE" action Function(ica_prank_interact)
        key "K_q" action Function(ica_prank_use_assist)
    elif ica_prank_phase == "caught":
        timer ICA_PRANK_CAUGHT_DELAY action Function(ica_prank_reset_to_checkpoint)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 900)

        frame:
            xysize (1500, 900)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (42, 32, 42, 32)

        text _("Operation: Extremely Pink Office") style "ica_prank_title":
            xpos 0
            ypos 0
            xsize 1416

        text _("Approach: [ica_prank_approach_label(ica_prank_approach)]") style "ica_prank_status":
            xpos 0
            ypos 58
            xsize 1416

        grid ICA_PRANK_GRID_WIDTH ICA_PRANK_GRID_HEIGHT:
            xpos 36
            ypos 128
            spacing 2

            for grid_y in range(ICA_PRANK_GRID_HEIGHT):
                for grid_x in range(ICA_PRANK_GRID_WIDTH):
                    frame:
                        xysize (68, 68)
                        padding (2, 2, 2, 2)
                        background Solid(ica_prank_cell_background(grid_x, grid_y))
                        text "[ica_prank_cell_label(grid_x, grid_y)]" style "ica_prank_cell_text":
                            xalign 0.5
                            yalign 0.5

        frame:
            xpos 900
            ypos 128
            xsize 500
            ysize 490
            background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
            padding (30, 26, 30, 24)

            vbox:
                spacing 16
                text _("CURRENT OBJECTIVE") style "ica_prank_hud_heading"
                text _("[ica_prank_objective_text()]") style "ica_prank_hud_body"
                null height 5
                text _("Paint: [\"YES\" if ica_prank_has_paint else \"NO\"]") style "ica_prank_hud_body"
                text _("Walls painted: [len(ica_prank_painted_targets)] / [len(ICA_PRANK_WALL_TARGETS)]") style "ica_prank_hud_body"
                text _("Times spotted: [ica_prank_caught_count]") style "ica_prank_hud_body"
                null height 5
                text _("Orange tiles are Ulysses' current line of sight. Walls stop it.") style "ica_prank_hint"
                text _("Move: arrows or WASD\nInteract: E or Space\nIca assist: Q") style "ica_prank_hint"

                if ica_prank_approach == "play_fair":
                    text _("No assist: you agreed to help, so Ica is making you do the walking.") style "ica_prank_assist_text"
                elif ica_prank_assist_available:
                    if ica_prank_approach == "flirt":
                        textbutton _("DISTRACT ULYSSES") action Function(ica_prank_use_assist)
                    else:
                        textbutton _("GRAVITY COVER") action Function(ica_prank_use_assist)
                else:
                    text _("Ica's assist is spent for this objective.") style "ica_prank_assist_text"

        text _("[ica_prank_feedback]") style "ica_prank_feedback":
            xpos 70
            ypos 670
            xsize 1360

        hbox:
            xpos 330
            ypos 752
            spacing 12
            textbutton _("UP") action Function(ica_prank_move, 0, -1)
            textbutton _("LEFT") action Function(ica_prank_move, -1, 0)
            textbutton _("INTERACT") action Function(ica_prank_interact)
            textbutton _("RIGHT") action Function(ica_prank_move, 1, 0)
            textbutton _("DOWN") action Function(ica_prank_move, 0, 1)

        textbutton _("Withdraw"):
            xpos 1290
            ypos 36
            action Function(ica_prank_abort)

        if ica_prank_phase == "caught":
            frame:
                xalign 0.5
                yalign 0.5
                xsize 850
                ysize 230
                background Solid("#243846F2")
                padding (35, 28, 35, 28)
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 18
                    text _("CAUGHT") style "ica_prank_caught_title"
                    text _("Ica pulls you back to the last checkpoint. Finished work stays finished.") style "ica_prank_caught_body"

style ica_prank_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 44

style ica_prank_status:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 24

style ica_prank_cell_text:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#17394B"
    size 15
    bold True

style ica_prank_hud_heading:
    is gui_text
    color "#D26143"
    size 27
    bold True

style ica_prank_hud_body:
    is gui_text
    color "#00719A"
    size 22

style ica_prank_hint:
    is gui_text
    color "#4D6570"
    size 19

style ica_prank_assist_text:
    is gui_text
    color "#D26143"
    size 20

style ica_prank_feedback:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 27

style ica_prank_caught_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#FFFFFF"
    size 48
    bold True

style ica_prank_caught_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#FFFFFF"
    size 24
