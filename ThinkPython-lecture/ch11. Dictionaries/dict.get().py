'''
get(key,default) 
key -- The Key to be searched in the dictonary
default -- The value to be returned in case key does not exist
'''

counts = {"chuck":1,"annie":42,"jan":100}

print(counts.get("jan",0))
print(counts)

item = counts.get("lala")
print(item)
if not item:
	print ("sorry, not lala")

