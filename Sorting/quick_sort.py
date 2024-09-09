def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pivot = pivot(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
def pivot(arr: list[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i+=1
        while i <= j and arr[j] >= pivot:
            j-=1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

if __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    quick_sort(array)
    print(array)