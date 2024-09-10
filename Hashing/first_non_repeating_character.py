def nonRepeating(string: str, n: int) -> int:
    count_hash = dict()
    for i in range(n):
        if string[i] in count_hash:
            count_hash[string[i]] += 1
        else:
            count_hash[string[i]] = 1
    for key, value in count_hash.items():
        if value == 1:
            return key
    return -1

if __name__ == '__main__':
    x = input('Enter the string: ')
    ans = nonRepeating(x, len(x))
    print(ans)