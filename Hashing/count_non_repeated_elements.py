def count_non_repeated_elements(arr: list[int], n: int)-> int:
    count_nums = {}
    for num in arr:
        if num in count_nums:
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    count = 0
    for key, value in count_nums.items():
        if value == 1:
            count += 1
    return count

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    ans = count_non_repeated_elements(arr, len(arr))
    print(f'Number of non repeating elements is {ans}')