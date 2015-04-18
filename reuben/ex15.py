from sys import argv
#import an argument variable
#module is pre-existing code

script, filename = argv
#this line creates two variables that will become argv

txt = open(filename)
#defining the variable txt as the result of opening filename
#open is a function - opens whatever you type in the parenthesis

print "Type the filename for the first time:"
#prints a message

file_again = raw_input("> ")
#a prompt to input 

txt_again = open(file_again)
#

print txt_again.read()
#