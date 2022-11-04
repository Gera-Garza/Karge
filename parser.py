import ply.yacc as yacc
from lexico import tokens,lexer

predecende = (
    ('right', 'IF', 'WHILE'),
    ('left', 'ASSIGN'),
    ('left', 'AND', 'OR'),
    ('left', 'GREATER_THAN', 'LESS_THAN', 'EQUALS_TO', 'DIFF_THAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIP', 'DIVIDE'),
    ('left', 'L_PARENTHESIS', 'R_PARENTHESIS')
)


def t_program(t):
    '''
    programA : vars  programB
             | programB

    programB : function programB
             | main
    '''


def t_program_error(t):
    '''program : error'''
    t[0] = None
    t.parser.error = 1


def t_vars(t):
    '''
     vars : VARS L_BRACKET  varsB R_BRACKET

     varsB : varsC
           | varsC COMMA varsC

     varsC : ID np_add_var
           | ID L_BRACKET  CTE_INT R_BRACKET
     '''



def t_tipo(t):
    '''
    type : INT
          | FLOAT
          | BOOL
    '''
    t[0] = t[1]


def t_params(t):
    '''
    params : type  ID
           | type  ID  COMMA params
           | empty
    '''


def t_block(t):
    '''
    block : L_BRACE blockB R_BRACE

    blockB : statement blockB
           | empty
    '''


def t_vblock(t):
    '''
    vblock : L_PARENTHESIS vars vblockB R_PARENTHESIS
           | block

    vblockB : statement vblockB
            | empty
    '''

def p_statement(p):
    '''
    statement : assign
           | condicional
           | read
           | write
           | loop_cond
           | loop_range
           | return
           | void_func
    '''

def t_exp(t):
    '''
    exp : op expB

    expB : OR exp
          | AND exp
          | empty
    '''


def t_Op(t):
    '''
 op : exp op2

 op2 : LESS exp
      | GREATER_THAN exp
      | LESS_THAN exp
      | GREATER_THAN exp
      | EQUALS_TO  exp
      | DIFF_THAN exp
      | empty
 '''


def t_condicional(t):
    '''
    condicional : IF L_PARENTHESIS statement R_PARENTHESIS

    cond2 : ELSE block
          | empty
    '''


def t_assign(t):
    '''
    assign : var oper_assign exp SEMICOLON
    '''


def t_oper_bool(t):
    '''
    oper_bool :
        MULT
        | DIV
        | PLUS
        | MINUS
    '''
    t[0] = t[1]

def t_letrero(t):
    '''
    letrero : print L_PARENTHESIS LETRERO R_PARENTHESIS
    '''

def t_var_cte(t):
    '''
    var_cte : var
         | CTE_INT
         | CTE_FLOAT
    '''
    t[0] = t[1]

# Temporal se cambiara despues por uno adecuado


def p_loop_cond(p):
    '''
    loop_cond : WHILE L_PARENTHESIS  expression R_PARENTHESIS  block
    '''


def p_loop_range(p):
    '''
    loop_range : FOR var EQUAL  exp TO exp block
    '''


parser = yacc.yacc()


if __name__ == '__main__':
    try:
        file = open(sys.argv[1], 'r')
        code = ''
        for line in file:
            code += line
        parser.parse(code)

    except EOFError:
        raise SyntaxError('EOF Error')
