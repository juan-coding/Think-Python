word = 'banana'
counter = 0
index = 0
for letter in word:
	if letter == 'a':
		counter = counter + 1
print(counter)



def counter(w, c, index):
	counter = 0
	index = index
	for letter in w:
		if letter == c:
			counter = counter + 1
	print(counter)

print('')
counter('apple', 'a', 0)


