import machine
import utime
from ina219 import INA219

# Initialize I2C
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
#print(i2c)
# Create an INA219 instance
sensor = INA219(i2c)

# Function to calculate actual voltage considering the voltage divider
def actual_voltage(measured_voltage):
    #divider_ratio = 4.67 / (5.6+4.67)  # R2 / (R2+R1), use when necessary
    return measured_voltage

while True:
    try:
        # Measure bus voltage and current
        measured_voltage = sensor.getBusVoltage_V()  # Bus Voltage in volts
        current = sensor.getCurrent_mA()  # Current in milliamps

        # Adjust voltage based on the voltage divider
        adjusted_voltage = actual_voltage(measured_voltage)  # Adjusted voltage in volts

        # Print results
        print(f"Adjusted Voltage: {adjusted_voltage:.2f} V, Current: {current:.2f} mA")

        # Check for over-voltage
        if adjusted_voltage > 14:
            print("Warning! Voltage exceeds 14V!")

        utime.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        break
