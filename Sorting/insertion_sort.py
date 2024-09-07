def insertion_sort(arr: list[int])-> None:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        hole = i
        while hole>0 and arr[hole-1] > temp:
            arr[hole] = arr[hole-1]
            hole = hole - 1
        arr[hole] = temp

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    print(array)
    insertion_sort(array)
    print(array)