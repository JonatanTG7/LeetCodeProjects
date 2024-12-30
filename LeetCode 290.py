def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(s) != len(pattern):
        return False
    
    dict_s_pattern = {}
    dict_pattern_s = {}
    index_t = 0

    for word in s:
        if word in dict_s_pattern:
            if dict_s_pattern[word] != pattern[index_t]:
                return False
        elif pattern[index_t] in dict_pattern_s:
            if  dict_pattern_s[pattern[index_t]] != word:
                return False
        else:
            dict_s_pattern[word] = pattern[index_t]
            dict_pattern_s[pattern[index_t]] = word

        index_t += 1

    return True

pattern = "aaaa"
s = "dog cat cat fog"
result = wordPattern(pattern, s)
print(result)