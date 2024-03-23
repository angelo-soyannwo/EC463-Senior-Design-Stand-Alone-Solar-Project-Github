from machine import Pin, RTC, I2C
import utime as time
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

dir_pin = 18
step_pin = 17
CW = 1
CCW = 0
SPR = 200        #steps per revolution in full step mode

DIR = Pin(18, Pin.OUT)
STEP = Pin(17, Pin.OUT)
#initilialize direction
DIR.value(CW)

up_pin = 2
down_pin = 5
right_pin = 3
left_pin = 4
select_pin = 6

UP = Pin(up_pin, Pin.IN, Pin.PULL_DOWN)
DOWN = Pin(down_pin, Pin.IN, Pin.PULL_DOWN)
RIGHT = Pin(right_pin, Pin.IN, Pin.PULL_DOWN)
LEFT = Pin(left_pin, Pin.IN, Pin.PULL_DOWN)
OK = Pin(select_pin, Pin.IN, Pin.PULL_DOWN)

I2C_ADDR = 0x20    #Check with i2c.scan()
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0, Pin.PULL_UP), scl=Pin(1, Pin.PULL_UP), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
print("running")
lcd.clear()
# lcd.putstr("heyhey")
# time.sleep(3)

def lcd_settings():
    lcd.clear()
    lcd.show_cursor
    lcd.blink_cursor_on()

def RTC_pstn(pstn, front=0):
    if front:
        if pstn == 0:
            x_pos, y_pos = 0,0
        elif pstn==1:
            x_pos, y_pos = 5,0
        elif pstn==2:
            x_pos, y_pos = 8,0
        elif pstn==3:
            x_pos, y_pos = 0,1
        elif pstn==4:
            x_pos, y_pos = 3,1
        elif pstn==5:
            x_pos, y_pos = 6,1
    else:
        if pstn == 0:
            x_pos, y_pos = 3,0
        elif pstn==1:
            x_pos, y_pos = 6,0
        elif pstn==2:
            x_pos, y_pos = 9,0
        elif pstn==3:
            x_pos, y_pos = 1,1
        elif pstn==4:
            x_pos, y_pos = 4,1
        elif pstn==5:
            x_pos, y_pos = 7,1
        
    return x_pos, y_pos

def RTC_manual():
    lcd_settings()
    lcd.move_to(0,0)
    lcd.putstr("SET REFLECTORS")
    lcd.move_to(0,1)
    lcd.putstr("TO LOWEST")
    time.sleep(2)
    rotateMotor_manual()
    
    lcd_settings()
    pstn = 0
    #tm = [2024, 1, 1, 16, 0, 0]    #(year, month, day, hours, minutes, seconds)
    tm = time.localtime()
    tm = list(tm)
    lcd.move_to(0, 0)
#     lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d}\n{HH:>02d}:{MM:>02d}:{SS:>02d}".format(
#             year=tm[0], month=tm[1], day=tm[2],
#             HH=tm[3], MM=tm[4], SS=tm[5]))
    lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d}".format(year=tm[0], month=tm[1], day=tm[2]))
    lcd.move_to(0, 1)
    lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=tm[3], MM=tm[4], SS=tm[5]))
    
    x_pos = 3
    y_pos = 0
    lcd.move_to(x_pos,y_pos)
    click = 0
    while OK.value()==1:
        pass
    #print(OK.value(),RIGHT.value(),LEFT.value(),UP.value(),DOWN.value())
    while OK.value() == 0:
        if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
            click = 0
        if click == 0:
            if RIGHT.value():
                if pstn<5:
                    pstn += 1
                    x_pos, y_pos = RTC_pstn(pstn)
                    lcd.move_to(x_pos, y_pos)
                    #print("right")
                click = 1
            elif LEFT.value():
                if pstn>0:
                    pstn -= 1
                    x_pos, y_pos = RTC_pstn(pstn)
                    lcd.move_to(x_pos, y_pos)
                    #print("left")
                click = 1
            elif UP.value():
                if pstn==0:
                    tm[pstn] += 1
                elif pstn==1:
                    if tm[pstn]==12:
                        tm[pstn] = 1
                    else:
                        tm[pstn] += 1
                elif pstn==2:
                    if (tm[1]==2 and ((tm[0]%4!=0 and tm[pstn]==28) or (tm[0]%4==0 and tm[pstn]==29))) or (tm[1]<8 and
                        ((tm[1]%2==1 and tm[pstn]==31) or (tm[1]%2==0 and tm[pstn]==30))) or (tm[1]>7 and
                            ((tm[1]%2==0 and tm[pstn]==31) or (tm[1]%2==1 and tm[pstn]==30))):
                        tm[pstn] = 1
                    else:
                        tm[pstn] += 1
                elif pstn==3:
                    if tm[pstn]==23:
                        tm[pstn] = 0
                    else:
                        tm[pstn] += 1
                elif pstn==4 or pstn==5:
                    if tm[pstn]==59:
                        tm[pstn] = 0
                    else:
                        tm[pstn] += 1
                        
                x_pos, y_pos = RTC_pstn(pstn, 1)
                lcd.move_to(x_pos, y_pos)
                lcd.putstr("{value:>02}".format(value=str(tm[pstn])))
                x_pos, y_pos = RTC_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                time.sleep(0.1)
                
            elif DOWN.value():
                if pstn == 0:
                    tm[pstn] -= 1
                elif pstn==1:
                    if tm[pstn]==1:
                        tm[pstn] = 12
                    else:
                        tm[pstn] -= 1
                elif pstn==2:
                    if tm[pstn]==1:
                        if tm[1]==2:
                            if tm[0]%4!=0:
                                tm[pstn] = 28
                            else:
                                tm[pstn] = 29
                        elif tm[1]<8:
                            if tm[1]%2==1:
                                tm[pstn] = 31
                            else:
                                tm[pstn] = 30
                        else:
                            if tm[1]%2==0:
                                tm[pstn] = 31
                            else:
                                tm[pstn] = 30    
                    else:
                        tm[pstn] -= 1
                elif pstn==3:
                    if tm[pstn]==0:
                        tm[pstn] = 23
                    else:
                        tm[pstn] -= 1
                elif pstn==4 or pstn==5:
                    if tm[pstn]==0:
                        tm[pstn] = 59
                    else:
                        tm[pstn] -= 1
                
                x_pos, y_pos = RTC_pstn(pstn, 1)
                lcd.move_to(x_pos, y_pos)
                lcd.putstr("{value:>02}".format(value=str(tm[pstn])))
                x_pos, y_pos = RTC_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                time.sleep(0.1)
                
    #lcd.hide_cursor()
    #lcd.clear()
    tm = tuple(tm)
    rtc = RTC()
    rtc.datetime((tm[0], tm[1], tm[2], 0, tm[3], tm[4], tm[5], 0))
    
    
