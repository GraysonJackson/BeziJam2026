
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen display_prefs():

    tag menu

    use game_menu(_("Display Settings"))

    viewport:
        
        style_prefix 'game_menu'
        mousewheel True pagekeys True
        scrollbars "vertical"
        has vbox

        hbox:
            box_wrap True
        
            vbox:
                style_prefix "radio"
                label _("Screen Mode")
                textbutton _("Window"):
                    # Ensures this button is selected when
                    # not in fullscreen.
                    selected not preferences.fullscreen
                    action Preference("display", "window")
                textbutton _("Fullscreen"):
                    action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("While Skipping:")
                textbutton _("Skip Unseen Text"):
                    action Preference("skip", "toggle")
                textbutton _("Skip After Choices"):
                    action Preference("after choices", "toggle")
                null height 20

            vbox:
                style_prefix "radio"
                label _("Auto-Forward Mode")
                text "Allow text to auto-advance without clicking." size 16 font "fonts/MonaspaceArgon-SemiBold.otf" color "#00719A"
                textbutton _("Enabled") action Preference("auto-forward", "enable") 
                textbutton _("Disabled") action Preference("auto-forward", "disable") 

            vbox:
                style_prefix "slider"
                box_wrap True
                yoffset -15
                label _("Auto-Forward Time")
                
                bar value Preference("auto-forward time")
                null height 5
                text "Leftmost is fastest." size 16 font "fonts/MonaspaceArgon-SemiBold.otf" color "#00719A"
                
                null height 15
                label _("Text Speed")
                bar value Preference("text speed")

            null height 50
                
            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

screen audio_prefs():
    tag menu

    use game_menu(_("Audio Settings"))

    viewport:
        style_prefix 'game_menu'
        scrollbars "vertical"
        has vbox

        vbox:
            yoffset 40
            spacing 3
            style_prefix "slider"
            box_wrap True
            
            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume")

            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)


            if config.has_music or config.has_sound:
                null height 15
                textbutton _("Mute All"):
                    style_prefix "check"
                    action Preference("all mute", "toggle")



default persistent.dyslexic_font = False

init python:
    _dyslexic_sync_initialized = False

    def set_dyslexic_font(enable):
        enable = bool(enable)
        persistent.dyslexic_font = enable
        _preferences.font_transform = "opendyslexic" if enable else None
        if getattr(persistent, "_gui_preference", None) is not None:
            if enable:
                persistent._gui_preference["font"] = "fonts/OpenDyslexic-Regular.ttf"
                persistent._gui_preference["interface_font"] = "fonts/OpenDyslexic-Regular.ttf"
                persistent._gui_preference["name_font"] = "fonts/OpenDyslexic-Regular.ttf"
            else:
                persistent._gui_preference["font"] = "MonaspaceNeon-Regular.otf"
                persistent._gui_preference["interface_font"] = "MonaspaceNeon-Regular.otf"
                persistent._gui_preference["name_font"] = "MonaspaceNeon-Regular.otf"
        renpy.free_memory()
        renpy.display.interface.display_reset = True
        renpy.restart_interaction()

    class SetDyslexicFont(Action, DictEquality):
        def __init__(self, enable):
            self.enable = bool(enable)

        def __call__(self):
            set_dyslexic_font(self.enable)

        def get_selected(self):
            is_dyslexic = (_preferences.font_transform == "opendyslexic") or bool(getattr(persistent, "dyslexic_font", False))
            return is_dyslexic if self.enable else not is_dyslexic

    def _sync_dyslexic_font_state():
        global _dyslexic_sync_initialized
        if not _dyslexic_sync_initialized:
            _dyslexic_sync_initialized = True
            if getattr(persistent, "dyslexic_font", False):
                _preferences.font_transform = "opendyslexic"
            elif _preferences.font_transform == "opendyslexic":
                persistent.dyslexic_font = True
            return

        is_trans = (_preferences.font_transform == "opendyslexic")
        if getattr(persistent, "dyslexic_font", False) != is_trans:
            persistent.dyslexic_font = is_trans

    if _sync_dyslexic_font_state not in config.interact_callbacks:
        config.interact_callbacks.append(_sync_dyslexic_font_state)

init 999 python:
    if getattr(persistent, "dyslexic_font", False):
        _preferences.font_transform = "opendyslexic"

screen accessibility_prefs():
    tag menu

    use game_menu(_("Accessibility"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True pagekeys True
        scrollbars "vertical"
        has vbox

        vbox:
            yoffset 20
            spacing 20

            vbox:
                style_prefix "radio"
                label _("Dyslexic Font")
                text _("Changes in-game text and UI fonts to OpenDyslexic for improved readability.") size 16 font "fonts/MonaspaceArgon-SemiBold.otf" color "#00719A"
                null height 5

                textbutton _("Default"):
                    action SetDyslexicFont(False)
                textbutton _("OpenDyslexic"):
                    action SetDyslexicFont(True)


### PREF
style pref_label:
    top_margin 15
    bottom_margin -8

style pref_label_text:
    yalign 1.0
    # outlines [ (absolute(3), "#ffffffff", 0, 0) ]

style pref_vbox:
    xsize 450

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

style radio_button_text:
    outlines [ (absolute(3), "#ffffffff", 0, 0) ]

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

style check_button_text:
    outlines [ (absolute(3), "#ffffffff", 0, 0) ]

## SLIDER
style slider_label:
    is pref_label
    bottom_margin 5
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 400

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675

