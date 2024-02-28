from machine import I2C, Pin
from bh1750 import BH1750  # Assuming the class you provided is saved in a file named bh1750.py
import utime

def calculate_solar_irradiation(lux):
    # Convert lux to solar radiation in W/m^2
    solar_radiation = lux / 126.7       #Converting lux into solar radiation

    # Determine the clearness index
    if lux < 15:
        clearness_index = 0.3     #0.3 means cloudy, 0.8 means bright sunny day. Lux has been tested
    elif 15 <= lux < 20:  
        clearness_index = 0.5
    else:
        clearness_index = 0.8

    # Angle of incidence adjustment
    angle_of_incidence_adjustment = 0.80   # varies from 0.75 to 0.85 in boston. 0.80 is average

    # Calculate solar irradiation
    solar_irradiation = solar_radiation * clearness_index * angle_of_incidence_adjustment
    return round(solar_irradiation, 3)  # Round to 3 decimal places

def main():
    # Initialize I2C bus for Raspberry Pi Pico
    i2c = I2C(0, scl=Pin(21), sda=Pin(20))

    # Create an instance of the BH1750 class
    light_sensor = BH1750(i2c)

    while True:
        # Measure the ambient light in lux
        lux = light_sensor.luminance(BH1750.CONT_HIRES_1)
        #print(f"Ambient light level: {lux} lux")

        # Calculate and print solar irradiation
        solar_irradiation = calculate_solar_irradiation(lux)
        print(f"Solar irradiation: {solar_irradiation} Wh/m^2")

        # Wait for a bit before taking another reading
        utime.sleep(3)

if __name__ == "__main__":
    main()
