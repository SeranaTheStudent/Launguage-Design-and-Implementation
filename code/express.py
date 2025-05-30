from abc import ABC, abstractmethod
from typing import Any, List

from tokens import Token


class ExprVisitor(ABC):
    @abstractmethod
    def visit_assign_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_binary_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_call_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_get_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_grouping_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_literal_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_logical_expr(self, expr: 'Expr'):
        pass

    @abstractmethod
    def visit_unary_expr(self, expr: 'Expr'):
        pass

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: ExprVisitor):
        pass

class Assign(Expr):
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_assign_expr(self)
    
class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_binary_expr(self)
    
class Call(Expr):
    def __init__(self, callee: Expr, paren: Token, arguments: List[Expr]):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_call_expr(self)
    
class Get(Expr):
    def __init__(self, object: Expr, name: Token):
        self.object = object
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_get_expr(self)
    
class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_grouping_expr(self)
    
class Literal(Expr):
    def __init__(self, value: Any):
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_literal_expr(self)
    
class Logical(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_logical_expr(self)
    
class Set(Expr):
    def __init__(self, object: Expr, name: Token, value: Expr):
        self.object = object
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_set_expr(self)
    
class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_unary_expr(self)