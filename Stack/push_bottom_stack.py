def push(stack,x):
    if not stack:
        stack.append(x)
        return 
    top = stack.pop()
    push(stack,x)
    stack.append(top)



