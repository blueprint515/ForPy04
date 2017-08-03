x = "There are %d types of people." % 10 # define variable x
binary = "binary" # define binary
do_not = "don't" # define do_not
# y is defined by two variables above
y = "Those who know %s and those who %s." % (binary, do_not) 

print x # print x
print y # print y

print 'I said: %r.' % x # print this sentence
print 'I also said: "%s".' % y # print this sentence

hilarious = True # define hilarious
joke_evaluation = "Isn't that joke so funny?! %r" # define jove_evaluation

print joke_evaluation % hilarious # print variables

w = "This is the left side of..." # define w
e = "a string with a right side." # define e

print w + e # print w + e