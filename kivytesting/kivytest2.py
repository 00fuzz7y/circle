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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    dob = ObjectProperty(None)

    def btn(self):
        print("name", self.name.text, "dob", self.dob.text)
        self.name.text = ''
        self.dob.text = ''
        

class TestApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TestApp().run()

