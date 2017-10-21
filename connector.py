#from wifi import Cell
#from wifi.scan import subprocess, cells_re
from jnius import autoclass, cast
import json

'''
class Linux(Cell):
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
'''


class Android(object):
    Context = autoclass('android.content.Context')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    def all(self):
        # WifiManager
        wifi = self.activity.getSystemService(self.Context.WIFI_SERVICE)

        return [x.SSID for x in wifi.getScanResults().toArray()]

    def start(self):
        pass