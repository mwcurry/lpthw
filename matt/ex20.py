from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "Whole file:\n"

print_all(current_file)

print "Now let's rewind!\n"

rewind(current_file)

print "Let's print three lines:\n"
'''
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
'''

def print_lines(n_to_print):
	for x in range(0, n_to_print):
		print_a_line(x, current_file)

print_lines(3)