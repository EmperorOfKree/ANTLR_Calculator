# Generated from C:/MyProjects/ANTLR_calculator\Calculator.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\6\3\6\3\6\5\6@\n\6")
        buf.write("\3\7\3\7\3\7\5\7E\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\bP\n\b\3\b\2\4\6\b\t\2\4\6\b\n\f\16\2\2\2W\2\32")
        buf.write("\3\2\2\2\4\34\3\2\2\2\6 \3\2\2\2\b.\3\2\2\2\n<\3\2\2\2")
        buf.write("\fD\3\2\2\2\16O\3\2\2\2\20\21\5\4\3\2\21\22\7\b\2\2\22")
        buf.write("\23\5\2\2\2\23\33\3\2\2\2\24\26\5\6\4\2\25\27\7\b\2\2")
        buf.write("\26\25\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30\31\7\2\2")
        buf.write("\3\31\33\3\2\2\2\32\20\3\2\2\2\32\24\3\2\2\2\33\3\3\2")
        buf.write("\2\2\34\35\7\n\2\2\35\36\7\f\2\2\36\37\5\6\4\2\37\5\3")
        buf.write("\2\2\2 !\b\4\1\2!\"\5\b\5\2\"+\3\2\2\2#$\f\5\2\2$%\7\13")
        buf.write("\2\2%*\5\b\5\2&\'\f\4\2\2\'(\7\r\2\2(*\5\b\5\2)#\3\2\2")
        buf.write("\2)&\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\7\3\2\2\2")
        buf.write("-+\3\2\2\2./\b\5\1\2/\60\5\n\6\2\609\3\2\2\2\61\62\f\5")
        buf.write("\2\2\62\63\7\16\2\2\638\5\n\6\2\64\65\f\4\2\2\65\66\7")
        buf.write("\17\2\2\668\5\n\6\2\67\61\3\2\2\2\67\64\3\2\2\28;\3\2")
        buf.write("\2\29\67\3\2\2\29:\3\2\2\2:\t\3\2\2\2;9\3\2\2\2<?\5\f")
        buf.write("\7\2=>\7\7\2\2>@\5\n\6\2?=\3\2\2\2?@\3\2\2\2@\13\3\2\2")
        buf.write("\2AB\7\r\2\2BE\5\f\7\2CE\5\16\b\2DA\3\2\2\2DC\3\2\2\2")
        buf.write("E\r\3\2\2\2FP\7\5\2\2GP\7\6\2\2HP\7\4\2\2IP\7\3\2\2JP")
        buf.write("\7\n\2\2KL\7\20\2\2LM\5\6\4\2MN\7\21\2\2NP\3\2\2\2OF\3")
        buf.write("\2\2\2OG\3\2\2\2OH\3\2\2\2OI\3\2\2\2OJ\3\2\2\2OK\3\2\2")
        buf.write("\2P\17\3\2\2\2\13\26\32)+\679?DO")
        return buf.getvalue()


