screen height_memory_minigame():
    modal True
    zorder 250


    add "gui/bgtile.png"
    add Solid("#172C3C55")
    if not minigame_paused:
        timer 0.5 repeat True action Function(height_memory_tick)

    fixed:
        xalign 0.5
        yalign 0.5
        xsize 1540
        ysize 1000

        add "gui/notebook.png" xysize (750, 995)
        add "gui/notebook.png" xpos 790 xysize (750, 995)

        vbox:
            xpos 95
            ypos 70
            xsize 560
            spacing 12

            text "RAZZLE'S RAPID RECALL":
                xalign 0.5
                size 43
                font "fonts/RandoWB.ttf"
                color "#D26143"

            text "Clear the distractions. Preserve the two height memories.":
                xalign 0.5
                text_align 0.5
                xmaximum 540
                size 23
                color "#251D18"

        vbox:
            xpos 885
            ypos 72
            xsize 560
            spacing 12

            hbox:
                xfill True
                text "CLEANUP [height_memory_progress]/[height_memory_required_cleanups]" size 27 color "#00719A"
                null width 35
                text "SETBACKS [height_memory_setbacks]" size 27 color "#D26143"

            bar:
                value StaticValue(height_memory_progress, height_memory_required_cleanups)
                xsize 540

            text "THOUGHT SCRAMBLE IN [max(0, int(height_memory_time_limit - height_memory_timer))]s":
                xalign 0.5
                size 25
                color "#654C3C"

            bar:
                value StaticValue(height_memory_time_limit - height_memory_timer, height_memory_time_limit)
                xsize 540

        for card in height_memory_board:
            $ memory_page = card["position"] // 4
            $ memory_slot = card["position"] % 4
            $ memory_column = memory_slot % 2
            $ memory_row = memory_slot // 2

            frame:
                xpos 92 + (memory_page * 790) + (memory_column * 305)
                ypos 310 + (memory_row * 238)
                xsize 286
                ysize 220
                background Frame("gui/frame.png", 35, 48, 35, 32)
                padding (18, 26, 18, 18)

                fixed:
                    add Transform(
                        "gui/button/tape_0.png" if card["position"] % 2 == 0 else "gui/button/tape_1.png",
                        xysize=(150, 60)):
                        xpos 48
                        ypos -36

                    textbutton card["text"]:
                        xalign 0.5
                        yalign 0.5
                        xsize 245
                        ysize 155
                        text_size 25
                        text_align 0.5
                        text_color "#251D18"
                        text_hover_color "#D26143"
                        background None
                        hover_background Solid("#E9906726")
                        action Function(height_memory_click, card["id"])

        frame:
            xpos 95
            ypos 810
            xsize 560
            ysize 115
            background Frame("gui/thoughtbubble.png", 38, 38, 38, 38)
            padding (24, 18)

            text "[height_memory_feedback]":
                xalign 0.5
                yalign 0.5
                text_align 0.5
                size 22
                color "#251D18"

        hbox:
            xpos 925
            ypos 840
            spacing 25

            textbutton "Let Razzle finish":
                action Function(abort_height_memory_minigame)
                text_size 23

    use minigame_controls("height")


style height_memory_minigame_button_text:
    font "MonaspaceNeon-Regular.otf"
