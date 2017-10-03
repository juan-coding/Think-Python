'''
number of variables must be same on the left and right side :
a, b = b, a
a, b, c = b, a, c
... 

right side can be any kind of seq (string, list, tuple, etc.)
'''

a = [1, 2]
b = ['a', 'b']
a, b = b, a


addr = 'monty@python.org'
uname, domain =addr.split('@')
print(uname,'\n',domain)



