# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def allLongestStrings(inputArray):
    longest = 0
    longest_strings = []
    
    for str in inputArray:
        if len(str) > longest:
            longest = len(str)
            # '*= 0' clears the list
            longest_strings *= 0
            longest_strings.append(str)
        elif len(str) == longest:
            longest_strings.append(str)
        else:
            continue        
    
    return longest_strings   