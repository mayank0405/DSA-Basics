def k_th_set(n,k):
    n = n >> (k-1)
    return n&1

n = int(input('Enter n: '))
k = int(input('Enter k: '))
print(k_th_set(n,k))