from Prime_check import prime_check
def check_divisors(n: int)-> int:
    count = 0
    i = 1
    while i*i <= n:
        if prime_check(i):
            if n%i == 0:
                count +=1
        i+=1
    return count

if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(check_divisors(num))