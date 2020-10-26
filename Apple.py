import pyautogui, time, keyboard, random, win32api, win32con

while 1:
    if pyautogui.locateOnScreen('apple.png', confidence=0.75, grayscale=True) != None:
        print('I can see an apple!')
        time.sleep(0.5)
    else:
        print('I cannot see any apples.')
        time.sleep(0.5)