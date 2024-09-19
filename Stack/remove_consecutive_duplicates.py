def removeDuplicates(s):
    stack = []
    for i in range(len(s)):
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            continue
    return ''.join(stack)


ch = 'aaaaaabbbbcddddeeeefghijjjj'
ans = removeDuplicates(ch)
print(ans)
