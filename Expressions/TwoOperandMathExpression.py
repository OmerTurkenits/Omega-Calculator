from Expressions.MathExpression import MathExpression


class TwoOperandMathExpression(MathExpression):
    def __init__(self, exp1: MathExpression, exp2: MathExpression):
        self.exp1 = exp1
        self.exp2 = exp2

    def calculate(self) -> float:
        pass

    @staticmethod
    def validate(left: str, right: str) -> bool:
        pass

