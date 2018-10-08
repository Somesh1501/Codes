def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_eight(f):
    do_four(f)
    do_four(f)

def print_beam():
    print('+----+----',end=' ')

def print_bar():
    print('+         ',end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')
    
def print_bars():
    do_four(print_bar)
    print(' ')
    
def print_row():
    print_beams()
    
def print_column():
    do_four(print_bars)

def grid():
    print_row()
    print_column()
    print_row()

grid()
