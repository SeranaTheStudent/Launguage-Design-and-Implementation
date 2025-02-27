def evaluate(rpn_expr):
    stack = []

    for token in rpn_expr:
        if isinstance(token, float): # If it's a number, push it to the stack
            stack.append(token)
        

        else: # If an operator, pop last two numbers and apply operation
            if len(stack) < 2:
                raise ValueError("Invalid expression: not enough operands")
            
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                stack.append(left / right)
            elif token == '==':
                stack.append(left == right)
            elif token == '!=':
                stack.append(left != right)
            elif token == '<':
                stack.append(left < right)
            elif token == '>':
                stack.append(left > right)
            elif token == '<=':
                stack.append(left <= right)
            elif token == '>=':
                stack.append(left >= right)
            elif token == 'and':
                stack.append(left and right)
            elif token == 'or':
                stack.append(left or right)
            elif token == '!':
                stack.append(not right)
            elif token == 'true':
                stack.append(True)
            elif token == 'false':
                stack.append(False)

    return stack[0]