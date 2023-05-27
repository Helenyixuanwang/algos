# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
#method 1
def pangram(str):
    seen = set()
    for i in range(len(str)):
        if str[i] not in seen:
            seen.add(str[i])

    if len(seen)==26:
        return True
    else:
        return False
    
# str1 = "thequickbrownfoxjumpsoverthelazydog"
str1= "leetcode"
print(pangram(str1))

#method 2
def pangram2(str):
    letters = set(str)
    seen = set()
    for c in letters:
        if c not in seen:
            seen.add(c)
    if len(seen) == 26:
        return True
    else:
        return False
    
str1 = "thequickbrownfoxjumpsoverthelazydog"
# str1= "leetcode"
print(pangram2(str1))

#method 3, even faster, copy from sample
def checkIfPangram(sentence):
        # Add every letter of 'sentence' to hash set 'seen'.
        seen = set(sentence)
        
        # If the size of 'seen' is 26, then 'sentence' is a pangram.
        return len(seen) == 26