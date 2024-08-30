from Prime_check import prime_check
def factorization(n: int) -> None:
    for i in range(2, n+1):
        if prime_check(i):
            x = i
            # we check how many times n is divisible by i
            while n%x == 0:
                print(i, end = ' ')
                x = x * i

if __name__ == '__main__':
    num = int(input('Enter n: '))
    factorization(num)