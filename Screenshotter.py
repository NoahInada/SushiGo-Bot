__author__ = 'Noah'
"""
1980x1020 resolution, miniclip window pushed to left half of screen
adjust pads as necessary
"""
from PIL import ImageGrab
import time
import ImageOps
from numpy import *
'''
x_pad = 21
y_pad = 233
#Desktop

x_pad = 145
y_pad = 214
#Laptop
'''
inc = 0
x_pad = 145
y_pad = 214
#laptop scrolled psiphon


bubbleCords = {
    'seat1': [(25, 64), (88, 74)],
    'seat2': [(126, 64), (189, 74)],
    'seat3': [(227, 64), (290, 74)],
    'seat4': [(328, 64), (391, 74)],
    'seat5': [(429, 64), (492, 74)],
    'seat6': [(530, 64), (593, 74)]
}

def getGrayscale(cords):
    global inc
    box = (cords[0][0]+x_pad, cords[0][1] + y_pad, cords[1][0] + x_pad, cords[1][1] + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    return a

def scanBubbles():
    for key in bubbleCords.keys():
        print key + ': ' + str(getGrayscale(bubbleCords[key]))

def getBubblesGS():
    bubbles = {}
    for key in bubbleCords.keys():
        bubbles[key] = getGrayscale(bubbleCords[key])
        #for finding bubble GS: print str(key) + ': ' + str(getGrayscale(bubbleCords[key]))
        time.sleep(.1)
    return bubbles

def screenGrab():
    box = (x_pad, y_pad, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    #'save' is from the time package. arguments:(file location, file type)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im
#cords for first bubble: (25, 64), (88, 74)
def findStartCord():
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
#findStartCord()

def grab():
    box = (x_pad, y_pad, x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a