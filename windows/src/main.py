import pyautogui as pya
import pyperclip
import time

import keyboard
import config

var  = ""
clipboard = ["" for i in range(11)]

possibleClipboards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def check_clipboard():

    pya.hotkey('cmd', 'c')
    time.sleep(0.1)

    return pyperclip.paste()

while True:

    while keyboard.is_pressed(config.baseKey) and keyboard.is_pressed(config.copyKey):
        
        for i in possibleClipboards:
        
            if keyboard.is_pressed(i):
        
                    var = check_clipboard()
                    print(var+" on clipboard "+i)

                    clipboard[int(i)] = var

    
    while keyboard.is_pressed(config.baseKey) and keyboard.is_pressed(config.pasteKey):
        
        for i in possibleClipboards:
             
            if i != "" and keyboard.is_pressed(i):
                
                pyperclip.copy(clipboard[int(i)])
                print("copied "+clipboard[int(i)]+ " to regular clipboard")
                time.sleep(0.1)