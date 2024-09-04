def print_1_n(n: int):
    if n == 0:
        return
    print_1_n(n-1)
    print(n, end =' ')

if __name__ == '__main__':
    n = int(input('Enter n: '))
    print_1_n(n)