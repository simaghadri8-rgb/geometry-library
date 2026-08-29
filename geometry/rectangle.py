import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def rectangle_diagonal(length, width):
    return math.sqrt(length ** 2 + width ** 2)