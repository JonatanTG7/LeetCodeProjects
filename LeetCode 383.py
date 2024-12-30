from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    maga_hash = {}
    maga_hash = Counter(magazine)

    for char in ransomNote:
        maga_hash[char] -=1
        if maga_hash[char] == -1:
            return False
    return True

ransomNote = "a"
magazine = ""
result =  canConstruct(ransomNote , magazine)
print(result)


#check with a if - else
# for char in ransomNote:
#     if char in maga_hash:
#         maga_hash[char] -=1
#         if maga_hash[char] == -1:
#             return False
#     else:
#         return False
# return True