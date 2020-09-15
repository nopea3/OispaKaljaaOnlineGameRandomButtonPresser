import pywinauto
from pywinauto import keyboard

import time
from random import randint
import pyautogui

time.sleep(5)
i = 0
a = 1
while i < 1000:
    a = randint(1,4)
    
    if a == 1:
        pywinauto.keyboard.send_keys('{VK_LEFT}')
    if a == 2:
        pywinauto.keyboard.send_keys('{VK_UP}')
    if a == 3:
        pywinauto.keyboard.send_keys('{VK_RIGHT}')
    if a == 4:
        pywinauto.keyboard.send_keys('{DOWN}')
    
    
    '''
    pywinauto.keyboard.send_keys('{VK_LEFT}')
    pywinauto.keyboard.send_keys('{VK_UP}')
    pywinauto.keyboard.send_keys('{VK_RIGHT}')
    pywinauto.keyboard.send_keys('{DOWN}')
    '''

    pyautogui.click()
    print("Random press", a, "how many presses done", i)
    i = i + 1
    time.sleep(0.001)
    
    