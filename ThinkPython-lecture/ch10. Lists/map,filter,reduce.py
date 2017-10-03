
'''
Operations:
Reduce (i.e. add_all()):
An operation combining a sequence of elements into a single value 

Map (i.e. capitalize_all()) 
It 'maps' a funciton onto each of the elements in a sequence. (

Filter(i.e., only_upper())
Select some of the elements from a list and return a sublist
'''


def add_all(t):
	''' to add all the numbers in the lsit t'''
	total = 0
	for x in t:
		total = total + x
	return total
''' total varibale used in this way sometimes called : 'accumulator' ''' 

sum(t) 
''' built-in function''' 




def capitalize_all(t):
	''' take a list of strings and returns a new list containisng capitalized strings'''
	res = []
	for s in t:
		res.append(s.capitalize())
	return res




def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res




