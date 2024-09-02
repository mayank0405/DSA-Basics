def insertAtIndex(arr: list[int], sizeOfArray: int, index: int, element: int) -> list[int]:
    if index >= sizeOfArray:
        return arr
    arr.append(0)
    for i in range(sizeOfArray-1, index, -1):
        arr[i] = arr[i-1]
    arr[index] = element
    return arr

def insert_method_2(arr: list[int], index: int, element: int)-> list[int]:
    return arr.insert(index, element)    

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    index = int(input('Enter index: '))
    element = int(input('Enter element: '))
    size = len(arr) + 1
    ans = insertAtIndex(arr, size, index, element)
    print(ans)
    print(insert_method_2(arr, index, element))