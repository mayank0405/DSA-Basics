def floor_value(arr: list[int], n: int, x: int) -> int:
    res = -1
    low, high = 0, n-1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            res = max(res, arr[mid])
            low = mid + 1
    return res

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    x = int(input('Enter the value: '))
    n = len(array)
    ans = floor_value(array, n, x)
    print(ans)

