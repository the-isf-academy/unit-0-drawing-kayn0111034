# Drawing project
# Author: Wesley Chui

from turtle import *

def setup(x, y):
    "Sets up the turtle, ready to draw, at the given coordinates"
    penup()
    goto(x, y)
    pendown()
    setheading(0)

def inner_draw_headphones(mirrored):
    setup(-100,-100)
    left(90)

    forward(30)
    left(51.34019175)
    #left(-1*51.34019175)
    forward(36.06)#64.03
    right(80)
    forward(44.72) #44.72 not understand
    right(60)
    forward(90)
def mirrored_inner_headphones():
    right(60)
    forward(44.72)
    right(80)
    forward(36.06)
    left(52)
    forward(30)

#outer_headphones
def outer_headphones():
    left(130)
    forward(70)
    left(85)
    forward(80)
    left(53)
    forward(90)
#mirrored
def mirrored_outer_headphones():
    left(53)
    forward(80)
    left(85)
    forward(70)

#small Draw_Headphones left
def small_left_draw_headphones():
    setup(-103,-95)
    left(90)

    forward(25)
    left(51.34019175)
    forward(39.6)
    right(80)
    forward(20)
    left(165)
    forward(35)
    left(95)
    forward(65)

#small Draw_Headphones right
def small_right_draw_headphones():
    setup(-15,-95)
    left(90)

    forward(25)
    right(51.34019175)
    forward(39.6)
    left(80)
    forward(20)
    right(165)
    forward(31)
    right(90)
    forward(65)


#Draw_mask
def draw_big_mask():
    setup(-100,-100)
    left(90)

    forward(25)
    right(110)
    forward(32)
    left(70)
    forward(16)
    right(105)
    forward(14)
    left(75)
    forward(32)

    setup(-100,-100)
    left(90)

    forward(5)
    right(130)
    forward(53)
    left(85)
    forward(57)

#mini_mask
def mini_mask():
    setup(-95,-95)
    left(90)

    forward(12)
    right(110)
    forward(30)
    left(70)
    forward(10)
    right(105)
    forward(8)
    left(74.5)
    forward(32)

    right(110)
    forward(10)
    right(50)
    forward(43)
    right(75)
    forward(45)

#Draw_hair
def draw_main_hair():
    setup(-115,-25)
    circle(-70,55)

#outerhair
def draw_outer_hair():
    setup(-70,-7)




if __name__ == '__main__':
    speed(0)
    inner_draw_headphones()
    mirrored_inner_headphones()
    outer_headphones()
    mirrored_outer_headphones()
    small_left_draw_headphones()
    small_right_draw_headphones()
    draw_big_mask()
    mini_mask()
    draw_main_hair()
    draw_outer_hair()


input("Press enter to continue...")
