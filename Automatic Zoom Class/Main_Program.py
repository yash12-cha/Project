import time
from datetime import datetime
from pynput.keyboard import Controller, Key
# Import file containing Meeting Details
from data import lst
import webbrowser

keyboard = Controller() # Controller method to control the Keyboard and simulate keystrokes

IS_STARTED = False

for i in lst:
    while True:
        if IS_STARTED == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                IS_STARTED = True
        elif IS_STARTED == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press('w')
                time.sleep(1)
                keyboard.press(Key.enter)
                IS_STARTED = False
                break
