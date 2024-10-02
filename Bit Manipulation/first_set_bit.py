def getFirstSetBit(n):
    if n == 0:
        return 0
    if n&1:
        return 1
    pos = 1
    while n:
        n = n >> 1
        pos = pos + 1
        if n&1:
            return pos


if __name__ == '__main__':
    n = int(input('Enter n: '))
    ans = getFirstSetBit(n)
    print(ans)