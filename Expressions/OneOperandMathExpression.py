from Expressions.MathExpression import MathExpression


class OneOperandMathExpression(MathExpression):
    def __init__(self, exp: MathExpression):
        self.exp = exp

    def calculate(self) -> float:
        pass

    @staticmethod
    def validate(left: str, right: str) -> bool:
        pass

