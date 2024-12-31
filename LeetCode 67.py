def addBinary(a: str, b:str) -> str:
    int_a = int(a,2)
    int_b = int(b,2)

    sum = int_a + int_b

    bit_sum = bin(sum)[2:]

    return bit_sum

a = "1111"
b = "1111"

result =addBinary(a,b)
print(result)