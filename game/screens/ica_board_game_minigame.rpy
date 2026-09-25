## Compact three-player pawn-race screen for Ica's third visit.
screen ica_board_game_minigame():
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
            spacing 18

            text _("Office Pawn Race") style "ica_board_title"

            if ica_board_phase == "approach":
                text _("Pick how you want to join Ica and Winston. Flirting adds 1 space to one move; getting cheeky adds 2; playing it cool adds none.") style "ica_board_body"
                text _("Race to space 12. Reach or pass it to finish. Landing on either opponent bumps that pawn back to start.") style "ica_board_hint"

                vbox:
                    xalign 0.5
                    spacing 10
                    textbutton _("Play It Cool — no bonus") action Function(ica_board_choose_approach, "play_fair")
                    textbutton _("Flirt — +1 space once") action Function(ica_board_choose_approach, "flirt")
                    textbutton _("Get Cheeky — +2 spaces once") action Function(ica_board_choose_approach, "cheat")

            else:
                hbox:
                    xfill True
                    spacing 34
                    text _("Turn [ica_board_turn_number]") style "ica_board_status"
                    if ica_board_phase == "player_turn":
                        text _("Your move") style "ica_board_status"
                    elif ica_board_phase == "ica_turn":
                        text _("Ica's move") style "ica_board_status"
                    elif ica_board_phase == "winston_turn":
                        text _("Winston's move") style "ica_board_status"
                    else:
                        text _("Race complete") style "ica_board_status"
                    text _("You: [ica_board_player_position] / [ICA_BOARD_FINISH]") style "ica_board_status"
                    text _("Ica: [ica_board_ica_position] / [ICA_BOARD_FINISH]") style "ica_board_status"
                    text _("Winston: [ica_board_winston_position] / [ICA_BOARD_FINISH]") style "ica_board_status"

                hbox:
                    xalign 0.5
                    spacing 3
                    for tile_index in range(ICA_BOARD_FINISH + 1):
                        frame:
                            xysize (98, 144)
                            padding (4, 5, 4, 5)
                            background Frame("gui/button/choice_hover_background.png", 24, 27, 13, 27)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 1
                                if tile_index == 0:
                                    text _("START") style "ica_board_tile_label"
                                elif tile_index == ICA_BOARD_FINISH:
                                    text _("FINISH") style "ica_board_tile_label"
                                else:
                                    text " " style "ica_board_tile_label"
                                if ica_board_player_position == tile_index:
                                    text _("YOU") style "ica_board_player_marker"
                                else:
                                    text " " style "ica_board_marker"
                                if ica_board_ica_position == tile_index:
                                    text _("ICA") style "ica_board_ica_marker"
                                else:
                                    text " " style "ica_board_marker"
                                if ica_board_winston_position == tile_index:
                                    text _("WIN") style "ica_board_winston_marker"
                                else:
                                    text " " style "ica_board_marker"
                                text "[tile_index]" style "ica_board_tile_number"

                text "[ica_board_feedback]" style "ica_board_body"

                if ica_board_phase == "player_turn":
                    text _("Choose one of your two movement cards:") style "ica_board_status"
                    hbox:
                        xalign 0.5
                        spacing 24
                        for card_value in ica_board_player_hand:
                            textbutton _("Move [card_value] spaces") action Function(ica_board_choose_card, card_value)

                    if ica_board_bonus_available and ica_board_movement_bonus > 0:
                        if ica_board_spend_bonus_next_move:
                            textbutton _("Spend +[ica_board_movement_bonus] bonus on this move: ON") action Function(ica_board_toggle_bonus)
                        else:
                            textbutton _("Spend +[ica_board_movement_bonus] bonus on this move: OFF") action Function(ica_board_toggle_bonus)
                    elif ica_board_bonus_available:
                        text _("Play It Cool: no movement bonus. Ica likes the attitude anyway.") style "ica_board_hint"
                    else:
                        text _("Your one-time movement bonus has been spent.") style "ica_board_hint"

                elif ica_board_phase == "ica_turn":
                    textbutton _("Resolve Ica's turn") action Function(ica_board_ica_turn)

                elif ica_board_phase == "winston_turn":
                    textbutton _("Resolve Winston's turn") action Function(ica_board_winston_turn)

                elif ica_board_phase == "complete_pending":
                    if ica_board_winner == "player":
                        text _("You win the race. Ica stares at the board, then gives you a grudging nod.") style "ica_board_body"
                    elif ica_board_winner == "ica":
                        text _("Ica wins the race. She barely looks up from the board: 'Skill issue, freshie.'") style "ica_board_body"
                    else:
                        text _("Winston wins the race and celebrates like he just saved the city.") style "ica_board_body"
                    textbutton _("Finish Game") action Function(finish_ica_board_game_minigame)

style ica_board_title:
    is gui_text
    xalign 0.5
    color "#D26143"
    size 48

style ica_board_body:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#D26143"
    size 27

style ica_board_hint:
    is gui_text
    xalign 0.5
    text_align 0.5
    color "#00719A"
    size 20

style ica_board_status:
    is gui_text
    color "#00719A"
    size 26

style ica_board_tile_label:
    is gui_text
    xalign 0.5
    color "#00719A"
    size 17

style ica_board_tile_number:
    is gui_text
    xalign 0.5
    color "#D26143"
    size 20

style ica_board_marker:
    is gui_text
    xalign 0.5
    color "#00719A"
    size 18

style ica_board_player_marker:
    is gui_text
    xalign 0.5
    color "#D26143"
    size 18

style ica_board_ica_marker:
    is gui_text
    xalign 0.5
    color "#00719A"
    size 18

style ica_board_winston_marker:
    is gui_text
    xalign 0.5
    color "#4F8A45"
    size 18
