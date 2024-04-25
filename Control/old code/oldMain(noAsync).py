import RTC_wifi1
import time
from machine import Pin, RTC
from math import floor

dir_pin = 18
step_pin = 17
CW = 1
CCW = 0
SPR = 200        #steps per revolution in full step mode

led = Pin("LED", Pin.OUT)
DIR = Pin(18, Pin.OUT)
STEP = Pin(17, Pin.OUT)
#initilialize direction
DIR.value(CW)
led.low()

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000

#For demo purposes, speeds up daily process by a factor of timeFactor.
#Example: timeFactor of 4 allows process of 24 hours to complete in 6 hours.
#Probably want to set time factor of 288 to complete day process in 5 minutes.
timeFactor = 360
top_pauseTime = 3600            #stay in top position for 1 hour
dayStart = 21600             #6 hours (into the day)
dayEnd = 64800               #18 hours (into the day)
operating_daytime = dayEnd - dayStart           #43200 seconds in 12 hours, motor only moves in daytime

def calibrateRTC():
    #Update Pico RTC datetime on startup
    #Change WIFI ssid and password in RTC_wifi module
    RTC_wifi1.connectWIFI()
    rtc = RTC()  
    RTC_wifi1.setTimeRTC(rtc)      # set time, from RTFC_wifi module
    print()
    print(rtc.datetime())      # display current datetime
    led.high()              #show successful calibration

def rotateMotor(steps, direction, delay, currSteps):
    for x in range(steps):
        DIR.value(direction)
        STEP.value(1)
        time.sleep(delay)
        STEP.value(0)
        time.sleep(delay)
        
        if direction == CW:
            currSteps += 1
        else:
            currSteps -= 1
            
    return currSteps
    
    
def dayProcess(timeFactor, operating_daytime, top_pauseTime, total_steps, dayStart, dayEnd):
    currSteps = 0             #increases with CW steps, decreases CCW
    targetSteps = 0
    TFday = 86400/timeFactor   #seconds in a day time factored
    TFdayStart = dayStart/timeFactor
    TFdayEnd = dayEnd/timeFactor
    timeframe = operating_daytime/timeFactor    #Time for day-cycle completion, for demo
    TFtop_pauseTime = top_pauseTime/timeFactor
    
    #Motor stops at the top for 1 hour, not included in delay calculation
    #0.8 to make the delay slightly shorter than exact timeframe, for leeway during time reads
    delay = 0.8*(timeframe - TFtop_pauseTime)/(total_steps*4)  #Example 2sec/(200steps*2) = 0.005 time between each step  
    
    #Used to find current steps position to rotate to, based on time in the day
    step_constant = (2/(timeframe - TFtop_pauseTime))*total_steps
    
    printed = False
    print("Begin")
    
    while True:
        currTime = time.localtime()
        (year,month,day,hour,minute,sec,wkday,yrday) = currTime
        dayBegEpoch = time.mktime((year,month,day,0,0,0,wkday,yrday))
        currEpoch = time.mktime(currTime)
        currDay = currEpoch - dayBegEpoch
        #print("currDay: ", currDay)
        
        #Example: currDay is 3hr:7min:0sec which is 11220 seconds, TFday is 30min=1800sec
        #TFcurrDay is 420sec=7min into the timeframe
        TFcurrDay = currDay % TFday
        
        if TFcurrDay >= TFdayStart and TFcurrDay <= TFdayEnd:
            if TFcurrDay <= TFdayStart + (timeframe - TFtop_pauseTime)/2:
                targetSteps = floor((TFcurrDay - TFdayStart) * step_constant)
#                 print("yo")
#                 print("targetSteps: ", targetSteps)
            elif TFcurrDay >= TFdayStart + (timeframe + TFtop_pauseTime)/2:
                targetSteps = floor(total_steps - (TFcurrDay - (TFdayStart + (timeframe + TFtop_pauseTime)/2))*step_constant)
#                 print("ba")
#                 print("targetSteps: ", targetSteps)

        #Prevent motor from rotating past structure limits    
        if targetSteps < 0 or targetSteps > total_steps:
            raise Exception("targetSteps out of range: ", targetSteps)
        
        if targetSteps >= 0 and targetSteps <= total_steps:
            if currSteps < targetSteps:
                currSteps = rotateMotor(targetSteps - currSteps, CW, delay, currSteps)
            elif currSteps > targetSteps:
                currSteps = rotateMotor(currSteps - targetSteps, CCW, delay, currSteps)
        
        #Only print every 10 seconds, excessive printing slows program down
        if TFcurrDay % 3 == 0:
            if printed == False:
                print("TFcurrDay: ", TFcurrDay)
                print("targetSteps: ", targetSteps)
                print("currSteps: ", currSteps)
                printed = True
        else:
            printed = False
                
 
        
if __name__ == "__main__":
    
    led.high()
    time.sleep(0.5)
    led.low()
       
    try:
        calibrateRTC()
    except:
        pass
    
    dayProcess(timeFactor, operating_daytime, top_pauseTime, total_steps, dayStart, dayEnd)