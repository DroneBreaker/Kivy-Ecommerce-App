from logging import root
from os import close
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.graphics import Ellipse
from kivy.graphics.context_instructions import Color
import main



class WindowScreen(ScreenManager):
    pass


class HomePage(Screen, StackLayout):
    # layout = GridLayout(cols=1, spacing=10, padding=10)

    def __init__(self, **kw):
        super(HomePage, self).__init__(**kw)

        # with self.canvas:
        #     Color(48/255, 46/255, 55/255, 1)
        #     Ellipse(pos=(.1, .1), size=(500,80))
            # Line(points=(500, 100, 150, 0, 150, 0), width=2)
        
        # layout = BoxLayout(padding=10)
        # self.search = MDTextField(hint_text='What can we get you?', pos_hint={'center_y': .5}, width=200)
        # self.submit = Button(text='Submit', on_press=self.on_submit)

        # layout.add_widget(self.search)
        # layout.add_widget(self.submit)

        # def __show__(): 
        #     return layout
    # layout = StackLayout()

    # for i in range(3):
    #     btn = Button(str(i), size_hint=(None, None))
    #     layout.add_widget(btn)

    #     return layout

    

    def on_submit(self):
        print('Sent')


class Anything(Screen):
    pass


class DeliveryPage(Screen):
    pass


class Restaurant(Screen):
    pass


class SuperMarket(Screen):
    pass


class Drinks(Screen):
    pass


class Pharmacy(Screen):
    pass


class Promotions(Screen):
    pass


class LoginPage(Screen):
    def anim(self, widget):
        anima =  Animation(pos_hint={'center_y': 1.16})
        anima.start(widget)

    def anim_draw(self, widget):
        anima =  Animation(pos_hint={'center_y': .85})
        anima.start(widget)

    def icons(self, widget):
       anima =  Animation(pos_hint={'center_y': .8})
       anima += Animation(pos_hint={'center_y': .85})
       anima.start(widget)

    def text(self, widget):
       anima =  Animation(opacity=0, duration=2)
       anima += Animation(opacity=1)
       anima.start(widget)

    def validate_user(self):
        user = self.ids.uname
        pwd = self.ids.pwdController
        label = self.ids.label

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            label.text = '[color=#FF0000]Username and/or password required[/color]'
        else:
            if uname == 'admin' and passw == 'the zombies':
                label.text = '[color=#00FF00]Logged in successfully![/color]'
                # main.App.get_running_app().root.current = 'home'
                # main.MDApp.get_running_app().root_window 
            else:
                label.text = '[color=#FF0000]Invalid username and/or password[/color]'

class SignUp(Screen):
    def anim(self, widget):
        anima =  Animation(pos_hint={'center_y': 1.16})
        anima.start(widget)

    def anim_draw(self, widget):
        anima =  Animation(pos_hint={'center_y': .85})
        anima.start(widget)

    def icons(self, widget):
       anima =  Animation(pos_hint={'center_y': .8})
       anima += Animation(pos_hint={'center_y': .85})
       anima.start(widget)

    def text(self, widget):
       anima =  Animation(opacity=0.5, duration=2)
       anima += Animation(opacity=1, pos_hint={'center_y': .75})
       anima.start(widget)