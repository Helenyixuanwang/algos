from collections import defaultdict
def groupAnagrams( strs):
        groups = defaultdict(list)
        print("groups are like ", groups)
        for s in strs:
            # print("s  ",s)
            key = "".join(sorted(s))
            
            print(key)
            groups[key].append(s)
        
        return groups.values()
        # return groups

strs= ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))