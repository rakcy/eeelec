from connector import Android
from time import time, sleep

class Scanner(object):
    beacons = []

    def scan(self, length=10):
        w = Android()
        return w.all()
    '''
        c = w.all()

        for ssid_idx in range(0,len(c)):
            ssid = c[ssid_idx].ssid

            if len(ssid) == length and ssid.isdigit() \
               and ssid not in self.beacons:
                self.beacons.append(ssid)

        return self.beacons
    '''

    '''
    def run(self, length=10, alive=1):
        self.beacon = []
        start = time()
        while(time() - start < 1):
            self.scan(length)

        start = time()
        while(time() - start < 1):
            pass

        return self.beacons
    '''