from typing import Any, List

import express
import state
from tokens import (
    TOKENTYPES as tt,
    Token,
)

class Interpreter(express.ExprVisitor, state.StmtVisitor):
    def evaluate(self, expr: express.Expr):
        return expr.accept(self)
    
    def execute(self, stmt: state.Stmt):
        stmt.accept(self)

    def interpret(self, stmts: List[state.Stmt]):
        for stmt in stmts:
            self.execute(stmt)
    
    @staticmethod
    def stringify(obj: Any):
        if isinstance(obj, str):
            return obj
        
        if obj is None:
            return 'null'
        
        if isinstance(obj, bool):
            return str(obj).lower()
        
        return str(obj)
    
    @staticmethod
    def is_truthy(obj: Any):
        return bool(obj)
    
    @staticmethod
    def is_equal(a: Any, b: Any):
        return a == b
    
    @staticmethod
    def is_number(obj:Any):
        return isinstance(obj, (int, float))
    
    def check_number_operand(self, operator: Token, operand: Any):
        if self.is_number(operand):
            return
        
        raise self.error(operator, "Operand must be a number.")
    
    def check_number_operands(self, operator: Token, left: Any, right: Any):
        if self.is_number(left) and self.is_number(right):
            return
        
        raise self.error(operator, "Operands must be numbers.")
    
    def visit_expression_stmt(self, stmt: state.Expression):
        self.evaluate(stmt.expression)

        return None
    
    def visit_print_stmt(self, stmt: state.Print):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))

        return None
    
    def visit_assign_expr(self, expr: express.Expr):
        pass

    def visit_binary_expr(self, expr: express.Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        token_type = expr.operator.type

        if token_type == tt.BANG_EQUAL:
            return not self.is_equal(left, right)
        elif token_type == tt.DOUBLE_EQUAL:
            return self.is_equal(left, right)
        elif token_type == tt.GREATER:
            self.check_number_operands(expr.operator, left, right)
            return left > right
        elif token_type == tt.GREATER_THAN_OR_EQUAL:
            self.check_number_operands(expr.operator, left, right)
            return left >= right
        elif token_type == tt.LESS:
            self.check_number_operands(expr.operator, left, right)
            return left < right
        elif token_type == tt.LESS_THAN_OR_EQUAL:
            self.check_number_operands(expr.operator, left, right)
            return left <= right
        elif token_type == tt.MINUS:
            self.check_number_operands(expr.operator, left, right)
            return left - right
        elif token_type == tt.PLUS:
            if (self.is_number(left) and self.is_number(right)) or (isinstance(left, str) and isinstance(right, str)):
                return left + right
            
        elif token_type == tt.SLASH:
            self.check_number_operands(expr.operator, left, right)
            return left / right
        elif token_type == tt.STAR:
            self.check_number_operands(expr.operator, left, right)
            return left * right
        elif token_type == tt.AND:
            return self.is_truthy(left) and self.is_truthy(right)
        elif token_type == tt.OR:
            return self.is_truthy(left) or self.is_truthy(right)
        
        return None
    
    def visit_call_expr(self, expr: express.Expr):
        pass

    def visit_get_expr(self, expr: express.Expr):
        pass

    def visit_grouping_expr(self, expr: express.Grouping):
        return self.evaluate(expr.expression)
    
    def visit_literal_expr(self, expr: express.Expr):
        return expr.value
    
    def visit_logical_expr(self, expr: express.Expr):
        pass

    def visit_unary_expr(self, expr: express.Unary):
        right = self.evaluate(expr.right)

        if expr.operator.type == tt.BANG:
            return not self.is_truthy(right)
        elif expr.operator.type == tt.MINUS:
            self.check_number_operand(expr.operator, right)
            return -right
        
        return None
            
     
        