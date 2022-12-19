from Exceptions.Exceptions import SumError
from Expressions import MathExpression
from Expressions.OneOperandMathExpression import OneOperandMathExpression


class Sum(OneOperandMathExpression):
    def __init__(self, exp: MathExpression):
        super().__init__(exp)

    def calculate(self) -> float:
        return self._sum(self.exp.calculate())

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return right == '' and not left == ''

    @staticmethod
    def _sum(n: float) -> float:

        dig_sum = 0
        is_neg = 1

        if n < 0:
            n *= -1
            is_neg = -1

        if not n % 1 == 0:
            raise SumError

        while n > 0:
            dig_sum += n % 10
            n //= 10

        return dig_sum * is_neg

