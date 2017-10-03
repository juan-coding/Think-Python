import turtle

#turtle.Turtle create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()

print(bob)


def polygon(t, length, n):
	angle = 360
	for i in range(n):
		t.fd(length)
		t.lt(angle)

polygon(bob,100,6) # try n = 6, .... 

turtle.mainloop()


