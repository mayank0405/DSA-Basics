def panagramCheck(str: str)->bool:
    str = str.lower()
    seen = set()
    for x in str:
        if 'a' <= x <= 'z':
            seen.add(x)
    return len(seen) == 26

if __name__ == '__main__':
    string = input('Enter the string: ')
    ans = panagramCheck(string)
    print(f'Is panagram or not: {ans}')