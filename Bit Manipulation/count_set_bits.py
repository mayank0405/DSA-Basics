def count_bits_1(n):
    count = 0
    while n:
        if n&1 == 1:
            count += 1
        n = n>>1
    return count

def count_bits_2(n):
    count = 0
    while n:
        n = n&n-1
        count +=1
    return count

n = int(input('Enter n: '))
print(count_bits_1(n))
print(count_bits_2(n))