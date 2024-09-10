def printElements(nums: list[int], n: int)-> None:
    count_dic = dict()
    for num in nums:
        if num in count_dic:
            count_dic[num] += 1
        else:
            count_dic[num] = 1
    for key, value in count_dic.items():
        if value == 1:
            print(key, end = ' ')
    

if __name__ == '__main__':
    arr = list(map(int, input('Enter the array: ').split()))
    printElements(arr, len(arr))