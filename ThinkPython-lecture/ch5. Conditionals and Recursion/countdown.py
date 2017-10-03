def countdown(n):
	''' use recursion'''
	if(n<=0):
		print("Blastoff!")
	else:
		print(n)
		countdown(n-1)

countdown(6)
