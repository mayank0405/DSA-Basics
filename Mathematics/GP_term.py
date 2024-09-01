def gp_term(first: int, second: int, n: int):
    if n == 0:
        return 0
    d = second//first
    i = 1
    ans = 1
    while i<=n:
        ans *= d
        i +=1
    return ans

if __name__ == '__main__':
    f = int(input('Enter first number: '))
    s = int(input('Enter second number: '))
    pos = int(input('Enter the position: '))
    print(gp_term(f,s,pos))