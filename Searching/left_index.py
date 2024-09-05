def leftMostindex(arr: list[int], n: int, k: int) -> int:
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high - low)//2
        if (arr[mid] == k and mid == 0) or (arr[mid] == k and arr[mid-1] < k):
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    N = len(arr)
    K = int(input('Enter the number: '))
    ans =  leftMostindex(arr, N, K)
    print(ans)