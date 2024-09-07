#here we SELECT the minimum element
def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    print(array)
    selection_sort(array)
    print(array)