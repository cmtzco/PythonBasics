# lol at the joke
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y 

print "I said: %r." % x # %r gives you a string in single quotes
print "I also said: '%s'." % y # %s gives you the string without the single quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
