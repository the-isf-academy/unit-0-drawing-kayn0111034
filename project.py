# Drawing project
# Author: Wesley Chui

from turtle import *

def setup(x, y):
    "Sets up the turtle, ready to draw, at the given coordinates"
    penup()
    goto(x, y)
    pendown()
    setheading(0)

#inner_draw_headphones
setup(-100,-100)
left(90)

forward(30)
left(51.34019175)
forward(36.06)#64.03
right(80)
forward(44.72) #44.72 not understand
right(60)
forward(90)
#mirrored
right(60)
forward(44.72)
right(80)
forward(36.06)
left(52)
forward(30)

#outer_draw_headphones
left(130)
forward(70)
left(85)
forward(80)
left(53)
forward(90)
#mirrored
left(53)
forward(80)
left(85)
forward(70)

#small Draw_Headphones left
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
setup(-100,-100)
left(90)

forward(28)
right(110)
forward(32)
left(85)
forward(16)
right(110)
forward(19)
left(70)
forward(32)

setup(-100,-100)
left(90)

forward(5)
right(130)
forward(53)
left(85)
forward(55)

#mini_mask
setup(-97,-100)
left(90)

input("Press enter to continue...")
