print("I have {} bags".format(7))

abbr1 = "SCBS {}"
print(abbr1.format("is short for our school name"))

abbr2 = "CIE {} {}"
print(abbr2.format("is short for", "Cambridge International Examinations"))

print("John is a {3} {2}, and {1} {0}!".format("happy", "smiling", "look", "great"))

print("John the {0} {1} a {pr}.".format("shark", "made", pr="pull request"))

print("John the {0} {1} a {john}.".format("shark", "made", john="pull request"))

print("John ate {0:f} percent of a {1}".format(75, "pizza"))

print("John ate {0:.3f} percent of a {1}".format(75, "pizza"))

print("John ate {0:.1f} percent of a {1}".format(75.76596, "pizza"))

print("John ate {0:.0f} percent of a {1}".format(75.76596, "pizza"))

print("Carl has {0:4} red {1:16}!".format(5, "balloons"))

# "*" use star instead of space; "^" align center; "20" 20 reserved spaces; "s" change "Nid" into string
print("{:*^20s}".format("Nid"))

print("{:$>20}".format("Nid"))

print("{:@<20}".format("Nid"))

print("Ian ate {0:5.0f} percent of a {1}".format(75.76596, "pizza"))

carl = "Carl has {} balloons today"
nballnoon = 8
print(carl.format(nballnoon))

print("{:>3s} {:>4s} {:>5s}".format("i", "i^2", "i^3"))
for i in range(3, 13):
    print("{:3d} {:4d} {:5d}".format(i, i**2, i**3))
