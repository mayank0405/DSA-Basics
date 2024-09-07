def bubble_sort(arr: list[int])-> None:
    n = len(arr)
    for i in range(n-1): #number of passes
        is_swapped = False #initially the elements have not been swapped
        for j in range(n-i-1): #number of swaps
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True #now two elements have been swapped
            if not is_swapped:
                break

if __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    print(array)
    bubble_sort(array)
    print(array)