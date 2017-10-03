

''' syntax same as for strings: using for loop'''
cheeses = ['Cheddar', 'Edam', 'Gouda', 'Holland']
for cheese in cheeses:
	print(cheese)


''' to write or update the elements, you need the indices'''
numbers = [42, 123]
for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2



''' A for loop over an empty list never runs the body '''
for x in []:
	print('This never happens')



