def sum_digits(n: int) -> int:
    if n <= 0:
        return 0
    return sum_digits(n//10) + n%10

if __name__ == '__main__':
    num = int(input('Enter number: '))
    ans = sum_digits(num)
    print(ans)