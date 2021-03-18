def maximum(x, y, z):
    if ((x > y) and (x > z)):
        maxi = x
    elif ((y > x) and (y > z)):
        maxi = y
    elif((z > x) and (z > y)):
        maxi = z
        
    return maxi

maximum(x, y, z)