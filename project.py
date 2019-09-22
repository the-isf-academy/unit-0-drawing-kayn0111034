# Drawing project
# Author: Wesley Chui

from turtle import *

def setup(x, y):
    "Sets up the turtle, ready to draw, at the given coordinates"
    penup()
    goto(x, y)
    pendown()
    setheading(0)

#draw_headphones
setup(-100,-100)

left(90)
forward(50)
left(51.34019175)
forward(36.06)#64.03
right(80)
forward(44.72) #44.72 not understand
right()
input("Press enter to continue...")
