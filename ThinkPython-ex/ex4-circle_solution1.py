# set n = 100 

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
	polygon(t,(2*math.pi*r)/100, 100)

circle(bob,100)

turtle.mainloop()

