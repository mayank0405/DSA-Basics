def length_of_string(string: str)-> int:
    length = 0
    for i in string:
        length += 1
    return length


if __name__ == '__main__':
    str = input('Enter the string: ')
    print('Length of a string is:', length_of_string(str))