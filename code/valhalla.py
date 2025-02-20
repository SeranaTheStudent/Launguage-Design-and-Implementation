import re

TOKEN_TYPES = {
    'NUMBER': r'\d+(\.\d+)?',
    'OPERATOR': r'[\+\-\*/]',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'WHITESPACE': r'\s+',
    'BOOLEAN': r'\btrue\b|\bfalse\b',
    'COMPARISON': r'\<=|>=|<|>|==|!=',
    'LOGICAL_OP': r'and|or',
    'NOT': r'!'
}

# bum
class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.input_text):
            match = None

            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.input_text, self.position)

                if match:
                    if token_type != 'WHITESPACE':
                        value = match.group(0)
                        if token_type == 'NUMBER':
                            value == float(value)
                        self.tokens.append((token_type, value))
                    self.position = match.end()
                    break

            if not match:
                raise SyntaxError(f"Unexpected character: {self.input_text[self.position]}")
            
        return self.tokens
    

expression = "8.5 / (2 * 9) - -3"
lexer = Lexer(expression)
tokens = lexer.tokenize()
print(tokens)