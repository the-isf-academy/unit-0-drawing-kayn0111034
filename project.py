# Drawing project
# Author: Wesley Chui

from  Testingproject import *

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


input("Press enter to continue...")
