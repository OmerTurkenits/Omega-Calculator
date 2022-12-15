from CalculatorModule.Config import Config
from Exceptions.Exceptions import InvalidSymbolError


class CalcFunctions:

    @staticmethod
    def is_numeric(expression_string: str) -> bool:
        """
        A function that checks if a string is a number. (Could be a positive, a negative, and a float)

        :param expression_string: the string.
        :return: if the string
        """
        try:
            float(expression_string)
            if not expression_string[0] == Config.ADD_SIGN:
                return True
            return False
        except ValueError:
            return False

    @staticmethod
    def unary_minus_manager(expression_string: str) -> str:
        char = Config.UNARY_MINUS_SIGN

        expression_string = CalcFunctions.replace_unary_minus(expression_string, char)

        # If there are 2 minuses, removes them.

        return expression_string

    @staticmethod
    def replace_unary_minus(expression_string: str, char: str) -> str:
        expression_string = list(expression_string)
        curr_index = 0

        for c in expression_string:
            if c == Config.SUB_SIGN:
                if CalcFunctions.is_numeric(expression_string[curr_index + 1]) \
                        and not CalcFunctions.is_numeric(expression_string[curr_index - 1]) \
                        or (expression_string[curr_index + 1] == Config.OPEN_BRACKET_SIGN
                            and not expression_string[curr_index - 1] == Config.CLOSED_BRACKET_SIGN):
                    expression_string[curr_index] = char

            curr_index += 1

        expression_string = "".join(expression_string)
        return expression_string

    @staticmethod
    def max_order() -> int:
        max_ord = 0
        for operator in Config.operator_order:
            max_ord = max(max_ord, Config.operator_order.get(operator))

        return max_ord + 1

    @staticmethod
    def check_invalid_symbols(expression_string: str) -> str:
        for i, c in enumerate(expression_string):
            if not (c in Config.operator_order.keys() or c == '.' or c == '(' or c == ')'
                    or CalcFunctions.is_numeric(c)):
                raise InvalidSymbolError(i)
        return expression_string

    @staticmethod
    def remove_surrounding_brackets(expression_string: str) -> str:
        """
        A function that checks if an expression is encapsulated with brackets. if so removes them.
        :param expression_string:
        :return:
        """
        if expression_string[0] != Config.OPEN_BRACKET_SIGN:
            return expression_string
        count = 0
        saw_bracket = False
        for i, c in enumerate(expression_string):
            if c == Config.OPEN_BRACKET_SIGN:
                count += 1
                saw_bracket = True
            elif c == Config.CLOSED_BRACKET_SIGN:
                if i == len(expression_string) - 1:
                    return CalcFunctionsc .remove_surrounding_brackets(expression_string[1:-1])
                count -= 1

            if count == 0 and saw_bracket:
                break

        return expression_string

