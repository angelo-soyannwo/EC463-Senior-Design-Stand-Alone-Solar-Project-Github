from machine import Pin
from time import sleep

botLim = Pin(14, Pin.IN, Pin.PULL_UP)
topLim = Pin(15, Pin.IN, Pin.PULL_UP)
swHit = 0     #1 for bottom hit, 2 for top hit
currSteps = 0

led = Pin("LED", Pin.OUT)
led.on()

def lim_handler(pin):
    global swHit
    global currSteps
    if pin==botLim:
        swHit = 1
        currSteps = 0
        print("bottom hit")
    else:
        swHit = 2
        print("top hit")
    led.high()
    print("14: ", botLim.value())
    print("15: ", topLim.value())
    

botLim.irq(trigger=Pin.IRQ_FALLING, handler=lim_handler)
topLim.irq(trigger=Pin.IRQ_FALLING, handler=lim_handler)

if __name__ == "__main__":
    led.low()
    sleep(0.5)
    led.high()
    sleep(0.5)
    led.low()
    
    while True:
        print("botLim: ", botLim.value())
        print(swHit)
        sleep(0.5)
        led.low()
