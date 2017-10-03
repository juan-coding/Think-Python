# Option 1: 
def draw_grid1():
	print("+","-","-","-","-","+","-","-","-","-","+")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("+","-","-","-","-","+","-","-","-","-","+")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("|", " "," "," "," ","|", " "," "," "," ","|")
	print("+","-","-","-","-","+","-","-","-","-","+")

draw_grid1()



# Option 2: using functions
# version 1

def do_twice(func, arg):
	func(arg)
	func(arg)

def print_twice(bruce):
	print(bruce)
	print(bruce)


def draw_grid2():
	print("+",do_twice(print_twice,"-"),"+")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("+",do_twice(print_twice,"-"),"+")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")

print('')	
draw_grid1()


# version 2 (code in version 1 not concise)
def row1():
	print("+",do_twice(print_twice,"-"),"+")

def row2():
	print("|",do_twice(print_twice," "),"|",do_twice(print_twice," "),"|")

print('')
row1()

'''
row2()
row2()
row2()
row2()
row1()
row2()
row2()
row2()
row2()
'''
