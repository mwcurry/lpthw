#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r \narg2: %r \n" % (arg1, arg2)

#okay, that *args is actually pointless, let's simplify
def print_two_again(arg1, arg2):
	print "arg1: %r \narg2: %r \n" % (arg1, arg2)

#take one arg
def print_one(arg1):
	print "arg1: %r \n" % arg1

#take no args
def print_none():
	print "Nutttttin \n"

print_two("Matt", "Curry")
print_two_again("Matt", "Curry2")
print_one("One!")
print_none()