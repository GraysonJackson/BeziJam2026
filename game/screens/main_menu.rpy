## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


image main_menu_background = "images/officeFinal.jpg"

image mm_freddy = Crop((998, 481, 1153, 1812), "images/FINISHEDSPRITES/freddyNeutralSmile.png")
image mm_ulysses = Crop((438, 38, 2031, 2443), "images/umbralBaseMouthClosed.png")
image mm_razzle = Crop((479, 130, 1495, 2351), "images/FINISHEDSPRITES/razzelHappyPeaceSign.png")


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"

    # Character sprites on the left: Razzle on left, Freddy foreground center, Ulysses on right
    fixed:
        xysize (1250, 1080)

        # Razzle (back-left of character group)
        add "mm_razzle":
            xpos 40
            yalign 1.0
            zoom 0.35

        # Ulysses (back-right of character group, strictly to the right of Razzle)
        add "mm_ulysses":
            xpos 500
            yalign 1.0
            zoom 0.35

        # Freddy (foreground center)
        add "mm_freddy":
            xpos 220
            yalign 1.0
            zoom 0.42

    add "gui/sidefade.png"

    # Title positioned at top-left above the characters
    vbox:
        pos (80, 50)
        spacing 10

        text _("Date and Deduce"):
            font "fonts/HotMustardBTN.ttf"
            size 76
            color "#D26143"
            outlines [ (absolute(4), "#FFFFFF", 0, 0) ]

        text _("A D&D Spinoff!"):
            font "fonts/HotMustardBTN.ttf"
            size 36
            color "#D26143"
            outlines [ (absolute(3), "#FFFFFF", 0, 0) ]

    vbox:
        style_prefix "main_menu"
        
        xalign 0.9
        yalign 0.5
        spacing 20

        textbutton _("Start") action Start()

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("display_prefs")    hover_background "gui/mm_hl2.png"

        textbutton _("About") action ShowMenu("about")

        textbutton _("Endings") action ShowMenu("ending_gallery")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style main_menu_button_text:
    text_align 1.0
    
    font "fonts/RandoWB.ttf"
    size 50
    selected_color '#D26143'
    idle_color "#D26143"
    insensitive_color "#778288"
    hover_color "#008DBF"

    xoffset 50
    yoffset 10
    

style main_menu_button:
    text_align 1.0
    xalign 1.0
    hover_background "gui/mm_hl.png"
