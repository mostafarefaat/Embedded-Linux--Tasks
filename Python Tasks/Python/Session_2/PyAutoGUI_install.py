import pyautogui

from time import sleep

pyautogui.hotkey('win')
sleep(2)
pyautogui.typewrite("vs")
sleep(2)

try:
    vscode_location = None
    while vscode_location is None:
        vscode_location = pyautogui.locateOnScreen('vscode.png')
        print("Center",pyautogui.center(vscode_location))
        sleep(2)
    pyautogui.click(994,200,duration=1)
    sleep(4)

    extensions_location = None
    while extensions_location is None:
        extensions_location = pyautogui.locateOnScreen('ext.png')
        print("Center",pyautogui.center(extensions_location))
        sleep(2)              
    pyautogui.click(extensions_location.left+30,extensions_location.top+20,duration=1)
    pyautogui.write("clangd")

    sleep(3)
    clangd_location = None
    while clangd_location is None:
        clangd_location = pyautogui.locateOnScreen('clangd.png')
        print("Center",pyautogui.center(clangd_location))
        sleep(2)              
    pyautogui.click(clangd_location.left+30,clangd_location.top+20,duration=1)

    sleep(3)
    install_icon_location = None
    while install_icon_location is None:
        install_icon_location = pyautogui.locateOnScreen('install.png')
        print("Center",pyautogui.center(install_icon_location))
        sleep(2)              
    pyautogui.click(install_icon_location.left+30,install_icon_location.top+20,duration=1)

    sleep(3)
    search_bar_location = None
    while search_bar_location is None:
        search_bar_location = pyautogui.locateOnScreen('search.png')
        print("Center",pyautogui.center(search_bar_location))
        sleep(2)              
    pyautogui.click(search_bar_location.left+30,search_bar_location.top+20,duration=1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')

    pyautogui.write("c++ testmate")

    sleep(3)
    ctestMAte_location = None
    while ctestMAte_location is None:
        ctestMAte_location = pyautogui.locateOnScreen('ctestmate.png')
        print("Center",pyautogui.center(ctestMAte_location))
        sleep(2)              
    pyautogui.click(ctestMAte_location.left+30,ctestMAte_location.top+20,duration=1)

    sleep(3)
    install_icon_location = None
    while install_icon_location is None:
        install_icon_location = pyautogui.locateOnScreen('install.png')
        print("Center",pyautogui.center(install_icon_location))
        sleep(2)              
    pyautogui.click(install_icon_location.left+30,install_icon_location.top+20,duration=1)

    sleep(3)
    search_bar_location = None
    while search_bar_location is None:
        search_bar_location = pyautogui.locateOnScreen('search.png')
        print("Center",pyautogui.center(search_bar_location))
        sleep(2)              
    pyautogui.click(search_bar_location.left+30,search_bar_location.top+20,duration=1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')

    pyautogui.write("c++ helper")

    sleep(3)
    chelper_location = None
    while chelper_location is None:
        chelper_location = pyautogui.locateOnScreen('chelper.png')
        print("Center",pyautogui.center(chelper_location))
        sleep(2)              
    pyautogui.click(chelper_location.left+30,chelper_location.top+20,duration=1)

    sleep(3)
    install_icon_location = None
    while install_icon_location is None:
        install_icon_location = pyautogui.locateOnScreen('install.png')
        print("Center",pyautogui.center(install_icon_location))
        sleep(2)              
    pyautogui.click(install_icon_location.left+30,install_icon_location.top+20,duration=1)

    sleep(3)
    search_bar_location = None
    while search_bar_location is None:
        search_bar_location = pyautogui.locateOnScreen('search.png')
        print("Center",pyautogui.center(search_bar_location))
        sleep(2)              
    pyautogui.click(search_bar_location.left+30,search_bar_location.top+20,duration=1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')

    pyautogui.write("cmake")

    sleep(3)
    cmake_location = None
    while cmake_location is None:
        cmake_location = pyautogui.locateOnScreen('cmake.png')
        print("Center",pyautogui.center(cmake_location))
        sleep(2)              
    pyautogui.click(cmake_location.left+30,cmake_location.top+20,duration=1)

    sleep(3)
    install_icon_location = None
    while install_icon_location is None:
        install_icon_location = pyautogui.locateOnScreen('install.png')
        print("Center",pyautogui.center(install_icon_location))
        sleep(2)              
    pyautogui.click(install_icon_location.left+30,install_icon_location.top+20,duration=1)

    sleep(3)
    search_bar_location = None
    while search_bar_location is None:
        search_bar_location = pyautogui.locateOnScreen('search.png')
        print("Center",pyautogui.center(search_bar_location))
        sleep(2)              
    pyautogui.click(search_bar_location.left+30,search_bar_location.top+20,duration=1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    
    pyautogui.write("cmake tools")


    sleep(3)
    cmaketools_location = None
    while cmaketools_location is None:
        cmaketools_location = pyautogui.locateOnScreen('cmaketools.png')
        print("Center",pyautogui.center(cmaketools_location))
        sleep(2)              
    pyautogui.click(cmaketools_location.left+30,cmaketools_location.top+20,duration=1)

    sleep(3)
    install_icon_location = None
    while install_icon_location is None:
        install_icon_location = pyautogui.locateOnScreen('install_2.png')
        print("Center",pyautogui.center(install_icon_location))
        sleep(2)              
    pyautogui.click(install_icon_location.left+30,install_icon_location.top+20,duration=1)

    sleep(3)
    search_bar_location = None
    while search_bar_location is None:
        search_bar_location = pyautogui.locateOnScreen('search.png')
        print("Center",pyautogui.center(search_bar_location))
        sleep(2)              
    pyautogui.click(search_bar_location.left+30,search_bar_location.top+20,duration=1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')

 
except pyautogui.ImageNotFoundException:
    print("Image not Found")
