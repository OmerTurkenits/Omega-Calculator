class OpenBracketsError(Exception):
    pass


class ClosedBracketsError(Exception):
    pass


class FactorialError(Exception):
    pass


class InvalidSymbolError(Exception):
    def __init__(self, index: int):
        self.index = index


class OperatorError(Exception):
    def __init__(self, operator: str):
        self.operator = operator
