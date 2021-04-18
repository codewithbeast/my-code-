import pyautogui
import os
import time
import datetime
import pywhatkit

hour_time = int(datetime.datetime.now().hour)
minute_time = int(datetime.datetime.now().minute)



zoom_path = "C:\\Users\\Mahada\\Desktop\\Zoom - Shortcut.lnk"
os.startfile(zoom_path)

time.sleep(2)
pyautogui.click(483,416)
time.sleep(2)
pyautogui.click(492,145)
pyautogui.press('backspace')

time.sleep(1)
pyautogui.write('starts at 2:30 pm and ends at 3:30 pm')
pyautogui.click(694,683)
time.sleep(2)
pyautogui.hotkey('alt','f4')
time.sleep(1.3)
pyautogui.click(724,129)
time.sleep(2)
pyautogui.click(750,174)
minute_time = minute_time+2
print(minute_time)
