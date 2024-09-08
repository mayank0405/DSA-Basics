def merge(arr: list[int], low: int, mid: int, high: int) -> None:
    left = arr[low: mid+1]
    right = arr[mid+1: high+1]
    i,j,m,n = 0,0, len(left), len(right)
    k = low
    count_inv = 0
    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            count_inv = m - i
            arr[k] = right[j]
            j+=1
        k+=1
    while i < m:
        arr[k] = left[i]
        k+=1
        i+=1
    while j < n:
        arr[k] = right[j]
        k+=1
        j+=1
    return count_inv

def count_inversions(arr: list[int], n: int)-> int:
    ans = 0
    def merge_sort(arr, l, h):
        nonlocal ans
        if l < h:
            m = l + (h - l)//2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, h)
            ans += merge(arr, l, m, h)
    merge_sort(arr, 0, n-1)
    return ans

def count_inversions_brute_force(arr: list[int], n: int)-> int:
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                ans += 1
    return ans

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split(' ')))
    a_len = len(array)
    ans = count_inversions(array, a_len)
    print('Number of inversions in the array: ', ans)
    ans2 = count_inversions_brute_force(array, a_len)
    print('Number of conversions through brute force: ', ans2)