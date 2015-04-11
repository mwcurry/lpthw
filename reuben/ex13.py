from sys import argv

script, first, second, third = argv

#These inputs allow you to select the variable names rather than assign

script = raw_input("what is your script called? ")
first = raw_input("What will be your first variable? ")
second = raw_input("What will your second variable be? ")
third = raw_input ("What will your last variable be? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third