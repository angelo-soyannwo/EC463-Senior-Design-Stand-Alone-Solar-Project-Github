import RTC_wifi
import time
from machine import Pin, RTC
from math import floor
import asyncMC
import uasyncio
import queue

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
timeFactor = 288
top_pauseTime = 3600            #stay in top position for 1 hour
dayStart = 21600             #6 hours (into the day)
dayEnd = 64800               #18 hours (into the day)
#operating_daytime = dayEnd - dayStart           #43200 seconds in 12 hours, motor only moves in daytime

def calibrateRTC():
    #Update Pico RTC datetime on startup
    #Change WIFI ssid and password in RTC_wifi module
    RTC_wifi.connectWIFI()
    rtc = RTC()  
    RTC_wifi.setTimeRTC(rtc)      # set time, from RTFC_wifi module
    print()
    print(time.localtime())      # display current datetime
    led.high()              #show successful calibration

def rotateMotor(steps, direction, delay, currSteps):
    for x in range(steps):
        DIR.value(direction)
        STEP.high()
        uasyncio.sleep(delay)
        STEP.low()
        uasyncio.sleep(delay)
        
        if direction == CW:
            currSteps += 1
        else:
            currSteps -= 1       
    return currSteps
    
def TFoperations(timeFactor, top_pauseTime, total_steps, dayStart, dayEnd):
    TFday = 86400/timeFactor   #seconds in a day time factored
    operating_daytime = dayEnd - dayStart
    TFdayStart = dayStart/timeFactor
    TFdayEnd = dayEnd/timeFactor
    timeframe = operating_daytime/timeFactor    #Time for day-cycle completion, for demo
    TFtop_pauseTime = top_pauseTime/timeFactor
    
    #Motor stops at the top for 1 hour, not included in delay calculation
    #0.8 to make the delay slightly shorter than exact timeframe, for leeway during time reads
    delay = 0.8*(timeframe - TFtop_pauseTime)/(total_steps*4)  #Example 2sec/(200steps*2) = 0.005 time between each step  
    
    #Used to find current steps position to rotate to, based on time in the day
    step_constant = (2/(timeframe - TFtop_pauseTime))*total_steps
    
    return TFday, operating_daytime, TFdayStart, TFdayEnd, timeframe, TFtop_pauseTime, delay, step_constant

async def dayProcess(q, timeFactor, top_pauseTime, total_steps, dayStart, dayEnd):
    currSteps = 0             #increases with CW steps, decreases CCW
    targetSteps = 0
    TFday, operating_daytime, TFdayStart, TFdayEnd, timeframe, TFtop_pauseTime, delay, step_constant = TFoperations(timeFactor, top_pauseTime, total_steps, dayStart, dayEnd)
    
    printed = False
    print("Begin")
    
    while True:
        if not q.empty():
            update = await q.get()
            if update[0]==0:   #updated RTC
                #reflectors go back to bottom?
                #not for now:
                pass
            elif update[0]==1:
                #non-async manual_motor in asyncMC
                #manual motor mode is done, reset reflectors back to bottom with limit switch
                pass
            elif update[0]==2:
                print(dayStart)
                print(TFdayStart)
                dayStart, dayEnd, top_pauseTime = update[1:]
                TFday, operating_daytime, TFdayStart, TFdayEnd, timeframe, TFtop_pauseTime, delay, step_constant = TFoperations(timeFactor, top_pauseTime, total_steps, dayStart, dayEnd)
                print(dayStart)
                print(TFdayStart)
            elif update[0]==3:
                timeFactor = update[1]
                TFday, operating_daytime, TFdayStart, TFdayEnd, timeframe, TFtop_pauseTime, delay, step_constant = TFoperations(timeFactor, top_pauseTime, total_steps, dayStart, dayEnd)
        
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
        
        #Only print every 10 seconds, printing slows program down
        if TFcurrDay % 10 == 0:
            if printed == False:
                print("TFcurrDay: ", TFcurrDay)
                print("targetSteps: ", targetSteps)
                print("currSteps: ", currSteps)
                printed = True
        else:
            printed = False
        
        await uasyncio.sleep(0.005)

async def main():
    q = queue.Queue()
    
    #LCD screen coroutine
    uasyncio.create_task(asyncMC.menu(q, dayStart, dayEnd, top_pauseTime, timeFactor))
    
    led.high()
    uasyncio.sleep(0.5)
    led.low()
    try:
        calibrateRTC()
    except:
        print("Warning: Time not calibrated")
        print(time.localtime())
        print("Calibrate time manually")
        #ManualController.RTC_manual()
        #pass
    
    #On LCD: "Set reflectors to lowest position."
    #Actually: reset to lowest position using limit switch on startup
    print("dayProcess started")
    await dayProcess(q, timeFactor, top_pauseTime, total_steps, dayStart, dayEnd)
    print("dayProcess ended")
    
if __name__ == "__main__":
    uasyncio.run(main())
    
    