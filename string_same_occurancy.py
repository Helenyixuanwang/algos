# Given a string s, determine if all characters have the same frequency.
#Leet 1941. Check if All Characters Have Equal Number of Occurrences
from collections import defaultdict

def string_occ(str):
    # function calls int() to supply a default count of zero. The increment operation then builds up the count for each letter.
    count = defaultdict(int)
    print(count)
    for c in str:
        count[c] += 1
    print(count)
    print(count.keys())
    print(count.values())
    print(set(count.values()))
    if len(set(count.values())) == 1:
        return True
    else:
        return False
    


str1 = "babab"
print(string_occ(str1))


