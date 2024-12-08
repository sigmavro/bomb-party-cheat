from pynput.keyboard import Listener, Key 
import pyperclip
import pyautogui
import sys
import time
import random
pyautogui.FAILSAFE = False
with open("wordlist.txt", "r") as file:
    word_list = file.read().splitlines()
def on_press(key):
    word = None
    word2 = None
    global bombpos, syllable, typearea, syllable2, chatarea
    random.shuffle(word_list)
    try:
        if key == Key.f4:
            bombpos = pyautogui.position()
            pyautogui.moveTo(bombpos)
            pyautogui.leftClick()
            pyautogui.leftClick()
            pyautogui.hotkey("ctrl", "c")
            syllable = pyperclip.paste()
            syllable = syllable.lower()
            for balls in word_list:
                if syllable in balls:
                    word = balls
                    break 
            if word:
                suffixlastpos = pyautogui.position() 
                pyautogui.moveTo(typearea)
                pyautogui.leftClick()
                pyautogui.typewrite(word, interval=0.10)
                pyautogui.hotkey("enter")
                pyperclip.copy("")
                pyautogui.moveTo(suffixlastpos)
        elif key == Key.f2:
            typearea = pyautogui.position()
        if key == Key.f8:
            bombpos2 = pyautogui.position()
            pyautogui.moveTo(bombpos2)
            pyautogui.leftClick()
            pyautogui.leftClick()
            pyautogui.hotkey("ctrl", "c")
            syllable2 = pyperclip.paste()
            syllable2 = syllable2.lower()
            for balls2 in word_list:
                if syllable2 in balls2:
                    word2 = balls2
                    break 
            if word2:
                pyautogui.moveTo(chatarea)
                pyautogui.leftClick()
                pyautogui.typewrite(word2, interval=0.04)
                pyautogui.hotkey("enter")
                pyperclip.copy("")
        elif key == Key.f9:
            chatarea = pyautogui.position()
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        sys.exit()
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
