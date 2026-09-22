screen height_memory_minigame():
    modal True
    zorder 250

    add Solid("#000000B8")
    timer 0.5 repeat True action Function(height_memory_tick)
    key "game_menu" action Function(abort_height_memory_minigame)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1540
        ysize 900
        background Solid("#1B1930F2")
        padding (35, 28)

        vbox:
            spacing 14

            hbox:
                xfill True
                spacing 20
                text "BRANDON'S THOUGHT BOARD" size 42 color "#F7D7A8"
                null width 20
                text "SETBACKS: [height_memory_setbacks]" size 27 color "#E99067" yalign 0.5

            text "Clean out the irrelevant memories. The useful observations are marked, but do not click them." size 25 color "#D6E7E8"

            hbox:
                spacing 24
                text "CLEANUP  [height_memory_progress] / [height_memory_required_cleanups]" size 27 color "#00B1E1" yalign 0.5
                fixed:
                    xsize 620
                    ysize 28
                    add Solid("#384758")
                    add Solid("#00B1E1") xsize (620 * height_memory_progress / float(height_memory_required_cleanups))
                text "SCRAMBLE IN [int(height_memory_time_limit - height_memory_timer)]" size 27 color "#F7D7A8" yalign 0.5

            frame:
                xsize 1470
                ysize 610
                background Solid("#25263D")
                padding (25, 25)

                fixed:
                    xsize 1420
                    ysize 560

                    for card in height_memory_board:
                        frame:
                            xpos (card["position"] % 3) * 465
                            ypos (card["position"] // 3) * 185
                            xsize 440
                            ysize 165
                            background Solid("#6A4058" if card["protected"] else "#30465B")
                            padding (16, 14)

                            vbox:
                                spacing 8
                                text ("IMPORTANT MEMORY" if card["protected"] else "DISTRACTION") size 21 color ("#FFD18A" if card["protected"] else "#8FD9E8")
                                textbutton card["text"]:
                                    xsize 405
                                    ysize 92
                                    text_size 26
                                    text_align 0.5
                                    text_color "#FFFFFF"
                                    text_hover_color "#FFE5B5"
                                    background Solid("#87506B" if card["protected"] else "#3C5D76")
                                    hover_background Solid("#A85F79" if card["protected"] else "#527D95")
                                    action Function(height_memory_click, card["id"])

            frame:
                xfill True
                ysize 78
                background Solid("#332B49")
                padding (18, 12)
                text "[height_memory_feedback]" size 25 color "#F7D7A8" xalign 0.5 text_align 0.5

            hbox:
                xalign 1.0
                spacing 20
                textbutton "Leave board" action Function(abort_height_memory_minigame) text_size 25

style height_memory_minigame_button_text:
    font "MonaspaceNeon-Regular.otf"
