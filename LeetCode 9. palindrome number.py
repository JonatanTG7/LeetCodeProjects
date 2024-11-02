class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_x = list(str(x))
        if len(list_x) == 1:
            return True
        for i in range(len(list_x)):
            if list_x[i] == list_x[len(list_x) - (i+1)] and i <= len(list_x) - (i+1):
                continue
            elif i > len(list_x) - (i+1):
                return True
            elif list_x[i] != list_x[len(list_x) - (i+1)]:
                return False



x = 121
solution = Solution()
result = solution.isPalindrome(x)
print(result)

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.