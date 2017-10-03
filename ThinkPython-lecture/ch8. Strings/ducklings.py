prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	print(letter + suffix)

''' incorrect output
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
'''


''' To fix the code to have Ouack, Quack'''
print('')
for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print(letter + 'u' + suffix)
	else:
		print(letter + suffix)
	
''' Correct output
Jack
Kack
Lack
Mack
Nack
Ouack
Pack
Quack
'''
