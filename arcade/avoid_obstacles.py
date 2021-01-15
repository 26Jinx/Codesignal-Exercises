# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

def avoidObstacles(inputArray):
    obs_pos = sorted(inputArray)
    empty_pos = []
    
    for i in range(obs_pos[-1]):
        if i not in obs_pos:
            empty_pos.append(i)
    
    jump = 1
    curr_pos = 0
    while curr_pos <= obs_pos[-1] + 1:
        if curr_pos in empty_pos or curr_pos > obs_pos[-1]:
            curr_pos += jump
            print(curr_pos)
        else:
            jump += 1
            curr_pos = 0
            print(jump)
            
    return jump