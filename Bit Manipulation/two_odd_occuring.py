def two_odd(l):
    xor = 0
    for i in l:
        xor = xor ^ i
    res1,res2 = 0,0
    xor = xor & ~(xor - 1) #rightmost set bit
    for i in l:
        if xor & i == 1: #for odd group
            res1 = res1 ^ i
        else: #for even group
            res2 = res2 ^ i

    print(res1, res2)

l = [3,4,3,4,5,4,4,6,7,7]
two_odd(l)

