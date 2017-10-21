__version__ = "1.0"
from scan import scan
from kivy.app import App
from kivy.uix.label import Label

class Hello(App):
    def build(self):
        beacons = scan(10)
        return Label(text=beacons[0])

Hello().run()