from machine import Pin, RTC, I2C
import utime as time
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import uasyncio
import queue

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

async def RTC_manual():
#     lcd_settings()
#     lcd.move_to(0,0)
#     lcd.putstr("SET REFLECTORS")
#     lcd.move_to(0,1)
#     lcd.putstr("TO LOWEST")
#     time.sleep(2)
#     rotateMotor_manual()
    
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
        await uasyncio.sleep(0.04)
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
                else:
                    pstn = 0
                    x_pos, y_pos = RTC_pstn(pstn)
                    lcd.move_to(x_pos, y_pos)
                #print("right")
                click = 1
            elif LEFT.value():
                if pstn>0:
                    pstn -= 1
                    x_pos, y_pos = RTC_pstn(pstn)
                    lcd.move_to(x_pos, y_pos)
                    
                else:
                    pstn = 5
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
                await uasyncio.sleep(0.1)
                #time.sleep(0.1) 
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
                await uasyncio.sleep(0.1)
                #time.sleep(0.1)
        await uasyncio.sleep(0.04)        
                
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

def numDig(N):
    count = 0
    if N==0:
        count = 1
    else:
        while N >= 1:
            count += 1
            N = N/10
    return count

async def nineDigSet(dig, digArr, pstn, click):
    if not (RIGHT.value() or LEFT.value() or UP.value() or DOWN.value()):
        click = 0
    if click == 0:
        if RIGHT.value():
            if pstn<dig-1:
                pstn += 1
                lcd.move_to(pstn, 0)
            click = 1
            await uasyncio.sleep(0.04)
        elif LEFT.value():
            if pstn>0:
                pstn -= 1
                lcd.move_to(pstn, 0)
            click = 1
            await uasyncio.sleep(0.04)
        elif UP.value():
            if digArr[pstn]==9:
                digArr[pstn] = 0
            else:
                digArr[pstn] += 1
            lcd.putstr(str(digArr[pstn]))
            lcd.move_to(pstn,0)
            await uasyncio.sleep(0.1)
        elif DOWN.value():
            if digArr[pstn]==0:
                digArr[pstn] = 9
            else:
                digArr[pstn] -= 1
            lcd.putstr(str(digArr[pstn]))
            lcd.move_to(pstn,0)
            await uasyncio.sleep(0.1)
    return digArr, pstn, click

async def set_timeFactor(timeFactor):
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
        await uasyncio.sleep(0.04)
        pass
    
    while OK.value() == 0:
        tF, pstn, click = await nineDigSet(3, tF, pstn, click)
        await uasyncio.sleep(0.04)
      
    timeFactor = 100*tF[0] + 10*tF[1] + tF[2]
    return timeFactor

    
async def set_dayStartEnd(dayStart, dayEnd, top_pauseTime):
    lcd_settings()
    pstn = 0
    dS = []
    dE = []
    pT = []
    dSdig = numDig(dayStart)
    dEdig = numDig(dayEnd)
    pTdig = numDig(top_pauseTime)
    for x in range(dSdig):
        dS.append(placeValue(dayStart,dSdig-x))
    for x in range(dEdig):
        dE.append(placeValue(dayEnd,dEdig-x))
    for x in range(pTdig):
        pT.append(placeValue(top_pauseTime, pTdig-x))
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
        await uasyncio.sleep(0.04)
        pass
    while OK.value()==0:
        dS, pstn, click = await nineDigSet(dSdig, dS, pstn, click)
        await uasyncio.sleep(0.04)
        
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
        await uasyncio.sleep(0.04)
        pass
    while OK.value()==0:
        dE, pstn, click = await nineDigSet(dEdig, dE, pstn, click)
        await uasyncio.sleep(0.04)

    #switch screen to top_pauseTime
    lcd_settings()
    lcd.move_to(2, 1)
    lcd.putstr("Top Pause Time")
    lcd.move_to(0, 0)
    lcd.putstr(str(top_pauseTime))
    pstn = 0
    lcd.move_to(pstn,0)

    while OK==1:
        await uasyncio.sleep(0.04)
        pass
    while OK.value()==0:
        pT, pstn, click = await nineDigSet(pTdig, pT, pstn, click)
        await uasyncio.sleep(0.04)
        
    dayStart = 0
    dayEnd = 0
    top_pauseTime = 0
    for i in range(dSdig):
        dayStart = dayStart + 10**(dSdig-i-1) * dS[i]
    for i in range(dEdig):
        dayEnd = dayEnd + 10**(dEdig-i-1) * dE[i]
    for i in range(pTdig):
        top_pauseTime = top_pauseTime + 10**(pTdig-i-1) * pT[i]
    
    return dayStart,dayEnd, top_pauseTime
   
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

async def menu(q, dayStart, dayEnd, top_pauseTime, timeFactor): 
    while True:
        print("Waiting for selection")
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
            await uasyncio.sleep(0.04)
        settingChanged = 1
        if pstn==0:
            await RTC_manual()
            await q.put([0])
        elif pstn==1:
            rotateMotor_manual()
            await q.put([1])
        elif pstn==2:
            dayStart, dayEnd, top_pauseTime = await set_dayStartEnd(dayStart, dayEnd, top_pauseTime)
            await q.put([2, dayStart, dayEnd, top_pauseTime])
        else:
            timeFactor = await set_timeFactor(timeFactor)
            await q.put([3, timeFactor])
        
        await uasyncio.sleep(0.04)
        #return settingChanged, dayStart, dayEnd, top_pauseTime, timeFactor
                
if __name__ == "__main__":
    dayStart = 21600
    dayEnd = 64800
    top_pauseTime = 3600
    timeFactor = 288
    q = queue.Queue()
#     RTC_manual()
#     rotateMotor_manual()
#     RTC_manual()
#     set_timeFactor(288)
#     set_dayStartEnd(21600, 64800)
#    while True:
        #settingChanged, dayStart, dayEnd, top_pauseTime, timeFactor = uasyncio.run(menu(q, dayStart, dayEnd, top_pauseTime, timeFactor))
    uasyncio.run(menu(q, dayStart, dayEnd, top_pauseTime, timeFactor))
