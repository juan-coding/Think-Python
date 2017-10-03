
# choose an appropriate value of n depending on circumference 

import turtle
import math

#turtle.Turtle create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()

print(bob)


def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

# length * n = circumference = 2*pi*r
def circle(t, r):
	circumference = 2*math.pi*r
	n = int(circumference/3)+1  # from Think Python
	length = circumference/n
	polygon(t,length, n)


circle(bob,100)

turtle.mainloop()

