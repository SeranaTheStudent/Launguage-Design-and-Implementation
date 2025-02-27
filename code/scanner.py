from tokens import TOKENTYPES

class scanner:
    def __init__(self, source:str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        
    @property
    def current_token(self) -> str:
        return self.source[self.start:self.current]

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def reset(self) -> None:
        self.start = 0
        self.current = 0
        self.line = 1

    def advance_line(self) -> None:
        self.line += 1

    def advance(self) -> str:
        self.current += 1
        return self.current_token

    def peek(self) -> str:
        if self.is_at_end():
            return '\0'

        return self.source[self.current]

    def peek_next(self) -> str:
        if (self.current + 1) > len(self.source):
            return '\0'

        return self.source[self.current + 1]

    def match(self, expected: str) -> bool:
        if self.is_at_end() or self.peek() != expected:
            return False

        self.advance()
        return True


