from collections import deque
from tokens import TOKENTYPES as tt
from codetypes import StringLiteral

def ParseError(Exception):
    def __init__(self,):

class Parser:
    """
    program     = declaration* eof ; (begining part)

    declararation = varDec1
                  | statement ;
    varDec1       = "var" IDENTIFIER ( "=" expression )? ";" ;
    statement     = express Statment
                   | printStmt
                   | block ;
    block          = "{" ( declaration )* "}" ; 

    exprStmt       = expression ";" ;
    printStmt      = "print" expression ";" ;

    expression     = assignment ;
    assignment     = identifier ( "=" assingment )?
                   | equality ;
    equality       -> comparison ( ( "!=" | "==" ) comparison )*
    comparison     -> term ( ( ">" | ">=" | "<" | "<=" ) term )*
    term           -> factor ( ( "-" | "+" ) factor )*
    factor         -> unary ( ( "/" | "*" ) unary )*
    unary          -> ( "!" | "-" ) unary
                   | primary
    primary        -> NUMBER |  
    """

