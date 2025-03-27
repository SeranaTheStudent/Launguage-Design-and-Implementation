from codetypes import StringLiteral

def evaluate(rpn_expr):
    stack = []

    for token in rpn_expr:
        if isinstance(token, (float, bool)): # If it's a number, push it to the stack
            stack.append(token)
        elif isinstance(token, StringLiteral):
            stack.append(token.value)
        else:
            if token == '!':
                if len(stack) < 1:
                    raise ValueError("Invalid expression: not enough operands")
                operand = stack.pop()
                stack.append(not operand)
            else:
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: not enough operands. Expected 2 but got {len(stack)}")
                    
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

    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands")

    return stack[0]