'''recursion'''



def fibonacci_seq(n):
	''' print out the fib sequence of n elements'''
	if n == 0:
		print(0)
		return 0
	elif n == 1:
		print(1)
		return 1
	else:
		print(n)
		return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci_seq(5)
print(result)