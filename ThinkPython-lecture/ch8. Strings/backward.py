def backword(s):
	''' take a stirng as an arg and displays letters backword'''
	length = len(s)
	for i in range(length):
		print(s[length-1-i])

backword("Python")

'''
n
o
h
t
y
P
'''