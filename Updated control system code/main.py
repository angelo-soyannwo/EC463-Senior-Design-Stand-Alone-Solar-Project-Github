import time
from machine import Pin, RTC, I2C
from math import fabs, floor
# import uasyncio
# import queue
# from lux_sensor_main import i2c2, light_sensor2
from lux_sensor_main import luxMain, connect_to_wifi
#from bh1750 import BH1750
import bh1750
import limSwitch
import manualMotor
import globalVars

# Initialize light sensors
i2c1 = I2C(0, scl=Pin(21), sda=Pin(20))
i2c2 = I2C(1, scl=Pin(19), sda=Pin(18))
# Create an instance of the BH1750 class
light_sensor1 = bh1750.BH1750(i2c1)
light_sensor2 = bh1750.BH1750(i2c2)

globalVars.swHit = 0

CW = 0
CCW = 1
SPR = 200        #steps per revolution in full step mode
up = CW
down = CCW

led = Pin("LED", Pin.OUT)
EN = Pin(11, Pin.OUT)
SLP = Pin(13, Pin.OUT)
RST = Pin(12, Pin.OUT)
DIR = Pin(16, Pin.OUT)
STEP = Pin(17, Pin.OUT)
#initilialize motor
EN.low()
SLP.high()
RST.high()
DIR.value(up)
led.low()

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000
rpm = 60
stepDelay = int(((30)/(rpm*SPR))*(10**6)) #microseconds, 7.5 ms/step, delay=3.75ms
print(stepDelay)
rest = 10 #How long to rest between each findLight

def RotateMotor(direction, delay, steps):
    MM = 0
    for x in range(steps):
        #check manual mode flag
        if globalVars.manualMode:
            manualMotor.rotateMotor_manual()
            MM = 1
            break
        
        #if switch hit and interrupt, stop motor movement
        if globalVars.swHit==1 and direction==down:
            break
        elif globalVars.swHit==2 and direction==up:
            break
        elif globalVars.swHit==1 and direction==up:
            EN.low()
            globalVars.swHit = 0
        elif globalVars.swHit==2 and direction==down:
            EN.low()
            globalVars.swHit = 0
            
        if not ((globalVars.swHit==1 and direction==down) or (globalVars.swHit==2 and direction==up)):
            DIR.value(direction)
            STEP.high()
            time.sleep_us(delay)
            #time.sleep(delay)
            STEP.low()
            time.sleep_us(delay)
            #time.sleep(delay)
            
            if direction == up:
                globalVars.currSteps += 1
            else:
                globalVars.currSteps -= 1
       
    return MM


#Lux noise threshold, move adjust reflectors if change in lux is greater than this
luxNzThrs = 20

def findLight(direction, stepDelay):
    #check manual mode flag
    if globalVars.manualMode:
        manualMotor.rotateMotor_manual()
        return direction
    EN.low()
    lux1 = light_sensor1.luminance(bh1750.BH1750.CONT_HIRES_1)
#     light_sensor2.set_mode(bh1750.BH1750.CONT_HIRES_1)
    lux2 = light_sensor2.luminance(bh1750.BH1750.ONCE_HIRES_1)
    prevLux = (lux1+lux2)/2
#     prevLux = lux2

    #direction = up      #Need to check if CW corresponds to up, start findLight routine when reflectors are at bottom
    baseSteps = 700    #Number of steps to rotate initially for finding light, decreases as direction changes, to hone in
    steps = baseSteps
    print("currSteps: ", globalVars.currSteps)
    print("direction: ", direction)
    MM = RotateMotor(direction, stepDelay, steps)
    if MM:
        return direction
    print("currSteps: ", globalVars.currSteps)
    lux1 = light_sensor1.luminance(bh1750.BH1750.CONT_HIRES_1)
    lux2 = light_sensor2.luminance(bh1750.BH1750.CONT_HIRES_1)
    lux = (lux1+lux2)/2
    #lux = lux2
    
    while True:
        #check manual mode flag
        if globalVars.manualMode:
            manualMotor.rotateMotor_manual()
            break
        #Motor active
        EN.low()
        #"Borrow" from the queue in case interrupted
        
        if globalVars.swHit==0:
            #optimal spot not found yet
            print("lux-prevLux: ", lux-prevLux)
            if fabs(lux - prevLux) > (luxNzThrs):
                if lux > prevLux:
                    #Continue in the direction that reflectors were already moving
                    MM = RotateMotor(direction, stepDelay, steps)
                    if MM:
                        break
                else:
                    #Reverse reflector direction and reduce amount reflectors move
                    direction = ~direction
                    steps = floor(0.75*steps)
                    MM = RotateMotor(direction, stepDelay, steps)
                    if MM:
                        break
            #optimal spot found
            else:
                #reset rotation amount to full amount for the next time reflectors need to find light
                steps = baseSteps
                break
        
        #If reflectors at limits
        else:
            #reverse direction
            direction = ~direction
            #optimal spot not found yet, go reverse direction, no longer at limit
            if fabs(lux - prevLux) > luxNzThrs:
                if lux < prevLux:
                    MM = RotateMotor(direction, stepDelay, steps)
                    globalVars.swHit = 0
                    if MM:
                        break
            else:
                #stay at limit, begin going away from limit at next check
                break
        
        prevLux = lux
        # Measure the ambient light in lux
        lux1 = light_sensor1.luminance(bh1750.BH1750.CONT_HIRES_1)
        lux2 = light_sensor2.luminance(bh1750.BH1750.CONT_HIRES_1)
        lux = (lux1+lux2)/2
        #print(f"Ambient light level: {lux} lux")
        #lux = lux2
        
    return direction
            
            
def posRst():
    EN.low()
    print("Initializing")
    
    while globalVars.swHit==0:
        #check manual mode flag
        if globalVars.manualMode:
            manualMotor.rotateMotor_manual()
        
        globalVars.currSteps = 2*total_steps
        RotateMotor(down, stepDelay, 200)

    globalVars.currSteps = 0
    

def main():
    connect_to_wifi("BU Guest (unencrypted)", "")
    
    # Queue for passing messages, initialize with currSteps = 0
    #q = queue.Queue()
    globalVars.currSteps = 0
    posRst()  #currSteps should be 0 here
    direction = up
    
    
    #coroutine for checking for manual motor control mode
    #uasyncio.create_task(manualMotor.waitManual())
    
    print("currSteps: ", globalVars.currSteps)
    while True:
        #Sending light sensor data to database
        lux1 = light_sensor1.luminance(bh1750.BH1750.CONT_HIRES_1)
        lux2 = light_sensor2.luminance(bh1750.BH1750.CONT_HIRES_1)
        luxMain(lux1, lux2)
        
        for x in range(4):
            led.high()
            time.sleep(0.2)
            led.low()
            time.sleep(0.2)
        
        print("Finding light")
        direction = findLight(direction, stepDelay)
        
        #Motor sleep
        EN.high()
        
        print("Found light. CurrSteps: ", globalVars.currSteps)
        
        for x in range(rest/0.005):
            #check manual mode flag every 5 ms
            if globalVars.manualMode:
                manualMotor.rotateMotor_manual()
            time.sleep(0.005)    
            
        #await uasyncio.sleep(rest)
        
        
if __name__ == "__main__":
    #uasyncio.run(main())
    main()