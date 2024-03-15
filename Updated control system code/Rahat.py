import RTC_DS3231
import time                                 #Important notes --------                     
from machine import Pin, Timer              # This code has been designed to completely stop the motor after 11:59 pm and start from 6 am
import utime                                # During 6 am - 11:59 pm,the motor will rotate per user's given number and direction which should be roughly from (sun's movement+reflector position)
                                            # It will rotate first 1-10 minutes of every hour per user's requirement
#import urandom                             # During its operational time, motor will take break 
                                            # Excessive number of rotations and speed will hurt the system significantly!!
                                            #Stepper motor only has been designed for precise control
                                            # Stepper model has various model and currently we are using the base model which means low power
                                            # Code has been designed for final product and quick demmo
                                            # Higher torque will decrease performance noticeably
#setup led pin for make led on              # For quick demo - just resset the time       
#led=Pin(22,Pin.OUT)        
#led.value(1)

#  **** are new line

dir_pin = Pin(18, Pin.OUT)
step_pin = Pin(17, Pin.OUT)
 
# Initialize timer
tim = Timer()
 
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

#less than 60 total rotation should be valid rotation
total_rotation= 20  # Very important number, require testing with reflectors to get this exact number


# new slot added on first_rotation  variable 

first_rotation="00:00:00"    #time slot 1   **** #All time in 24 hour format
second_rotation="06:00:00"   #time slot 2
third_rotation="12:00:00"     # time slot 3
forth_rotation="17:00:00"     # time slot 4


#random_number=10
#timer three
n=0
def main():
    global random_number
    global final_count
    while True:
        try:
            
            t = rtc.DS3231_ReadTime(1)
            print(t)
            time.sleep(1)



# 1st slot only show time from line 60 to line 138. It's a midnight, so time for the motor to get some good sleep

#****  start

            if t >= first_rotation and t <second_rotation :        # Midnight
                    if t >= second_rotation:
                        break
                    print("slot1")
                    end_time_hour1 = 2    # Dummy number, not important
                    if t=='00:01:00':
                        new_time=f'00:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                #print(f' new time variable ------------{new_time}')
                                if new_time == t:
                                    #print("break")
                                    break
                                
                            if end_time_hour1>=10:
                                new_time=f'00:0{end_time_hour1}:00'
                                if new_time == t:
                                    break
                                
                    if t=='01:01:00':
                        new_time=f'01:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                #print(f' new time variable ------------{new_time}')
                                if new_time == t:
                                    #print("break")
                                    break
                            if end_time_hour1>=10:
                                if new_time == t:
                                    break             
                                
                    if t=='02:01:00':
                        new_time=f'02:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                #print(f' new time variable ------------{new_time}')
                                if new_time == t:
                                    #print("break")
                                    break
                            if end_time_hour1>=10:
                                if new_time == t:
                                    break
                    if t=='03:01:00':
                        new_time=f'03:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                if new_time == t:
                                    break
                            if end_time_hour1>=10:
                                if new_time == t:
                                    break
                                
                                
                    if t=='04:01:00':
                        new_time=f'04:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                if new_time == t:
                                    break
                            if end_time_hour1>=10:
                                if new_time == t:
                                    break
                                
                                
                    if t=='05:01:00':
                        new_time=f'05:0{end_time_hour1}:00'
                        while True:
                            t = rtc.DS3231_ReadTime(1)
                            print(t)
                            time.sleep(1)
                            if end_time_hour1 <=9:
                                if new_time == t:
                                    break
                            if end_time_hour1>=10:
                                if new_time == t:
                                    break
#****     end                        
                                


