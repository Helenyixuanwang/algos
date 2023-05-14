def reverseString( s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while(i < j):
              s[i] , s[len(s)-1-i] =  s[len(s)-1-i], s[i]
              i += 1
              j -= 1
        return s

print(reverseString([1,3,6,7,9,10]))