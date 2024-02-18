import random
def genEven():
    '''
    Generates a random number x, where 0 <= x < 100
    '''
    rNum = random.randint(0, 99)
    while rNum%2!=0:
        return genEven()
    return rNum


"""while True:
    even = genEven()
    print even
    if even%2!=0:
        print 'ERRADO'
        break"""

def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    rNum = random.randint(9, 20)
    while rNum!=12:
        return deterministicNumber()
    return rNum

def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    return 12

"""while True:
    even = deterministicNumber()
    print even
    if even%2!=0:
        print 'ERRADO'
        break"""



import random
def stochasticNumber():
    '''
    Stochastically generates a uniformly distributed even number between 9 and 21
    '''
    # Your code here

    return 2 * random.randrange(5, 11)

while True:
    even = stochasticNumber()
    print even
    if even%2!=0:
        print 'ERRADO'
        break



    
