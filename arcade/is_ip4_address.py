# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    # convert the inputString to a list of its parts separated by a '.'
    parts = inputString.split('.')
    
    # check that there are four parts
    if len(parts) != 4:
        print('length check')
        return False
    
    # check to see that they are numbers
    if all(parts) and all(s.isnumeric() for s in parts):
        # check to see that there are no numbers with leading zeros
        int_parts = list(map(lambda x: int(x) if x == str(int(x)) else None, parts))
        print(int_parts)
    else:
        print('int check')
        return False
    
    # check that each part is within the acceptable range [0, 255]
    for n in int_parts:
        if n not in range(0, 256):
            print('range check')
            return False
    
    # if it passes all test, return True
    return True