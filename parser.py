import pathlib
import ply.yacc as yacc
import ply.lex as lex

predecende = (
    ('right', 'IF', 'WHILE'),
    ('left', 'ASSIGN'),
    ('left', 'AND', 'OR'),
    ('left', 'GREATER_THAN', 'LESS_THAN', 'EQUALS_TO', 'DIFF_THAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIP', 'DIVIDE'),
    ('left', 'L_PARENTHESIS', 'R_PARENTHESIS')
)

cuadruplos = []
cuadruplos.append(["goto","main","",""])
contador = 0

# Lexico
reservadas = [
    'PROGRAM',
    'VAR',
    'ID',
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
    'BINS',
    'EDGECOLOR',
    'PLT',
    'XLABEL',
    'YLABEL',
    'TITLE',
    'SHOW',
    'BEGIN',
    'ENDFUN'
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

t_ignore = ' \t\n'

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


def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON block
    '''

def p_block(p):
    '''
    block : VAR declarations functions
          | functions
    '''

def p_declarations(p):
    '''
    declarations : INT id_list SEMICOLON declarations
                 | empty
    '''

def p_id_list(p):
    '''
    id_list : ID COMMA id_list
            | ID
    '''

def p_functions(p):
    '''
    functions : VOID function LP params RP compound_statement functions
              | INT function LP params RP compound_statement functions
              | empty
    '''

def p_function(p):
    '''
    function : ID
             | ID ASSIGN expression
    '''

def p_params(p):
    '''
    params : INT ID COMMA params
           | INT ID
           | empty
    '''

def p_compound_statement(p):
    '''
    compound_statement : LL statements RL
    '''

def p_statements(p):
    '''
    statements : statement SEMICOLON statements
               | empty
    '''

def p_statement(p):
    '''
    statement : assignment_statement
              | if_statement
              | for_statement
              | print_statement
              | return_statement
              | function_call
    '''

def p_assignment_statement(p):
    '''
    assignment_statement : ID ASSIGN expression
    '''

def p_if_statement(p):
    '''
    if_statement : IF LP condition RP compound_statement
                | IF LP condition RP compound_statement ELSE compound_statement
    '''

def p_for_statement(p):
    '''
    for_statement : FOR LP assignment_statement SEMICOLON condition SEMICOLON assignment_statement RP compound_statement
    '''

def p_print_statement(p):
    '''
    print_statement : PRINT LP expression RP
    '''

def p_return_statement(p):
    '''
    return_statement : RETURN expression
    '''

def p_function_call(p):
    '''
    function_call : ID LP arguments RP
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

def p_expression(p):
    '''
    expression : term PLUS expression
               | term MINUS expression
               | term
    '''

def p_term(p):
    '''
    term : factor MULT term
         | factor DIV term
         | factor
    '''

def p_factor(p):
    '''
    factor : CONST_INT
           | CONST_FLOAT
           | ID
           | LP expression RP
    '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at {p.value}")

# Construcción del parser
parser = yacc.yacc()

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