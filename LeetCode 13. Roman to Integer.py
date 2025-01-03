class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        roman_int = 0
        index=0
        while index < len(s):
            if s[index] == "I":
                if index + 1 < len(s) and s[index+1] == "V":
                    roman_int += 4
                    index+=2
                elif index + 1 < len(s) and s[index+1] == "X":
                    roman_int += 9
                    index += 2
                else:
                    roman_int += roman_dict[s[index]]
                    index += 1
            elif s[index] == "X":
                if index + 1 < len(s) and s[index+1] == "L":
                    roman_int += 40
                    index += 2
                elif index + 1 < len(s) and s[index+1] == "C":
                    roman_int += 90
                    index += 2
                else:
                    roman_int += roman_dict[s[index]]
                    index +=1
            elif s[index] == "C":
                if index + 1 < len(s) and s[index+1] == "D":
                    roman_int += 400
                    index += 2
                elif index + 1 < len(s) and s[index+1] == "M":
                    roman_int += 900
                    index += 2
                else:
                    roman_int += roman_dict[s[index]]
                    index += 1
            else:
                roman_int += roman_dict[s[index]]
                index += 1
        return roman_int

x = "III"
solution = Solution()
result = solution.romanToInt(x)
print(result)

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.