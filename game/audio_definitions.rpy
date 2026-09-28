## Audio definitions and music controller for Date and Deduce.
## Music composed by JDSherbert (https://jdsherbert.itch.io)
## Minigame Music Pack [FREE] & Nostalgia Music Pack [FREE]

define audio.music_razzle = "audio/music/refreshing_dawn.ogg"          # Minigame Pack: Refreshing Dawn
define audio.music_dhampir = "audio/music/sk8r_bruh.ogg"               # Nostalgia Pack: Sk8r Bruh
define audio.music_madeline = "audio/music/digital_waves.ogg"          # Minigame Pack: Digital Waves
define audio.music_nicky = "audio/music/streetlights.ogg"              # Minigame Pack: Streetlights
define audio.music_winston = "audio/music/beach_vibes.ogg"             # Minigame Pack: Beach Vibes
define audio.music_ica = "audio/music/link_cable.ogg"                  # Nostalgia Pack: Link Cable
define audio.music_ulysses = "audio/music/smooth_driving.ogg"          # Minigame Pack: Smooth Driving (candidate audition)
define audio.music_minigame = "audio/music/blackjack.ogg"              # Minigame Pack: Blackjack (creator-selected)
define audio.music_title = "audio/music/treehouse_party.ogg"           # Nostalgia Pack: Treehouse Party
define audio.music_celebration = "audio/music/treehouse_party.ogg"     # Nostalgia Pack: Treehouse Party
define audio.music_corrupted = "audio/music/corrupted_circuitry.ogg"   # Minigame Pack: Corrupted Circuitry
define audio.music_suspense = "audio/music/electric_eel_fishing.ogg"   # Minigame Pack: Electric Eel Fishing

default previous_scene_music = None

init python:
    def play_route_music(track, fadein=1.0, fadeout=0.5):
        """Play a music track on the music channel without restarting if already playing."""
        if not track:
            return
        current = renpy.music.get_playing(channel="music")
        if current != track:
            renpy.music.play(track, channel="music", loop=True, fadein=fadein, fadeout=fadeout)

    def stop_route_music(fadeout=1.0):
        """Fade out music smoothly."""
        renpy.music.stop(channel="music", fadeout=fadeout)

    def push_minigame_music(track=None, fadein=0.5, fadeout=0.5):
        """Save current music and switch to minigame track."""
        store.previous_scene_music = renpy.music.get_playing(channel="music")
        if track is None:
            track = store.audio.music_minigame
        if renpy.music.get_playing(channel="music") != track:
            renpy.music.play(track, channel="music", loop=True, fadein=fadein, fadeout=fadeout)

    def pop_minigame_music(fadein=0.5, fadeout=0.5):
        """Restore music track from before minigame."""
        prev = store.previous_scene_music
        store.previous_scene_music = None
        if prev:
            if renpy.music.get_playing(channel="music") != prev:
                renpy.music.play(prev, channel="music", loop=True, fadein=fadein, fadeout=fadeout)
        else:
            renpy.music.stop(channel="music", fadeout=fadeout)
