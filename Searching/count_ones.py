def count_ones(nums: list[int], n: int) -> int:
    def last_occurence(nums: list[int], n: int)-> int:
        low, high = 0, n-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == 1 and nums[mid+1] == 0:
                return mid
            elif nums[mid+1] == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    last = last_occurence(nums, n)
    if last == -1:
        return 0
    return last - 0 + 1

if __name__ == '__main__':
    binary_array = list(map(int, input('Enter binary array: ').split()))
    array_length = len(binary_array)
    ans = count_ones(binary_array, array_length)
    print('Number of ones in non-decreasing bonary array is: ', ans)