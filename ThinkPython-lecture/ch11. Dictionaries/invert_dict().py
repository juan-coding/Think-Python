def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


def invert_dict(d):
	'''invert dict: mapping from frequencies to letters'''
	inverse = dict()
	for k in d:
		v = d[k]
		if v not in inverse:
			inverse[v] = [k]
		else:
			inverse[v].append(k)
	return inverse




hist = histogram('parrot')
result = invert_dict(hist)
print(result)

''' output:
{1: ['p', 'a', 'o', 't'], 2: ['r']}
'''		


