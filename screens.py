from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from bag import Bag
import REcreation as Rc
from kivy.uix.textinput import TextInput

def bindPlz(self, inst, val):
    self.val = inst.val

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
            print('wtf')
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
        print("{} {} {} {}".format(password, name, dataloc, created))

        self.n = "Account Name: " + name
        self.email = "Email: " + self.current
        self.created = "Created On: " + created
        self.dataloc = "data saved in: " + dataloc

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

# Bag retrieves our users
db = Bag("users.txt")
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
