import time
from machine import Pin, RTC

dir_pin = 18
step_pin = 17
CW = 1
CCW = 0
SPR = 200        #steps per revolution in full step mode

led = Pin("LED", Pin.OUT)
DIR = Pin(18, Pin.OUT)
STEP = Pin(17, Pin.OUT)
EN = Pin(15, Pin.OUT)
#initilialize direction
EN.high()
DIR.value(CW)
led.low()

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000
delay = 0.01

currSteps = 0

def rotateMotor(steps, direction, delay, currSteps):
    for x in range(steps):
        DIR.value(direction)
        STEP.high()
        time.sleep(delay)
        STEP.low()
        time.sleep(delay)
        
        if direction == CW:
            currSteps += 1
        else:
            currSteps -= 1
            
    return currSteps

print("here")
#current = rotateMotor(total_steps,CW,delay,currSteps)
#print(current)
EN.low()
for x in range(total_steps):
        STEP.high()
        time.sleep(delay)
        STEP.low()
        time.sleep(delay)