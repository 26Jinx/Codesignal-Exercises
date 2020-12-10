# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def shapeArea(n):
    area = 1
    
    for x in range(n):
        area += x*4
        
    return area