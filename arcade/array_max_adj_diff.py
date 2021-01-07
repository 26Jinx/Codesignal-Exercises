# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE

def arrayMaximalAdjacentDifference(inputArray):
    max_d = 0
    
    for i in range(len(inputArray)-1):
        abs_d = inputArray[i] - inputArray[i+1] if inputArray[i] > inputArray[i+1] else inputArray[i+1] - inputArray[i]
        
        if abs_d > max_d:
            max_d = abs_d
    
    return max_d