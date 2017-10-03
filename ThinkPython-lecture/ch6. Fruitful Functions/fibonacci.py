'''
0 1 1 2 3 5 8 13 21 34 55...
f(0) = 0
f(1) = 1

or 
1 1 2 3 5 8 13 21 34 55 89...
f(1) = 1
f(2) = 1
'''


def fibonacci(n):
	''' compute the nth element'''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(5)
print(result)