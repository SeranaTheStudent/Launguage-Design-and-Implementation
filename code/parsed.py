from typing import List, Optional
import express
import state

from tokens import (
    TOKENTYPES as tt,
    Token)

class parser:
    def __init__(self, tokens: list[Token]):
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
    
    def check(self, typ: tt):
        if self.at_end():
            return False
        
        return self.peek().type == typ
    
    def advance(self):
        if not self.at_end():
            self.current += 1
        
        return self.previous()
    
    def peek(self):
        return self.tokens[self.current]
    
    def match(self, *types: tt):
        for typ in types:
            if self.check(typ):
                self.advance()
                return True
        
        return False
    
    @staticmethod
    def error(token: Token, message: str):
        raise SyntaxError(f"[line {token.line}] Error at '{token.lexeme}': {message}")
    
    def consume(self, typ: tt, message: str):
        if self.check(typ):
            return self.advance()
        
        raise self.error(self.peek(), message)
    
    def expression(self):
        return self.equality()
    
    def statement(self):
        if self.match(tt.PRINT):
            return self.print_statement()
        
        return self.expression_statement()

    def print_statement(self):
        value = self.expression()
        self.consume(tt.SEMICOLON, "Expect ';' after value.")

        return state.Print(value)
    
    def expression_statement(self):
        expr = self.expression()
        self.consume(tt.SEMICOLON, "Expect ';' after expression.")

        return state.Expression(expr)
    
    def assignment(self):
        pass
    
    def equality(self):
        expr = self.comparison()

        while self.match(tt.BANG_EQUAL, tt.DOUBLE_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = express.Binary(expr, operator, right)
        
        return expr

    def comparison(self):
        expr = self.addition()

        while self.match(
            tt.GREATER,
            tt.GREATER_THAN_OR_EQUAL,
            tt.LESS,
            tt.LESS_THAN_OR_EQUAL
        ):
            operator = self.previous()
            right = self.comparison()
            expr = express.Binary(expr, operator, right)
        
        return expr

    def primary(self):
        if self.match(tt.FALSE):
            return express.Literal(False)
        elif self.match(tt.TRUE):
            return express.Literal(True)
        elif self.match(tt.NULL):
            return express.Literal(None)
        
        if self.match(
            tt.INTEGER,
            tt.FLOAT,
            tt.STRING,
        ):
            return express.Literal(self.previous().literal)
        
        if self.match(tt.LPAREN):
            expr = self.expression()
            self.consume(tt.RPAREN, "Expect ')' after expression.")
            return express.Grouping(expr)
        
        raise self.error(self.peek(), "Expect expression.")

    def Unary(self):
        if self.match(tt.BANG, tt.MINUS):
            operator = self.previous()
            right = self.Unary()

            return express.Unary(operator, right)
        
        return self.primary()
    
    def binary(self):
        expr = self.Unary()

        while self.match(tt.AND, tt.OR):
            operator = self.previous()
            right = self.Unary()
            expr = express.Binary(expr, operator, right)
        
        return expr

    def addition(self):
        expr = self.multiplication()

        while self.match(tt.MINUS, tt.PLUS):
            operator = self.previous()
            right = self.multiplication()
            expr = express.Binary(expr, operator, right)
        
        return expr
    
    def multiplication(self):
        expr = self.binary()

        while self.match(tt.SLASH, tt.STAR):
            operator = self.previous()
            right = self.Unary()
            expr = express.Binary(expr, operator, right)
        
        return expr
    
    def synchronize(self):
        self.advance()

        while not self.at_end():
            if self.previous().type == tt.SEMICOLON:
                return

            if self.peek().type in (
                    tt.CLASS,
                    tt.FUNCTION,
                    tt.VAR,
                    tt.FOR,
                    tt.IF,
                    tt.WHILE,
                    tt.PRINT,
                    tt.RETURN,
            ):
                return

            self.advance()

    def parse(self) -> List[state.Stmt]:
        stmts: List[state.Stmt] = []

        while not self.at_end():
            stmts.append(self.statement())

        return stmts