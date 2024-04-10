from machine import Pin
import time

up_pin = 2
down_pin = 3
select_pin = 0

UP = Pin(up_pin, Pin.IN, Pin.PULL_DOWN)
DOWN = Pin(down_pin, Pin.IN, Pin.PULL_DOWN)
OK = Pin(select_pin, Pin.IN)

if __name__ == "__main__":
    while True:
        print(OK.value())
        time.sleep(1)