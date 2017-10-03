def factorial_checkType(n):
	'''To avoid infite recursion, we check the type of function's argument to avoid infinite recursion'''
	if not isinstance(n, int): 
		print("factorial is only defined for integers.")
		return  
	elif n < 0:
		print("Factorial is not defined for negative integers")
	elif n == 0:
		return 1
	else:
		return n * factorial_checkType(n-1)



factorial_checkType(8.9)