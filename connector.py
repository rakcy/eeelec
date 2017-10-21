#from wifi import Cell
#from wifi.scan import subprocess, cells_re
from jnius import autoclass, cast

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
    
    #ConnectivityManager = autoclass('android.net.ConnectivityManager')
    #WifiConfiguration = autoclass('android.net.wifi.WifiConfiguration')
    
    #Activity = autoclass('android.app.Activity')

    beacons = []

    def all(self):
        '''
        wifi = cast(self.ConnectivityManager,
                    self.activity.getSystemService(self.Context.WIFI_SERVICE))
        '''
        Context = autoclass('android.content.Context')
        #WifiManager = autoclass('android.net.wifi.WifiManager')
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        activity = PythonActivity.mActivity
        #wifi = activity.getSystemService(Context.WIFI_SERVICE)
        WifiManager = autoclass('android.net.wifi.WifiManager')
        return wifi.getScanResults()