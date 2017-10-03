fin = open('words.txt')
print(fin.readline())
print(fin.readline())
print(fin.readline())

''' 
aa

aah

aahed
'''

for line in fin:
	word = line.strip()
	print(word)

	