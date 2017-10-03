''' Use while loop to write a traversal'''

fruit = 'banana'

print("Using while loop to write a traversal")
index = 0
while(index < len(fruit)):
	print(fruit[index])
	index = index + 1

print('')
print("Using a for loop to write a traversal")
for letter in fruit:
	print(letter)

print('')
print("Another for loop version")
for i in range(len(fruit)):
	print(fruit[i])