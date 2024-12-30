def isIsomorphic(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    dict_s_t = {}
    dict_t_s = {}
    index_t = 0

    for char in s:
        if char in dict_s_t:
            if dict_s_t[char] != t[index_t]:
                return False
        elif t[index_t] in dict_t_s:
            if  dict_t_s[t[index_t]] != char:
                return False
        else:
            dict_s_t[char] = t[index_t]
            dict_t_s[t[index_t]] = char

        index_t += 1
    
    return True


s = "aaqwseddeswaq"
t = "llokijuujikll"
result = isIsomorphic(s, t)
print(result)