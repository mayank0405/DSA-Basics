def hcf_1(a: int, b: int) -> int:
    # Ensure a is greater or equal to b for simplicity
    if a < b:
        a, b = b, a
        
    # Start checking from the minimum of a and b
    x = b
    while x > 0:
        if (a % x) == 0 and (b % x) == 0:
            return x
        x -= 1
    return 1

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == '__main__':
    a1 = int(input('Enter first number: '))
    a2 = int(input('Enter second number: '))
    print(f'HCF of {a1} and {a2} is {hcf_1(a1, a2)}')
    print(f'HCF of {a1} and {a2} is {gcd(a1, a2)}')
