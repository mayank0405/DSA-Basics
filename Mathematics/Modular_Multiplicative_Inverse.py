def modInverse(a: int, m: int)-> int:
    for i in range(1,m):
        if (a*i)%m == 1:
            return i
    return 1


if __name__ == '__main__':
    a = int(input('Enter a: '))
    m = int(input('Enter m: '))
    print(modInverse(a,m))