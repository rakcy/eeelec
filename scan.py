from wifi import Cell


#c = list of scanned wifi

def scan( length ):
    c=Cell().all('wlo1')
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

