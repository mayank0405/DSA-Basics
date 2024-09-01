def absolute_value(a: int)-> int:
    if a == 0:
        return 0
    elif a < 0:
        return a*-1
    else:
        return a

if __name__ == '__main__':
    n = int(input('Enter number: '))
    print(absolute_value(n))