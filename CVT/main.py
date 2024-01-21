
# Import necessary libraries
import machine, utime, onewire, ds18x20, time
from ina219 import INA219

# Initialize I2C for INA219
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
sensor = INA219(i2c)

# Function to calculate actual voltage considering the voltage divider
def actual_voltage(measured_voltage):
    # divider_ratio = 4.67 / (5.6+4.67)  # R2 / (R2+R1), use when necessary
    return measured_voltage

# Initialize DS18B20 temperature sensor
ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
#print('Found DS devices: ', roms)

# Main loop
while True:
    # INA219 sensor data reading
    try:
       # Measure bus voltage and current
        measured_voltage = sensor.getBusVoltage_V()  # Bus Voltage in volts
        current = sensor.getCurrent_mA()  # Current in milliamps

        # Adjust voltage based on the voltage divider
        adjusted_voltage = actual_voltage(measured_voltage)  # Adjusted voltage in volts
        print(f"Adjusted Voltage: {adjusted_voltage:.2f} V, Current: {current:.2f} mA")
    except Exception as e:
        print("INA219 read error:", e)

    # DS18B20 sensor data reading
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        tempC = ds_sensor.read_temp(rom)
        tempF = tempC * (9/5) + 32
        print(f"DS18B20 Temperature (ºC): {tempC:.2f}, Temperature (ºF): {tempF:.2f}")

    # Sleep for a short duration (adjust as needed)
    time.sleep(2)
