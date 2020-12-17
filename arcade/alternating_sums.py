# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

def alternatingSums(a):
    team1 = []
    team2 = []
    
    for i, n in enumerate(a):
        if (i % 2 == 0):
            team1.append(n) 
        else:
            team2.append(n) 
            
    ans = [sum(team1), sum(team2)]
    
    return ans