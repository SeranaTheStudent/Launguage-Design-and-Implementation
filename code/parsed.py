from collections import deque
from tokens import TOKENTYPES as tt
from codetypes import StringLiteral

class ParseError(Exception):
    def __init__(self,):
        pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
    
    def at_end(self):
        return self.peek().type == tt.EOF
    
    def previous(self):
        return self.tokens[self.current - 1]
    
    def next(self):
        if self.at_end():
            raise EOFError("End of file, cannot retrieve next token")
        
        return self.tokens[self.current + 1]
    
    def check(self, token_type):
        if self.at_end():
            return False
        
        return self.peek().type == token_type