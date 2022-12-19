from Expressions import MathExpression
from Expressions.OneOperandMathExpression import OneOperandMathExpression


class Neg(OneOperandMathExpression):
    def __init__(self, exp: MathExpression):
        super().__init__(exp)

    def calculate(self) -> float:
        return self.exp.calculate() * -1

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return left == '' and not right == '' and right.find('~') == -1
