def find_peak(nums: list[int]) -> int:
    n = len(nums) - 1
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        if nums[mid] < nums[mid+1]:
            low = mid + 1
        if nums[mid-1] > nums[mid]:
            high = mid - 1
    return -1

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    ans = find_peak(arr)
    print(ans)
