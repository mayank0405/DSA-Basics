def sum_n_natural_numbers(n: int) -> int:
    return (n*(n-1))/2

if __name__ == '__main__':
    n = int(input('Enter n: '))
    ans = sum_n_natural_numbers(n)
    print(ans)
    