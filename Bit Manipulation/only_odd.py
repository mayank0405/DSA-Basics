def only_one_odd(l):
    res = 0
    for i in l:
        res =res ^ i
    return res

arr = [10,30,30,10,30,30,20]
print(only_one_odd(arr))