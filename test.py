from kivy.core.audio import SoundLoader
from kivy.properties import DictProperty, NumericProperty, BooleanProperty, OptionProperty, ObjectProperty, \
    StringProperty
sound = SoundLoader.load('bg.ogg')
music_volume = NumericProperty(1)
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.volume=music_volume
    
    sound.play()