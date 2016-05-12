"""
 
All coordinates assume a screen resolution of 1366x768, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Screen fully scrolled up.
x_pad = 187
y_pad = 237
Play area =  x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480
"""

# Imports
# -----------------
import ImageGrab
import os
import time

# Globals
# ------------------
 
x_pad = 187
y_pad = 237

# Functions
# ------------------
def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+ '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
