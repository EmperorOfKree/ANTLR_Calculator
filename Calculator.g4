grammar Calculator;

// FONT https://github.com/shmatov/antlr4-calculator/blob/master/Calculator.g4

INT    	 : [0-9]+;
DOUBLE 	 : [0-9]+'.'[0-9]+;
PI     	 : 'pi';
E      	 : 'e';
EXP    	 : '^';
NL     	 : '\n';
WS     	 : [ \t\r]+ -> skip;
VARIAVEL : [a-zA-Z_][a-zA-Z_0-9]*;

PLUS  : '+';
EQUAL : '=';
MINUS : '-';
MULT  : '*';
DIV   : '/';
LPAR  : '(';
RPAR  : ')';

entrada
    : setVar NL entrada     # ToSetVar
    | maisOuMenos NL? EOF 	# Calculate
    ;

setVar
    : VARIAVEL EQUAL maisOuMenos # SetVariable
    ;


maisOuMenos 
    : maisOuMenos PLUS multOuDiv  # Soma
    | maisOuMenos MINUS multOuDiv # Subtracao
    | multOuDiv                   # MutiplicaOuDivide
    ;

multOuDiv
    : multOuDiv MULT exponencial # Multiplicacao
    | multOuDiv DIV exponencial  # Divisao
    | exponencial                # toExp
    ;

exponencial
    : unaryMinus (EXP exponencial)? # Exp
    ;

unaryMinus
    : MINUS unaryMinus # MudancaDeSinal
    | atom             # ToAtom
    ;

atom
    : PI                    # ConstantePI
    | E                     # ConstanteE
    | DOUBLE                # Double
    | INT                   # Int
    | VARIAVEL              # Variavel
    | LPAR maisOuMenos RPAR # Parenteses
    ;
