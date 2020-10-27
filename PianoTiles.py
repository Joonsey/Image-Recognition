from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con

#displayMousePosition()

# tile 1 = X600 / Y550
# tile 2 = X700 / Y550
# tile 3 = X800 / Y550
# tile 4 = X900 / Y550

DEFAULTY = 600
tile1 = 375
tile2 = 465
tile3 = 550
tile4 = 650

# website: https://www.agame.com/game/magic-piano-tiles


def clickMouse(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(tile1, DEFAULTY)[2] == 0:
        clickMouse(tile1, DEFAULTY)

    if pyautogui.pixel(tile2, DEFAULTY)[2] == 0:
        clickMouse(tile2, DEFAULTY)

    if pyautogui.pixel(tile3, DEFAULTY)[2] == 0:
        clickMouse(tile3, DEFAULTY)

    if pyautogui.pixel(tile4, DEFAULTY)[2] == 0:
        clickMouse(tile4, DEFAULTY)