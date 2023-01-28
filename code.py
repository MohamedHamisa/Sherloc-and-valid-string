from collections import Counter

def isValid(s):
    # Write your code here
    my_dict = Counter(s)
    
    freq = Counter(my_dict.values())
    
    if len(freq) > 2:
        return "NO"
    elif len(freq) == 1:
        return "YES"
    else:
        if freq.get(1, 0)==1:
            return "YES"
        elif abs(max(freq)-min(freq))==1 and (min(freq.values())==1):
            return "YES"
        else:
            return "NO"



