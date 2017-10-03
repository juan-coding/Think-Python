
def square_root(x, a):
	''' use Newton method to compute square root of a
	given any initial value x. '''
	while True:
		print(x)
		y = (x + a/x) / 2
		if y == x:
			break
		x = y
	return y


result = square_root(8,4)
print('')
print(result)



