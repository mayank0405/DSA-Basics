def immediate_smaller(arr: list[int], x: int) -> int:
    closest = -1
    for i in range(len(arr)):
        if arr[i] < x:
            if arr[i] == -1 or arr[i] > closest:
                closest = arr[i]
    return closest

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    x = int(input('Enter x: '))
    ans = immediate_smaller(arr, x)
    print(ans)