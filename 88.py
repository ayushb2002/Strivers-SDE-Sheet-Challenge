def sorted_insert(stack,p):
    if not stack or stack[-1]<p:
        stack.append(p)
        return

    s = stack.pop()
    sorted_insert(stack,p)
    stack.append(s)

def sortStack(stack):
    if not stack:
        return

    p = stack.pop()
    sortStack(stack)
    sorted_insert(stack,p)