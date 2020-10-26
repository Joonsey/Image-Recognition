from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con

#displayMousePosition()

# tile 1 = X600 / Y550
# tile 2 = X700 / Y550
# tile 3 = X800 / Y550
# tile 4 = X900 / Y550

# website: https://www.agame.com/game/magic-piano-tiles


def clickMouse(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(600, 550)[2] == 0:
        clickMouse(600, 550)

    if pyautogui.pixel(700, 550)[2] == 0:
        clickMouse(700, 550)

    if pyautogui.pixel(800, 550)[2] == 0:
        clickMouse(800, 550)

    if pyautogui.pixel(900, 550)[2] == 0:
        clickMouse(900, 550)