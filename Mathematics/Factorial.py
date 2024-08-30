def factorial(n: int) -> int:
    fac = 1
    if n < 0:
        print('Invalid Number')
        return -1
    if n == 0:
        return 1
    i = n
    while i>0:
        fac = fac * i
        i -= 1
    return fac

if __name__ == '__main__':
    n = int(input('Enter number: '))
    print(f'Factorial of a number: {factorial(n)}')
    