from Expressions import MathExpression
from Expressions.TwoOperandMathExpression import TwoOperandMathExpression


class Sub(TwoOperandMathExpression):
    def __init__(self, exp1: MathExpression, exp2: MathExpression):
        self.exp1 = exp1
        self.exp2 = exp2

    def calculate(self) -> float:
        return self.exp1.calculate() - self.exp2.calculate()

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return not left == '' and not right == ''
