import json
import network
import urequests as requests
import time
import machine
#from sensors import readVoltage, readCurrent

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



#read potentiometer analogue voltage
def readPower(resistance_value):
    #read potentiometer analogue voltage
    potentiometer_val = machine.ADC(0)

    #Convert 16 bit number to voltage
    voltage = (3.3/65106)*potentiometer_val.read_u16()-(430.5/65106)
    power = voltage**2/resistance_value
    print("voltage: " + str(voltage))
    print("Power: " + str(power))
    return power
    

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
        print(date)
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
            "collection": "luminances",
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

def main():
    
    # Initialize I2C bus for Raspberry Pi Pico
    i2c = I2C(0, scl=Pin(21), sda=Pin(20))

    # Create an instance of the BH1750 class
    light_sensor = BH1750(i2c)
    
    connect_to_wifi("BU Guest (unencrypted)", "")
    
    while True:
        try:
            response = requests.get(url='http://worldtimeapi.org/api/timezone/America/New_York')
            date=response.json()["datetime"][0:10].replace("-", "/")
            
            print(response.json()["datetime"])
            
            # Measure the ambient light in lux
            lux = light_sensor.luminance(BH1750.CONT_HIRES_1)
            #print(f"Ambient light level: {lux} lux")

            # Calculate and print solar irradiation
            solar_irradiation = calculate_solar_irradiation(lux)
            print(f"Solar irradiation: {solar_irradiation} Wh/m^2")

            # Wait for a bit before taking another reading

            
            #updateDict = {
            #    "date": current_day["date"],
            #    "power": current_day["power"],
            #    "times": current_day["times"],
            #}
            
            filterDict = {
                    "day": date,
            }
            
            print("sending...")
            findOne(filterDict)
            pushOne(filterDict, {"luminances": solar_irradiation})
            pushOne(filterDict, {"times": response.json()["datetime"]})
            updateOne({"day": "current_day"}, {"luminance": solar_irradiation, "day": "current_day"})
            print("Finished updating")
            #updateOne(filterDict, updateDict)
            
            time.sleep(30)
                
        except Exception as e:
            print(e)

#readPower(1000)
if __name__ == "__main__":
    main()
    
    

