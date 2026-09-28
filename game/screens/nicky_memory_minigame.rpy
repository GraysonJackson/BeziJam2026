## Modal case-file matching screen for Nicky's third visit.

screen nicky_memory_minigame():
    modal True
    zorder 250


    add Solid("#080B12")
    add "gui/bgtile.png" alpha 0.16

    if nicky_memory_phase == "matching" and nicky_memory_time_remaining > 0:
        if not minigame_paused:
            timer 1.0 repeat True action Function(nicky_memory_countdown_tick)
    if nicky_memory_phase == "mismatch":
        if not minigame_paused:
            timer NICKY_MEMORY_MISMATCH_DELAY action Function(nicky_memory_tick)
    if nicky_memory_peek_active:
        if not minigame_paused:
            timer NICKY_MEMORY_PEEK_SECONDS action Function(nicky_memory_end_peek)

    $ nicky_phase_number = nicky_memory_phase_index + 1
    $ nicky_phase_name = NICKY_MEMORY_PHASE_NAMES[nicky_memory_phase_index]
    $ nicky_matches = len(nicky_memory_matched_pairs)
    $ nicky_build_result = nicky_memory_reveal.get("value", "")
    $ nicky_individual_result = nicky_memory_reveal.get("scope") == "individual"

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 920)

        frame:
            xysize (1500, 920)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (36, 28, 36, 28)

        text _("NICKY'S CASE-FILE MATCH") style "nicky_memory_title":
            ypos 0
            xsize 1428

        text _("Round [nicky_phase_number] of 2 — [nicky_phase_name]") style "nicky_memory_subtitle":
            ypos 56
            xsize 1428

        if nicky_memory_phase != "result":
            frame:
                xpos 28
                ypos 120
                xsize 1080
                ysize 630
                background Solid("#173E4BEF")
                padding (34, 32, 34, 32)

                grid 4 3:
                    spacing 14

                    for card in nicky_memory_cards:
                        $ card_face_up = nicky_memory_card_is_face_up(card["id"])
                        $ card_matched = card["pair_id"] in nicky_memory_matched_pairs
                        $ card_hinted = card["id"] in nicky_memory_hint_card_ids
                        $ card_label = card["text"] if card_face_up else "CASE FILE\n?"
                        $ card_color = "#58A88A" if card_matched else ("#D7A84C" if card_hinted else ("#F3E8D9" if card_face_up else "#274E5D"))
                        $ card_text_color = "#251D18" if card_face_up else "#FFFFFF"

                        textbutton "[card_label]":
                            xsize 230
                            ysize 160
                            background Solid(card_color)
                            hover_background Solid("#D26143")
                            text_style "nicky_memory_card_text"
                            text_color card_text_color
                            sensitive (
                                nicky_memory_phase == "matching"
                                and not nicky_memory_peek_active
                                and not card_matched
                                and card["id"] not in nicky_memory_selected_ids
                                and len(nicky_memory_selected_ids) < 2
                            )
                            action Function(nicky_memory_flip, card["id"])

            frame:
                xpos 1135
                ypos 120
                xsize 330
                ysize 630
                background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                padding (24, 24, 24, 24)

                vbox:
                    spacing 16
                    text _("BRIEFING STATUS") style "nicky_memory_heading"
                    text _("Matches: [nicky_matches] / [NICKY_MEMORY_PAIRS_PER_PHASE]") style "nicky_memory_body"
                    text _("Mistakes: [nicky_memory_mistakes]") style "nicky_memory_body"

                    if nicky_memory_time_remaining > 0:
                        text _("Time: [nicky_memory_time_remaining]s") style "nicky_memory_timer"
                    else:
                        text _("Time: REVIEW MODE") style "nicky_memory_timer_expired"

                    textbutton _("REVEAL ALL BRIEFLY"):
                        action Function(nicky_memory_reveal_all)
                        sensitive nicky_memory_phase == "matching" and not nicky_memory_selected_ids and not nicky_memory_peek_active

                    if nicky_memory_hint_available:
                        textbutton _("ACCEPT NICKY'S HINT") action Function(nicky_memory_hint)

                    if nicky_memory_phase == "phase_complete":
                        if nicky_memory_phase_index == 0:
                            textbutton _("NEXT RECORD SET") action Function(nicky_memory_next_phase)
                        else:
                            textbutton _("REVIEW BUILD RESULT") action Function(nicky_memory_next_phase)

                    null height 4
                    textbutton _("LET NICKY FINISH") action Function(nicky_memory_assist)

            frame:
                xpos 78
                ypos 785
                xsize 1340
                ysize 92
                background Frame("gui/thoughtbubble.png", 38, 38, 38, 38)
                padding (26, 16, 26, 16)

                text _("[nicky_memory_feedback]") style "nicky_memory_feedback"

        else:
            frame:
                xpos 240
                ypos 155
                xsize 1020
                ysize 600
                background Solid("#F3E8D9F2")
                padding (60, 48, 60, 48)

                vbox:
                    xalign 0.5
                    spacing 28

                    text _("CORROBORATED RESULT") style "nicky_memory_result_title"
                    if nicky_individual_result:
                        text _("The surviving measurements clear two individually tested suspect profiles.") style "nicky_memory_result_body"
                        text _("Cross-referenced booking sheets eliminate these two profiles from the crime scene timeline.") style "nicky_memory_result_explanation"
                    else:
                        text _("The surviving measurements do not support a [nicky_build_result] attacker.") style "nicky_memory_result_body"
                        text _("Corroborated booking measurements rule out the surviving suspects matching this build group.") style "nicky_memory_result_explanation"
                    textbutton _("RECORD FINDING"):
                        xalign 0.5
                        action Function(finish_nicky_memory_minigame)

            text _("[nicky_memory_feedback]") style "nicky_memory_feedback":
                ypos 800
                xsize 1220

    use minigame_controls("memory")


style nicky_memory_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 44
    bold True

style nicky_memory_subtitle:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 24

style nicky_memory_heading:
    is gui_text
    color "#D26143"
    size 27
    bold True

style nicky_memory_body:
    is gui_text
    color "#00719A"
    size 24

style nicky_memory_timer:
    is gui_text
    color "#58A88A"
    size 24
    bold True

style nicky_memory_timer_expired:
    is gui_text
    color "#D26143"
    size 22
    bold True

style nicky_memory_hint:
    is gui_text
    color "#4D6570"
    size 18

style nicky_memory_card_text:
    is button_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 20
    bold True

style nicky_memory_feedback:
    is gui_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#251D18"
    size 23

style nicky_memory_result_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 38
    bold True

style nicky_memory_result_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 30
    bold True

style nicky_memory_result_explanation:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#251D18"
    size 22
