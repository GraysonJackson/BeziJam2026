## Modal laboratory interface for Madeline's centrifuge test.

screen madeline_centrifuge_minigame():
    modal True
    zorder 250

    add "labOutline"
    add Solid("#121A24CC")

    if madeline_centrifuge_phase == "spinning":
        timer 0.2 repeat True action Function(madeline_centrifuge_tick)

    $ selected_tube_label = MADELINE_CENTRIFUGE_TUBES[madeline_centrifuge_selected_tube]["label"] if madeline_centrifuge_selected_tube else "NONE"
    $ centrifuge_left_mass = _madeline_centrifuge_side_mass("left")
    $ centrifuge_right_mass = _madeline_centrifuge_side_mass("right")
    $ centrifuge_effective_balance = madeline_centrifuge_effective_balance()
    $ centrifuge_revealed_type = madeline_centrifuge_reveal.get("value", "")
    $ centrifuge_individual_result = madeline_centrifuge_reveal.get("scope") == "individual"

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1540, 950)

        frame:
            xysize (1540, 950)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (38, 30, 38, 30)

        text "MADELINE'S CENTRIFUGE TEST" style "madeline_centrifuge_title":
            xpos 0
            ypos 0
            xsize 1464

        text "Balance the opposing tube masses, run the rotor, then read the separated bands." style "madeline_centrifuge_subtitle":
            xpos 0
            ypos 56
            xsize 1464

        frame:
            xpos 45
            ypos 130
            xsize 400
            ysize 620
            background Solid("#F3E8D9EE")
            padding (24, 22, 24, 22)

            vbox:
                spacing 14
                text "TUBE BANK" style "madeline_centrifuge_heading"
                text "Select a tube, then select a rotor slot." style "madeline_centrifuge_body"

                for tube_id, tube_data in MADELINE_CENTRIFUGE_TUBES.items():
                    $ tube_is_placed = tube_id in madeline_centrifuge_slots.values()
                    textbutton "[tube_data['label']]  •  [tube_data['mass']]g":
                        xsize 340
                        ysize 72
                        background Solid(tube_data["color"] if madeline_centrifuge_selected_tube == tube_id else "#274E5D")
                        hover_background Solid("#D26143")
                        text_color "#FFFFFF"
                        text_size 20
                        sensitive madeline_centrifuge_phase == "setup" and not tube_is_placed
                        action Function(madeline_centrifuge_select_tube, tube_id)

                null height 8
                text "Selected: [selected_tube_label]" style "madeline_centrifuge_body"

        frame:
            xpos 475
            ypos 130
            xsize 610
            ysize 620
            background Solid("#173E4BEF")
            padding (25, 22, 25, 22)

            text "ROTOR" style "madeline_centrifuge_heading_light":
                xpos 0
                ypos 0
                xsize 560

            add Solid("#8DD4D044"):
                xpos 125
                ypos 115
                xsize 310
                ysize 310

            add Solid("#D26143AA"):
                xpos 274
                ypos 110
                xsize 12
                ysize 320

            add Solid("#D26143AA"):
                xpos 120
                ypos 264
                xsize 320
                ysize 12

            for slot_id, slot_x, slot_y in (
                    ("left_top", 65, 125),
                    ("left_bottom", 65, 325),
                    ("right_top", 375, 125),
                    ("right_bottom", 375, 325)):
                $ slotted_tube = madeline_centrifuge_slots.get(slot_id, "")
                $ slot_label = MADELINE_CENTRIFUGE_TUBES[slotted_tube]["label"] if slotted_tube else "EMPTY SLOT"
                $ slot_mass = MADELINE_CENTRIFUGE_TUBES[slotted_tube]["mass"] if slotted_tube else 0
                textbutton "[slot_label]\n[slot_mass]g":
                    xpos slot_x
                    ypos slot_y
                    xsize 155
                    ysize 100
                    background Solid("#58A88A" if slotted_tube else "#596B78")
                    hover_background Solid("#D26143")
                    text_color "#FFFFFF"
                    text_size 17
                    text_align 0.5
                    sensitive madeline_centrifuge_phase == "setup"
                    action Function(madeline_centrifuge_select_tube, slot_id)

            text "LEFT: [centrifuge_left_mass]g" style "madeline_centrifuge_rotor_text":
                xpos 70
                ypos 470
            text "RIGHT: [centrifuge_right_mass]g" style "madeline_centrifuge_rotor_text":
                xpos 355
                ypos 470

        frame:
            xpos 1115
            ypos 130
            xsize 380
            ysize 620
            background Solid("#F3E8D9EE")
            padding (25, 22, 25, 22)

            vbox:
                spacing 16
                text "BALANCE & SPIN" style "madeline_centrifuge_heading"
                text "Effective balance: [centrifuge_effective_balance:+d]" style "madeline_centrifuge_body"
                text "Fine trim: [madeline_centrifuge_trim:+d]" style "madeline_centrifuge_body"

                hbox:
                    spacing 8
                    textbutton "LEFT" action Function(madeline_centrifuge_balance, "trim_left") sensitive madeline_centrifuge_phase == "setup"
                    textbutton "RESET" action Function(madeline_centrifuge_balance, "trim_reset") sensitive madeline_centrifuge_phase == "setup"
                    textbutton "RIGHT" action Function(madeline_centrifuge_balance, "trim_right") sensitive madeline_centrifuge_phase == "setup"

                null height 8
                text "SPIN PROGRESS" style "madeline_centrifuge_body"
                bar value StaticValue(madeline_centrifuge_spin_progress, 100) xsize 315
                text "STABILITY [madeline_centrifuge_stability]%" style "madeline_centrifuge_body"
                bar value StaticValue(madeline_centrifuge_stability, 100) xsize 315

                if madeline_centrifuge_phase == "setup":
                    textbutton "START SPIN" action Function(madeline_centrifuge_start_spin)
                elif madeline_centrifuge_phase == "spinning":
                    text "ROTOR ACTIVE" style "madeline_centrifuge_warning"
                elif madeline_centrifuge_phase == "retry":
                    textbutton "UNLOCK & RETRY" action Function(madeline_centrifuge_balance, "retry")
                elif madeline_centrifuge_phase == "read_pending":
                    textbutton "READ BANDS" action Function(madeline_centrifuge_read_result)
                elif madeline_centrifuge_phase == "result":
                    if centrifuge_individual_result:
                        text "INDIVIDUAL REFERENCES CLEARED" style "madeline_centrifuge_result"
                    else:
                        text "EXCLUDED TYPE: [centrifuge_revealed_type]" style "madeline_centrifuge_result"
                    textbutton "RECORD RESULT" action Function(finish_madeline_centrifuge_minigame)

        frame:
            xpos 70
            ypos 785
            xsize 1180
            ysize 115
            background Frame("gui/thoughtbubble.png", 38, 38, 38, 38)
            padding (28, 18, 28, 18)

            text "[madeline_centrifuge_feedback]" style "madeline_centrifuge_feedback"

        textbutton "Let Madeline finish":
            xpos 1270
            ypos 810
            xsize 220
            action Function(madeline_centrifuge_assist)

style madeline_centrifuge_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 43
    bold True

style madeline_centrifuge_subtitle:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 23

style madeline_centrifuge_heading:
    is gui_text
    color "#8D3027"
    size 27
    bold True

style madeline_centrifuge_heading_light:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#8DD4D0"
    size 27
    bold True

style madeline_centrifuge_body:
    is gui_text
    color "#251D18"
    size 20

style madeline_centrifuge_rotor_text:
    is gui_text
    color "#FFFFFF"
    size 21
    bold True

style madeline_centrifuge_warning:
    is gui_text
    color "#D26143"
    size 25
    bold True

style madeline_centrifuge_result:
    is gui_text
    color "#00719A"
    size 25
    bold True

style madeline_centrifuge_feedback:
    is gui_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#251D18"
    size 23
