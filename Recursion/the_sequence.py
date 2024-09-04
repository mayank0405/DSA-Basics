def theSequence(n: int):
    if n == 0:
        return 1
    return n + n*theSequence(n-1)

if __name__ == '__main__':
    n = int(input('Enter n: '))
    ans = theSequence(n)
    print(ans)