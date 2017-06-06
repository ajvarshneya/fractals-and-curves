#
# utilities.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#

# These functions do math with tuples.
def tuple_add(tuple1, tuple2):
	add = lambda x,y: x + y
	return map(add, tuple1, tuple2)

def tuple_sub(tuple1, tuple2):
	sub = lambda x,y: x - y
	return map(sub, tuple1, tuple2)

def tuple_mul(tuple1, scale):
	mul = lambda x: x * scale
	return map(mul, tuple1)

def tuple_div(tuple1, scale):
	div = lambda x: x / scale
	return map(div, tuple1)

