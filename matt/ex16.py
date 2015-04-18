#Chapter 16

from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want to erase it, hit RETURN."

raw_input("?")

print "Opening the file. . ."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Please provide me with three lines. \n"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file!"

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

to_write = "%s\n%s\n%s" % (line1, line2, line3)
target.write(to_write)

print "And finally, a close."
target.close()