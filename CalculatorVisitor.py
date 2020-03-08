# Generated from C:/MyProjects/ANTLR_calculator\Calculator.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#ToSetVar.
    def visitToSetVar(self, ctx:CalculatorParser.ToSetVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Calculate.
    def visitCalculate(self, ctx:CalculatorParser.CalculateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#SetVariable.
    def visitSetVariable(self, ctx:CalculatorParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#MutiplicaOuDivide.
    def visitMutiplicaOuDivide(self, ctx:CalculatorParser.MutiplicaOuDivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Soma.
    def visitSoma(self, ctx:CalculatorParser.SomaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Subtracao.
    def visitSubtracao(self, ctx:CalculatorParser.SubtracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Multiplicacao.
    def visitMultiplicacao(self, ctx:CalculatorParser.MultiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#toExp.
    def visitToExp(self, ctx:CalculatorParser.ToExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Divisao.
    def visitDivisao(self, ctx:CalculatorParser.DivisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Exp.
    def visitExp(self, ctx:CalculatorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#MudancaDeSinal.
    def visitMudancaDeSinal(self, ctx:CalculatorParser.MudancaDeSinalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ToAtom.
    def visitToAtom(self, ctx:CalculatorParser.ToAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ConstantePI.
    def visitConstantePI(self, ctx:CalculatorParser.ConstantePIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ConstanteE.
    def visitConstanteE(self, ctx:CalculatorParser.ConstanteEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Double.
    def visitDouble(self, ctx:CalculatorParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Int.
    def visitInt(self, ctx:CalculatorParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Variavel.
    def visitVariavel(self, ctx:CalculatorParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Parenteses.
    def visitParenteses(self, ctx:CalculatorParser.ParentesesContext):
        return self.visitChildren(ctx)



del CalculatorParser