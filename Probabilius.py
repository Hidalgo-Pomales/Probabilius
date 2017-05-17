# -----------------------------------------------------------------------------
# ProbabiliusUtils.py
#
# Probabilius is a programing language to solve basic probability
# and statistics problems.
# -----------------------------------------------------------------------------

import ProbabiliusUtils as Utils


# Reserved Words
reserved = {
    'avg': 'AVG',
    'permu': 'PERMU',
    'combi': 'COMBI',
    'mode' : 'MODE',
    'median':'MEDIAN',
    'trim':'TRIM',
    'union': 'UNION',
    'inter': 'INTER',
    'complem': 'COMPLEM',
    'varian': 'VARIAN',
    'stddev': 'STDDEV',
    'cirper': 'CIRPER',
    'partial': 'PARTIAL',
    'range': 'RANGE',
    'totalPer': 'TOTALPER',
    'combination': 'COMBINATION'
}

# Tokens
tokens = [
             'LIST', 'LISTCHAR','ID', 'NUMBER',
             'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
             'LPAREN', 'RPAREN', 'COMMA'
         ] + list(reserved.values())

# Simple Regular Expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'


# List Regular Expression
def t_LIST(t):
    r'[(][-?0-9,]+[-?0-9][)]'
    t.type = 'LIST'
    return t

# List Regular Expression
def t_LIST2(t):
    r'[(][\'a-zA-z\'][,\'a-zA-Z\']*[)]'
    t.type = 'LISTCHAR'
    return t


#
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_average(t):
    'statement : AVG LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
       print("Average: ",Utils.calculateAverage(numbers))
    except ValueError:
        print("Enter numbers!")


def p_statement_permuCHAR(t):
    'statement : PERMU LPAREN LISTCHAR RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of string without the ""
    tempList=[]
    for x in numbers:
        tempList.append(str(x).replace("\'",""))
    try:
        print("Permutations: ", (Utils.calculatePermutations(tempList)))
    except ValueError:
        print("Enter numbers!")

def p_statement_permu(t):
    'statement : PERMU LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Permutations: ", Utils.calculatePermutations(numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_totalPer(t):
    'statement : TOTALPER LPAREN NUMBER RPAREN'
    number = t[3]

    try:
        print("Permutations: ", Utils.calculateNumberOfPermutations(number))

    except ValueError:
        print("Enter numbers!")

def p_statement_cirper(t):
    'statement : CIRPER LPAREN NUMBER RPAREN'
    numbers = t[3]
    # Convert the list into an actual list of ints
    try:
        print("Number Circular Permutations: ", Utils.calculateCircularPermutations(numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_combi(t):
    'statement : COMBI LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Combinations: ", Utils.calculateCombinations(numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_combiCHAR(t):
    'statement : COMBI LPAREN LISTCHAR RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of string without the ""
    tempList=[]
    for x in numbers:
        tempList.append(str(x).replace("\'",""))
    try:
        print("Combinations: ", (Utils.calculateCombinations(tempList)))
    except ValueError:
        print("Enter numbers!")

def p_statement_combination(t):
    'statement : COMBINATION LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Combinations: ", Utils.calculateNumberOfCombinations(numbers))
    except ValueError:
        print("Enter n followed by k")

def p_statement_mode(t):
    'statement : MODE LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Mode: ", Utils.calculateMode(numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_median(t):
    'statement : MEDIAN LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Median: ", Utils.calculateMedian(numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_trimmedmean(t):
    'statement : TRIM LPAREN NUMBER COMMA LIST RPAREN'
    percent = t[3]
    numbers = t[5][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Trimmed Mean: ", Utils.calculateTrimmedMean(percent, numbers))

    except ValueError:
        print("Enter numbers!")

def p_statement_union(t):
    'statement : UNION LPAREN LIST COMMA LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    numbers2 =t[5][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    # Convert the list into an actual list of ints
    numbers2 = list(map(int, numbers2))
    try:
        print("UNION: ", Utils.calculateUnion(numbers,numbers2))

    except ValueError:
        print("Enter numbers!")

def p_statement_intersection(t):
    'statement : INTER LPAREN LIST COMMA LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    numbers2 =t[5][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    # Convert the list into an actual list of ints
    numbers2 = list(map(int, numbers2))
    try:
        print("Intersection: ", Utils.calculateIntersection(numbers,numbers2))

    except ValueError:
        print("Enter numbers!")


def p_statement_complement(t):
    'statement : COMPLEM LPAREN LIST COMMA LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    numbers2 =t[5][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    # Convert the list into an actual list of ints
    numbers2 = list(map(int, numbers2))
    try:
        print("Complement: ", Utils.calculateComplement(numbers,numbers2))

    except ValueError:
        print("Enter numbers!")

def p_statement_varian(t):
    'statement : VARIAN LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Variance: ", Utils.calculateVariance(numbers))
    except ValueError:
        print("Enter numbers!")

def p_statement_stddev(t):
    'statement : STDDEV LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Standard Deviation: ", Utils.calculateStandardDeviation(numbers))
    except ValueError:
        print("Enter numbers!")

def p_statement_assign(t):
    'statement : ID EQUALS expression'
    names[t[1]] = t[3]

    for x in t:
        print(x)
    print(names)


def p_statement_expr(t):
    'statement : expression'
    print(t[1])


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_list(t):
    'expression : LIST'
    t[0] = t[1]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_name(t):
    'expression : ID'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


def p_error(t):
    print("Syntax error at '%s'" % t.value)

def p_statement_partial(t):
    'statement : PARTIAL LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Number Partial Permutations: ", Utils.calculatePartialPermutations(numbers))
    except ValueError:
        print("Enter n followed by k")

def p_statement_range(t):
    'statement : RANGE LPAREN LIST RPAREN'
    numbers = t[3][1:-1].split(',')
    # Convert the list into an actual list of ints
    numbers = list(map(int, numbers))
    try:
        print("Range: ", Utils.CalculateRange(numbers))
    except ValueError:
        print("Enter numbers!")

import ply.yacc as yacc

parser = yacc.yacc()

while True:
    try:
        s = input('Probabilius > ')  # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)