from  Testingproject import *

if __name__ == '__main__':
    speed(0)

    setup(-100,-100)
    left(90)

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
    #mirrored_outer_headphones()
    setup(-103,-97)
    left(90)
    small_draw_headphones(1)
#    small_right_draw_headphones()
    setup(-20,-97)
    left(90)
    small_draw_headphones(-1)

    setup(-100,-100)
    left(90)
    draw_big_mask_top(1)

    setup(-24,-100)
    left(90)
    draw_big_mask_top(-1)

    setup(-103,-97)
    left(90)
    draw_big_mask_bottom(1)

    setup(-24,-97)
    left(90)
    draw_big_mask_bottom(-1)

    setup(-95,-95)
    left(90)
    mini_mask_top(1)

    setup(-29,-93)
    left(90)
    mini_mask_top(-1)

    setup(-28,-93)
    right(90)
    mini_mask_bottom(1)

    setup(-95,-95)
    left(15)
    mini_mask_bottom(-1)

    setup(-115,-25)
    draw_main_hair1()

    right(35)
    backward(10)

    left(65)
    draw_main_hair2()

    setup(-105,-40)
    draw_outer_eye()


input("Press enter to continue...")
