def count_digits(n: int)-> int:
    if n == 0:
        return 0
    return count_digits(n//10) + 1

if __name__ == '__main__':
    num = int(input('Enter num: '))
    ans = count_digits(num)
    print(ans)