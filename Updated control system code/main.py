import time
from machine import Pin, RTC, I2C
from math import fabs, floor
import uasyncio
import queue
# from lux_sensor_main import i2c2, light_sensor2
# import lux_sensor_main
from bh1750 import BH1750
import limSwitch
import manualMotor

# Initialize light sensors
# i2c1 = I2C(0, scl=Pin(21), sda=Pin(20))
i2c2 = I2C(1, scl=Pin(19), sda=Pin(18))
# Create an instance of the BH1750 class
# light_sensor1 = BH1750(i2c1)
light_sensor2 = BH1750(i2c2)

limSwitch.swHit = 0
# botLim = Pin(14, Pin.IN)
# topLim = Pin(15, Pin.IN)
# swHit = 0     #1 for bottom hit, 2 for top hit

CW = 0
CCW = 1
SPR = 200        #steps per revolution in full step mode
up = CW
down = CCW

led = Pin("LED", Pin.OUT)
EN = Pin(11, Pin.OUT)
DIR = Pin(16, Pin.OUT)
STEP = Pin(17, Pin.OUT)
#initilialize motor
EN.low()
DIR.value(up)
led.low()

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000
rpm = 60
stepDelay = (30)/(rpm*SPR) #milliseconds, 5 ms/step, delay=2.5ms
rest = 10 #How long to rest between each findLight

# def lim_handler(sw):
#     print("Limit hit")
#     global swHit
#     swHit = sw
# 
# botLim.irq(triggermachine.Pin.IRQ_RISING, handler=lim_handler(1))
# topLim.irq(triggermachine.Pin.IRQ_RISING, handler=lim_handler(2))

async def asyncRotateMotor(direction, delay, steps):
    for x in range(steps):
        #if switch hit and interrupt, stop motor movement
        if limSwitch.swHit==1 and direction==down:
            break
        elif limSwitch.swHit==2 and direction==up:
            break
        elif limSwitch.swHit==1 and direction==up:
            limSwitch.swHit = 0
        elif limSwitch.swHit==2 and direction==down:
            limSwitch.swHit = 0
            
        if not ((limSwitch.currSteps<=0 and direction==down) or (limSwitch.currSteps>=total_steps and direction==up)):
            DIR.value(direction)
            STEP.high()
            await uasyncio.sleep(delay/4)
            #time.sleep(delay)
            STEP.low()
            await uasyncio.sleep(delay/4)
            #time.sleep(delay)
            
            if direction == up:
                limSwitch.currSteps += 1
            else:
                limSwitch.currSteps -= 1
       
    return limSwitch.currSteps


#Lux noise threshold, move adjust reflectors if change in lux is greater than this
luxNzThrs = 10
# #Need to check if CW corresponds to up, start findLight for the first time with this direction, reflectors at bottom
# direction = up

async def findLight(direction, stepDelay):
    EN.low()
    #lux1 = light_sensor1.luminance(BH1750.CONT_HIRES_1)
#     light_sensor2.set_mode(BH1750.CONT_HIRES_1)
    lux2 = light_sensor2.luminance(BH1750.ONCE_HIRES_1)
    #prevLux = (lux1+lux2)/2
    prevLux = lux2

    #direction = up      #Need to check if CW corresponds to up, start findLight routine when reflectors are at bottom
    baseSteps = 200    #Number of steps to rotate initially for finding light, decreases as direction changes, to hone in
    steps = baseSteps
    print("currSteps: ", limSwitch.currSteps)
    print("direction: ", direction)
    await asyncRotateMotor(direction, stepDelay, steps)
    print("currSteps: ", limSwitch.currSteps)
    #lux1 = light_sensor1.luminance(BH1750.CONT_HIRES_1)
    lux2 = light_sensor2.luminance(BH1750.CONT_HIRES_1)
    #lux = (lux1+lux2)/2
    lux = lux2
    
    while True:
        #Motor active
        EN.low()
        #"Borrow" from the queue in case interrupted
        
        if limSwitch.swHit==0:
            #optimal spot not found yet
            if lux - prevLux > fabs(luxNzThrs):
                if lux > prevLux:
                    #Continue in the direction that reflectors were already moving
                    await asyncRotateMotor(direction, stepDelay, steps)
                else:
                    #Reverse reflector direction and reduce amount reflectors move
                    direction = ~direction
                    steps = floor(0.75*steps)
                    await asyncRotateMotor(direction, stepDelay, steps)
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
            if lux - prevLux > fabs(luxNzThrs):
                if lux < prevLux:
                    await asyncRotateMotor(direction, stepDelay, steps)
                    limSwitch.swHit = 0
            else:
                #stay at limit, begin going away from limit at next check
                break
        
        prevLux = lux
        # Measure the ambient light in lux
        #lux1 = light_sensor1.luminance(BH1750.CONT_HIRES_1)
        lux2 = light_sensor2.luminance(BH1750.CONT_HIRES_1)
        #lux = (lux1+lux2)/2
        #print(f"Ambient light level: {lux} lux")
        lux = lux2
        
    return direction
            
            
async def posRst():
    while limSwitch.swHit==0:
        limSwitch.currSteps = 2*total_steps
        await asyncRotateMotor(down, stepDelay, 200)
    limSwitch.currSteps = 0
    

async def main():
    
    # Queue for passing messages, initialize with currSteps = 0
    #q = queue.Queue()
    limSwitch.currSteps = 0
    
    await posRst()  #currSteps should be 0 here
    direction = up
    
    
    #coroutine for checking for manual motor control mode
    uasyncio.create_task(manualMotor.waitManual())
    
    print("currSteps: ", limSwitch.currSteps)
    while True:
        print("Finding light")
        direction = await findLight(direction, stepDelay)
        
        #Motor sleep
        EN.high()
        
        print("Found light. CurrSteps: ", limSwitch.currSteps)
        await uasyncio.sleep(rest)
        
        
if __name__ == "__main__":
    uasyncio.run(main())
#     direction = up
#     currSteps = 0
#     while True:
#         direction = await findLight(direction, stepDelay, currSteps)
#         #Motor sleep
#         await uasyncio.sleep(rest)
    
    

