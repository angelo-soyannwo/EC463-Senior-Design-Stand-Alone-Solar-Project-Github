from my_lib import RTC_DS3231
rtc = RTC_DS3231.RTC()
rtc.DS3231_SetTime (b'\x00\x45\x23')
t = rtc.DS3231_ReadTime (1)
print(t)

