from Expressions.Add import Add
from Expressions.Sub import Sub
from Expressions.Mul import Mul
from Expressions.Div import Div
from Expressions.Pow import Pow
from Expressions.Mod import Mod
from Expressions.Avg import Avg
from Expressions.Max import Max
from Expressions.Min import Min
from Expressions.Neg import Neg
from Expressions.Fac import Fac
from Expressions.Sum import Sum
from Expressions.UnaryMinus import UnaryMinus


class Config:
    # Consts for operator signs:
    ADD_SIGN = '+'
    SUB_SIGN = '-'
    MUL_SIGN = '*'
    DIV_SIGN = '/'
    POW_SIGN = '^'
    MOD_SIGN = '%'
    AVG_SIGN = '@'
    MAX_SIGN = '$'
    MIN_SIGN = '&'
    NEG_SIGN = '~'
    FAC_SIGN = '!'
    SUM_SIGN = '#'
    OPEN_BRACKET_SIGN = '('
    CLOSED_BRACKET_SIGN = ')'
    UNARY_MINUS_SIGN = ''

    # Operator orders
    operator_order = {ADD_SIGN: 1, SUB_SIGN: 1, MUL_SIGN: 2, DIV_SIGN: 2, POW_SIGN: 3, MOD_SIGN: 4, MAX_SIGN: 5,
                      MIN_SIGN: 5, AVG_SIGN: 5, NEG_SIGN: 6, FAC_SIGN: 6, SUM_SIGN: 6}

    # Translation between sign and class
    operator_classes = {ADD_SIGN: Add, SUB_SIGN: Sub, MUL_SIGN: Mul, DIV_SIGN: Div, POW_SIGN: Pow, MOD_SIGN: Mod,
                        MAX_SIGN: Max, MIN_SIGN: Min, AVG_SIGN: Avg, NEG_SIGN: Neg, FAC_SIGN: Fac, SUM_SIGN: Sum}

    right = [Neg, UnaryMinus]
    left = [Fac, Sum]
