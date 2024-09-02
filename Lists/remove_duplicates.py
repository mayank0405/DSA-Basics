def remove_duplicates(arr: list[int]) -> int:
    res = 1
    for i in range(1, len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res +=1
    print(arr)
    return res

arr = [10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30]
ans = remove_duplicates(arr)
print(ans)