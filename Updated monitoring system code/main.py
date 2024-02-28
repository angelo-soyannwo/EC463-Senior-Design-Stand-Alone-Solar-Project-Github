# Import necessary libraries
import machine, utime, onewire, ds18x20
from ina219 import INA219
from bh1750 import BH1750

# Initialize I2C for INA219 and BH1750
i2c_ina219 = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
i2c_bh1750 = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))  # Adjust pins as necessary

# INA219 sensor setup
sensor_ina219 = INA219(i2c_ina219, 0x40)

# BH1750 light sensor setup
sensor_bh1750 = BH1750(i2c_bh1750, 0x23)

# Function to calculate actual voltage considering the voltage divider
def actual_voltage(measured_voltage):
    # divider_ratio = 4.67 / (5.6+4.67)  # R2 / (R2+R1), use when necessary
    return measured_voltage

# Initialize DS18B20 temperature sensor
ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

# Main loop
while True:
    # INA219 sensor data reading
    try:
        measured_voltage = sensor_ina219.getBusVoltage_V()  # Bus Voltage in volts
        current = sensor_ina219.getCurrent_mA()  # Current in milliamps     # Connect Vin of INA219 to the + of load
        adjusted_voltage = actual_voltage(measured_voltage)  # Adjusted voltage in volts
        print(f"Adjusted Voltage: {adjusted_voltage:.2f} V, Current: {current:.2f} mA")
    except Exception as e:
        print("INA219 read error:", e)

    # DS18B20 sensor data reading
    ds_sensor.convert_temp()
    utime.sleep_ms(750)  # Wait for DS18B20 conversion
    for rom in roms:
        tempC = ds_sensor.read_temp(rom)
        tempF = tempC * (9/5) + 32
        print(f"DS18B20 Temperature (ºC): {tempC:.2f}, Temperature (ºF): {tempF:.2f}")

    # BH1750 sensor data reading for solar irradiation
    try:
        lux = sensor_bh1750.luminance(BH1750.ONCE_HIRES_1)
        solar_irradiation = lux / 126.7
        print("Solar Irradiation: {:.2f} W/m²".format(solar_irradiation))
    except OSError as e:
        print("Failed to read from BH1750 sensor, error:", e)

    # Sleep for a short duration (adjust as needed)
    utime.sleep(2)
