
def check_fermat(a, b, c, n):
	if(n > 2 and a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong")
	print("No, that doesn't work")


a = input()
b = input()
c = input()
n = input()

a = int(a)
b = int(b)
c = int(c)
n = int(n)


check_fermat(a, b, c, n)
