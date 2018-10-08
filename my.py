#program for writing H
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_eight(f):
    do_four(f)
    do_four(f)

def asterisk():
    print('++++',end='')

def asterisk2():
    do_twice(asterisk)
    
def star():
    do_twice(asterisk2)
    print(' ')
def stars():
    do_twice(star)
    
def print_line():
    print('++++')

def print_lines():
    do_eight(print_line)

def blank():
    print('+       ',end=' ')

def blanks():
    do_four(blank)
    print('')
def blanka():
    do_twice(blanks)
    
def grid():
    print_lines()
    blanks()
    print_lines()
def L():
    print_lines()
    stars()
    print_lines()

L()
