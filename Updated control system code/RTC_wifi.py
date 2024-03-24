import network
from machine import Pin, RTC
import rp2
import sys
import utime as time
import usocket as socket
import ustruct as struct

led = Pin("LED", Pin.OUT)
led.low()

ssid, password = "DARLIE", "8TIERrack!"
#ssid, password = "BU Guest (unencrypted)", ""

# Timezone offset from GMT
GMT_OFFSET = 3600 * 4 # 3600 = 1 h (wintertime)

# NTP-Host
NTP_HOST = 'pool.ntp.org'

# Retrieve time from NTP Server
def getTimeNTP():
    NTP_DELTA = 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(NTP_HOST, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(2)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    except:
        for x in range(4):
            led.high()
            time.sleep(0.1)
            led.low()
            time.sleep(0.1)        
    finally:
        s.close()
    ntp_time = struct.unpack("!I", msg[40:44])[0]
    return time.gmtime(ntp_time - NTP_DELTA - GMT_OFFSET)

# Copy time to PI pico´s RTC
def setTimeRTC(rtc):
    tm = getTimeNTP()
    rtc.datetime((tm[0], tm[1], tm[2], 0, tm[3], tm[4], tm[5], 0))     #weekday cannot be set

def connectWIFI():  
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
        
    max_wait = 5
    print('Waiting for connection')
    #try:
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1    
        time.sleep(1)
    status = None
    if wlan.status() != 3:
        for x in range(2):
            led.high()
            time.sleep(0.2)
            led.low()
            time.sleep(0.2) 
        raise RuntimeError('Connections failed')
        
    else:
        status = wlan.ifconfig()
        print('connection to', ssid,'succesfull established!', sep=' ')
        print('IP-adress: ' + status[0])
    ipAddress = status[0]
    #except:
        


if __name__ == "__main__":
    connectWIFI()  
    rtc = RTC()  
    setTimeRTC(rtc)
    print()
    #print(rtc.datetime())                    #yr,mnth,dy,wkdy,hr,min,sec,subsec
    print(time.localtime())                  #yr,mnth,dy,hr,min,sec,wkdy,yrdy --- Still based on RTC
    #print(time.mktime(rtc.datetime()))       #Don't use rtc.datetime to convert to epoch seconds
    print(time.mktime(time.localtime()))     #Must use localtime, NOT datetime (order is different)
