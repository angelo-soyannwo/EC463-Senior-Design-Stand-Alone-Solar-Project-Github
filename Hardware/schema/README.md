# Brief PCB Netlist Explanation

Netlist Explanations :
 - Load + = Load from solar charge controller
 - Load - = Return path from solar charge controller. This is ground.
 - Vin P + = Positive from solar panels
 - Vin P - = Negative from solar panels
 - 3.3V_M = 3.3V from monitoring pico
 - 3.3V_C = 3.3V from control pico
 - 5V = Input from a 12V-5V converter. This is an external component
 - VCC = Vin -  from the INA219. This is 12V, and is idential to Load+.

