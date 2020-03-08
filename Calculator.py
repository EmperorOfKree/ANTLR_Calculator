from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorVisitorImpl import CalculatorVisitorImpl
from CalculatorParser import CalculatorParser


def main():
    print(calculate("1+5"))                                                 # 6
    print(calculate("1-5"))                                                 # -4
    print(calculate("1*5"))                                                 # 5
    print(calculate("1/5"))                                                 # 0.2
    print(calculate("5^5"))                                                 # 3125
    print(calculate("(1+(10+20*100))/50"))                                  # 40.22
    print(calculate("((100/5)*100)-100"))                                   # 1900
    print(calculate("a = 1+2\nb = a^2\nc = a + b * (a - 1)\na + b + c"))    # 33


def calculate(source):
    enter_data = InputStream(source)
    return do_compilation(enter_data)


def do_compilation(source):
    lexer = CalculatorLexer(source)
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    tree = parser.entrada()
    visitor = CalculatorVisitorImpl()
    return visitor.visit(tree)


if __name__ == '__main__':
    main()
