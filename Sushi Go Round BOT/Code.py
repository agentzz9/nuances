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
import win32api, win32con
import ImageOps
from numpy import *

# Globals
# ------------------
 
x_pad = 187
y_pad = 237

# Classes
# ------------------
class Cord:
     
    f_shrimp = (39, 329)
    f_rice = (95, 337)
    f_nori = (32, 383)
    f_roe = (88, 390)
    f_salmon = (37, 435)
    f_unagi = (88, 438)

#--------------------
    phone = (589, 354)

    menu_toppings = (518, 273)
    t_closephone = (594, 333)
    t_shrimp = (464, 210)
    t_unagi = (547, 213)
    t_nori = (461, 263)
    t_fishegg = (544, 274)
    t_salmon = (467, 328)
    t_back = (557, 330)
    t_exit = (593, 337)

    menu_rice = (531, 296)
    menu_sake = (523, 319)
    r_rice = s_sake = (547, 268)
    r_back = s_back = (505, 334)
    r_exit = s_exit = (583, 336)
    
    delivery_norm = (483, 289)

    #--toclear plates
    plate_1 = (85, 208)
    plate_2 = (188, 209)
    plate_3 = (287, 209)
    plate_4 = (390, 208)
    plate_5 = (492, 210)
    plate_6 = (588, 207)
    

# Inventory
#-------------------

foodOnHand = {
    'shrimp':5,
    'rice':10,
    'nori':10,
    'roe':10,
    'salmon':5,
    'unagi':5
    }


# Functions
# ------------------
def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab()
    return im
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+ '.png', 'PNG')

def grab():
    box = (x_pad + 1, y_pad + 1, x_pad+640 ,y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab())
    a = array( im.getcolors() )
    a = a.sum()
    print a
    return a


# Bubbles_____________________________________

'''
10px y
63px x

box1 25, 63
box2 126, 63
box3 227, 63
box4 328, 63
box5 429, 63
box6 530, 63

'''

def get_seat_one():
    box = (x_pad+25,y_pad+63,x_pad+25+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (x_pad+126,y_pad+63,x_pad+126+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (x_pad+227,y_pad+63,x_pad+227+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (x_pad+328,y_pad+63,x_pad+328+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (x_pad+429,y_pad+63,x_pad+429+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (x_pad+530,y_pad+63,x_pad+530+63,y_pad+63+10)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

sushiTypes = {2999:'onigiri', 
              3256:'caliroll',
              2926:'gunkan'}

class Blank:
    seat_1 = 5684
    seat_2 = 4731
    seat_3 = 9543
    seat_4 = 9059
    seat_5 = 4790
    seat_6 = 7581
    
#Bubbles, seats END.________________________

    
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def startGame():
    button_mute_music_cords = (308, 369)
    button_play_cords = (313, 200)
    button_continue_1_cords = (320, 390)
    button_continue_2_cords = (320, 390)
    button_skip_tutorial_cords = (582, 449)
    button_continue_3_cords = (308, 373)

    mousePos(button_mute_music_cords)
    leftClick()
    time.sleep(.1)
    
    mousePos(button_play_cords)
    leftClick()
    time.sleep(.1)

    mousePos(button_continue_1_cords)
    leftClick()
    time.sleep(.1)

    mousePos(button_continue_2_cords)
    leftClick()
    time.sleep(.1)

    mousePos(button_skip_tutorial_cords)
    leftClick()
    time.sleep(.1)

    mousePos(button_continue_3_cords)
    leftClick()
    time.sleep(.1)

def clear_tables():
    mousePos(Cord.plate_1)
    leftClick()
    mousePos(Cord.plate_2)
    leftClick()
    mousePos(Cord.plate_3)
    leftClick()
    mousePos(Cord.plate_4)
    leftClick()
    mousePos(Cord.plate_5)
    leftClick()
    mousePos(Cord.plate_6)
    leftClick()
    time.sleep(1)
    
def foldMat():
    mousePos((Cord.f_rice[0]+40, Cord.f_rice[1]))
    leftClick()
    time.sleep(.5)

'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
'''
def makeFood(food):
    if food == 'caliroll':
        print 'Making caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)
        
    elif food == 'onigiri':
        print 'Making onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print 'Making gunkan'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)

        
def buyFood(food): #test this... facing issues

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(0.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.r_rice) != (240, 240, 240):
            print 'rice is available'
            mousePos(Cord.r_rice)
            time.sleep(.1)
            leftClick()
            time.sleep(.1)
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            mousePos(Cord.r_exit)
            leftClick()
            time.sleep(1)
            #buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(0.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (0, 34, 64):
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            time.sleep(.1)
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            #buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(0.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_fishegg) != (0, 34, 64):
            print 'roe is available'
            mousePos(Cord.t_fishegg)
            time.sleep(.1)
            leftClick()
            time.sleep(.1)
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            #buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)

def check_bubs():

    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1
 
    else:
        print 'Table 1 unoccupied'
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2
 
    else:
        print 'Table 2 unoccupied'
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3
 
    else:
        print 'Table 3 unoccupied'
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4
 
    else:
        print 'Table 4 unoccupied'
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5
 
    else:
        print 'Table 5 unoccupied'
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 1 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6
 
    else:
        print 'Table 6 unoccupied'
 
    clear_tables()
                          
def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()
