# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

def arrayChange(inputArray):
    res = 0
    last = 0
    
    for i in range(1, len(inputArray)):
        # if diff > 0, it is decreasing
        # if diff = 0, both are same
        # if diff < 0, it is increasing
        diff = (inputArray[i-1] + last) - inputArray[i]
        
        if diff < 0:
            last = 0
        else:
            last = diff + 1
            res += diff + 1
            
    return res