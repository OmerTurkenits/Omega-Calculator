# An exception for when the expression has more opening brackets than closing ones.
class OpenBracketsError(Exception):
    pass


# An exception for when the expression has more closing brackets than opening ones.
class ClosedBracketsError(Exception):
    pass


# An exception for when the expression has a factorial of a negative number.
class FactorialError(Exception):
    pass


# An exception for when the expression has a sum of a float.
class SumError(Exception):
    pass


# An exception for when the expression has an invalid symbol.
class InvalidSymbolError(Exception):
    def __init__(self, symbol: str, index: int):
        self.symbol = symbol
        self.index = index


# An exception for when the expression has an error with its operands.
class OperatorError(Exception):
    def __init__(self, operator: str):
        self.operator = operator
