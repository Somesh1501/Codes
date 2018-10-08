#program for writing F


def do_twice(f):
    f()
    f()

def do_four():
    do_twice()
    do_twice()

def do_eight():
    do_four()
    do_four()

def print_beam():
    print('@@@@',end='')

def print_beams():
    do_twice(print_beam)
    print('')

def pri():
    print('@@@@')

def prit():
    do_twice(pri)
    
def oc():
    do_twice(print_beams)
    prit()
def os():
    do_twice(oc)

os()

