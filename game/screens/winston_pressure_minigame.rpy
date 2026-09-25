## Modal interrogation-pressure table for Winston's third visit.

screen winston_pressure_minigame():
    modal True
    zorder 250

    add Solid("#090B10")
    add "gui/bgtile.png" alpha 0.13

    $ pressure_target = winston_pressure_current_target_name()
    $ pressure_number = min(winston_pressure_target_index + 1, len(winston_pressure_targets))
    $ pressure_total = winston_pressure_hand_total(winston_pressure_player_hand)
    $ dealer_total = winston_pressure_hand_total(winston_pressure_dealer_hand)
    $ reveal_dealer = winston_pressure_phase in ("answered", "retry", "result")

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1500, 920)

        frame:
            xysize (1500, 920)
            background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
            padding (36, 28, 36, 28)

        text _("WINSTON'S CONTROLLED PRESSURE TEST") style "winston_pressure_title":
            ypos 0
            xsize 1428

        if winston_pressure_phase != "result":
            text _("Interview [pressure_number] of [len(winston_pressure_targets)] — [pressure_target]") style "winston_pressure_subtitle":
                ypos 56
                xsize 1428

            frame:
                xpos 30
                ypos 116
                xsize 980
                ysize 635
                background Solid("#18333FEF")
                padding (34, 28, 34, 28)

                vbox:
                    spacing 12

                    text _("SUSPECT'S DEFENSE") style "winston_pressure_heading"
                    hbox:
                        spacing 14
                        for index, card in enumerate(winston_pressure_dealer_hand):
                            $ dealer_hidden = (index == 1 and not reveal_dealer)
                            $ dealer_card_rank = card["rank"]
                            $ dealer_card_suit = card["suit"]
                            frame:
                                xsize 180
                                ysize 190
                                background Solid("#283E52" if dealer_hidden else "#EFE2C8")
                                padding (12, 12, 12, 12)
                                if dealer_hidden:
                                    text _("CASE\nFILE\n?") style "winston_pressure_card_hidden"
                                else:
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        text "[dealer_card_rank]" style "winston_pressure_card_rank"
                                        text "[dealer_card_suit]" style "winston_pressure_card_suit"

                    if reveal_dealer:
                        text _("Defense total: [dealer_total]") style "winston_pressure_total"
                    else:
                        text _("Defense total: ?") style "winston_pressure_total"

                    null height 6
                    text _("YOUR PRESSURE") style "winston_pressure_heading"
                    viewport:
                        xsize 900
                        ysize 150
                        draggable True
                        mousewheel "horizontal"

                        hbox:
                            spacing 10
                            for card in winston_pressure_player_hand:
                                $ player_card_rank = card["rank"]
                                $ player_card_suit = card["suit"]
                                frame:
                                    xsize 150
                                    ysize 150
                                    background Solid("#F4E7CC")
                                    padding (10, 10, 10, 10)
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        text "[player_card_rank]" style "winston_pressure_card_rank"
                                        text "[player_card_suit]" style "winston_pressure_card_suit_small"

                    text _("Pressure total: [pressure_total] / 21") style "winston_pressure_total"

            frame:
                xpos 1040
                ypos 116
                xsize 425
                ysize 635
                background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                padding (26, 24, 26, 24)

                vbox:
                    spacing 16
                    text _("INTERVIEW CONTROL") style "winston_pressure_heading"
                    if winston_pressure_phase == "playing":
                        textbutton _("PRESSURE — DRAW") action Function(winston_pressure_press)
                        textbutton _("QUESTION — STAND") action Function(winston_pressure_question)
                        textbutton _("USE INTUITION") action Function(winston_pressure_use_intuition)
                        textbutton _("LET WINSTON HANDLE THIS ONE") action Function(winston_pressure_assist_current)
                    elif winston_pressure_phase in ("bust", "retry"):
                        textbutton _("RESET THE INTERVIEW") action Function(winston_pressure_retry)
                        textbutton _("LET WINSTON HANDLE THIS ONE") action Function(winston_pressure_assist_current)
                    elif winston_pressure_phase == "answered":
                        textbutton _("NEXT SUSPECT") action Function(winston_pressure_next_target)

                    null height 8
                    text _("Completed: [len(winston_pressure_completed)] / [len(winston_pressure_targets)]") style "winston_pressure_stat"
                    text _("Busts: [winston_pressure_busts]") style "winston_pressure_stat"
                    text _("Perfect 21s: [winston_pressure_exact_twenty_ones]") style "winston_pressure_stat"
                    text _("Intuition reads: [winston_pressure_intuition_uses]") style "winston_pressure_stat"

                    if winston_pressure_phase in ("playing", "bust", "retry"):
                        textbutton _("LET WINSTON FINISH ALL") action Function(winston_pressure_assist_all)

            frame:
                xpos 78
                ypos 765
                xsize 1340
                ysize 108
                background Frame("gui/thoughtbubble.png", 38, 38, 38, 38)
                padding (28, 18, 28, 18)
                text _("[winston_pressure_feedback]") style "winston_pressure_feedback"

        else:
            frame:
                xpos 230
                ypos 145
                xsize 1040
                ysize 620
                background Solid("#F4E7CCF2")
                padding (62, 50, 62, 50)

                vbox:
                    xalign 0.5
                    spacing 28
                    text _("INTERVIEWS COMPLETE") style "winston_pressure_result_title"
                    text _("All active suspects were tested. Two individual stress profiles conflict with the established timeline and can be cleared.") style "winston_pressure_result_body"
                    text _("Performance changes Winston's response, never the seeded evidence result.") style "winston_pressure_result_note"
                    textbutton _("RECORD THE FINDING"):
                        xalign 0.5
                        action Function(finish_winston_pressure_minigame)

            text _("[winston_pressure_feedback]") style "winston_pressure_feedback":
                ypos 805
                xsize 1220

style winston_pressure_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 42
    bold True

style winston_pressure_subtitle:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 24

style winston_pressure_heading:
    is gui_text
    color "#D26143"
    size 26
    bold True

style winston_pressure_total:
    is gui_text
    color "#FFFFFF"
    size 23
    bold True

style winston_pressure_help:
    is gui_text
    color "#4D6570"
    size 18

style winston_pressure_stat:
    is gui_text
    color "#00719A"
    size 22

style winston_pressure_card_hidden:
    is gui_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#FFFFFF"
    size 27
    bold True

style winston_pressure_card_rank:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#251D18"
    size 48
    bold True

style winston_pressure_card_suit:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 18
    bold True

style winston_pressure_card_suit_small:
    is winston_pressure_card_suit
    size 15

style winston_pressure_feedback:
    is gui_text
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#251D18"
    size 22

style winston_pressure_result_title:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 40
    bold True

style winston_pressure_result_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 27

style winston_pressure_result_note:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#251D18"
    size 21
