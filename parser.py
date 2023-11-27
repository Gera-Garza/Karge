import pathlib
import sys

import ply.yacc as yacc
import ply.lex as lex
from DirFunciones import DirFunciones
from TablaVars import TablaVars

predecende = (
    ('right', 'IF', 'WHILE'),
    ('left', 'ASSIGN'),
    ('left', 'AND', 'OR'),
    ('left', 'GREATER_THAN', 'LESS_THAN', 'EQUALS_TO', 'DIFF_THAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIP', 'DIVIDE'),
    ('left', 'L_PARENTHESIS', 'R_PARENTHESIS')
)

# Lexico
reservadas = [
    'PROGRAM',
    'VAR',
    'INT',
    'FLOAT',
    'CHAR',
    'IF',
    'ELSE',
    'READ',
    'PRINT',
    'VOID',
    'RETURN',
    'FOR',
    'WHILE',
    'AVG',
    'MEDIAN',
    'MODE',
    'MAX',
    'MIN',
    'STDEV',
    'HIST',
    'COLOR',
    'MAIN',
    'BINS',
    'EDGECOLOR',
    'PLT',
    'XLABEL',
    'YLABEL',
    'TITLE',
    'SHOW'
]
tokens = reservadas + [

    # ; { } , = ( ) [ ]
    'SEMICOLON', 'LL', 'RL',
    'COMMA', 'ASSIGN', 'LP', 'RP',
    'LB', 'RB',

    # operators + - * /
    'PLUS', 'MINUS', 'MULT', 'DIV',

    # bool > < != == && ||
    'GREATER_THAN', 'LESS_THAN', 'DIFF_THAN',
    'EQUALS_TO', 'AND', 'OR',

    # Constants
    'CONST_ID', 'CONST_INT', 'CONST_FLOAT', 'CONST_CHAR', 'LETRERO'
]


# bool > < != == && ||
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_DIFF_THAN = r'!='
t_ASSIGN = r'='
t_EQUALS_TO = r'=='
t_AND = r'&&'
t_OR = r'\|\|'

# Operators + - * /
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'

# ;  { } , = ( ) [ ]
t_SEMICOLON = r';'
t_LL = r'{'
t_RL = r'}'
t_COMMA = r','
t_LB = r'\['
t_RB = r'\]'
t_LP = r'\('
t_RP = r'\)'

