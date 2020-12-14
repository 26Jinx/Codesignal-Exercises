# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def sortByHeight(a):
    
    # let's first create a dictionary of all of the indexes for trees and remove -1s from the list
    trees = []
    people = []
    
    for i, n in enumerate(a):
        if n == -1:
            trees.append(i)
        else:
            people.append(a[i])

    # sort list without -1s
    people.sort()
    
    # reconstruct list by order
    for idx in trees:
        people.insert(idx, -1)
        
    return people 