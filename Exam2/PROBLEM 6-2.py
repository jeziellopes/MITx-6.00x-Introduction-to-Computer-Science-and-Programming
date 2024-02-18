import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # Your code here

    global CURRENTRABBITPOP
    global MAXRABBITPOP

    probRabbitRep = 1.0 - (CURRENTRABBITPOP/(MAXRABBITPOP*1.0))

    curPopRab = CURRENTRABBITPOP
    for i in range(curPopRab):
        if random.random() < probRabbitRep:
            if CURRENTRABBITPOP < MAXRABBITPOP:
                CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # Your code here
    
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global MAXRABBITPOP

    probFoxEatRabbit = (CURRENTRABBITPOP/(MAXRABBITPOP*1.0))
    probBithFox = 1/3.0
    probFoxDies = 1/10.0
    
    curPopRab = CURRENTRABBITPOP
    curPopFox = CURRENTFOXPOP
    
    for i in range(curPopFox):
        if random.random() < probFoxEatRabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() < probBithFox:
                CURRENTFOXPOP += 1
        elif random.random() < probFoxDies and CURRENTFOXPOP > 10:
            CURRENTFOXPOP -= 1

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # Your code here

    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    popRabFox = ([],[])

    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        popRabFox[0].append(CURRENTRABBITPOP)
        popRabFox[1].append(CURRENTFOXPOP)

    return popRabFox

simulation = runSimulation(200)

##pylab.figure()
##pylab.plot(range(200), simulation[0])
##pylab.plot(range(200), simulation[1])
##pylab.xlabel('Time Steps')
##pylab.ylabel('Population')
##pylab.title('Growth of Fox and Rabbit Population in a Forest')
##pylab.legend(('Rabbit Population','Fox Population'),loc='best')
##pylab.show()

rabbitPopulationOverTime = simulation[0]
foxPopulationOverTime = simulation[1]

coeffRabbit = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
coeffFox = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)

pylab.plot(pylab.polyval(coeffRabbit, range(len(rabbitPopulationOverTime))))
pylab.plot(pylab.polyval(coeffFox, range(len(foxPopulationOverTime))))
pylab.xlabel('Time Steps')
pylab.ylabel('Polyfit Curve Population')
pylab.title('Polyfit Curve Population for Fox and Rabbit Population')
pylab.legend(('Rabbit Polyfit Curve','Fox Polyfit Curve'),loc='best')
pylab.show()


     