t_ignore = ' \t'

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_LETRERO(t):
    r'\"[a-zA-Z_][a-zA-z0-9_ ]*\"'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_CONST_FLOAT(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t

def t_CONST_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CONST_ID(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_error(t):
    print("caracter ilegal''%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
###########################################################
# empieza el parser
###########################################################
dirFun = DirFunciones()
tabVar = TablaVars()
cont = 0
cuadruplos = []
cuadruplos.append(["goto","main","",""])
temp=["t1","t2","t3","t4","t5","t6","t7",'t8']
psaltos = []
last_Type = None
def p_program(p):
    '''
    program : PROGRAM CONST_ID program2
    '''

def p_program2(p):
    '''
    program2 : varBlock program3 mainBlock
    '''

def p_program3(p):
    '''
    program3 : functionBlock program3
            | empty
    '''

def p_varBlock(p):
    '''
    varBlock : VAR LL var2 RL
        | empty
    '''

def p_var2(p):
    '''
    var2 : typeBlock CONST_ID var3 SEMICOLON var4
    '''
    tabVar.add_var(p[2],p[1])

def p_var3(p):
    '''
    var3 : COMMA CONST_ID var3
        | empty
    '''
    if len(p) > 2:
        global last_Type
        tabVar.add_var(p[2], last_Type)


def p_var4(p):
    '''
    var4 : var2
        | empty
    '''

def p_typeBlock(p):
    '''
    typeBlock : INT
              | FLOAT
    '''
    global last_Type
    last_Type = p[1]
    p[0] = p[1]


def p_functionBlock(p):
    '''
    functionBlock : typeBlock CONST_ID LP params RP LL codeBlockR RL
                | VOID CONST_ID LP params RP LL codeBlock RL
    '''


def p_params(p):
    '''
    params : typeBlock CONST_ID params2
           | empty
    '''


def p_params2(p):
    '''
     params2 : COMMA params
            | empty
     '''


def p_codeBlock(p):
    '''
     codeBlock :  varBlock statements
                | statements
     '''

def p_codeBlockR(p):
    '''
     codeBlockR :  varBlock statementsR
                | statementsR
     '''


def p_statements(p):
    '''
    statements : statements statement
               | empty
    '''



def p_statementsR(p):
    '''
    statementsR : statementsR statement
                | return_statement
               | empty
    '''


def p_statement(p):
    '''
    statement : assignment_statement
              | if_statement
              | for_statement
              | print_statement
              | function_call
    '''


def p_assignment_statement(p):
    '''
    assignment_statement : CONST_ID ASSIGN expression SEMICOLON
    '''
    global cuadruplos
    cuadruplos = cuadruplos + [("=", p[3], p[1])]


def p_if_statement(p):
    '''
    if_statement : IF LP condition RP LL statements RL
                | IF LP condition RP LL statements RL ELSE LL statements RL
    '''


def p_for_statement(p):
    '''
    for_statement : FOR LP assignment_statement condition SEMICOLON assignment_statement RP LL statements RL
    '''


def p_print_statement(p):
    '''
    print_statement : PRINT LP expression_list RP SEMICOLON
                   | PRINT LP LETRERO RP SEMICOLON
    '''

def p_expression_list(p):
    '''
    expression_list : expression COMMA expression_list
                   | expression
    '''


def p_expression(p):
    '''
    expression : term PLUS expression
               | term MINUS expression
               | term
    '''
    global cont, cuadruplos
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == "+"):
        cuadruplos = cuadruplos + [("+", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1
    else:
        cuadruplos = cuadruplos + [("-", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1


def p_term(p):
    '''
    term : factor MULT term
         | factor DIV term
         | factor
    '''
    global cont, cuadruplos
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == "*"):
        cuadruplos = cuadruplos + [("*", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1
    else:
        cuadruplos = cuadruplos + [("/", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1


def p_factor(p):
    '''
    factor : CONST_INT
           | CONST_FLOAT
           | CONST_ID
           | LP expression RP
           | function_call
    '''
    p[0] = p[1]


def p_return_statement(p):
    '''
    return_statement : RETURN expression SEMICOLON
    '''


def p_function_call(p):
    '''
    function_call : CONST_ID LP arguments RP SEMICOLON
    '''


def p_arguments(p):
    '''
    arguments : expression COMMA arguments
              | expression
              | empty
    '''


def p_condition(p):
    '''
    condition : expression GREATER_THAN expression
              | expression LESS_THAN expression
              | expression DIFF_THAN expression
              | expression EQUALS_TO expression
              | expression AND expression
              | expression OR expression
    '''
    global cont, cuadruplos
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == ">"):
        cuadruplos = cuadruplos + [(">", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1
    elif (p[2] == "<"):
        cuadruplos = cuadruplos + [("<", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1
    elif (p[2] == "=="):
        cuadruplos = cuadruplos + [("==", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1
    else:
        cuadruplos = cuadruplos + [("!=", p[1], p[3], temp[cont])]
        p[0] = temp[cont]
        cont = cont + 1

def p_mainBlock(p):
    '''
    mainBlock : MAIN LP RP LL codeBlock RL
    '''

def p_empty(p):
    'empty :'
    p[0]=None

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}' regla: {p.type}")
    else:
        print("Syntax error: Unexpected end of input")
# Construcción del parser
parser = yacc.yacc(debug=True, module= sys.modules[__name__])

def ejecutar_operacion(operador, operando1, operando2, resultado):
    # Lógica para ejecutar la operación según el cuádruplo
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2
    elif operador == '=':
        print(f'Asignación: {resultado} = {operando1}')
    else:
        print("acabo")

def leer_cuadruplos():
    for cuadruplo in cuadruplos:
        operador, operando1, operando2, resultado = cuadruplo
        resultado_operacion = ejecutar_operacion(operador, operando1, operando2, resultado)
        print(f'Resultado de la operación: {resultado_operacion}')
# Ejemplo de uso
if __name__ == '__main__':
    # Lee el código desde un archivo utilizando pathlib.Path
    file_path = pathlib.Path("test/test1FA.txt")
    if file_path.is_file():
        data = file_path.read_text(encoding="utf-8")

        # Parsea el código
        result = parser.parse(data)
        print("Parsing successful.")
    else:
        print(f"Error: El archivo {file_path} no existe.")
    print(f"estos son los cuadruplos: {cuadruplos}")
    leer_cuadruplos()