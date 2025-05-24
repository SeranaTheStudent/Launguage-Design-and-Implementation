from enum import Enum
from typing import Dict, Tuple, Any

class TOKENTYPES(Enum):
    # singles tokens
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '['
    RBRACKET = ']'
    LBRACE = '{'
    RBRACE = '}'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    COLON = ':'
    SEMICOLON = ';'
    SLASH = '/'
    BACKSLASH = '\\'
    STAR = '*'
    UNDERSCORE = '_'
    QUESTION_MARK = '?'
    PERCENT = '%'
    AT_SIGN = '@'
    AMPERSAND = '&'
    DOLLAR = '$'
    CARET = '^'
    TILDE = '~'
    PIPE = '|'

    # One or more tokens
    BANG = '!'
    BANG_EQUAL = '!='
    EQUAL = '='
    DOUBLE_EQUAL = '=='
    GREATER = '>'
    GREATER_THAN_OR_EQUAL = '>='
    LESS = '<'
    LESS_THAN_OR_EQUAL = '<='
    ARROW = '->'
    HASHBANG = '#!'
    HASH = '#'
    ELLIPSIS = '...'
    TRIPLE_QUOTE = '"""'

    # keywords
    GET = 'get'
    SET = 'set'
    DELETE = 'delete'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
    IF = 'if'
    ELSE = 'else'
    SWITCH = 'switch'
    CASE = 'case'
    WHEN = 'when'
    WHILE = 'while'
    UNLESS = 'unless'
    BREAK = 'break'
    FOR = 'for'
    IN = 'in'
    DO = 'do'
    NULL = 'null'
    TRUE = 'true'
    FALSE = 'false'
    TRY = 'try'
    CATCH = 'catch'
    FINALLY = 'finally'
    NEW = 'new'
    CLASS = 'class'
    EXTENDS = 'extends'
    SELF = 'self'
    FUNCTION = 'function'
    RETURN = 'return'
    YIELD = 'yield'
    ASYNC = 'async'
    STATIC = 'static'
    LAMBDA = 'lambda'
    CONST = 'const'
    LET = 'let'
    VAR = 'var'
    PRIVATE = 'private'
    END = 'end'
    PRINT = 'print'

    #  String Starters
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    # new line
    NEWLINE = '\n'

    # space
    TAB = '\t'
    SPACE = ' '

    # String terminators
    NULL_CHAR = '\0'

    #End-user identifiers
    IDENTIFIER = 'identifier'
    INTEGER = 'int'
    FLOAT = 'float'
    STRING = 'str'

    # End of file
    EOF = ''


# importing typing is used here.
_keywords: Tuple[str] = (
    'true', 'false', 'null', 'and', 'or', 'if', 'else', 'function', 'return',
    'for', 'class', 'const', 'let', 'while', 'var', 'print'
)

KEYWORDS: Dict[str, TOKENTYPES] = {key: TOKENTYPES(key) for key in _keywords}

SINGLE_CHARACTERS: Tuple[str] = (
    '(', ')', '{', '}', ',', '.', '-', '+', ';', '*',
)

ONE_OR_MORE: Tuple[str] = ('!', '!=', '=', '==', '>', '>=', '<', '<=')

WHITESPACE: Tuple[str] = (' ', '\r', '\t')

STRING_STAR: Tuple[str] = ('"', "'")


class Token:
    def __init__(
            self,
            typ: TOKENTYPES,
            lexeme: str,
            literal: Any,
            line: int
    ) -> None:
        self.type = typ
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'{self.type}: {self.lexeme}, {self.literal}, {self.line}'

    def __repr__(self):
        properties = f'{self.type}, {self.lexeme}, {self.literal}, {self.line}'
        return f'{self.__class__.__name__}({properties})'
