__author__ = 'Noah'

import Screenshotter
import Constants
import win32api
import win32con
import time

Cord = Constants.Cordinates
Recipe = Constants.Recipes
Colors = Constants.AllColors
Shot = Screenshotter
rotationTimer = 0
numClicks = 0
x_pad = Shot.x_pad
y_pad = Shot.y_pad

foodOnHand = {'shrimp': 5, 'rice': 10, 'nori':10, 'roe':10, 'salmon':5, 'unagi':5}
ingredientTimer = {'shrimp': 4, 'rice': 4, 'nori': 4, 'roe': 4, 'salmon': 4, 'unagi': 4}


def incIngredientTimer():
    for food in ingredientTimer:
        ingredientTimer[food] += 1


def checkForBreak():
    if numClicks >= 100:
        raise ValueError('reached ' + str(numClicks) + ' clicks')


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    #print "Click."

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
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y

def click(cord):
    global numClicks
    numClicks += 1
    mousePos(cord)
    leftClick()
    print numClicks

def checkHasDolla(RGB_cord, expected_RGB):
    s = Shot.screenGrab()
    if s.getpixel(RGB_cord) == expected_RGB:
        return False
    else:
        return True


def normal_deliver():
    click(Cord.normal_delivery)


def exit_menu():
    click(Cord.exit_menu)


def bought_food(food):
    global ingredientTimer
    foodOnHand[food] += 5
    ingredientTimer[food] = 0


def boughtmo_food(food):
    global ingredientTimer
    foodOnHand[food] += 10
    ingredientTimer[food] = 0


def check_to_buy_food():
    for food, j in foodOnHand.items():
        if food == 'rice' or food == 'nori' or food == 'roe':
            if j <= 5 and ingredientTimer[food] > 3 :
                print 'Replenishing ' + food + '...'
                buy_food(food)
        else:
            if j <= 2 and ingredientTimer[food] > 3:
                print 'Replenishing ' + food + '...'
                buy_food(food)


def buy_food(food):
    click(Cord.phone)
    if food == 'rice':
        click(Cord.rice_menu)
        if checkHasDolla(Cord.m_rice, Colors.no_rice):
            print 'Bought Rice!'
            click(Cord.m_rice)
            normal_deliver()
            boughtmo_food('rice')
        else:
            print 'Could not buy rice'
            click(Cord.exit_menu)
    else:
        click(Cord.topping_menu)
        if checkHasDolla(Cord.toBuyFoodCords[food], Colors.no_roe):
            print 'Bought ' + food + '!'
            click(Cord.toBuyFoodCords[food])
            normal_deliver()
            boughtmo_food(food)
        else:
            print 'Could not buy ' + food
            exit_menu()


def check_for_enough(food):
    for ingredient in Recipe.foods[food].keys():
        if foodOnHand[ingredient] < Recipe.foods[food][ingredient] or ingredientTimer[ingredient] <= 3:
            print 'Cannot make ' + food
            return False
    print 'Making... ' + food
    return True


def make_food(food):
    for ingredient in Recipe.foods[food].keys():
        for num in range(Recipe.foods[food][ingredient]):
            click(Cord.onHandFoodCords[ingredient])
            foodOnHand[ingredient] -= 1
    fold_mat()


def fold_mat():
    click((193, 382))
    print 'Folded!'
    time.sleep(1.2)


def check_bubs():
    global rotationTimer
    GS_Array = Shot.getBubblesGS()
    for key in GS_Array:
        if GS_Array[key] in Colors.sushiGS.keys():
            desiredFood = Colors.sushiGS[GS_Array[key]]
            print key + ' wants a ' + desiredFood
            if check_for_enough(desiredFood):
                make_food(desiredFood)
        else:
            print str(GS_Array[key]) + 'Nothing desired at table' + key
    check_to_buy_food()
    clear_tables()
    incIngredientTimer()


def intro_sequence():
    click((316, 206))
    click((302, 387))
    click((581, 454))
    click((307, 383))


def clear_tables():
    for plate_cord in Cord.plates:
        click(plate_cord)
    time.sleep(.1)


def loop_cords(num_o_cords):
    for i in range(num_o_cords):
        time.sleep(3.0)
        get_cords()


def pause():
    time.sleep(3.0)


def main():
    pause()
    intro_sequence()
    while True:
        check_bubs()
        #checkForBreak()
        print 'one rotation'
main()