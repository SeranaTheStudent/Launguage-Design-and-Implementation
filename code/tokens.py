TOKENTYPES = {
    'NUMBER': r'-?\d+(\.\d+)?',
    'OPERATOR': r'[\+\-\*/]',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'WHITESPACE': r'\s+',
    'BOOLEAN_F': r'\bfalse\b',
    'BOOLEAN_T': r'\btrue\b',
    'DOUBLE_EQUAL': r'==',
    'LESS_EQUAL': r'<=',
    'GREATER_EQUAL': r'>=',
    'LESS_THAN': r'<',
    'GREATER_THAN': r'>',
    'EQUAL': r'=',
    'ALERT_EQUAL': r'!=',
    'AND': r'and',
    'OR': r'or',
    'NOT': r'!',
    #'STRING': r'\".*\"'
    'STRING': r'"[^"]*"',
    'EOF': None
}

