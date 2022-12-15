from CalculatorModule.CalcFunctions import CalcFunctions
from CalculatorModule.Config import Config
from Exceptions.Exceptions import ClosedBracketsError, OpenBracketsError, FactorialError, InvalidSymbolError, \
    OperatorError
from Expressions.MathExpression import MathExpression
from Expressions.Num import Num
from Expressions.UnaryMinus import UnaryMinus


class Calculator:

    @staticmethod
    def calculate(expression_string: str):

        try:

            # Removes spaces:
            expression_string = expression_string.replace(" ", "").replace("\t", "")

            # Check invalid symbols: //Remember '.' of floating number
            expression_string = CalcFunctions.check_invalid_symbols(expression_string)

            # Manage unary minuses:
            expression_string = CalcFunctions.unary_minus_manager(expression_string)

            # Replace starting minuses with unary minus operator:
            if expression_string[0] == Config.SUB_SIGN:
                for c in expression_string:
                    if c == Config.SUB_SIGN:
                        expression_string = expression_string.replace(Config.SUB_SIGN, Config.UNARY_MINUS_SIGN, 1)
                    else:
                        break

            # Calculate:
            x = Calculator.to_object(expression_string)

            # Print the result:
            print("\033[92mResult: \033[0m" + str(x.calculate()))

        # Exceptions:
        except IndexError:
            print("\033[91mNo Data Entered!\033[0m")
        except KeyError:
            print("\033[91mInvalid Data!\033[0m")
        except OperatorError as opError:
            print(f"\033[91mInvalid '{opError.operator}' Operation!\033[0m")
        except OpenBracketsError:
            print("\033[91mBracket Error!, More Opening Brackets Then Closing Brackets.\033[0m")
        except ClosedBracketsError:
            print("\033[91mBracket Error!, More Closing Brackets Then Opening Brackets.\033[0m")
        except FactorialError:
            print("\033[91mFactorial Error!, The Factorial Of A Negative Number Is Not Possible.\033[0m")
        except InvalidSymbolError as invalidSymbol:
            print("\033[91m "*invalidSymbol.index+"↑\033[0m")
            print(f"\033[91mInvalid Symbol At Index {invalidSymbol.index}.\033[0m")
        except ZeroDivisionError:
            print("\033[91mError!, Division By Zero\033[0m")

    @staticmethod
    def to_object(expression_string: str) -> MathExpression:
        """
        A recursive function that gets a string and turns it into a "MathExpression" type object.
        :param expression_string: the math expression string
        :return:
        """

        # If the expression is surrounded by brackets, removes the surrounding brackets.
        expression_string = CalcFunctions.remove_surrounding_brackets(expression_string)

        if expression_string[0] == Config.SUB_SIGN:
            return UnaryMinus(Calculator.to_object(expression_string[1:]))

        # If the string is a number, Return the number as a Num object.
        if CalcFunctions.is_numeric(expression_string):
            return Num(float(expression_string))

        # Returns the last lowest order operator and its index in the string:
        min_operator, min_operator_index = Calculator.find_lowest_order_operator(expression_string)

        # Separate the left and right of the operator:
        left, right = expression_string[:min_operator_index], expression_string[min_operator_index + 1:]

        # Validate the sides of the expression:
        if not Config.operator_classes[min_operator].validate(left, right):
            raise OperatorError(min_operator)
        else:
            # If the operation has a right operand (Unary):
            if Config.operator_classes[min_operator] in Config.right:
                return Config.operator_classes[min_operator](Calculator.to_object(right))

            # If the operation has a right operand (Unary):
            if Config.operator_classes[min_operator] in Config.left:
                return Config.operator_classes[min_operator](Calculator.to_object(left))

            # If the operation is binary and has a right and a left operand:
            return Config.operator_classes[min_operator](Calculator.to_object(left), Calculator.to_object(right))

    @staticmethod
    def find_lowest_order_operator(expression_string: str) -> {str, int}:
        """

        :param expression_string:
        :return:
        """

        min_operator = ''
        min_operator_index = 0
        curr_index = 0
        bracket_count = 0

        for c in expression_string:
            # Bracket Manager
            if c == Config.OPEN_BRACKET_SIGN:
                bracket_count += 1
            if c == Config.CLOSED_BRACKET_SIGN:
                bracket_count -= 1

            # If there are more closing brackets than opening brackets:
            if bracket_count < 0:
                raise ClosedBracketsError  # Bracket error

            if bracket_count == 0:
                if c in Config.operator_order:

                    # If an operator hasn't been found yet
                    if min_operator == '':
                        min_operator = c
                        min_operator_index = curr_index
                        curr_index += 1
                        continue

                    if Config.operator_order[c] <= Config.operator_order[min_operator] and (not Config.operator_classes[c] in Config.right or expression_string[curr_index - 1] != Config.UNARY_MINUS_SIGN) \
                            and not (expression_string[curr_index] == Config.SUB_SIGN and expression_string[curr_index - 1] == Config.SUB_SIGN):
                        min_operator = c
                        min_operator_index = curr_index
            curr_index += 1

        # If there are more opening brackets than closing brackets:
        if bracket_count > 0:
            raise OpenBracketsError  # Bracket error

        return min_operator, min_operator_index



