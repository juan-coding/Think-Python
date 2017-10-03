
def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


def print_hist(h):
     ''' To traverse the keys'''
     for c in h:
     	print(c, h[c])


def print_sorted_hist(h):
	''' To traverse the keys in sorted order '''
	for c in sorted(h):
		print(c, h[c])


h = histogram("parrot")
print_hist(h)
print('')
print_sorted_hist(h)

''' output: 
p 1
a 1
r 2
o 1
t 1

a 1
o 1
p 1
r 2
t 1
'''