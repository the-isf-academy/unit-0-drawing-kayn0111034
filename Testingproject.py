# Drawing project
# Author: Wesley Chui

from turtle import *

def setup(x, y):
    "Sets up the turtle, ready to draw, at the given coordinates"
    penup()
    goto(x, y)
    pendown()
    setheading(0)

def inner_draw_headphones(direction): #mirrored

    forward(30)
    left(direction*51.34019175)
    forward(36.06)#64.03
    right(direction*80)
    forward(44.72) #44.72 not understand
    right(direction*60)
    forward(45)

#outer_headphones
def outer_headphones(direction):
    left(direction*130)
    forward(70)
    left(direction*85)
    forward(80)
    left(direction*55)
    forward(45)
#small Draw_Headphones left
def small_draw_headphones(direction):

    forward(25)
    left(direction*51.34019175)
    forward(39.6)
    right(direction*80)
    forward(20)
    left(direction*165)
    forward(35)
    left(direction*91)
    forward(60)

#Draw_mask
def draw_big_mask_top(direction):


    forward(25)
    right(direction*110)
    forward(32)
    left(direction*70)
    forward(13)

def draw_big_mask_bottom(direction):

    forward(5)
    right(direction*130)
    forward(51)

#mini_mask
def mini_mask_top(direction):

    forward(12)
    right(direction*110)
    forward(30)
    left(direction*70)
    forward(8)


def mini_mask_bottom(direction):
    """
    right(direction*105)
    forward(8)
    left(direction*74.5)
    forward(32)

    right(direction*110)
    forward(10)
    right(direction*50)
    forward(43)
    right(75)
    forward(45)
    """

    right(51)
    forward(43)
    #right(75)
    #forward(45)
#Draw_hair
def draw_main_hair1():
    for hair in range(60):
        forward(1)
        right(0.8)
def draw_main_hair2():
    for hair in range (35):
        forward(1.5)
        right(0.85)
#use loop instead of circle
#outerhair
def draw_outer_hair1():
    for tophair in range(40):
        forward(1)
        right(1.5)
    setup(-3,-35)
    right(60)
    for righthair in range(130):
        forward(0.15)
        right(0.5)
def draw_outer_eye():
    for eye in range(20):
        forward(2)
        right(2)
    left(40)
    backward(20)
    right(180)
    for eyes in range(120):
        forward(0.2)
        right(0.6)
def draw_inner_eye():
    for sharingan in range(750):
        forward(0.04)
        right(0.5)



if __name__ == '__main__':
    speed(0)

    setup(-100,-100)
    left(90)
    fillcolor('dim grey')
    begin_fill()
    inner_draw_headphones(1)
    #mirrored_inner_headphones(1)
    setup(-24,-100)
    left(90)

    inner_draw_headphones(-1)

    setup(-24,-100)
    right(90)
    outer_headphones(1)

    setup(-100,-100)
    right(90)
    outer_headphones(-1)
    end_fill()
    #mirrored_outer_headphones()
    setup(-103,-95)
    left(90)
    fillcolor('steel blue')
    begin_fill()
    small_draw_headphones(1)

#    small_right_draw_headphones()
    setup(-20,-95)
    left(90)
    small_draw_headphones(-1)
    end_fill()

    fillcolor('dark green')

    setup(-100,-100)
    left(90)
    begin_fill()
    draw_big_mask_top(1)

    setup(-24,-100)
    left(90)
    draw_big_mask_top(-1)

    setup(-100,-97)
    left(90)
    draw_big_mask_bottom(1)

    setup(-24,-97)
    left(90)
    draw_big_mask_bottom(-1)
    end_fill()
    setup(-95,-92)
    left(90)
    fillcolor('sea green')
    begin_fill()
    mini_mask_top(1)

    setup(-29,-92)
    left(90)
    mini_mask_top(-1)

    setup(-28,-93)
    right(95)
    mini_mask_bottom(1)

    setup(-95,-93)
    left(15)
    mini_mask_bottom(-1)
    end_fill()
    setup(-115,-25)
    draw_main_hair1()

    right(35)
    backward(10)

    left(65)
    draw_main_hair2()

    fillcolor('dodger blue')

    setup(-105,-40)
    begin_fill()
    draw_outer_eye()
    end_fill()

    setup(-86,-43)
    fillcolor('black')
    begin_fill()
    draw_inner_eye()
    end_fill()

    setup(-40,-7)
    draw_outer_hair1()
