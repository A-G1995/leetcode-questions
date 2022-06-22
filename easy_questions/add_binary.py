def addBinary(a: str, b: str) -> str:
    sum = bin(int(a, 2) + int(b, 2))
    print(sum[2:])

addBinary("1010", "1011")