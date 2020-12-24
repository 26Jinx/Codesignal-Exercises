# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def palindromeRearranging(inputString):
    ltrs_dict = {}
    
    for ltr in list(inputString):
        if ltr in ltrs_dict:
            ltrs_dict[ltr] += 1
        else:
            ltrs_dict[ltr] = 1
            
    print(ltrs_dict)
    
    odd_count = 0
    
    for v in ltrs_dict.values():
        if odd_count < 2:
            # if v is odd
            if v % 2:
                odd_count += 1
        else:
            return False
        
    return odd_count < 2