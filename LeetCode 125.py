def isPalindrom(s: str) ->bool:
    new_s = ""
    list_s = []
    for char in s:
        if char.isalpha():
            list_s.append(char.lower())
        if char.isnumeric():
            list_s.append(char)
    new_s =''.join(list_s)

    return new_s == new_s[::-1]

answer= isPalindrom("0P")
print(answer)