def isAnagram(a: str,b: str)->bool:
    if len(a) != len(b):
        return False
    hash_a, hash_b = dict(), dict()
    for i in a:
        if i in hash_a:
            hash_a[i] += 1
        else:
            hash_a[i] = 1
    for j in b:
        if j in hash_b:
            hash_b[j] += 1
        else:
            hash_b[j] = 1
    return hash_a == hash_b

if __name__ == '__main__':
    str1 = input('Enter string 1: ')
    str2 = input('Enter string 2: ')
    print('Is Anagram or not?: ', isAnagram(str1, str2))