class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'pi'", "'e'", 
                     "'^'", "'\n'", "<INVALID>", "<INVALID>", "'+'", "'='", 
                     "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "DOUBLE", "PI", "E", "EXP", "NL", 
                      "WS", "VARIAVEL", "PLUS", "EQUAL", "MINUS", "MULT", 
                      "DIV", "LPAR", "RPAR" ]

    RULE_entrada = 0
    RULE_setVar = 1
    RULE_maisOuMenos = 2
    RULE_multOuDiv = 3
    RULE_exponencial = 4
    RULE_unaryMinus = 5
    RULE_atom = 6

    ruleNames =  [ "entrada", "setVar", "maisOuMenos", "multOuDiv", "exponencial", 
                   "unaryMinus", "atom" ]

    EOF = Token.EOF
    INT=1
    DOUBLE=2
    PI=3
    E=4
    EXP=5
    NL=6
    WS=7
    VARIAVEL=8
    PLUS=9
    EQUAL=10
    MINUS=11
    MULT=12
    DIV=13
    LPAR=14
    RPAR=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EntradaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_entrada

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CalculateContext(EntradaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.EntradaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def maisOuMenos(self):
            return self.getTypedRuleContext(CalculatorParser.MaisOuMenosContext,0)

        def EOF(self):
            return self.getToken(CalculatorParser.EOF, 0)
        def NL(self):
            return self.getToken(CalculatorParser.NL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculate" ):
                listener.enterCalculate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculate" ):
                listener.exitCalculate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculate" ):
                return visitor.visitCalculate(self)
            else:
                return visitor.visitChildren(self)


    class ToSetVarContext(EntradaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.EntradaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setVar(self):
            return self.getTypedRuleContext(CalculatorParser.SetVarContext,0)

        def NL(self):
            return self.getToken(CalculatorParser.NL, 0)
        def entrada(self):
            return self.getTypedRuleContext(CalculatorParser.EntradaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToSetVar" ):
                listener.enterToSetVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToSetVar" ):
                listener.exitToSetVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToSetVar" ):
                return visitor.visitToSetVar(self)
            else:
                return visitor.visitChildren(self)



    def entrada(self):

        localctx = CalculatorParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entrada)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalculatorParser.ToSetVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.setVar()
                self.state = 15
                self.match(CalculatorParser.NL)
                self.state = 16
                self.entrada()
                pass

            elif la_ == 2:
                localctx = CalculatorParser.CalculateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.maisOuMenos(0)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalculatorParser.NL:
                    self.state = 19
                    self.match(CalculatorParser.NL)


                self.state = 22
                self.match(CalculatorParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_setVar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetVariableContext(SetVarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.SetVarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIAVEL(self):
            return self.getToken(CalculatorParser.VARIAVEL, 0)
        def EQUAL(self):
            return self.getToken(CalculatorParser.EQUAL, 0)
        def maisOuMenos(self):
            return self.getTypedRuleContext(CalculatorParser.MaisOuMenosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetVariable" ):
                listener.enterSetVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetVariable" ):
                listener.exitSetVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetVariable" ):
                return visitor.visitSetVariable(self)
            else:
                return visitor.visitChildren(self)



    def setVar(self):

        localctx = CalculatorParser.SetVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_setVar)
        try:
            localctx = CalculatorParser.SetVariableContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CalculatorParser.VARIAVEL)
            self.state = 27
            self.match(CalculatorParser.EQUAL)
            self.state = 28
            self.maisOuMenos(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaisOuMenosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_maisOuMenos

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MutiplicaOuDivideContext(MaisOuMenosContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MaisOuMenosContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOuDiv(self):
            return self.getTypedRuleContext(CalculatorParser.MultOuDivContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMutiplicaOuDivide" ):
                listener.enterMutiplicaOuDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMutiplicaOuDivide" ):
                listener.exitMutiplicaOuDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutiplicaOuDivide" ):
                return visitor.visitMutiplicaOuDivide(self)
            else:
                return visitor.visitChildren(self)


    class SomaContext(MaisOuMenosContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MaisOuMenosContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def maisOuMenos(self):
            return self.getTypedRuleContext(CalculatorParser.MaisOuMenosContext,0)

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)
        def multOuDiv(self):
            return self.getTypedRuleContext(CalculatorParser.MultOuDivContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma" ):
                listener.enterSoma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma" ):
                listener.exitSoma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoma" ):
                return visitor.visitSoma(self)
            else:
                return visitor.visitChildren(self)


    class SubtracaoContext(MaisOuMenosContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MaisOuMenosContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def maisOuMenos(self):
            return self.getTypedRuleContext(CalculatorParser.MaisOuMenosContext,0)

        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)
        def multOuDiv(self):
            return self.getTypedRuleContext(CalculatorParser.MultOuDivContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtracao" ):
                listener.enterSubtracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtracao" ):
                listener.exitSubtracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtracao" ):
                return visitor.visitSubtracao(self)
            else:
                return visitor.visitChildren(self)



    def maisOuMenos(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.MaisOuMenosContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_maisOuMenos, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalculatorParser.MutiplicaOuDivideContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 31
            self.multOuDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.SomaContext(self, CalculatorParser.MaisOuMenosContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_maisOuMenos)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        self.match(CalculatorParser.PLUS)
                        self.state = 35
                        self.multOuDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.SubtracaoContext(self, CalculatorParser.MaisOuMenosContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_maisOuMenos)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        self.match(CalculatorParser.MINUS)
                        self.state = 38
                        self.multOuDiv(0)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultOuDivContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_multOuDiv

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicacaoContext(MultOuDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MultOuDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOuDiv(self):
            return self.getTypedRuleContext(CalculatorParser.MultOuDivContext,0)

        def MULT(self):
            return self.getToken(CalculatorParser.MULT, 0)
        def exponencial(self):
            return self.getTypedRuleContext(CalculatorParser.ExponencialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacao" ):
                listener.enterMultiplicacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacao" ):
                listener.exitMultiplicacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacao" ):
                return visitor.visitMultiplicacao(self)
            else:
                return visitor.visitChildren(self)


    class ToExpContext(MultOuDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MultOuDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exponencial(self):
            return self.getTypedRuleContext(CalculatorParser.ExponencialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToExp" ):
                listener.enterToExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToExp" ):
                listener.exitToExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToExp" ):
                return visitor.visitToExp(self)
            else:
                return visitor.visitChildren(self)


    class DivisaoContext(MultOuDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.MultOuDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOuDiv(self):
            return self.getTypedRuleContext(CalculatorParser.MultOuDivContext,0)

        def DIV(self):
            return self.getToken(CalculatorParser.DIV, 0)
        def exponencial(self):
            return self.getTypedRuleContext(CalculatorParser.ExponencialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisao" ):
                listener.enterDivisao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisao" ):
                listener.exitDivisao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivisao" ):
                return visitor.visitDivisao(self)
            else:
                return visitor.visitChildren(self)



    def multOuDiv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.MultOuDivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_multOuDiv, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalculatorParser.ToExpContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 45
            self.exponencial()
            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.MultiplicacaoContext(self, CalculatorParser.MultOuDivContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multOuDiv)
                        self.state = 47
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 48
                        self.match(CalculatorParser.MULT)
                        self.state = 49
                        self.exponencial()
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.DivisaoContext(self, CalculatorParser.MultOuDivContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multOuDiv)
                        self.state = 50
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 51
                        self.match(CalculatorParser.DIV)
                        self.state = 52
                        self.exponencial()
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExponencialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_exponencial

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpContext(ExponencialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExponencialContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryMinus(self):
            return self.getTypedRuleContext(CalculatorParser.UnaryMinusContext,0)

        def EXP(self):
            return self.getToken(CalculatorParser.EXP, 0)
        def exponencial(self):
            return self.getTypedRuleContext(CalculatorParser.ExponencialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exponencial(self):

        localctx = CalculatorParser.ExponencialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exponencial)
        try:
            localctx = CalculatorParser.ExpContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.unaryMinus()
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 59
                self.match(CalculatorParser.EXP)
                self.state = 60
                self.exponencial()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryMinusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_unaryMinus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MudancaDeSinalContext(UnaryMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.UnaryMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)
        def unaryMinus(self):
            return self.getTypedRuleContext(CalculatorParser.UnaryMinusContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMudancaDeSinal" ):
                listener.enterMudancaDeSinal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMudancaDeSinal" ):
                listener.exitMudancaDeSinal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMudancaDeSinal" ):
                return visitor.visitMudancaDeSinal(self)
            else:
                return visitor.visitChildren(self)


    class ToAtomContext(UnaryMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.UnaryMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(CalculatorParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToAtom" ):
                listener.enterToAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToAtom" ):
                listener.exitToAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAtom" ):
                return visitor.visitToAtom(self)
            else:
                return visitor.visitChildren(self)



    def unaryMinus(self):

        localctx = CalculatorParser.UnaryMinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryMinus)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculatorParser.MINUS]:
                localctx = CalculatorParser.MudancaDeSinalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(CalculatorParser.MINUS)
                self.state = 64
                self.unaryMinus()
                pass
            elif token in [CalculatorParser.INT, CalculatorParser.DOUBLE, CalculatorParser.PI, CalculatorParser.E, CalculatorParser.VARIAVEL, CalculatorParser.LPAR]:
                localctx = CalculatorParser.ToAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariavelContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIAVEL(self):
            return self.getToken(CalculatorParser.VARIAVEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel" ):
                listener.enterVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel" ):
                listener.exitVariavel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariavel" ):
                return visitor.visitVariavel(self)
            else:
                return visitor.visitChildren(self)


    class ParentesesContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(CalculatorParser.LPAR, 0)
        def maisOuMenos(self):
            return self.getTypedRuleContext(CalculatorParser.MaisOuMenosContext,0)

        def RPAR(self):
            return self.getToken(CalculatorParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenteses" ):
                listener.enterParenteses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenteses" ):
                listener.exitParenteses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenteses" ):
                return visitor.visitParenteses(self)
            else:
                return visitor.visitChildren(self)


    class ConstantePIContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PI(self):
            return self.getToken(CalculatorParser.PI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantePI" ):
                listener.enterConstantePI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantePI" ):
                listener.exitConstantePI(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantePI" ):
                return visitor.visitConstantePI(self)
            else:
                return visitor.visitChildren(self)


    class ConstanteEContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def E(self):
            return self.getToken(CalculatorParser.E, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstanteE" ):
                listener.enterConstanteE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstanteE" ):
                listener.exitConstanteE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstanteE" ):
                return visitor.visitConstanteE(self)
            else:
                return visitor.visitChildren(self)


    class DoubleContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(CalculatorParser.DOUBLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble" ):
                return visitor.visitDouble(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = CalculatorParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculatorParser.PI]:
                localctx = CalculatorParser.ConstantePIContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(CalculatorParser.PI)
                pass
            elif token in [CalculatorParser.E]:
                localctx = CalculatorParser.ConstanteEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(CalculatorParser.E)
                pass
            elif token in [CalculatorParser.DOUBLE]:
                localctx = CalculatorParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(CalculatorParser.DOUBLE)
                pass
            elif token in [CalculatorParser.INT]:
                localctx = CalculatorParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(CalculatorParser.INT)
                pass
            elif token in [CalculatorParser.VARIAVEL]:
                localctx = CalculatorParser.VariavelContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(CalculatorParser.VARIAVEL)
                pass
            elif token in [CalculatorParser.LPAR]:
                localctx = CalculatorParser.ParentesesContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(CalculatorParser.LPAR)
                self.state = 74
                self.maisOuMenos(0)
                self.state = 75
                self.match(CalculatorParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.maisOuMenos_sempred
        self._predicates[3] = self.multOuDiv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def maisOuMenos_sempred(self, localctx:MaisOuMenosContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multOuDiv_sempred(self, localctx:MultOuDivContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




