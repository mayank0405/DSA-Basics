def count_vowels(str: str)-> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    x = set(str)
    v = 0
    for i in x:
        if i in vowels:
            v += 1
    return v


if __name__ == '__main__':
    string = input('Enter the string: ')
    print('Number of vowels: ', count_vowels(string))