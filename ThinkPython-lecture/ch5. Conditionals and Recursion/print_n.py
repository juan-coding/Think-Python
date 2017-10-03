def print_n(s,n):
	''' def a recursive function to print a string n times'''
	if(n <= 0):
		return 
	else:
		print(s)
		print_string(s, n-1)

print_string("hello", 3)



