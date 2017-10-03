def do_twice(f):
	f()
	f()

def print_spam():
	print("twospam")

do_twice(print_spam)



# modify do_twice
def do_twice1(func, arg):
	func(arg)
	func(arg)

def print_twice(bruce):
	print(bruce)
	print(bruce)
	

# define a new function do_four()
def do_four(func,arg):
	do_twice1(func,arg) 
	do_twice1(func,arg)


# call function
print('')
do_twice1(print_twice,"spam")
print('')
do_four(print_twice, "eightdog")
