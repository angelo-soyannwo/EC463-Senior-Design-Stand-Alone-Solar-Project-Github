from machine import Pin
import time
from math import floor
# import uasyncio
# import queue
import limSwitch
import globalVars

up_pin = 2
down_pin = 3
select_pin = 4

UP = Pin(up_pin, Pin.IN, Pin.PULL_DOWN)
DOWN = Pin(down_pin, Pin.IN, Pin.PULL_DOWN)
OK = Pin(select_pin, Pin.IN, Pin.PULL_DOWN)

CW = 0
CCW = 1
SPR = 200        #steps per revolution in full step mode
up = CW
down = CCW

led = Pin("LED", Pin.OUT)
EN = Pin(11, Pin.OUT)
DIR = Pin(16, Pin.OUT)
STEP = Pin(17, Pin.OUT)
#initilialize direction
EN.low()
DIR.value(CW)
led.low()

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000
rpm = 100
stepDelay = int(((30)/(rpm*SPR))*(10**6)) #microseconds, 7.5 ms/step, delay=3.75ms
print(stepDelay)


def man_handler(pin):
    globalVars.manualMode = 1
    
OK.irq(trigger=Pin.IRQ_RISING, handler=man_handler)

def rotateMotor(direction, stepDelay, steps):
    for x in range(steps):
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
#             print(globalVars.currSteps)
            DIR.value(direction)
            STEP.high()
            time.sleep_us(stepDelay)
            STEP.low()
            time.sleep_us(stepDelay)
        
            if direction == up:
                globalVars.currSteps += 1
            else:
                globalVars.currSteps -= 1       

def rotateMotor_manual():
    print("Manual mode")
    while OK.value()==1:
        pass
    
    EN.low()
    while OK.value()==0:
        if globalVars.swHit==0:
            if UP.value():
                rotateMotor(up, stepDelay, 1)
            elif DOWN.value():
                rotateMotor(down, stepDelay, 1)
        elif globalVars.swHit==1:
            if UP.value():
                rotateMotor(up, stepDelay, 1)
                globalVars.swHit = 0
        elif globalVars.swHit==2:
            if DOWN.value():
                rotateMotor(down, stepDelay, 1)
                globalVars.swHit = 0
    EN.high()
    print("Auto mode")
    globalVars.manualMode = 0
    
            
# async def waitManual():
#     while True:
#         print("waiting")
#         print(limSwitch.currSteps)
#         while OK.value()==1:
#             pass
#         while OK.value()==0:
#             await uasyncio.sleep(0.001)
#         EN.low()
#         print("manual")   
#         await rotateMotor_manual()
#         EN.high()
#     
        
def main():
    #q = queue.Queue()
    globalVars.currSteps = 2000
    while True:
        rotateMotor_manual()
#     await waitManual()
        
if __name__ == "__main__":
    main()