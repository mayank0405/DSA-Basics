def count(s: str)-> int:
    n = len(s)
    i = 0
    count = 0
    while i < n:
        j = i
        while j < n and s[j] == ' ':
            if j == n-1:
                return count
            j+=1
        z = j
        while z < n and s[z] != ' ':
            z+=1
        count += 1
        i = z
        j = z
    return count

if __name__ == '__main__':
    string = input('Enter string: ')
    ans = count(string)
    print(ans)