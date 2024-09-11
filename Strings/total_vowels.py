def total_vowels(str)->int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = 0
    for i in str:
        if i in vowels:
            ans += 1
    return ans

if __name__ == '__main__':
    string = input('Enter the string: ')
    print('The total number of vowels: ', total_vowels(string))