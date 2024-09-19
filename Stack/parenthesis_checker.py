def checker(s):
    stack = []
    for x in s:
        if x in ('(', '[', '{'):
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1], x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

def isMatching(a,b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b =='}'):
        return True
    else:
        return False


str1 = '[({})]'
str2 = '()'
str3 = '([]'
str4 = ')]}]'
print(f'For {str1} {checker(str1)}')
print(f'For {str2} {checker(str2)}')
print(f'For {str3} {checker(str3)}')
print(f'For {str4} {checker(str4)}')