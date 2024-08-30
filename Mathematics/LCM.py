def lcm_1(a: int, b: int) -> int:
    c = max(a,b)
    while True:
        if (c%a == 0) and (c%b == 0):
            return c
        c += 1

def lcm_2(a: int, b: int) -> int:
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        return gcd(b, a%b)
    hcf = gcd(a,b)
    return int((a*b)/hcf)

if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(f'\nLCM of {a} and {b} is {lcm_1(a,b)}')
    print(f'\nLCM of {a} and {b} is {lcm_2(a,b)}')