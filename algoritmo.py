# coding: utf-8
import math


def is_triangle(triangle):
    pass

def calculate_area(triangle):
    pass

if __name__ == '__main__':
    triangle_data = raw_input('Input triangle "a, b, c": ')

    try:
        triangle = tuple([int(l) for l in triangle_data.split(',')])
    except ValueError:
        print "Not a valid input"

    if not is_triangle(triangle):
        print("{} is not a valid triangle".format(triangle))
    else:
        area = calculate_area(triangle)
        print("area for {} is: {}".format(triangle, area))
