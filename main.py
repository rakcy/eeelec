__version__ = "1.0"
from scan import Scanner
from kivy.app import App
from kivy.uix.label import Label

class Main(App):
    def build(self):
        try:
            s = Scanner()
            beacons = s.run()
            return Label(text=str(beacons))
        except Exception as e:
            return Label(text=str(e))

Main().run()