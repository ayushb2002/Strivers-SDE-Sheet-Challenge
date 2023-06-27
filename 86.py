def isValidParenthesis(expression):
    stack = []
    for i in expression:
        if i in ['{', '[', '(']:
            stack.insert(0, i)
        else:
            if i == '}' and len(stack) > 0 and stack[0] == '{':
                stack.pop(0)
            elif i == ')' and len(stack) > 0 and stack[0] == '(':
                stack.pop(0)
            elif i == ']' and len(stack) > 0 and stack[0] == '[':
                stack.pop(0)
            else:
                return False

    if len(stack) > 0:
        return False

    return True