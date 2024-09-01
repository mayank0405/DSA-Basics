def convert(c: int) -> int:
    return ((9/5)*c) + 32

if __name__ == '__main__':
    t = int(input('Enter temperature: '))
    print(convert(t))