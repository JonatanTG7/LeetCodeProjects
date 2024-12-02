class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for index in range(len(s)):
            if s[index] == "(":
                stack.append("(")
            elif s[index] == "[":
                stack.append("[")
            elif s[index] == "{":
                stack.append("{")
            elif len(stack) == 0:
                return False
            else:
                bracket = stack.pop()
                if bracket_dict[bracket] != s[index]:
                    return False
        if len(stack) == 0:
            return True
        return False
            
solution = Solution()
answer = solution.isValid("{{{()()()()}}}")
print(answer)