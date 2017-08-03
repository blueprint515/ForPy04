name = 'Zed A. Shaw'
age = 35 # not a lie
height = 170 # cm
weight = 70 # kilo
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %r." % name
print "He's %r cm tall." % height
print "He's %r kilos heavy" % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % ( age, height, weight, 
    age + height + weight)