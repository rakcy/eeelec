from scan import Scanner
from time import sleep

s = Scanner()
while(True):
    beacons = s.run()

    print(beacons)

    sleep(4)