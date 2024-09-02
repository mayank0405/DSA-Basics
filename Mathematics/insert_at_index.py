def insert_index(l: list[int], sizeOfArray: int, index: int, element: int):
    if index > sizeOfArray:
        return
    if index == sizeOfArray-1:
        l[sizeOfArray-1] = element
    i = sizeOfArray - 1
    l[i] = -1
    while i>=0:
        temp = l[i]
        l[i] = l[i-1]
        l[i-1] = element
    print(f'{element} inserted at {index} position: ', l)

if __name__ == '__name__':
    arr = list(map(int, input('Enter array: ').split()))
    index = int(input('Enter index: '))
    element = int(input('Enter element: '))
    s = len(arr)
    insert_index(arr, s, index, element)

    