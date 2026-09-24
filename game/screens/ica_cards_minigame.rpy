## Ica's modal high-card screen.

screen ica_cards_minigame():
    modal True
    zorder 150

    add "gui/bgtile.png"

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1500, 900)
        background Frame("gui/button/choice_idle_background.png", 24, 27, 13, 27)
        padding (55, 42, 55, 42)

        vbox:
            xfill True
            spacing 22

            text _("Ica's High-Card Hangout") style "ica_cards_title"

            if ica_cards_phase == "approach":
                text _("Pick an approach before the deal. Easier tactics help with the cards, but Ica pays attention to how hard you try.") style "ica_cards_body"

                vbox:
                    spacing 12
                    textbutton _("Play It Cool") action Function(ica_cards_choose_approach, "play_fair")
                    text _("No tricks and no performance. No gameplay edge.") style "ica_cards_hint"
                    textbutton _("Flirt") action Function(ica_cards_choose_approach, "flirt")
                    text _("Distract her with banter. Your calls get a small edge.") style "ica_cards_hint"
                    textbutton _("Get Cheeky") action Function(ica_cards_choose_approach, "cheat")
                    text _("Peek when Ica looks away. Your calls get a stronger edge.") style "ica_cards_hint"

                textbutton _("Maybe another time") action Function(abort_ica_cards_minigame)

            elif ica_cards_phase in ("play", "feedback", "complete_pending"):
                hbox:
                    xfill True
                    spacing 38
                    text _("Approach: [ica_cards_approach_label(ica_cards_approach)]") style "ica_cards_status"
                    text _("Call edge: +[ica_cards_difficulty_reduction]") style "ica_cards_status"
                    text _("Round [ica_cards_round] / [ica_cards_round_count]") style "ica_cards_status"
                    text _("You [ica_cards_player_score] - Ica [ica_cards_ica_score]") style "ica_cards_status"

                text _("[ica_cards_approach_description(ica_cards_approach)]") style "ica_cards_hint"

                hbox:
                    xalign 0.5
                    spacing 80
                    frame:
                        xysize (430, 245)
                        background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 12
                            text _("Ica's card") style "ica_cards_card_label"
                            text _("[ica_cards_card_name(ica_cards_current_ica_card)]") style "ica_cards_card"
                    frame:
                        xysize (430, 245)
                        background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 12
                            text _("Your card") style "ica_cards_card_label"
                            if ica_cards_current_player_card:
                                text _("[ica_cards_card_name(ica_cards_current_player_card)]") style "ica_cards_card"
                            else:
                                text _("?") style "ica_cards_card"

                if ica_cards_phase == "play":
                    text _("Call whether your hidden card will be higher or lower. Your one double call awards two points—to whoever wins it.") style "ica_cards_body"
                    hbox:
                        xalign 0.5
                        spacing 18
                        textbutton _("Higher") action Function(ica_cards_choose, "higher")
                        textbutton _("Lower") action Function(ica_cards_choose, "lower")
                        textbutton _("Double: Higher"):
                            sensitive ica_cards_double_available
                            action Function(ica_cards_choose, "double_higher")
                        textbutton _("Double: Lower"):
                            sensitive ica_cards_double_available
                            action Function(ica_cards_choose, "double_lower")

                    text _("DOUBLE READY" if ica_cards_double_available else "Double call spent") style "ica_cards_hint"

                elif ica_cards_phase == "feedback":
                    text _("[ica_cards_round_result]") style "ica_cards_body"
                    textbutton _("Continue") action Function(ica_cards_next_round)

                elif ica_cards_phase == "complete_pending":
                    text _("[ica_cards_result_text()]") style "ica_cards_body"
                    text _("The final result is settled by score, then by the deterministic high-card tiebreaker if needed.") style "ica_cards_hint"
                    textbutton _("Finish Game") action Function(finish_ica_cards_minigame)

                if ica_cards_phase in ("play", "feedback"):
                    textbutton _("Leave before the result") action Function(abort_ica_cards_minigame)

style ica_cards_title:
    is gui_text
    xalign 0.5
    color "#D26143"
    size 48

style ica_cards_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 28

style ica_cards_hint:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 22

style ica_cards_status:
    is gui_text
    color "#00719A"
    size 24

style ica_cards_card_label:
    is gui_text
    xalign 0.5
    color "#00719A"
    size 25

style ica_cards_card:
    is gui_text
    xalign 0.5
    color "#D26143"
    size 82
