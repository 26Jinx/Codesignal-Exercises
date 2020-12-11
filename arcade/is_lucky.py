# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def isLucky(n):
    n = str(n)
    ticket_no = [int(l) for l in list(n)]
    print(ticket_no)
    half_i = len(ticket_no) // 2
    first_half = ticket_no[:half_i]
    second_half = ticket_no[half_i:]
    
    if sum(first_half) == sum(second_half):
        return True
    else:
        return False