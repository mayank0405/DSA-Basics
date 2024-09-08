def merge(nums: list[int], nums2: list[int])-> list[int]:
    m,n = len(nums), len(nums2)
    i,j = 0,0
    l = []
    while i < m and j < n:
        if nums[i] == nums[j]:
            l.append(nums[i])
            i+=1
            j+=1
        elif nums[i] < nums2[j]:
            l.append(nums[i])
            i+=1
        else:
            l.append(nums2[j])
            j+=1
    while i < m:
        l.append(nums[i])
        i+=1
    while j < n:
        l.append(nums2[j])
        j+=1
    return l

if __name__ == '__main__':
    arr1 = list(map(int, input('Enter array: ').split()))
    arr2 = list(map(int, input('Enter array: ').split()))
    ans = merge(arr1, arr2)
    print(ans)