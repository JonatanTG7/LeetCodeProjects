def isSubsequence(s: str , t: str) -> bool:
    if len(s) == 0: 
        return True
    
    if len(s) > len(t):
        return False
    
    index_s = 0

    for char in t:
        if s[index_s] == char:
            index_s += 1
        
        if index_s == len(s):
            return True
        
    return False

s = "ababb"
t = "avdsbabacccdsbd"
result = isSubsequence(s,t)
print(result)