from machine import Pin
import time
import uasyncio
import queue
import limSwitch

up_pin = 2
down_pin = 3
select_pin = 0

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

# botLim = Pin(14, Pin.IN)
# topLim = Pin(15, Pin.IN)
# swHit = 0     #1 for bottom hit, 2 for top hit

total_rotations = 20
total_steps = SPR*total_rotations    #200*20 = 4000
rpm = 60
stepDelay = (30)/(rpm*SPR) #seconds, 7.5 ms/step, delay=3.75ms

# def lim_handler(sw):
#     print("Limit hit")
#     global swHit
#     swHit = sw
# 
# botLim.irq(triggermachine.Pin.IRQ_RISING, handler=lim_handler(1))
# topLim.irq(triggermachine.Pin.IRQ_RISING, handler=lim_handler(2))

def rotateMotor(direction, stepDelay, steps):
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
            print(limSwitch.currSteps)
            DIR.value(direction)
            STEP.high()
            time.sleep(stepDelay)
            STEP.low()
            time.sleep(stepDelay)
        
            if direction == CW:
                limSwitch.currSteps += 1
            else:
                limSwitch.currSteps -= 1       

async def rotateMotor_manual():
#     global limSwitch.swHit
    while OK.value()==1:
        pass
    while OK.value()==0:
        if limSwitch.swHit==0:
            if UP.value():
                rotateMotor(up, stepDelay, 1)
            elif DOWN.value():
                rotateMotor(down, stepDelay, 1)
        elif limSwitch.swHit==1:
            if UP.value():
                rotateMotor(up, stepDelay, 1)
                limSwitch.swHit = 0
        elif limSwitch.swHit==2:
            if DOWN.value():
                rotateMotor(down, stepDelay, 1)
                limSwitch.swHit = 0
    
            
async def waitManual():
    while True:
        print("waiting")
        print(limSwitch.currSteps)
        while OK.value()==1:
            pass
        while OK.value()==0:
            await uasyncio.sleep(0.001)
        EN.low()
        print("manual")   
        await rotateMotor_manual()
        EN.high()
    
        
async def main():
    #q = queue.Queue()
    limSwitch.currSteps = 2000
    await waitManual()
        
if __name__ == "__main__":
    uasyncio.run(main())