def placeValue(N, D): 
    rem = 0
    for x in range(D): 
        rem = N % 10
        N = N // 10
    return rem

def set_timeFactor(timeFactor):
    lcd_settings()
    pstn = 0
    tF = [placeValue(timeFactor,3), placeValue(timeFactor,2), placeValue(timeFactor,1)]
    lcd.move_to(5,1)
    lcd.putstr("Time Factor")
    lcd.move_to(0, 0)
    lcd.putstr(str(timeFactor))
    lcd.move_to(pstn, 0)
    click = 0
    
    while OK.value()==1:
        pass
    
    while OK.value() == 0:
        if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
            click = 0
        if click == 0:
            if RIGHT.value():
                if pstn<2:
                    pstn += 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif LEFT.value():
                if pstn>0:
                    pstn -= 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif UP.value():
                if tF[pstn]==9:
                    tF[pstn] = 0
                else:
                    tF[pstn] += 1
                lcd.putstr(str(tF[pstn]))
                lcd.move_to(pstn,0)
                time.sleep(0.1)
            elif DOWN.value():
                if tF[pstn]==0:
                    tF[pstn] = 9
                else:
                    tF[pstn] -= 1
                lcd.putstr(str(tF[pstn]))
                lcd.move_to(pstn,0)
                time.sleep(0.1)
      
    #lcd.hide_cursor()
    #lcd.clear()
    timeFactor = 100*tF[0] + 10*tF[1] + tF[2]
    return timeFactor

    
def set_dayStartEnd(dayStart, dayEnd):
    lcd_settings()
    pstn = 0
    dS = []
    dE = []
    for x in range(5):
        dS.append(placeValue(dayStart,5-x))
        dE.append(placeValue(dayEnd,5-x))
#     dS = [2,1,6,0,0]             #default 6 hours (into the day)
#     dE = [6,4,8,0,0]               #default 18 hours (into the day)
    lcd.move_to(4,1)
    lcd.putstr("Start of Day")
    lcd.move_to(0, 0)
