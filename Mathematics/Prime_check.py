def prime_check(n: int)-> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(prime_check(num))