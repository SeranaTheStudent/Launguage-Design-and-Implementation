from valhalla import Lexer
from parsed import parse
from Interp import evaluate

expression = ["1 - 2", "2.5 + 2.5 - 1.25", "(10 * 2) / 6", "8.5 / (2 * 9) - -3", "true == false", "true != flase"]
for i in expression:
    lexer = Lexer(i)
    tokens = lexer.tokenize()

    rpn_expr = parse(tokens)
    print("RPN Output", rpn_expr)
    result = evaluate(rpn_expr)

    print(result)