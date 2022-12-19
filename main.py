from CalculatorModule.CalcFunctions import CalcFunctions
from CalculatorModule.Calculator import Calculator
from CalculatorModule.Config import Config


def main():
    # Prints a welcome message.
    print(Config.WELCOME_MESSAGE)

    # Find the unary minus sign once:
    CalcFunctions.find_unary_minus_char()

    while True:
        try:
            x = input("\nEnter A Math Equation:\n")
            Calculator.calculate(x)
        except EOFError:
            print("Program Ended...")
            break
        except KeyboardInterrupt:
            print("Program Ended...")
            break


if __name__ == '__main__':
    main()
