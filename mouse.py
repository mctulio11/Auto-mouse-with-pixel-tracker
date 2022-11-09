import pyautogui as pag
import random
import time
import sys
print('Press ctrl-c to quit')

try:
    while True:
        x = random.randint(1, 1080)
        y = random.randint(1, 1080)
        pag.moveTo(x,y,.5)
        time.sleep(.1)

except KeyboardInterrupt:
    print('\n')   