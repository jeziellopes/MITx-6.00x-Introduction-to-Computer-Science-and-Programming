import random
def dist1():
    return random.randrange(1) * 2 - 1

def dist2():
    if random.randrange(1) > 0.5:
        return random.randrange(1)
    else:
        return random.randrange(1) - 1

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)
