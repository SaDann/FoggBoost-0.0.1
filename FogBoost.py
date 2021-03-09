###Library Imports###

import os
import time
import subprocess
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager , Screen

### Config Window ###
Config.set('graphics', 'resizable', '0'),
Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '330')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

### Class Start ###

class Menu(Screen):
    pass

class Options(Screen):
    pass

class Function(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class LabelButton(ButtonBehavior, Label):
    pass

class FogBoostApp(App):
    def build(self):
        self.icon = os.path.join('config', 'fb.png')
        return WindowManager()


if __name__ == '__main__':
    FogBoostApp().run()
