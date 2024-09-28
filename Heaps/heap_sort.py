def heapify(arr, n, i):
    #max heap
    #0-based indexing
    parent = i
    left_child = 2*i + 1
    right_child = 2*i + 2
    if left_child < n and arr[left_child] > arr[parent]:
        parent = left_child
    if right_child < n and arr[right_child] > arr[parent]:
        parent = right_child
    if parent != i:
        #if parent is changed then swap the values and heapify
        arr[parent], arr[i] = arr[i], arr[parent]
        heapify(arr, n, parent)
def heap_sort(arr, n):
    #build heap using heapify O(n)
    for i in range((n-1)//2, -1, -1):
        heapify(arr, n, i)
    #remove the elements one by one and heapify them
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
