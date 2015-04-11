X = 200.0
max_occupancy = 650
tenants = 575
excess_capacity = max_occupancy - tenants
average_occupancy = tenants / apartments
average_occupancy2 = tenants / X


print "There are", tenants, "people living here."
print "There are", apartments, "units in this building."
print "There is room for", excess_capacity, "more people."
print "The building has on average", average_occupancy, "per apartment."
print "The building has on average", average_occupancy2, "per apartment."
