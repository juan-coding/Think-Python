# https://docs.python.org/3/library/turtle.html

from turtle import *
bob = turtle.Turtle()

bob.color('red', 'yellow')
bob.begin_fill()
while True:
    bob.forward(200)
    bob.left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()