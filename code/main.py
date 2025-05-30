from scanner import scanner
from parsed import parser
from Interp import Interpreter
import sys

if len(sys.argv) == 1:
    print("Please input a valid file path to run.")
    exit(1)

file_path = sys.argv[1]    
f = open(file_path, "r")
for i in f:
    lexer = scanner(i)
    tokens = lexer.scan_tokens()

    rpn_expr = parser(tokens)
    stmts = rpn_expr.parse()
    interpreter = Interpreter()
    for stmt in stmts:
        interpreter.evaluate(stmt)