def binary_sort(arr: list[int])-> None:
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == 0:
            left+=1
        if arr[right] == 1:
            right-=1
    print(arr)

if  __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    binary_sort(array)