from my_lib import RTC_DS3231 # RTC library pins 21 and pin 20 use for i2c 
import time
from machine import Pin, Timer # Raspberry Pi Pico Pins Import library 
import utime

#setup led pin for make led on 
#led=Pin(22,Pin.OUT)        
#led.value(1)

dir_pin = Pin(16, Pin.OUT) # Stepper motor pin for DIR
step_pin = Pin(17, Pin.OUT) # Stepper motor pin for Step
 
# Initialize timer
tim = Timer() # 
 
def step(t):
    global step_pin
    step_pin.value(not step_pin.value())
 
def rotate_motor(delay):
    # Set up timer for stepping
    tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step) 

 
# Initialize timer
tim = Timer()

#rtc variable define for get current time 
rtc = RTC_DS3231.RTC()



#setup for motor move according to time 
first_rotation="05:00:00"    #timer 1 starting duration
second_rotation="11:00:00"   #timer 2 starting duration
third_rotation="16:00:00"    #timer third starting duration


print("running") # 

#timer three
n=0
def main():
    while True:
        try:
            t = rtc.DS3231_ReadTime(1)
            print(t) # print current RTC time
            time.sleep(1) 
            if t >= first_rotation and t <second_rotation :
                        spl=first_rotation.split(":")
                        first=spl[0]
                        # steps calculated from 5 to 11 hrs is 11 as per motor rotation and sleep time set below
                        # Calculation:
                        # 5am to 11am
                        # total hours  = 6
                        # total steps = 68
                        # total hours / total steps=11.33
                        # motor moves 11 steps in every hour
                        # 11x6=66
                            
                        if t==f'{first}:58:00':
                            dir_pin.value(1)
                            print(f'current time is {t}')
                            print("Time 5am to 11pm ")
                            print("Total number of running steps 11 in this duration")
                            # steps calculated from 5 to 11 hrs is 11 as per motor rotation and sleep time set below
                            
                            
                            steps_per_revolution1=22500 # found delay during testing to achive the 1 steps in that duration 

                            # Spin motor slowly
                            rotate_motor(600000) # Slow down the steps so motor rotation within the time.
                            
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)

                                
                        if t=="06:08:00":
                                print(f'current time is {t}')
                                print("Time 5am to 11pm under ")
                                print("Total number of running steps 11 in this duration")

                                # Set motor direction clockwise
                                dir_pin.value(1)  # 1 means move formward 0 means backward direction                      
                                steps_per_revolution1=22500 # # found delay during testing to achive the 1 steps in that duration

                                # Spin motor slowly
                                rotate_motor(600000)
                                utime.sleep_ms(steps_per_revolution1)

                                step_pin.low()
                                dir_pin.low()
                                tim.deinit()  # stop the timer
                                utime.sleep(1)
                            
                        if t=="07:30:00":
                            print(f'current time is {t}')
                            print("Time 5am to 11pm under ")
                            print("Total number of running steps 11 in this duration")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            print('running')
                            
                            steps_per_revolution1=22500 # found delay during testing to achive the 1 steps in that duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)

                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="08:40:00":
                            print(f'current time is {t}')
                            print("Time 5am to 11pm under ")
                            print("Total number of running steps 11 in this duration")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            print('running')
                            
                            steps_per_revolution1=22500 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)

                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="09:45:00":
                            print(f'current time is {t}')
                            print("Time 5am to 11pm under ")
                            print("Total number of running steps 11 in this duration")


                            # Set motor direction clockwise
                            dir_pin.value(1)                    
                            steps_per_revolution1=22500 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                         
        #                     
                        if t=="10:50:00":
                            print(f'current time is {t}')
                            print("Time 5am to 11pm under ")
                            print("Total number of running steps 11 in this duration")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            steps_per_revolution1=22500 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
            if t >= second_rotation and t < third_rotation:
                        spl2=second_rotation.split(":")
                        second=spl2[0]
                        # 11am to 4 pm
                        # total hours  = 5
                        # total steps = 68
                        # total hours / total steps =13.6
                        # motor moves 14 steps in every hour
                        # 14x5=70
                        # complete 2 extra steps of pending in last session

                        
                        if t==f'{second}:13:00':
                            print(f'current time is {t}')
                            print("Time 11am to 4pm ")
                            print("Total number of running steps = 14")
                      # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=27000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)

                                
                        if t=="12:14:00":
                            print(f'current time is {t}')
                            print("Time 11am to 4pm under ")
                            print("Total number of running steps = 14")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            print('running')
                            
                            steps_per_revolution1=27000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="13:15:00":
                            print(f'current time is {t}')
                            print("Time 11am to 4pm under ")
                            print("Total number of running steps = 14")
                            # Set motor direction clockwise
                            dir_pin.value(1)                    
                            steps_per_revolution1=27000 # found this delay during testing to achive the 1 steps in this  duration
                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="14:16:00":
                            print(f'current time is {t}')
                            print("Time 11am to 4pm under ")
                            print("Total number of running steps = 14")
                            # Set motor direction clockwise
                            dir_pin.value(1)                    
                            steps_per_revolution1=27000 # found this delay during testing to achive the 1 steps in this  duration
                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="15:17:00":
                            print(f'current time is {t}')
                            print("Time 11am to 4pm under ")
                            print("Total number of running steps = 14")
                            # Set motor direction clockwise
                            dir_pin.value(1)
                            print('running')
                            
                            steps_per_revolution1=27000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
            
            
            
            if t>= third_rotation and t< "23:59:59":
                        spl3=third_rotation.split(":")
                        third=spl3[0]
                        
                        # 4pm to 5am
                        # total hours  = 13
                        # total steps = 68
                        # total hours / total steps=5.2
                        # motor moves 5 steps in every hour but on last rotation it moves 8 steps for complete rotation
                        # 13x5=65+3=68

                        if t==f'{third}:21:00':
                            print(f'current time is {t}')
                            print("Time 4pm to 5am ")
                            print("Total number of running steps = 5")

        #                     direction clockwise
                            dir_pin.value(1)
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)

                                
                        if t=="17:22:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="18:23:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="19:24:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="20:25:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="21:26:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="22:01:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            print("175")
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)

                                
                        if t=="22:27:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")

                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="23:28:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="01:29:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="02:01:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
                            
                        if t=="03:01:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 5")
                            dir_pin.value(1)
                            
                            steps_per_revolution1=10000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        #                     
                        if t=="03:45:00":
                            print(f'current time is {t}')
                            print("Time 4pm to 5am under ")
                            print("Total number of running steps = 8")
                            
                            # Set motor direction clockwise
                            dir_pin.value(1)
                            
                            steps_per_revolution1=15000 # found this delay during testing to achive the 1 steps in this  duration

                            # Spin motor slowly
                            rotate_motor(600000)
                            utime.sleep_ms(steps_per_revolution1)
                            step_pin.low()
                            dir_pin.low()
                            tim.deinit()  # stop the timer
                            utime.sleep(1)
        
        except KeyboardInterrupt:
          print("Keyboard interrupt")
          #led.value(0)
          return None
          
main()

