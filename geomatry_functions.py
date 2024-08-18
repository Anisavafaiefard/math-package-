from math import pi, sqrt

def volume_of_complete_sphere(r):
    # r : radius
    fraction = 4/3
    return fraction * pi * (r**3)

def space_of_complete_sphere(r):
    return 4*pi*r**2

def space_half_filled_sphere(r):
    return 3 * pi * r ** 2

def volume_of_pyramid(space_base, height):
    fraction = 1/3
    return fraction * space_base * height

def space_rectangle(length, width):
    return length * width

def space_square(square_side):
    return square_side ** 2

def triangle_type_detector(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        print("Right triangle", "\n", f"the area of this Right triangle is:{(b * c)//2 }")
    elif b ** 2 == c ** 2 + a ** 2:
        print("Right triangle", "\n", f"the area of this Right triangle is:{(a * c)//2 }")
    elif c ** 2 == a ** 2 + b ** 2:
        print("Right triangle", "\n", f"the area of this Right triangle is : {(b * a)//2 }")
    elif a == b == c:
        x = "{:.2f}"
        print("equilateral triangle", "\n" f"the area of this Right triangle is : {x.format((sqrt(3)/4)* (a ** 2))}")


