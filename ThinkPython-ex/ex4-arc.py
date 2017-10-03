import turtle
import math

#turtle.Turtle create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()

print(bob)


# length * n = circumference = 2*pi*r

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def arc(t, r, angle):
	circumfence = 2*math.pi*r
	arc_length = circumfence*angle/360
	n = int(arc_length/3)+1
	step_length = arc_length/n
	step_angle = angle/n
	polyline(t, n, step_length, step_angle)


arc(bob,100,90)

turtle.mainloop()

