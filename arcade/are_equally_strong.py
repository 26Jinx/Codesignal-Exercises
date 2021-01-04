# https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStr = yourLeft if yourLeft >= yourRight else yourRight
    frndStr = friendsLeft if friendsLeft >= friendsRight else friendsRight
    
    yourWeak = yourLeft if yourLeft < yourRight else yourRight
    frndWeak = friendsLeft if friendsLeft < friendsRight else friendsRight
    
    if yourStr == frndStr and yourWeak == frndWeak:
        return True
    else:
        return False