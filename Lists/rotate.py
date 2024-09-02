def reverse_list(arr: list[int], b: int, e: int):
    while b <= e:
        arr[b], arr[e] = arr[e], arr[b]
        b+=1
        e-=1

def Rotate(arr: list[int], d: int, n: int) -> list[int]:
    if d == 0:
        return arr
    reverse_list(arr, 0, len(arr)-1)
    reverse_list(arr, 0, d)
    reverse_list(arr, d+1, len(arr)-1)
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter array to be rotated: ').split()))
    d = int(input('Enter d: '))
    rotated_array = Rotate(arr, d, len(arr))
    print(rotated_array)