from Expressions import MathExpression
from Expressions.OneOperandMathExpression import OneOperandMathExpression


class Fac(OneOperandMathExpression):
    def __init__(self, exp: MathExpression):
        super().__init__(exp)

    def calculate(self) -> float:
        return self._factorial(self.exp.calculate())

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return right == '' and not left == ''

    @staticmethod
    def _factorial(n: float):
        fact = 1

        if n < 0 or not n % 1 == 0:
            raise ValueError

        for i in range(1, int(n) + 1):
            fact = fact * i
        return fact
