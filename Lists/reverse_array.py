def reverse(arr: list[int]) -> list[int]:
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    return arr

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    reversed_array = reverse(arr)
    print(reversed_array)