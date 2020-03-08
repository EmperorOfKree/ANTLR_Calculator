from CalculatorVisitor import CalculatorVisitor
from CalculatorParser import CalculatorParser
import math


class CalculatorVisitorImpl(CalculatorVisitor):

    def visitCalculate(self, ctx: CalculatorParser.CalculateContext):
        return self.visit(ctx.maisOuMenos())

    def visitSetVariable(self, ctx: CalculatorParser.SetVariableContext):
        valor = float(self.visit(ctx.maisOuMenos()))
        self.variaveis[str(ctx.VARIAVEL())] = valor
        return valor

    def visitSoma(self, ctx: CalculatorParser.SomaContext):
        return self.visit(ctx.maisOuMenos()) + self.visit(ctx.multOuDiv())

    def visitSubtracao(self, ctx: CalculatorParser.SubtracaoContext):
        return self.visit(ctx.maisOuMenos()) - self.visit(ctx.multOuDiv())

    def visitMultiplicacao(self, ctx: CalculatorParser.MultiplicacaoContext):
        return self.visit(ctx.multOuDiv()) * self.visit(ctx.exponencial())

    def visitDivisao(self, ctx: CalculatorParser.DivisaoContext):
        return self.visit(ctx.multOuDiv()) / self.visit(ctx.exponencial())

    def visitExp(self, ctx: CalculatorParser.ExpContext):
        if ctx.exponencial():
            return math.pow(self.visit(ctx.unaryMinus()), self.visit(ctx.exponencial()))

        return self.visit(ctx.unaryMinus())

    def visitMudancaDeSinal(self, ctx: CalculatorParser.MudancaDeSinalContext):
        return self.visit(ctx.unaryMinus())*-1

    def visitConstantePI(self, ctx: CalculatorParser.ConstantePIContext):
        return math.pi

    def visitConstanteE(self, ctx: CalculatorParser.ConstanteEContext):
        return math.e

    def visitDouble(self, ctx: CalculatorParser.DoubleContext):
        return float(str(ctx.DOUBLE()))

    def visitInt(self, ctx: CalculatorParser.IntContext):
        return float(str(ctx.INT()))

    def visitVariavel(self, ctx: CalculatorParser.VariavelContext):
        return self.variaveis[str(ctx.VARIAVEL())]

    def visitParenteses(self, ctx: CalculatorParser.ParentesesContext):
        return self.visit(ctx.maisOuMenos())

    def __init__(self):
        self.variaveis = {}
