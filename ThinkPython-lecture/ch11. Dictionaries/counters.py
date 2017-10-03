def histogram(s):
	''' count how many times each letter appear in string s'''
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] = d[c] + 1
	return d



def histogram_(s):
	''' using get() to write concise code: get(key, default) return values 
	of the key (return default in case key does not exist)'''
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d



''' test functions: '''
h = histogram("brontosaurus")
h_ = histogram_('brontosaurus')
print(h)
print(h_)
print(h == h_)

''' output:
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
True
'''