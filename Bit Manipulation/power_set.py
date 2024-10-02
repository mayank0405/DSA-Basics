def power_set(arr):
    n = len(arr)
    subset = []
    subsets = 2**n
    for i in range(subsets):
        l = []
        for j in range(n):
            if (i & 1<<j):
                l.append(arr[j])
        subset.append(l)
    return subset

if __name__ == '__main__':
    ans = power_set([1,2,3])
    print(ans)
    