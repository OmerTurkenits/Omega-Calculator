from CalculatorModule import Calc
from Expressions import MathExpression
from Expressions.TwoOperandMathExpression import TwoOperandMathExpression


class Add(TwoOperandMathExpression):
    def __init__(self, exp1: MathExpression, exp2: MathExpression):
        super().__init__(exp1, exp2)

    def calculate(self) -> float:
        return self.exp1.calculate() + self.exp2.calculate()

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return not left == '' and not right == ''
