import math

def area_of_tri(x, y, z):
    s = 0.5 * (x + y + z)
    area = math.sqrt(s * (s - x) * (s - y) * (s - z)) #herons formula to find the area of a triangle
    return area

area_of_tri(x, y, z)