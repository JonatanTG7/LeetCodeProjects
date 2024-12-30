def lengthOfLastWord(s:str) -> int:
    indexL = -1
    indexR = -1
    count = 0
    for i in range(len(s)-1,-1,-1):

        if indexR == -1 and s[i-1] != " " and s[i] == " ":
            indexR = i-1
        elif indexR == -1 and s[-1] != " ":
            indexR = i

        if indexL == -1 and s[i] != " " and s[i-1] == " ":
            indexL = i
        elif indexL == -1 and 0 == i and s[i] != " ":
            indexL = i


        if indexL != -1 and indexR != -1:
            count = indexR - indexL + 1
            return count

    return count 

s = "     "
result = lengthOfLastWord(s)
print(result)