def pallindrome_check_1(n: int) -> bool:
    st = str(n)
    return st == st[::-1]

def pallindrome_check_2(n: int)-> bool:
    reversed_number = 0
    n_copy = n
    if n_copy < 0:
        n_copy = abs(n)
    while n_copy>0:
        rem = n_copy%10
        reversed_number = (reversed_number * 10) + rem
        n_copy = n_copy // 10
    return n == reversed_number

if __name__ == '__main__':
    num = int(input('Enter the number: '))
    print(pallindrome_check_1(num))
    print(pallindrome_check_2(num))
    