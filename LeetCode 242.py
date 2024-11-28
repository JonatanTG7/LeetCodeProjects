class Solution:
    def isAnagram(self, s: str, t: str):

        if len(s) != len(t):
            return False

        word_dict = {}
        for i in range(len(s)):
            if s[i] in word_dict:
                word_dict[s[i]] += 1
            else:
                word_dict[s[i]] = 1

        for i in range(len(t)):
            if t[i] in word_dict:
                word_dict[t[i]] -= 1

        for key in word_dict:
            if word_dict[key] != 0:
                return False
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) #True
print(solution.isAnagram("rat", "car")) #False