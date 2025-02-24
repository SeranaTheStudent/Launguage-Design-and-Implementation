def exluate(rpn_expr):
    stack = []

    for token in rpn_expr:
        if isinstance(token, float): # If it's a number, push it to the stack
            stack.append(token)
        else: # If an operator, pop last two numbers and apply operation
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(left / right)

    return stack[0]