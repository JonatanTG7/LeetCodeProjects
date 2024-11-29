from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            anagram_sig = "".join(sorted(str))
            anagrams[anagram_sig].append(str)
        
        return list(anagrams.values())
    
solution = Solution()
print(solution.groupAnagrams(["eat","tea","ttan","ate","nat","bat","bta","tan"]))