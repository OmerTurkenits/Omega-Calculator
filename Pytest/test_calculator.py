import pytest

from CalculatorModule.CalcFunctions import CalcFunctions
from CalculatorModule.Calculator import Calculator


# Simple Errors:
def test_simple_error_1(capsys):
    Calculator.calculate("2^+3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_simple_error_2(capsys):
    Calculator.calculate("2^+4")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_simple_error_3(capsys):
    Calculator.calculate("2^+3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_simple_error_4(capsys):
    Calculator.calculate("2^+3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_simple_error_5(capsys):
    Calculator.calculate("2^+3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_gibberish_input(capsys):
    Calculator.calculate("gfjkdsdjf")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


def test_empty_input(capsys):
    Calculator.calculate("")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert CalcFunctions.is_numeric(stdout)


# Simple Operation Tests:
def test_add(capsys):
    Calculator.calculate("5+3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "8.0\n"


def test_sub(capsys):
    Calculator.calculate("7-2")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "5.0\n"


def test_mul(capsys):
    Calculator.calculate("5*5")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "25.0\n"


def test_div(capsys):
    Calculator.calculate("9/3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "3.0\n"


def test_pow(capsys):
    Calculator.calculate("4^2")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "16.0\n"


def test_mod(capsys):
    Calculator.calculate("13%3")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "1.0\n"


def test_max(capsys):
    Calculator.calculate("6$8")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "8.0\n"


def test_min(capsys):
    Calculator.calculate("6&8")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "6.0\n"


def test_avg(capsys):
    Calculator.calculate("4@6")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "5.0\n"


def test_neg(capsys):
    Calculator.calculate("~20")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "-20.0\n"


def test_fac(capsys):
    Calculator.calculate("5!")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "120.0\n"


def test_sum(capsys):
    Calculator.calculate("345#")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "12.0\n"


# Complex Tests:
def test_complex_1(capsys):
    Calculator.calculate("(2---3#)*(5$20)-5!*9")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "-1100.0\n"


def test_complex_2(capsys):
    Calculator.calculate("--3!-(~4/-0.5)+-6$5")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "3.0\n"


def test_complex_3(capsys):
    Calculator.calculate("2&3-((123#/10%3)-20@10)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "11.0\n"


def test_complex_4(capsys):
    Calculator.calculate("176+(12*176/(89^70%144))")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "176.0\n"


def test_complex_5(capsys):
    Calculator.calculate("(1+2)*(11#^5)%6$(7&8@9)+3!")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "6.0\n"


def test_complex_6(capsys):
    Calculator.calculate("(4$24&(49@15+1!+5))-5^2")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "-1.0\n"


def test_complex_7(capsys):
    Calculator.calculate("~---3!#*(3@5--8)#+2!")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "20.0\n"


def test_complex_8(capsys):
    Calculator.calculate("((30%4)&(6@3))--((6^8)#-2!)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "36.0\n"


def test_complex_9(capsys):
    Calculator.calculate("(454/2)#^(2&1*3$2)-600")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "731.0\n"


def test_complex_10(capsys):
    Calculator.calculate("(1234#%3)$(5^3*0.5)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "62.5\n"


def test_complex_11(capsys):
    Calculator.calculate("(2^3*6$4*3!*8@2*7&12)#")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "9.0\n"


def test_complex_12(capsys):
    Calculator.calculate("(62$6)*45@55^(74@34%4)/5^4")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "248.0\n"


def test_complex_13(capsys):
    Calculator.calculate("--5&34$((78%4)*7)#+6*10")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "65.0\n"


def test_complex_13(capsys):
    Calculator.calculate("-(3^5&54*43)#+55%6*3$5")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "-13.0\n"


def test_complex_14(capsys):
    Calculator.calculate("(123#!)/(4^3&(8@4))+0.5@1")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "12.0\n"


def test_complex_15(capsys):
    Calculator.calculate("(3.7$5@45*2.5-11&20)-22#!")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "27.5\n"


def test_complex_16(capsys):
    Calculator.calculate("(65&34@(3434%67))%(456&6)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "1.5\n"


def test_complex_17(capsys):
    Calculator.calculate("(66&4567#-765&43)$(-200&655)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "-21.0\n"


def test_complex_18(capsys):
    Calculator.calculate("(45@47#*6)%(4345#)/2")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "4.0\n"


def test_complex_19(capsys):
    Calculator.calculate("((573#*32$65)/(5*111#))--5")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "70.0\n"


def test_complex_20(capsys):
    Calculator.calculate("78*(0.5&634)%(32$345#)")
    stdout, stderr = capsys.readouterr()
    print(stdout)
    assert stdout == "39.0\n"



