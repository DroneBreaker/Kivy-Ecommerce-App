from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.screenmanager import FallOutTransition, ScreenManager
from pages.ui import LoginPage, HomePage, DeliveryPage, Promotions, Restaurant, SignUp, SuperMarket, Drinks, Anything, Pharmacy
from kivyauth.google_auth import initialize_google, login_google, logout_google

Window.size=(300, 600)


class Store(App, MDApp):
    KV_FILES = [
        'store.kv',
        'anything.kv',
        'delivery.kv',
        'drinks.kv',
        'pharmacy.kv',
        'promotions.kv',
        'restaurant.kv',
        'supermarket.kv',
        'login.kv', 
        'signup.kv'
    ]
    CLASSES = {
        'HomePage': 'pages.ui',
        'DeliveryPage': 'pages.ui',
        'Restaurant': 'pages.ui',
        'SuperMarket': 'pages.ui',
        'Anything': 'pages.ui',
        'Drinks': 'pages.ui',
        'Pharmacy': 'pages.ui', 
        'Promotions': 'pages.ui',
        'LoginPage': 'pages.ui',
        'SignUp': 'pages.ui'
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': 'True'})
    ]

    def build_app(self):
        # Window.clearcolor = (1,1,1,1)
        self.theme_cls.theme_style = 'Dark' #/for kivymd
        # initialize_google(self.after_login, self.error_listener)

        sm = ScreenManager(transition=FallOutTransition())
        sm.add_widget(LoginPage())
        sm.add_widget(HomePage())
        sm.add_widget(DeliveryPage())
        sm.add_widget(Restaurant())
        sm.add_widget(SuperMarket())
        sm.add_widget(Anything())
        sm.add_widget(Drinks())
        sm.add_widget(Pharmacy())
        sm.add_widget(Promotions())
        sm.add_widget(SignUp())
        
        return sm

Store().run()