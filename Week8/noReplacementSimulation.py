import random

def oneTrial():
    balls = ['R', 'R', 'R', 'G', 'G', 'G']
    chosenBalls = []
    for i in range(3):
        ball = random.choice(balls)
        balls.remove(ball)
        chosenBalls.append(ball)
    if (chosenBalls[0]==chosenBalls[1] and chosenBalls[1]==chosenBalls[2]):
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numTrue = 0
    
    for i in range(numTrials):
        if oneTrial():
            numTrue += 1
            
    return float(numTrue)/float(numTrials)

    
#print noReplacementSimulation(10000)


def probFlu1():
    days = []
    flusTimes = 0
    for i in range(30):
        days.append('D')

    for i in range(3):
        days[random.randrange(0,30)] = 'F'
    
    for i in days:
        if i == 'F':
            flusTimes += 1
    return flusTimes/30.0
    
#print probFlu()

def getDay1(daysList):
    return random.choice(daysList)


def probFlu1():
    flu = 0
    daysList = 'F F F D D D D D D D D D D D D D D D D D D D D D D D D D D D'.split(' ')
    for i in range(30):
        day = random.choice(daysList)
        daysList.remove(day)
        if day == 'F':
            flu += 1
    return flu/30.0

def simProbFlu1(mounths):
    days = []
    flu = 0
    for i in range(mounths):
        daysList = 'F F F D D D D D D D D D D D D D D D D D D D D D D D D D D D'.split(' ')
        for i in range(30):
            days.append(getDay(daysList))
            daysList.remove(days[i])

    for i in days:
        if i == 'F':
            flu += 1

    return flu/(mounths*30.0)
    

def getDay(daysList):
    return random.choice(daysList)


def probFlu():
    flu = 0
    probList = ['F','D','D','D','D','D','D','D','D','D']
    
    for i in range(30):
        day = random.choice(probList)
        if day == 'F':
            flu += 1

    return flu/10.0


"""def probFlu(mounths):
    flu = 0
    for i in range(mounths):
        if isFlu():
            flu += 1
    return flu/float(mounths)"""










