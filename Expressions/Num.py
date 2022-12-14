from Expressions.MathExpression import MathExpression


class Num(MathExpression):
    def __init__(self, num: float):
        self.num = num

    def calculate(self) -> float:
        return self.num

    @staticmethod
    def validate(left: str, right: str) -> bool:
        return left == '' and right == ''
