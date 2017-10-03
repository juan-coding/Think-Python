''' return values'''

def compare(x, y):
	if(x > y):
		return 1
	elif(x == y):
		0
	elif(x < y):
		-1

x = input()
y = input()

x = int(x)
y = int(y)

compare(x,y)

