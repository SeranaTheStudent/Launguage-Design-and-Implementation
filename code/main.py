from valhalla import Lexer
from parsed import parse
from Interp import evaluate

f = open("./testscript.txt", "r")
for i in f:
    lexer = Lexer(i)
    tokens = lexer.tokenize()

    rpn_expr = parse(tokens)
    print("RPN Output", rpn_expr)
    result = evaluate(rpn_expr)

    print(result)