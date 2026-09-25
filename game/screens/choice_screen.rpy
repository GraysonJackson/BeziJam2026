
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    frame:
        xalign 0.5
        ypos 25
        xsize 1240
        ysize 900
        background None
        padding (20, 20)

        viewport:
            mousewheel True
            draggable True
            pagekeys True
            scrollbars "vertical"

            vbox:
                xalign 0.5
                spacing (10 if len(items) >= 7 else 18)
                for i in items:
                    textbutton i.caption:
                        action i.action
                        xsize 1140
                        padding (38, (10 if len(items) >= 7 else 18), 38, (10 if len(items) >= 7 else 18))
                        text_size (28 if len(items) >= 7 else 34)


style choice_vbox:
    xalign 0.5
    spacing 18

style choice_button:
    is default # This means it doesn't use the usual button styling
    xsize 1140
    background Frame("gui/button/choice_[prefix_]background.png",
        24, 27, 13, 27)
    padding (38, 18, 38, 18)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    selected_color '#D26143'
    idle_color "#008DBF"
    insensitive_color "#778288"
    hover_color "#E99067"
    text_align 0.5
    xmaximum 1050



        
