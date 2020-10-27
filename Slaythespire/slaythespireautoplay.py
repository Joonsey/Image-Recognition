import pyautogui, time, win32api, win32con, keyboard
from pyautogui import screenshot, locateOnScreen, displayMousePosition

Energy = 3

#displayMousePosition()

def clickMouse(x,y):
    win32api.SetCursorPos((x, y))
    time.sleep(1.8)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

class Hand():
    def __init__(self):
        self.strike = self.locatestrike()
        self.defend = self.locatedefend()
        self.enemy = self.locateenemy()

    def locatedefend(self):
        print('Tries to locate defend...')
        d = pyautogui.locateOnScreen('defends/defend.png', confidence=0.7)
        d1 = pyautogui.locateOnScreen('defends/defend 1.png', confidence=0.7)
        d2 = pyautogui.locateOnScreen('defends/defend 2.png', confidence=0.7)
        if d != None:
            return d
        elif d1 != None:
            return d1
        elif d2 != None:
            return d2
        

    def locatestrike(self):
        print('Tries to locate strike...')
        d = pyautogui.locateOnScreen('strikes/strike.png', confidence=0.7)
        d1 = pyautogui.locateOnScreen('strikes/strike 1.png', confidence=0.7)
        d2 = pyautogui.locateOnScreen('strikes/strike 2.png', confidence=0.7)
        if d != None:
            return d
        elif d1 != None:
            return d1
        elif d2 != None:
            return d2

    def locateenemy(self):
        print('Tries to locate enemy...')
        e1 = pyautogui.locateOnScreen('enemies/enemy 1.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e2 = pyautogui.locateOnScreen('enemies/enemy 2.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e3 = pyautogui.locateOnScreen('enemies/enemy 3.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e4 = pyautogui.locateOnScreen('enemies/enemy 4.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e5 = pyautogui.locateOnScreen('enemies/enemy 5.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e6 = pyautogui.locateOnScreen('enemies/enemy 6.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e7 = pyautogui.locateOnScreen('enemies/enemy 7.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e8 = pyautogui.locateOnScreen('enemies/enemy 8.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e9 = pyautogui.locateOnScreen('enemies/enemy 9.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e10 = pyautogui.locateOnScreen('enemies/enemy 10.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e11 = pyautogui.locateOnScreen('enemies/enemy 11.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        e12 = pyautogui.locateOnScreen('enemies/enemy 12.png', region=(1050, 500, 850, 350), confidence=0.5, grayscale=True)
        if e1 != None:
            return e1
        elif e2 != None:
            return e2
        elif e3 != None:
            return e3
        elif e4 != None:
            return e4
        elif e5 != None:
            return e5
        elif e6 != None:
            return e6
        elif e7 != None:
            return e7
        elif e8 != None:
            return e8
        elif e9 != None:
            return e9
        elif e10 != None:
            return e10
        elif e11 != None:
            return e11
        elif e12 != None:
            return e12



def strike(box, enemy):
    try:
        print('Located strike')
        win32api.SetCursorPos((int(box[0]+(box[2]/2)), int(box[1]+(box[3]/2)+50)))
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1.8)
        win32api.SetCursorPos((int(enemy[0]+(enemy[2]/2)), int(enemy[1]+(enemy[3]/2)+25)))
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    except: 
        return False
        time.sleep(2)
        mapscreen()


def defend(box):
    try:
        print('Located defend')
        win32api.SetCursorPos((int(box[0]+(box[2]/2)), int(box[1]+(box[3]/2)+50)))
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1.8)
        win32api.SetCursorPos((int(box[0]+(box[2]/2)), int(box[1]+(box[3]/2)-165)))
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    except:
        return False


def mapscreen():
    location = locateOnScreen('Icons/skipRewardsButton.png',confidence=0.65, grayscale=True)
    location2 = locateOnScreen('Icons/skipCardButton.png',confidence=0.65, grayscale=True)
    if location != None:
        print('Skipped reward...')
        clickMouse(int(location[0]+(location[2]/2)), int(location[1]+(location[3]/2)))
        time.sleep(2)
        print('Looking for icons...')
        found = False
        while found == False:
            location2 = locateOnScreen('Icons/enemyicon.png', confidence=0.8, grayscale=True) 
            if location2 != None:
                print('Clicking enemies')
                clickMouse(int(location2[0]+(location2[2]/2)), int(location2[1]+(location2[3]/2)))
                found = True

    elif location2 != None:
        print('Skipped reward...')
        clickMouse(int(location2[0]+(location2[2]/2)), int(location2[1]+(location2[3]/2)))
        time.sleep(2)
        print('Looking for icons...')
        found = False
        while found == False:
            location2 = locateOnScreen('Icons/enemyicon.png', confidence=0.8, grayscale=True) 
            if location2 != None:
                print('Clicking enemies')
                clickMouse(int(location2[0]+(location2[2]/2)), int(location2[1]+(location2[3]/2)))
                found = True


def getEnergy():
    found = False
    while found == False:
        try:
            if locateOnScreen('energy/3 energy.png', confidence=0.8, grayscale=True) != None:
                print('You have 3 energy')
                return 3
                time.sleep(0.5)
                found = True
            elif locateOnScreen('energy/2 energy.png', confidence=0.8, grayscale=True) != None:
                print('You have 2 energy')
                return 2
                time.sleep(0.5)
                found = True            
            elif locateOnScreen('energy/1 energy.png', confidence=0.8, grayscale=True) != None:
                print('You have 1 energy')
                return 1
                time.sleep(0.5)
                found = True            
            elif locateOnScreen('energy/0 energy.png', confidence=0.8, grayscale=True) != None:
                print('You have 0 energy')
                return 0
                time.sleep(0.5)
                found = True
            
        except:
            pass
while True:
    mapscreen()
    if getEnergy() == 0:
        try:
            location = locateOnScreen('Icons/EndTurnButton.png',confidence=0.9, grayscale=True)
            clickMouse(int(location[0]+(location[2]/2)), int(location[1]+(location[3]/2)))
            print('clicked')
            time.sleep(4)
            mapscreen()
        except:
            mapscreen()    

    else:
        while getEnergy() != 0:
            hand = Hand()
            if not strike(hand.strike, hand.enemy):
                if not defend(hand.defend):
                    mapscreen()
                    #try:
                    #    location = locateOnScreen('Icons/EndTurnButton.png',confidence=0.9, grayscale=True)
                    #    clickMouse(int(location[0]+(location[2]/2)), int(location[1]+(location[3]/2)))
                    #    print('clicked')
                    #    time.sleep(4)
                    #except:
                    #    mapscreen()