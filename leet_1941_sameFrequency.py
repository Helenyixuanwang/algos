# Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

# Given a string s, determine if all characters have the same frequency.

# For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
# this is a review, the idea is the same as original one from crash course
from collections import defaultdict
def same_occu(str):
    dict = defaultdict(int)

    for c in str:
        dict[c] += 1
    print(dict.values())
    print(set(dict.values()))
    return len(set(dict.values()))==1

str = "abacbc"
# str = "aaabb"
print(same_occu(str))
