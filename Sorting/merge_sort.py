#Merge sort is a divide and conquer algorithm
#First we keep dividing the arrays and then merge them together

def merge_arrays(arr: list[int], low: int, mid: int, high: int):
    left = arr[low: mid+1]
    right = arr[mid+1: high+1]
    i,j,m,n = 0,0,len(left), len(right)
    k = low #k is initialized to low: starting of the initial array
    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        elif right[j] < left[i]:
            arr[k] = right[j]
            j+=1
        k+=1
    
    while i < m:
        arr[k] = left[i]
        k+=1
        i+=1
    while j < n:
        arr[k] = right[j]
        k+=1
        j+=1

def merge_sort(arr: list[int], l: int, h: int):
    if l < h:
        m = l + (h - l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, h)
        merge_arrays(arr, l, m, h)


arr = [10, 5, 30, 15, 7]
merge_sort(arr, 0, 4)
print(arr)