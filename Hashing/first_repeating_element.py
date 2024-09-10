def firstRepeat(nums: list[int], n: int)-> int:
    count_dict = dict()
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for key, value in count_dict.items():
        if value > 1:
            return nums.index(key)
    return -1

if __name__ == '__main__':
    arr = list(map(int, input('Enter the array: ').split()))
    ans = firstRepeat(arr, len(arr))
    print(f'Index of first repeating element: {ans}')