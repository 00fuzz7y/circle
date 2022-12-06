from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from bag import Bag
import REcreation as Rc
from kivy.uix.textinput import TextInput

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='some'))

fields = []

buildstring =
"""
<Base@GridLayout>:
    orientation: "tb-lr"
    cols: 3

<SheetWindow>:
    n: n

"""
