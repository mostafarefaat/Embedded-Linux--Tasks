import pyautogui

from time import sleep

pyautogui.hotkey('win')
sleep(2)
pyautogui.typewrite("fire")
sleep(2)

#Open FireFox
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('firefox.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("Fire Fox Image not Found")

pyautogui.click(location.left+50,location.top+30,duration=1)
sleep(3) #Wait for Site to Open

#Click on Search bar and write Gmail
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('firefoxsearch.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("Fire Fox Search Image not Found")

pyautogui.click(location.left+30,location.top+20,duration=1)
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')
pyautogui.press('backspace')
pyautogui.write("gmail")
pyautogui.press('enter')
sleep(4)#Wait for search

#Click on Gmail result
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('gmail.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("Gmail Result Image not Found")

pyautogui.click(location.left+50,location.top+50,duration=1)
sleep(5)#Wait for Gmail to Open

#Click Select all
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('select_all_icon.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("Select All Icon Image not Found")

pyautogui.click(location.left+30,location.top+20,duration=1)
sleep(0.5)#Wait for Selection

#Click Mark as Read
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('mark_as_read.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("mark As Read Icon Image not Found")

pyautogui.click(location.left+30,location.top+20,duration=1)
sleep(0.5)#Wait for Selection

