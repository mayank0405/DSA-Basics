def posOfRightMostDiffBit(m,n):
    if n == 0 or m == 0:
        return 0
    pos = 1
    while m or n:
        if (m&1) ^ (n&1) == 1:
            return pos
        m = m>>1
        n = n>>1
        pos = pos + 1
    return -1

if __name__ == '__main__':
    m = int(input('Enter m: '))
    n = int(input('Enter n: '))
    ans = posOfRightMostDiffBit(m,n)
    print(ans)