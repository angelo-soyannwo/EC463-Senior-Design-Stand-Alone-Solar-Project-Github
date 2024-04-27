from machine import Pin
import utime

# Define pin numbers
trigger_pin = 0
echo_pin = 1

# Initialize pins
trigger = Pin(trigger_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)

def get_distance():
    # Ensure trigger starts low
    trigger.low()
    utime.sleep_us(5)

    # Trigger the sensor
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Wait for the echo pin to go high (start of the pulse)
    while echo.value() == 0:
        pass

    start = utime.ticks_us()  # Record the time when echo goes high

    # Wait for the echo pin to go low (end of the pulse)
    while echo.value() == 1:
        pass

    end = utime.ticks_us()  # Record the time when echo goes low

    # Calculate the duration of the pulse
    pulse_duration = utime.ticks_diff(end, start)

    # Distance calculation (speed of sound is 34300 cm/s)
    distance = (pulse_duration / 2) / 29.1

    return distance

while True:
    distance = get_distance()
    print("Distance: {:.2f} cm".format(distance))
    utime.sleep(1)


