# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
    # first sort list
    statues.sort()
    
    # check to see if every integer in the range of smallest to the largest statues exist
    # count every time that it does not
    count = 0
    
    for i in range(statues[0], statues[-1]):        
        if i in statues:
            continue
        else: 
            count += 1
    
    return count