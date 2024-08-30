def count_digits(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    if n < 0:
        n = abs(n)
    while n>0:
        count += 1
        n = n // 10
    return count

if __name__ == '__main__':
    n = int(input('Enter n: '))
    print('Number of digits: ', count_digits(n))
