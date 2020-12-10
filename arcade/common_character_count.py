# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32/

def commonCharacterCount(s1, s2):
    total = 0
    common_letters = set(s1) & set(s2)
    
    def make_dict(lst, ltrs_needed):
        new_dict = {}
        
        for elem in lst:
            if elem in new_dict:
                new_dict[elem] += 1
            elif elem in ltrs_needed:
                new_dict[elem] = 1
            else:
                continue
                
        return new_dict
    
    s1_dict = make_dict(s1, common_letters)
    #print(s1_dict)
    s2_dict = make_dict(s2, common_letters)
    #print(s2_dict)

    for ltr, count in s1_dict.items():
        total += count if count < s2_dict[ltr] else s2_dict[ltr]
            
            
    return total