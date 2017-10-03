''' most list methods are void: they modify the list and return None.
t = t.sort()  incorrect'''

t = ['e','a', 'b', 'c']
print(t)

t.append('d')
print(t)

t.sort()
print(t)

'''
['e', 'a', 'b', 'c']
['e', 'a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'e']
'''