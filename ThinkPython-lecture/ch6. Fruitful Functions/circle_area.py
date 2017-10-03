import math

''' FUnction: 
Given center of circle point and the perimeter point:
xc, yc: center point
xp, yp: perimeter point
, compute circle area
'''




def area(radius):
	a = math.pi * (radius**2)
	return a 

def  distance(xc, yc, xp, yp):
	dx = xc - xp
	dy = yc - yp
	dxsquared = dx**2
	dysquared = dy**2
	radius = math.sqrt(dxsquared, dysquared)
	return radius

def circle_area(xc, yc, xp, yp):

	radius = distance(xc, yc, xp, yp)
	circle_area = area(radius)
	return circle_area

''' A concise version'''
def circle_area2(xc, yc, xp, yp):
	return area(distance(xc, yc, xp, yp))


