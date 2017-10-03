import math

''' Understanding the problem''' 
z**2 = x**2 + y**2

''' A simple and workable function'''
def hypotenuse(x, y):
	return 0.0


''' store values in temporary variables''' 
def hypotenuse(x, y):
	hsquared = x**2 + y**2
	print("hypotenuse squared: ", hsquared) 


''' test function'''
hypotenuse(3,4)


''' adding code to the function body'''
def hypotenuse(x,y):
		hsquared = x**2 + y**2
		return math.sqrt(hsquared)

hypotenuse(3, 4)


