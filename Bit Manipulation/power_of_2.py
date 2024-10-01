def isPower_2_method_1(n):
    while n>1:
        if n%2 != 0:
            return False
        n = n//2
    return True

def isPower_2_method_2(n):
    #check for odd
    if n&1 == 1:
        return False
    if n&(n-1) == 1: #The rightmost set bit of n becomes 0 and everting after it also 
        #becomes zero because of AND opertion so the whole number becomes zero.
        return False
    else:
        return True

n = int(input('Enter n: '))
print(isPower_2_method_1(n))