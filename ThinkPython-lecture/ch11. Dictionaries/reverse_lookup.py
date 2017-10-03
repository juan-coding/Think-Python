def reverse_lookup(d, v):
	''' Find key via its value'''
	for k in d:
		if d[k] == v:
			return k
	raise LookupError("value does not appear in the dic") # or just raise LookupError() 
	'''a built-in exception''' 




