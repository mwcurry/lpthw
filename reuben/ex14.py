from sys import argv

script, user_name = argv
prompt = '-'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Which program are you using to code?"
software = raw_input(prompt)

print "Alright, so you said %r about liking me.\nYou live in %r.  Not sure where that is.\nAnd you have a %r computer." % (likes, lives, computer)
#instead of using the triple quotation and return, I used the \n line break.
print "You currently use %r to program.  Nice." % software