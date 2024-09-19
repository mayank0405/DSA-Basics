def reverse(stack):
    if not stack:
        return
    top = stack.pop()
    reverse(stack)
    stack.append(top)