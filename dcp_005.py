'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)
Implement car and cdr.
'''

def cons(a, b):
    return lambda f : f(a, b)
	
	
def car(pair):
    # return pair[0]
	first = lambda x, y: x
	return pair(first)
	
def cdr(pair):
    # return pair[1]
	last = lambda x, y: y
	return pair(last)
	

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4