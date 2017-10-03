def find(word, letter):
	''' find() is the inverse of the [] operator: searching function'''
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1 


def find(w, c, index):
	''' modify find() to allow additional argument: 
	the index in word where it should start looking'''
	index = index
	while index < len(w):
		if word[index] == c:
			return index
		index = index + 1
	return -1 


result = find("hellow", 'w', 2)
print(result)
