
music._play_default_background(music.built_in_playable_melody(Melodies.FUNK),
    music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
