"""kivy wouldn't initialise without these.
    seeing if environment fixed [it wasn't, but the config stuck]
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

this is going to be the UI once i can get the backend running
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Fucking idiot-something worked. thank the gods")

if __name__== "__main__":
    MyApp().run()

