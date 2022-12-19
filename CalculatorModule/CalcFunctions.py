from CalculatorModule.Config import Config
from Exceptions.Exceptions import InvalidSymbolError
from Expressions.UnaryMinus import UnaryMinus


# A function class for the calculator:

class CalcFunctions:

    @staticmethod
    def is_numeric(expression_string: str) -> bool:
        """
        A function that checks if a string is a number. (Could be a positive, a negative, and a float)
        :param expression_string: the expression string.
        :return: return true if the string is a number, else returns false.
        """
        try:
            float(expression_string)
            if not expression_string[0] == Config.ADD_SIGN:
                return True
            return False
        except ValueError:
            return False

    @staticmethod
    def replace_unary_minus(expression_string: str, char: str) -> str:
        """
        A function that replaces every unary minus with a new unary minus sign.
        :param expression_string: the expression string.
        :param char: The new sign of the unary minuses.
        :return: returns the expression string after modification.
        """

        expression_string = list(expression_string)

        # Replace starting minuses with the new sign of the unary minuses:
        if expression_string[0] == Config.SUB_SIGN:
            for curr_index, c in enumerate(expression_string):
                if c == Config.SUB_SIGN:
                    expression_string[curr_index] = char
                elif c not in Config.right:
                    break

        # Replace the rest of the unary minuses with the new sign of the unary minuses:
        for curr_index, c in enumerate(expression_string):
            if c == Config.SUB_SIGN:
                if (not CalcFunctions.is_numeric(expression_string[curr_index - 1])) and not (expression_string[
                                                                                                  curr_index - 1] in Config.left) and (CalcFunctions.is_numeric(expression_string[curr_index + 1])) and \
                        expression_string[curr_index - 1] != Config.CLOSED_BRACKET_SIGN:
                    expression_string[curr_index] = char

        expression_string = "".join(expression_string)
        return expression_string

    @staticmethod
    def find_unary_minus_char():
        Config.UNARY_MINUS_SIGN = 'M'
        Config.operator_order[Config.UNARY_MINUS_SIGN] = CalcFunctions.max_order()
        Config.operator_classes[Config.UNARY_MINUS_SIGN] = UnaryMinus

    @staticmethod
    def max_order() -> int:
        """
        A function that checks the order dict from Config.py and returns the highest order of an operator
        :return: The highest order of an operator.
        """
        max_ord = 0
        for operator in Config.operator_order:
            max_ord = max(max_ord, Config.operator_order.get(operator))

        return max_ord + 1

    @staticmethod
    def check_invalid_symbols(expression_string: str) -> str:
        """
        A function that check invalid symbols in the expression.
        :param expression_string: the expression string.
        :return: if there is an invalid symbol, raises an exception.
        """
        for i, c in enumerate(expression_string):
            if not (c in Config.operator_order.keys() or c == '.' or c == '(' or c == ')'
                    or CalcFunctions.is_numeric(c)):
                raise InvalidSymbolError(c, i)
        return expression_string

    @staticmethod
    def remove_surrounding_brackets(expression_string: str) -> str:
        """
        A function that checks if an expression is encapsulated with brackets. if so removes them.
        :param expression_string: the expression string.
        :return: the new expression string (or the original one if not encapsulated with brackets)
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
                    return CalcFunctions.remove_surrounding_brackets(expression_string[1:-1])
                count -= 1

            if count == 0 and saw_bracket:
                break

        return expression_string
