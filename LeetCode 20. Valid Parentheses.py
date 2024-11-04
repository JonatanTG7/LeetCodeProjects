class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if  len(stack) >=1 and stack.pop() == "(" :
                    continue
                else:
                    stack.append(")")
            elif s[i] == ']':
                if len(stack) >=1 and stack.pop() == "[":
                    continue
                else:
                    stack.append("]")
            elif s[i] == '}':
                if len(stack) >=1 and stack.pop() == "{":
                    continue
                else:
                    stack.append("}")
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                stack.append(s[i])

        return len(stack) == 0

s="))"

solution = Solution()
result = solution.isValid(s)
print(result)

# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true


