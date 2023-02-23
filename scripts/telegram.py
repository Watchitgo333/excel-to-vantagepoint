import pyautogui as pg
from PIL import ImageGrab
import time
import pytesseract
from pytesseract import Output

#print(pg.position())

x,y = pg.locateCenterOnScreen("wspacelong.png")

#pg.moveTo(x,y)
pg.leftClick(x,y)

pg.hotkey('shift', 'tab')

pg.typewrite('22007\n')

pg.hotkey('ctrl', 'f')

time.sleep(1.5)

pg.typewrite('schematic\n')

x,y = pg.locateCenterOnScreen("sd3.png", confidence=.8)

if x or y == None:
    print("none")

pg.leftClick(x,y)

pg.hotkey('ctrl', 'f')

pg.typewrite('mechanical\n')

x,y = pg.locateCenterOnScreen("mech2.png", confidence=.8)

pg.leftClick(x,y)

pg.press("tab")

pg.press("enter")

pg.press("tab", presses = 3, interval=.5)

pg.typewrite("00012\n")

pg.press("tab",interval=1)

pg.typewrite(".25")

x,y = pg.locateCenterOnScreen("comment.png", confidence=.8)

pg.leftClick(x,y)

pg.typewrite("Katie is the best!")