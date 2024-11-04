class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return "\"\""

        min_length = min(strs , key=len)

        for i in range(len(min_length)):
            print(i)
            for string in strs:
                print(string)
                print(f"{min_length[i]}  vs  {string[i]}")
                if min_length[i] != string[i]:
                    return min_length[:i]
        return min_length


strs = ["flower","flow","flight"]

solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)
