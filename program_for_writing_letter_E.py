#program for writing letter E
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_eight():
    do_four()
    do_four()

def print_beam():
    print('++++++',end='')
def print_p():
    print('++++')
  
def print_bba():
    do_twice(print_p)

def print_beams():
    do_twice(print_beam)
    print('')
def print_bams():
    do_twice(print_beams)

def L():
    print_bams()
    print_bba()
    
def M():
    do_twice(L)
    print_bams()

M()
