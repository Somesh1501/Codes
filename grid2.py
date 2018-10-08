#grid 1
def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)
def do_three(a,b):
    print(a)
    do_four(b)
    print(a)
def print_line():
    print('+ - - - -',end='  ')
def print_bar():
    print('|             ',end=' ')
def print_lines():
    do_twice(print_line)
    print('+')
def print_bars():
    do_twice(print_bar)
    print('|')
def print_row():
    print_lines()
    do_four(print_bars)
def grid():
    print_row()
    print_row()
    print_lines()

#grid 4X4
def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()
