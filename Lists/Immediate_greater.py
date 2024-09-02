def immediate_greater(arr: list[int], x: int) -> int:
    closest = -1
    for i in range(len(arr)):
        if x < arr[i]:
            if closest == -1 or closest < arr[i]:
                closest = arr[i]
    return closest



if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    x = int(input('Enter x: '))
    ans = immediate_greater(arr, x)
    print(ans)