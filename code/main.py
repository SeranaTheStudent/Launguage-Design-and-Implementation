from scanner import scanner
from parsed import parser
from Interp import Interpreter

f = open("./testscript.txt", "r")
for i in f:
    lexer = scanner(i)
    tokens = lexer.scan_tokens()

    rpn_expr = parser(tokens)
    stmts = rpn_expr.parse()
    interpreter = Interpreter()
    for stmt in stmts:
        interpreter.evaluate(stmt)