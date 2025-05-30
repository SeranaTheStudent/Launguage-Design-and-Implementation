from abc import ABC, abstractmethod

from express import Expr


class StmtVisitor(ABC):
    @abstractmethod
    def visit_expression_stmt(self, expr: 'Stmt'):
        pass

    @abstractmethod
    def visit_print_stmt(self, expr: 'Stmt'):
        pass


class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: StmtVisitor):
        pass


class Expression(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_expression_stmt(self)


class Print(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_print_stmt(self)