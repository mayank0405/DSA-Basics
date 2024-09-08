def merge_arrays(nums: list[int], low: int, mid: int, high: int)-> None:
    left = nums[low: mid+1]
    right = nums[mid+1: high+1]
    i,j,m,n = 0,0,len(left), len(right)
    k = low
    while i < m and j < n:
        if left[i] == right[j]:
            nums[k] = left[i]
            i+=1
            j+=1
        elif left[i] < right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    while i < m:
        nums[k] = left[i]
        k+=1
        i+=1
    while j < n:
        nums[k] = right[j]
        k+=1
        j+=1
    return nums

if __name__ == '__main__':
    nums = [10, 15, 20, 40, 8, 11, 55]
    merge_arrays(nums, 0, 3, 6)
    print(nums)