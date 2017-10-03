import turtle

#turtle.Turtle create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()

print(bob)

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

square(bob, 100)

#to prevent window dispear after drawing a square
turtle.mainloop()