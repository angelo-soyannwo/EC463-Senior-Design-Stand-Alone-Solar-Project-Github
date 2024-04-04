# Import necessary libraries
import machine, utime, onewire, ds18x20
from ina219 import INA219

import json
import network
import urequests as requests
import time
import machine
#from bh1750 import BH1750

# Initialize I2C for INA219 and BH1750
i2c_ina219 = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
#i2c_bh1750 = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))  # Adjust pins as necessary

# INA219 sensor setup
sensor_ina219 = INA219(i2c_ina219, 0x40)

# BH1750 light sensor setup
#sensor_bh1750 = BH1750(i2c_bh1750, 0x23)

# Function to calculate actual voltage considering the voltage divider
def actual_voltage(measured_voltage):
    # divider_ratio = 4.67 / (5.6+4.67)  # R2 / (R2+R1), use when necessary
    return measured_voltage

url = "https://us-east-1.aws.data.mongodb-api.com/app/data-frxlp/endpoint/data/v1/action/"

def connect_to_wifi(ssid, psk):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting to Connect")
        time.sleep(10)
    if not wlan.isconnected():
        raise Exception("Wifi not available")
    print("Connected to WiFi")

def createOne(date):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        filter_dict = {"day": date}
        document = {"day": date, "temperature_farenheit": [], "luminances": [], "temperature_celcius": [], "times": []}
        update = {"$set": document}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "graphs",
            "filter": filter_dict,
            "update": document,
            "upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            print("graph created")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)


def findOne(filter_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "graphs",
            "filter": filter_dict,
            #"update": update_dict,
            #"upsert": True,
        }
        response = requests.post(url + "findOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            if response.text == "{\"document\":null}":
                print("No graph corresponding to todays date found")
                print(filter_dict["day"])
                createOne(filter_dict["day"])
                
        else:
            print(response.status_code)
            print("findOne Error")
        response.close()
    except Exception as e:
        print(e)

def updateOne(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$set": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "temperatures",
            "filter": filter_dict,
            "update": update_dict,
            "upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def pushOne(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$push": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "graphs",
            "filter": filter_dict,
            "update": update,
            #"upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def pushOne(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$push": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "graphs",
            "filter": filter_dict,
            "update": update,
            #"upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)
        
        
#Functions to update the days collection in the database
def createOneDay(date):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        filter_dict = {"day": date}
        document = {"times": [], "power": [], "date": date,}
        update = {"$set": document}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "days",
            "filter": filter_dict,
            "update": document,
            "upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            print("day created")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)


def findOneDay(filter_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "days",
            "filter": filter_dict,
            #"update": update_dict,
            #"upsert": True,
        }
        response = requests.post(url + "findOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            if response.text == "{\"document\":null}":
                print("No day corresponding to todays date found")
                print(filter_dict["date"])
                createOneDay(filter_dict["date"])
                
        else:
            print(response.status_code)
            print("findOne Error")
        response.close()
    except Exception as e:
        print(e)


def pushOneDay(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$push": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "days",
            "filter": filter_dict,
            "update": update,
            #"upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)
def updateCurrentAndVoltage(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$set": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "solararrays",
            "filter": filter_dict,
            "update": update_dict,
            "upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)
        
def insertAnomaly(filter_dict, update_dict):
    try:
        headers = {
            "api-key": "fuQa5n8PAJ38cvm0m1kAjfCuI3slNoBpPHYud7uTR2RsIeY75F8RcGGSAUGjPWXB",
            #"Connection": "upgrade",
            #"Upgrade": "HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"
        }
        update = {"$set": update_dict}
        searchPayload = {
            "dataSource": "Sol-Cluster",
            "database": "Sol",
            "collection": "anomalies",
            "filter": filter_dict,
            "update": update_dict,
            "upsert": True,
        }
        response = requests.post(url + "updateOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
            
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def main():
    
    # Initialize DS18B20 temperature sensor
    ds_pin = machine.Pin(22)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    roms = ds_sensor.scan()
    
    connect_to_wifi("BU Guest (unencrypted)", "")
    
    while True:
        try:
            response = requests.get(url='http://worldtimeapi.org/api/timezone/America/New_York')
            date=response.json()["datetime"][0:10].replace("-", "/")
            
            print(response.json()["datetime"])
            
            power = 0
            voltage_reading = 0
            current_reading = 0
            
            try:
                measured_voltage = sensor_ina219.getBusVoltage_V()  # Bus Voltage in volts
                current = sensor_ina219.getCurrent_mA()  # Current in milliamps # Connect Vin of INA219 to the + of load
                real_current = current/1000
                adjusted_voltage = actual_voltage(measured_voltage)  # Adjusted voltage in volts
                power = (adjusted_voltage * real_current)/1000 # power in wats
                voltage_reading = adjusted_voltage
                current_reading = real_current
                print(f"Adjusted Voltage: {adjusted_voltage:.2f} V, Current: {real_current:.2f} mA")
                
            except Exception as e:
                
                print("INA219 read error:", e)
                
            ds_sensor.convert_temp()
            utime.sleep_ms(750)  # Wait for DS18B20 conversion
            tempC = 0
            tempF = 0
            for rom in roms:
                tempC = ds_sensor.read_temp(rom)
                tempF = tempC * (9/5) + 32
                print(f"DS18B20 Temperature (ºC): {tempC:.2f}, Temperature (ºF): {tempF:.2f}")
            

            print(tempC)
            print(tempF)
            print(power)
            
            # graph filter dict
            filterDict = {
                    "day": date,
            }
            
            #print("sending...")
            
            #update graph (temperature, luminosity and timestamps)
            findOne(filterDict)
            print("Updating temperature, luminosity")
            pushOne(filterDict, {"temperature_farenheit": tempF})
            pushOne(filterDict, {"times": response.json()["datetime"]})
            pushOne(filterDict, {"temperature_celsius": tempC})
            updateOne({"day": "current_day"}, {"day": "current_day", "temperature_celsius": tempC, "temperature_farenheit": tempF})
            
            #Update the day with power and and timestamp data
            findOneDay({"date": date})
            print("Updating power")
            pushOneDay({"date": date}, {"power": power})
            pushOneDay({"date": date}, {"times": response.json()["datetime"][0:-4] + '0:00'})
            
            if (current_reading < 0.1 or voltage_reading < 0.1):
                insertAnomaly({"date": response.json()["datetime"][0:-4] + '0:00'},
                              
                              {"date": response.json()["datetime"][0:-4] + '0:00',
                               "current": current_reading,
                               "voltage": voltage_reading,
                               }
                              )
            
            
            #Update current and voltage values
            filter_dictionary = {"id": "65539e775435e37264e3e6ff"}
            
            update_dictionary = {"id": "65539e775435e37264e3e6ff",
                                 "Voltage_reading": str(voltage_reading),
                                 "location": "Warren Towers",
                                 "solarPanels": [],
                                 "Current_reading": str(current_reading)
                                 }
            updateCurrentAndVoltage(filter_dictionary, update_dictionary)

            print("Finished updating")
            #updateOne(filterDict, updateDict)
            
            time.sleep(30)
                
        except Exception as e:
            print(e)

#readPower(1000)
if __name__ == "__main__":
    main()
