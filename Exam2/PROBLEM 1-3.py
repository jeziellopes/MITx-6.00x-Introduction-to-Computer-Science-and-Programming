import pylab
import random

def PROBLEM13():

    #list = [random.gauss( 50,10) + random.gauss( 70, 10 ) for i in range(100)]

    listA = [random.gauss( 50,10) for i in range(100)]
    listB = [random.gauss( 70, 10 ) for i in range(100)]

    meanList = [(listA[i]+listB[i])/2.0 for i in range(100)]

    pylab.figure()
    #pylab.plot(range(len(list)), list)
    pylab.plot(range(100), listA)
    pylab.plot(range(100), listB)
    pylab.plot(range(100), meanList)            
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Population')
    pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
    pylab.show()
    
#PROBLEM13()

def PROBLEM14():

    randomList1 = [int(random.random() * 2) for i in range(1000)]
    randomList2 = [random.choice((0,1)) for i in range(1000)]

    pylab.figure()
    pylab.plot(range(1000), randomList1)
    pylab.plot(range(1000), randomList2)
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Population')
    pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
    pylab.show()

#PROBLEM14()


    

#PROBLEM33

def LV():

    ballsW = ['W' for i in range(500)]
    ballsB = ['B' for i in range(500)]

    balls = ballsW+ballsB

    random.shuffle(balls)

    ball = balls[random.randint(0, 999)]
    cont = 0
    
    while ball == 'B':
        cont+=1
        ball = balls[random.randint(0, 999)]
    return cont

listLV = [LV() for i in range(1000)]

##pylab.figure()
###pylab.plot(range(1000), listLV)
##pylab.hist(listLV, 10)
##pylab.title('ResistantVirus simulation')
##pylab.xlabel('Time Steps')
##pylab.ylabel('Average Population')
##pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
##pylab.show()



def MC():

    ballsW = ['B' for i in range(500)]
    ballsB = ['W' for i in range(500)]

    balls = ballsW+ballsB

    random.shuffle(balls)


    pos = random.randint(0, 999)
    ball = balls[pos]
    cont = 0
    
    while pos < 999:
        if ball == 'W': 
            return cont
        cont+=1
        pos += 1
        ball = balls[pos]
    return cont

##listMC = [MC() for i in range(1000)]
##
##pylab.figure()
###pylab.plot(range(1000), listMC)
##pylab.hist(listMC, 10)
##pylab.title('ResistantVirus simulation')
##pylab.xlabel('Time Steps')
##pylab.ylabel('Average Population')
##pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
##pylab.show()




def MC():

    ballsW = ['B' for i in range(250)]
    ballsB = ['W' for i in range(250)]
    ballsR = ['R' for i in range(250)]
    ballsG = ['G' for i in range(250)]

    balls = ballsW+ballsB+ballsR+ballsG

    random.shuffle(balls)

    pos = random.randint(0, 999)
    ball = balls[pos]
    cont = 0
    
    while pos < 999:
        if ball == 'W': 
            return cont
        cont+=1
        pos += 1
        ball = balls[pos]
    return cont

listMC = [MC() for i in range(1000)]

##pylab.figure()
###pylab.plot(range(1000), listMC)
##pylab.hist(listMC, 10)
##pylab.title('ResistantVirus simulation')
##pylab.xlabel('Time Steps')
##pylab.ylabel('Average Population')
##pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
##pylab.show()

ballW = 0
for i in range(1000):
    listProb = []
    for i in listMC:
        if i == 0:
            ballW += 1
    listProb.append(ballW/1000.0)

print 'probW ' +str(sum(listProb)/1000.0)
