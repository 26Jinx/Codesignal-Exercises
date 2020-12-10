# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

def almostIncreasingSequence(sequence): 
    
    # function to check for strictly increasing sequence
    # returns true if is increasing, the index if not
    def is_increasing(seq):
        for i in range(len(seq)-1):
            if seq[i] < seq[i+1]:
                continue
            else:
                return i
        
        return True
    
    # creates new sequence withouth the out of order element    
    def new_seq_without(idx, seq):
        if idx == 0:
            return seq[1:]
        elif idx == len(seq)-1:
            return seq[:idx]
        else:
            return seq[:idx] + seq[idx+1:]
     
    # initial test to check for increasing sequence   
    result = is_increasing(sequence)

    # if the initial test is false, then check two new sequences: 
    # one that removes the index returned from is_increasing, and 
    # another that removes the index to the right of one returned
    # if either sequence is increasing, return true, otherwise false
    if result is True:
        return result
    else:
        return (is_increasing(new_seq_without(result, sequence)) is True) or (is_increasing(new_seq_without(result+1, sequence)) is True)