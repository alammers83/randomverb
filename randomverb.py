def random_verb():

    verb = randint(0,1)

    if verb == 0:
        return 'run'
    else:
        return 'kayak'

print random_verb()
