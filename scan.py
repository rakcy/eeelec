from connector import Android
from time import time, sleep

class Scanner(object):
    beacons = []
    mine = "6666666666"

    def scan(self, length=10):
        w = Android()

        c = w.all()

        for ssid in c:
            if len(ssid) == length and ssid.isdigit() \
               and ssid not in self.beacons:
                self.beacons.append(ssid)

        return self.beacons

    def startHotspot(self):
        pass

    def run(self, length=10, alive=1):
        self.beacon = []
        start = time()
        while(time() - start < 1):
            self.scan(length)

        start = time()
        while(time() - start < 1):
            self.startHotspot()

        return self.beacons