from valhalla import TOKEN_TYPES, tokenize
from collections import deque

OPERATOR_PRECEDENCE = {
    '+': 1, '-': 1,
    '*':2, '/':2,
}

def parse(tokens):
    output_queue = []
    operator_stack = deque()

    for token_type, value in tokens:
        if token_type == "NUMBER":
            output_queue.append(value)
        elif token_type == "OPERATOR":
            while (operator_stack and operator_stack[-1] in OPERATOR_PRECEDENCE and OPERATOR_PRECEDENCE[operator_stack[-1]] >= OPERATOR_PRECEDENCE[value]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(value)
        elif token_type == "LPAREN":
            operator_stack.append(value)
        elif token_type == "RPAREN":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

