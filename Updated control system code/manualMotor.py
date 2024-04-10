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

def rotateMotor(direction, stepDelay, steps, currSteps):
    for x in range(steps):
        #if switch hit and interrupt, stop motor movement
        if limSwitch.swHit==1 and direction==down:
            break
        if limSwitch.swHit==2 and direction==up:
            break
        if limSwitch.swHit==1 and direction==up:
            swHit = 0
        if limSwitch.swHit==2 and direction==down:
            swHit = 0
            
        if not ((currSteps<=0 and direction==down) or (currSteps>=total_steps and direction==up)):
            print(currSteps)
            DIR.value(direction)
            STEP.high()
            time.sleep(stepDelay)
            STEP.low()
            time.sleep(stepDelay)
        
            if direction == CW:
                currSteps += 1
            else:
                currSteps -= 1       
    return currSteps

async def rotateMotor_manual(q, currSteps):
#     global limSwitch.swHit
    while OK.value()==1:
        pass
    while OK.value()==0:
        if limSwitch.swHit==0:
            if UP.value():
                currSteps = rotateMotor(up, stepDelay, 1, currSteps)
            elif DOWN.value():
                currSteps = rotateMotor(down, stepDelay, 1, currSteps)
        elif limSwitch.swHit==1:
            if UP.value():
                currSteps = rotateMotor(up, stepDelay, 1, currSteps)
                limSwitch.swHit = 0
        elif limSwitch.swHit==2:
            if DOWN.value():
                currSteps = rotateMotor(down, stepDelay, 1, currSteps)
                limSwitch.swHit = 0
    
    await q.put(currSteps)
            
async def waitManual(q):
    while True:
        print("waiting")
        while OK.value()==1:
            pass
        while OK.value()==0:
            await uasyncio.sleep(0.1)
        EN.low()
        print("manual")   
        currSteps = await q.get()
        await rotateMotor_manual(q, currSteps)
        EN.high()
    
        
async def main():
    q = queue.Queue()
    currSteps = 0
    await q.put(currSteps)
    await waitManual(q)
        
if __name__ == "__main__":
    uasyncio.run(main())