#     lcd.putstr("{}{}{}{}{}".format(dS[0], dS[1], dS[2], dS[3], dS[4]))
    lcd.putstr(str(dayStart))
    lcd.move_to(pstn,0)
    click = 0

    while OK.value()==1:
        pass
    while OK.value()==0:
        if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
            click = 0
        if click == 0:
            if RIGHT.value():
                if pstn<4:
                    pstn += 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif LEFT.value():
                if pstn>0:
                    pstn -= 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif UP.value():
                if dS[pstn]==9:
                        dS[pstn] = 0
                else:
                    dS[pstn] += 1
                lcd.putstr(str(dS[pstn]))
                lcd.move_to(pstn,0)
                time.sleep(0.1)
            elif DOWN.value():
                if dS[pstn]==0:
                        dS[pstn] = 9
                else:
                    dS[pstn] -= 1
                lcd.putstr(str(dS[pstn]))
                lcd.move_to(pstn,0)
                time.sleep(0.1)
        
    #switch screen to dayEnd
    lcd_settings()
    lcd.move_to(6, 1)
    lcd.putstr("End of Day")
    lcd.move_to(0, 0)
    lcd.putstr(str(dayEnd))
    pstn = 0
    lcd.move_to(pstn,0)
    
    while OK==1:
        #do nothing until OK button is let go
        pass
    
    while OK.value()==0:
        if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
            click = 0
        if click == 0:
            if RIGHT.value():
                if pstn<4:
                    pstn += 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif LEFT.value():
                if pstn>0:
                    pstn -= 1
                    lcd.move_to(pstn, 0)
                click = 1
            elif UP.value():
                if dE[pstn]==9:
                    dE[pstn] = 0
                else:
                    dE[pstn] += 1
                lcd.putstr(str(dE[pstn]))
                lcd.move_to(pstn,0)
            elif DOWN.value():
                if dE[pstn]==0:
                    dE[pstn] = 9
                else:
                    dE[pstn] -= 1
                lcd.putstr(str(dE[pstn]))
                lcd.move_to(pstn,0)

    #lcd.hide_cursor()
    #lcd.clear()
    dayStart = 0
    dayEnd = 0
    for i in range(5):
        dayStart = dayStart + 10**(5-i) * dS[i]
        dayEnd = dayEnd + 10**(5-i) * dE[i]
    
    return dayStart,dayEnd
   
def rotateMotor(steps, direction, delay):
    for x in range(steps):
        DIR.value(direction)
        STEP.high()
        time.sleep(delay)
        STEP.low()
        time.sleep(delay)

def rotateMotor_manual():
    lcd_settings()
    lcd.move_to(0, 0)
    lcd.putstr("Reflector Manual Control")
    
    while OK.value()==1:
        pass
    while OK.value()==0:
        if UP.value():
            rotateMotor(1,CW,0.01)
        elif DOWN.value():
            rotateMotor(1,CCW,0.01)
            
    #lcd.clear()
    
def menu_pstn(pstn):
    if pstn==0:
        x_pos, y_pos = 0,0
    elif pstn==1:
        x_pos, y_pos = 8,0
    elif pstn==2:
        x_pos, y_pos = 0,1
    elif pstn==3:
        x_pos, y_pos = 9,1
        
    return x_pos, y_pos

lcd.custom_char(0, bytearray([0x08,
  0x0C,
  0x0E,
  0x0F,
  0x0E,
  0x0C,
  0x08,
  0x00]))

def menu(dayStart, dayEnd, timeFactor):
    settingChanged = 0
    lcd_settings()
    lcd.move_to(1, 0)
    lcd.putstr("RTC")
    lcd.move_to(9, 0)
    lcd.putstr("MnlCtrl")
    lcd.move_to(1, 1)
    lcd.putstr("DayHrs")
    lcd.move_to(10, 1)
    lcd.putstr("TmFctr")
    
    pstn = 0
    x_pos,y_pos = menu_pstn(pstn)
    lcd.move_to(pstn,0)
    lcd.putchar(chr(0))
    lcd.move_to(x_pos, y_pos)
    click = 0
    while OK.value()==0:
        if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
            click = 0
        if click == 0:
            if RIGHT.value():
                click = 1
                lcd.putstr(" ")
                if pstn==3:
                    pstn = 0
                else:
                    pstn += 1
                x_pos,y_pos = menu_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                lcd.putchar(chr(0))
                lcd.move_to(x_pos, y_pos)
              
            elif LEFT.value():
                click = 1
                lcd.putstr(" ")
                if pstn==0:
                    pstn = 3
                else:
                    pstn -= 1
                x_pos,y_pos = menu_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                lcd.putchar(chr(0))
                lcd.move_to(x_pos, y_pos)
            elif UP.value():
                click = 1
                lcd.putstr(" ")
                if pstn > 1:
                    pstn -= 2
                else:
                    pstn += 2
                x_pos,y_pos = menu_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                lcd.putchar(chr(0))
                lcd.move_to(x_pos, y_pos)
            elif DOWN.value():
                click = 1
                lcd.putstr(" ")
                if pstn < 2:
                    pstn += 2
                else:
                    pstn -= 2
                x_pos,y_pos = menu_pstn(pstn)
                lcd.move_to(x_pos, y_pos)
                lcd.putchar(chr(0))
                lcd.move_to(x_pos, y_pos)
    
    settingChanged = 1
    if pstn==0:
        RTC_manual()
    elif pstn==1:
        rotateMotor_manual()
    elif pstn==2:
        dayStart,dayEnd = set_dayStartEnd(dayStart, dayEnd)
    else:
        timeFactor = set_timeFactor(timeFactor)
    return settingChanged, dayStart, dayEnd, timeFactor
                
if __name__ == "__main__":
#     RTC_manual()
#     rotateMotor_manual()
#     RTC_manual()
#     set_timeFactor(288)
#     set_dayStartEnd(21600, 64800)
    while True:
        menu(21600, 64800, 288)
    