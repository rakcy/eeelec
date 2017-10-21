from wifi import Cell
from wifi.scan import subprocess, cells_re

class Wifi(Cell):
    def all(cls):
        """
        Returns a list of all cells extracted from the output of iwlist.
        """
        try:
            iwlist_scan = subprocess.check_output(['/sbin/iwlist', 'scan'],
                                                  stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            raise InterfaceError(e.output.strip())
        else:
            iwlist_scan = iwlist_scan.decode('utf-8')
        cells = map(Cell.from_string, cells_re.split(iwlist_scan)[1:])

        return cells

#c = list of scanned wifi

def scan( length ):
    c=Wifi().all()
    print c 
    int(length)
    beacon = []

    list_len=len(c) #get length of list c
    print list_len
    for ssid_idx in range(0,list_len):
        if len(c[ssid_idx].ssid) == length:
            ssid = c[ssid_idx].ssid
            beacon.append(ssid)
            print beacon
    return

scan(10)

