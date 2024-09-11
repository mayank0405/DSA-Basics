def reverse_string(str)-> str:
    rev = ''
    i = len(str)-1
    while i>=0:
        rev += str[i]
        i-=1
    return rev

if __name__ == '__main__':
    string = input('Enter the string: ')
    print('Reverse of a string: ', reverse_string(string))