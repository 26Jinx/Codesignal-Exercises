# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def areSimilar(a, b):
    count = 0
    i = 0
    diff = set()
    
    while count < 4 and i < len(a):
        if a[i] != b[i]:
            diff.add(a[i])
            diff.add(b[i])
            count += 1
        
        # increment so we don't have an infinite loop
        i += 1
        
    if count == 0:
        return True
    elif count == 2:
        if len(diff) == 2:
            return True
        else:
            return False
    else:
        return False