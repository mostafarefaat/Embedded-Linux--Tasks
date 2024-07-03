import pyautogui

from time import sleep

import webbrowser


webbrowser.get('firefox').open_new_tab("https://www.google.com")
sleep(3) #Wait for Site to Open


#Click on Gmail 
try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('gmail.png')
        #print("Center",pyautogui.center(location))
        sleep(1)
except pyautogui.ImageNotFoundException:
    print("Gmail Result Image not Found")

pyautogui.click(location.left+20,location.top+10,duration=1)
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

