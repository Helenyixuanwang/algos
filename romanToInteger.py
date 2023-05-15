# Python3 program to Validate the Roman numeral
 
# Function to Validate the Roman numeral
def ValidationOfRomanNumerals(string):
    # Importing regular expression
    import re
    # Searching the input string in expression and
    # returning the boolean value
    print(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string)))
 
# Driver code
 
# Given string
# string="XI"
# Function call
# ValidationOfRomanNumerals(string)

#### transfer roman numeral to interger
def romanToInt(str):
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(str) - 1):
            if roman_dict[str[i]] < roman_dict[str[i+1]]:
                total -= roman_dict[str[i]]
            else:
                total += roman_dict[str[i]]
        return total + roman_dict[str[-1]]


str1 = "XLV"
ValidationOfRomanNumerals(str1)
print(romanToInt(str1))
# print(romanToInt(""))