#1111---------------------------------------------------------                           
            if t >= second_rotation and t < third_rotation:
                        if t >= third_rotation:
                            break
                        print("slot2")
                        if t=='06:01:00':        # 6 am
                            minute=1
                            count=1
                            #define only minutes in ent_time_hour1 variable 
                            end_time_hour1 = 10  # It is good for our system to complete all require rotations within first 10 minutes
                                                # Good for driver and motor itself, after 10 minutes motor will stop until next t
                                                 # Number can choose from 1<= end_time_hour1<=10. 1 could be used for demonstration purpose.
                                                 # I prefer atleast 3 as whole purpose of this system to move the the reflectorsover the period of time. !
                                                 
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour1}')

                            
                            complete_motor_to_run= 4080*total_rotation   # Fixed number for now, 4080 has been verified after testing.
                                                                          # 4080 for 1 exactly 360 degree full rotation. 
                                                                         # Increasing this number will increase the number of rotations than expected which means faster speed.
                                                                         # Be careful !!
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour1
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0


                            get_datatype=isinstance(run_pr_rotation,float)   # necessary to tackle the random+weired floating issue system is facing
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')
                                    
                                    
                            while True:
                                print("in first  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:    #safety purpose, just incase
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'06:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)      #Clock-wise, 0 for anti-clock
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)   # Fixed number for now, number has been verified after testing. #Perfect speed for exact 360 rotation
                                                                  # Decreasing this number will incraese the speed. Be careful
                                            utime.sleep_ms(steps_per_revolution1)  
                                            step_pin.low() #Sending pulse to motor
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1) # 1 mean clock-wise, 0 for anti-clock. Choose as you wish
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)  # Excessive speed will hurt the motor as we are only providing 12V. Max voltage I/P is 24V
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'06:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                            
                                        
                                        
                        if t=='07:01:00':    #same logic/reasoning like previous t  # 7 am
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour2 variable 
                            end_time_hour2 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour2}')

                            
                            complete_motor_to_run=4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour2
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in second  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'07:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'07:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                
                        if t=='08:01:00':  # 8 am in the morning
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour3 variable 
                            end_time_hour3 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour3}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour3
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'08:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'08:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#                              
#                              
                        if t=='09:01:00':         # 9 am
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour4 variable 
                            end_time_hour4 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour4}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour4
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'09:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'09:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#             #                     
                        if t=='10:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour5 variable 
                            end_time_hour5 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour5}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour5
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'10:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        rotation_complete="done"
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'10:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#             #                         
#         #                     
                        if t=='11:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour6 variable 
                            end_time_hour6 = 10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour6}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour6
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'11:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour6 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'11:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour6 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#  ---------------------------------------------------------------------------------------------------------------
            if t>= third_rotation and t< forth_rotation:
                        print("slot3")
                        if t=='12:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour1 variable 
                            end_time_hour1 =10

                            complete_motor_to_run= 4080*total_rotation
                            run_pr_rotation=complete_motor_to_run /end_time_hour1
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')
                                
                            while True:
                                print("in first  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'12:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'12:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                            
                                        
                                        
                        if t=='13:01:00':
                            minute=1
                            count=1


                            #define only miutes in ent_time_hour2 variable 
                            end_time_hour2 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour2}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour2
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in second  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'13:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'13:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                
                        if t=='14:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour3 variable 
                            end_time_hour3 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour3}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour3
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'14:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'14:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#                              
#                              
                        if t=='15:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour4 variable 
                            end_time_hour4 =10


                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour4
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'15:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'15:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#             #                     
                        if t=='16:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour5 variable 
                            end_time_hour5 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour5}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour5
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'16:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'16:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                        
#-------------------------------------------------------------------------------------------------------------------
                                        
            if t >= forth_rotation and t < "23:59:59":
                        print("slot4")
                        if t=='17:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour1 variable 
                            end_time_hour1 =10

                            complete_motor_to_run= 4080*total_rotation
                            run_pr_rotation=complete_motor_to_run /end_time_hour1
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')
                                
                            while True:
                                print("in first  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'17:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'17:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour1 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                            
                                        
                                        
                        if t=='18:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour2 variable 
                            end_time_hour2 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour2}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour2
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in second  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'18:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'18:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour2 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
                                
                        if t=='19:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour3 variable 
                            end_time_hour3 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour3}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour3
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'19:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'19:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour3 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#                              
#                              
                        if t== '20:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour4 variable 
                            end_time_hour4 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour4}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour4
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'20:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'20:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour4 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)
#             #                     
                        if t=='21:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour5 variable 
                            end_time_hour5 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour5}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour5
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'0{add4}:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(20000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(20000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'21:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour5 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                        if t=='22:01:00':
                            minute=1
                            count=1

                            #define only miutes in ent_time_hour6 variable 
                            end_time_hour6 =10
                            
                            
                            print(f' this is t variable -------------{total_rotation}')
                            print(f' this is final end_time ------------{end_time_hour6}')

                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour6
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'22:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour6 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'22:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour6 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)


                        if t=='23:01:00':
                            minute=1
                            count=1


                            #define only miutes in ent_time_hour7 variable 
                            end_time_hour7 =10
              
                            
                            complete_motor_to_run= 4080*total_rotation
                            print(f' this is complete_motor_to_run ------------{complete_motor_to_run}')
                            
                            
                            run_pr_rotation=complete_motor_to_run /end_time_hour7
                            print(f' this is run_pr_rotation ------------{run_pr_rotation}')
                            convint=int(run_pr_rotation)
                            print(convint)
                            count_rotation=0
                            get_datatype=isinstance(run_pr_rotation,float)
                            if get_datatype==True:
                                print("float datatype")
                                
                                get_float=str(run_pr_rotation).split(".")
                                get_float_number= f'.{get_float[1]}'
                                print(f' this is get_float_number ------------{get_float_number}')
                                if get_float_number==".0":
                                    print("invalid data")
                                else:
                                    get_int=float(get_float_number)
                                    get_float_final_val= int( * get_int)
                                    print(f' this is get_float_final_val ------------{get_float_final_val}')

                                
                            while True:
                                print("in fourth  hour")

                                if  minute <= 9:
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'23:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour7 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
                                        utime.sleep_ms(steps_per_revolution1)
                                        step_pin.low()
                                        dir_pin.low()
                                        tim.deinit()  # stop the timer
                                        utime.sleep(1)

                                if minute > 9 :
                                    print(count_rotation)
                                    if count_rotation==complete_motor_to_run:
                                        
                                        break
                                    

                                    
                                    if minute > 1 :
                                        t = rtc.DS3231_ReadTime(1)
                                        print(t)
                                        time.sleep(1)

                                        
                                    if t==f'23:0{minute}:00':
                                        minute += 1
                                        print(minute)
                                        
                                        count_rotation+=convint
                                        print(f' total number of count_rotation -----{count_rotation}')
                                        if count_rotation > complete_motor_to_run:
                                            get_balance=convint*end_time_hour7 - complete_motor_to_run
                                            get_balance_str=str(get_balance).replace("-","")
                                            get_balance_int=int(get_balance_str)
                                            print(get_balance_int)
                                            dir_pin.value(1)
                                            steps_per_revolution1=get_balance_int

                                            # Spin motor slowly
                                            rotate_motor(10000)
                                            utime.sleep_ms(steps_per_revolution1)
                                            step_pin.low()
                                            dir_pin.low()
                                            tim.deinit()  # stop the timer
                                            utime.sleep(1)
                                            print("rotation complete ")
                                            break
                                        
                                        dir_pin.value(1)
                                        print(f'current time is {t}')
                                        steps_per_revolution1=convint

                                        # Spin motor slowly
                                        rotate_motor(10000)
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









