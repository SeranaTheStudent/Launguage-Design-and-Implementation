import re
from tokens import TOKENTYPES

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.input_text):
            match = None

            for token_type, pattern in TOKENTYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.input_text, self.position)

                if match:
                    if token_type != 'WHITESPACE':
                        value = match.group(0)
                        if token_type == 'NUMBER':
                            value = round(float(value), 2) #round to 2 decimal places
                        elif token_type == 'BOOLEAN_T':
                            value = True 
                        elif token_type == 'BOOLEAN_F':
                            value = False
                        self.tokens.append((token_type, value))
                    self.position = match.end()
                    break

            if not match:
                raise SyntaxError(f"Unexpected character: {self.input_text[self.position]}")
            
        return self.tokens
    