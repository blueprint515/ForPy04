from sys import argv

script, user_name = argv
prompts = 'Great '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompts)

print "Where do you live %s?" % user_name
lives = raw_input(prompts)

print "What kind of computer do you have?"
computer = raw_input(prompts)

print "Which film do you like?"
film = raw_input(prompts)

print "What flower do you like?"
flower = raw_input(prompts)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure whether that is.
And you have a %r computer.
You like the film of %r.
You said you love %r.
""" % (likes, lives, computer, film, flower)