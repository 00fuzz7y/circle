from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from bag import Bag
import REcreation as Rc
from kivy.uix.textinput import TextInput
from screens import *

# needs to be altered such that tab = next and enter will submit & next
class TabTextInput(TextInput):

    def __init__(self, *args, **kwargs):
        self.next = kwargs.pop('next', None)
        super(TabTextInput, self).__init__(*args, **kwargs)

    def set_next(self, next):
        self.next = next

    def _keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key in (9, 13) and self.next is not None:
            self.next.focus = True
            self.next.select_all()
        else:
            super(TabTextInput, self)._keyboard_on_key_down(window, keycode, text, modifiers)

class CreateAccountWindow(Screen):
    namae = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # verifies and sterilizes input, saves it, and moves back to login screen
    def submit(self):
        print(self.namae.text)
        print(self.email.text)
        print(self.password.text)
        if self.namae.text != "" and self.email.text != "" and \
                self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namae.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    # move to login window
    def login(self):
        self.reset()
        sm.current = "login"

    # clear our text fields
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namae.text = ""

# login, or move to make one
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # if the login is both stored and correct show user info
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            # this passes the validated user to main
            UserWindow.current = self.email.text
            self.reset()
            sm.current = "user"
        else:
            invalidLogin()

    # create a new account
    def createBtn(self):
        self.reset()
        sm.current = "create"

    # refresh the text fields
    def reset(self):
        self.email.text = ""
        self.password.text = ""

# display user info, and either logout or move to userdata
class UserWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    dataloc = ObjectProperty(None)
    data = ListProperty(None)
    current = ""

    # switch back to login window
    def logOut(self):
        self.current = ""
        sm.current = "login"

    # check out the things
    def mahThingz(self):
        ThingzWindow.current = self.current
        sm.current = "thingz"

    # runs when the window is loaded
    def on_enter(self, *args):
        password, name, dataloc, created, data = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
        self.dataloc.text = "data saved in: " + dataloc

# display things user has created; offer to create/edit, and move to logout
class ThingzWindow(Screen):
    n = ObjectProperty(None)
    dataloc = ObjectProperty(None)
    # thingz = ListProperty(None)
    current = ""

    # move back to userinfo
    def checkUser(self):
        UserWindow.current = self.current
        sm.current = "user"

    # return us to the login screen
    def logOut(self):
        self.current = ""
        sm.current = "login"

    def newThingz(self):
        NewThingz.current = self.current
        sm.current = "new"

    # runs when the window is loaded
    def on_enter(self, *args):
        password, name, dataloc, created, data = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.dataloc.text = "data saved in: " + dataloc
        # self.thingz.text = "thingz shall be displayed here"

# make a new character through here, please.
class NewThingz(Screen):

    def create(self):
        pass


# Root widget to switch out our windows
class WindowManager(ScreenManager):
    pass


# popup for mismatched login data
def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

# popup for invalid user input
def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def loadScreens():
    pass

# setting up our App environment with:
# our stylesheet data
kv = Builder.load_file("GUI.kv")
# # Bag retrieves our users
db = Bag("users.txt")

# # a widget that shows our windows
sm = WindowManager()
# # the screens to navigate between
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),
    UserWindow(name="user"), ThingzWindow(name="thingz"), NewThingz(name="new")]
# # add the screens to our App
for screen in screens:
    sm.add_widget(screen)
#
# # set our start screen
sm.current = "login"


# the containing class for our App
class TableTopApp(App):
    def build(self):
        return sm

# if this file is called, run TableTop
if __name__ == "__main__":
    #
    # # Bag retrieves our users
    # db = Bag("users.txt")
    # a widget that shows our windows
    sm = WindowManager()
    # the screens to navigate between
    screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),
        UserWindow(name="user"), ThingzWindow(name="thingz"), NewThingz(name="new")]
    # add the screens to our App
    for screen in screens:
        sm.add_widget(screen)

    # set our start screen
    sm.current = "login"

    TableTopApp().run()
