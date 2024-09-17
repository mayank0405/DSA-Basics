def hoare_partition(arr: list[int], low: int, high: int)-> int:
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i+=1
        j-=1
        while arr[j] > pivot:
            j-=1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr: list[int], low: int, high: int)-> None:
    while low < high:
        pivot = hoare_partition(arr, low, high)
        quickSort(arr, low, pivot)
        low = pivot + 1

if __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    quickSort(array, 0, len(array)-1)
    print(array)