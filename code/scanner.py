from typing import List, Union, Any, Optional

from tokens import (
    TOKENTYPES as tt,
    Token,
    KEYWORDS,
    SINGLE_CHARACTERS,
    ONE_OR_MORE,
    STRING_STAR,
    WHITESPACE,
)

class scanner:
    def __init__(self, source:str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        
    @property
    def current_token(self):
        return self.source[self.start:self.current]

    def at_end(self):
        return self.current >= len(self.source)

    def reset(self):
        self.start = 0
        self.current = 0
        self.line = 1

    def advance_line(self):
        self.line += 1

    def advance(self):
        self.current += 1
        return self.current_token

    def peek(self):
        if self.at_end():
            return '\0'

        return self.source[self.current]

    def peek_at_next(self):
        if (self.current + 1) > len(self.source):
            return '\0'

        return self.source[self.current + 1]

    def match(self, expected: str):
        if self.at_end() or self.peek() != expected:
            return False

        self.advance()
        return True
    
    def identifier(self):
        while self.peek().isalnum():
            self.advance()

        text: str = self.current_token
        typ: tt = KEYWORDS.get(text, tt.IDENTIFIER)
        self.add_token(typ)
    
    def number(self):
        def consume_digits():
            while self.peek().isdigit():
                self.advance()

        typ: tt = tt.INTEGER
        consume_digits()

        if self.peek() == '.' and self.peek_at_next().isdigit():
            typ = tt.FLOAT
            self.advance()
            consume_digits()

        if self.peek() == '.':
            raise SyntaxError('invalid')
        
        token: str = self.current_token
        value: Union[float, int] = float(token) if '.' in token else int(token)

        self.add_token(typ, value)

    def string(self, starter:str):
        while self.peek() != starter and not self.at_end():
            if self.peek() == '\n':
                self.advance_line()
            self.advance()

        self.advance()
        text: str = self.source[(self.start + 1):(self.current - 1)]
        self.add_token(tt.STRING, text)

    def comment(self):
        while self.peek() != '\n' and not self.at_end():
            self.advance()

    def add_token(self, typ: tt, literal: Optional[any] = None):
        token = Token(typ, self.current_token, literal, self.line)
        self.tokens.append(token)

    def scan_token(self):
        char = self.advance()

        if char in SINGLE_CHARACTERS:
            self.add_token(tt(char))
        elif char in ONE_OR_MORE:
            compunds = [e for e in ONE_OR_MORE if e.startswith(char) and len(e) == 2]

            token = char

            for compound in compunds:
                if self.match(compound[1]):
                    token = compound
                    break

            self.add_token(tt(token))
        elif char in WHITESPACE:
            return
        elif char == '\n':
            self.advance_line()
        elif char == '/':
            if self.match('/'):
                self.comment()
            else:
                self.add_token(tt.SLASH)
        elif char in STRING_STAR:
            self.string(char)
        elif char.isdigit():
            self.number()
        elif char.isalpha():
            self.identifier()
        else:
            raise SyntaxError(f"Unexpected character '{char}' at line {self.line}")
                    
        
    
    def scan_tokens(self):
        while not self.at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(tt.EOF, tt.EOF.value, None, self.line))
        return self.tokens

