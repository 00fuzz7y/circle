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


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text=" YANAME "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text=" YADOB "))
        self.dob = TextInput(multiline=False)
        self.inside.add_widget(self.dob)

        self.inside.add_widget(Label(text=" YAAAAASSSS"))
        self.wev = TextInput(multiline=False)
        self.inside.add_widget(self.wev)

        self.add_widget(self.inside)

        self.submit = Button(text='submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        dob = self.dob.text
        wev = self.wev.text

        print(name, dob, wev)

        self.name.text = ""
        self.dob.text = ""
        self.wev.text = ""


# return Label(text="Fucking idiot-something worked. thank the gods")
class TestApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TestApp().run()

