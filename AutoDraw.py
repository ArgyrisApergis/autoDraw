# packages
import os
import cv2
import pyautogui as pg
import time

paint_path = "C:/Users/Archie/AppData/Local/Microsoft/WindowsApps/Microsoft.Paint_8wekyb3d8bbwe/mspaint.exe"
os.startfile(paint_path)

# coordinates of where to start drawing (change if needed!)
x_start = 300
y_start = 300

originalImage = cv2.imread('./bulk/image2.png')

# convert image to grayscale
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# convert image to black and white
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# loop over pixel rows
for y in range(len(blackAndWhiteImage)):
    # init row
    row = blackAndWhiteImage[y]
    # put mouse mointer into initial position
    pg.moveTo(x_start, y_start)   
    # loop over pixel cols
    for x in range(len(row)):
        if row[x] == 0:
                # draw pixel!
            pg.click(x_start + x, y_start + y, _pause=False)
    
            # animation speed
            time.sleep(0.0001)