from sys import argv
#import an argument variable

script, filename = argv
#assigns filename as the argument variable

txt = open(filename)
#opens the argument variable
#or does it define the txt function?

print "Here's your file %r:" % filename
#prints a message with a raw variable and pulls in the assigned argument variable

print txt.read()
#prints the imported script

print "Type the filename again:"
#prints a message

file_again = raw_input("> ")
#a prompt to input 

txt_again = open(file_again)
#

print txt_again.read()
#