
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""{b}Date and Deduce: A D&D Spinoff!{/b}

Grayson (\"TriUnity\") Jackson — Code and Writing
Haven (\"Rabbit\") Herring — Background Art
AB (\"PoeBeau\") Manness — Character Art

{b}Special Thanks{/b}
Adyn, Avagail, Braden, Christian, Evan, Geoff, Harlowe, Jace, Rose, Rowan

{b}Assets and Tools{/b}
Visual novel GUI kit by {a=https://timepatches.info}Madi Wander{/a}.
Created using {a=https://github.com/shawna-p/EasyRenPyGui}Fenik's EasyRen'Py GUI{/a}.
{a=https://beaumaher.gumroad.com/l/rando-sans}Rando Sans{/a} by Beau Maher.
{a=https://monaspace.githubnext.com/}Monaspace{/a}.
Built with {a=https://www.renpy.org/}Ren'Py{/a}.
""")


screen about():

    tag menu

    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n" xsize 500


        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36

style about_text:
    font "fonts/MonaspaceNeon-Regular.otf"
    color "#DB8D7A"
    size 23

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"))

    viewport:
        xsize 550
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        hbox:

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")
            textbutton _("Play") action SetScreenVariable("device", "play")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help
        elif device == "play":
            use play_help

        null height 25


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")


screen play_help():

    hbox:
        label _("Choices")
        text _("Choices are permanent after selection. Rollback is intentionally disabled.")

    hbox:
        label _("Log")
        text _("Use Log from the dialogue bar or game menu to reread up to 250 recent lines.")

    hbox:
        label _("Suspects")
        text _("Review remaining suspects and formally recorded evidence without advancing dialogue.")

    hbox:
        label _("Notes")
        text _("Write your own notes for subtle observations that are not entered into the evidence file.")

    hbox:
        label _("Minigames")
        text _("Rules appear before play. Leaving a required investigation game lets your partner finish so the story can continue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate Gamepad") action GamepadCalibrate() xoffset 5 text_size 30





style help_button:
    xmargin 12
    xoffset -15
style help_button_text:
    size 26


style help_label:
    xsize 150
    right_padding 30

style help_label_text:
    xalign 0.0
    textalign 0.0
    size 30
    yalign 0.5

style help_text:
    color "#DB8D7A"
    size 20
    font "fonts/MonaspaceNeon-Regular.otf"
    yalign 0.5
