name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 # inches
weight = 180.00 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_kg = weight / 2.20
height_m = height * 2.540

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % height_m
print "He's %d pounds heavy." % weight
print "He's %d kilos heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are actually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)