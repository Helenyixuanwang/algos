# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import defaultdict

def ransom(ransom, magazine):
    dict = defaultdict(int)
    for c in magazine:
        dict[c] += 1
    print(dict)
    times = len(ransom)

    for letter in ransom:
        if letter in dict:
            print("letter is ", letter)
            dict[letter] -= 1
            
            if dict[letter] == -1:
                return False
            times -= 1
            print("times is ", times)
    if times == 0:
        return True
    else:
        return False
    
ransomNote = "aa"
magazine = "aab"

# ransomNote = "aa"
# magazine = "ab"

print(ransom(ransomNote, magazine))
