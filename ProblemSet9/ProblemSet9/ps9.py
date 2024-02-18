# 6.00 Problem Set 9

import numpy
import random
import pylab
#from ps8b import *
from ps8b_precompiled_27 import *
from datetime import datetime

random.seed()

#
# PROBLEM 1
#

def simulationDelayedTreatment(numTrials, timeStepsB):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    print datetime.now()

    #timeStepsB = 0
    timeStepsL = 150
    timeSteps = timeStepsB + timeStepsL

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': True}
    mutProb = 0.005

    finalPop = []
    popMenor50 = 0
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances,
                                    mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)

        for step in range(timeSteps):
            if step == timeStepsB:
                patient.addPrescription('guttagonol')
            patient.update()

        finalPop.append(patient.getTotalPop())
        
        if patient.getTotalPop() <= 50:
            popMenor50 += 1
            
##    print 'Numero de virus: ' + str(numViruses) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'
##    print 'clearProb: ' + str(clearProb) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'
    print 'Resistense: ' + str(resistances['guttagonol']) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'

    pylab.figure()
    pylab.hist(finalPop, bins=10, label = 'resistances: ' + str(resistances['guttagonol']) + ' Curados: ' + str(popMenor50) + ' Percent: ' + str((popMenor50 * 100)/float(numTrials)) + ' %')
    pylab.title('Resistant Virus simulation')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    pylab.legend(loc=0)
    print datetime.now()
    print
    #pylab.show()
    pylab.savefig('150-numViruses\Graph-Trial-1000-resistances-' + str(resistances['guttagonol']) + '.png')
    
##    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 300, 150)
##    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 150, 150)
##    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 75, 150)
##    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 0, 150)
##    simulationWithDrug(10, 100, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 5, 5)
    
##    simulationDelayedTreatment(1000, 300)


##for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
#for i in [1, 10, 100, 1000, 100000]:
#for i in [100000]:
##for i in [0.05, 0.10, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
##    simulationDelayedTreatment(1000, 150, i)

##simulationDelayedTreatment(100, 150)
    
##simulationDelayedTreatment(1000, 75)
##simulationDelayedTreatment(1000, 0)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials, timeStepsDelay):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    print datetime.now()

    timeStepsB = 150
    #timeStepsDelay = 150
    timeStepsL = 150
    timeSteps = timeStepsB + timeStepsDelay + timeStepsL

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    finalPop = []
    popMenor50 = 0
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances,
                                    mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)

        for step in range(timeSteps):
            if step == timeStepsB:
                patient.addPrescription('guttagonol')
            if step == timeStepsB + timeStepsDelay:
                patient.addPrescription('grimpex')
            patient.update()

        finalPop.append(patient.getTotalPop())
        
        if patient.getTotalPop() <= 50:
            popMenor50 += 1
            
##    print 'Numero de virus: ' + str(numViruses) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'
##    print 'clearProb: ' + str(clearProb) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'
##    print 'Resistense: ' + str(resistances['guttagonol']) + ' Pacientes curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'
##    print 'mutProb: ' + str(mutProb) + ' Curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'

    print 'timeStepsDelay: ' + str(timeStepsDelay) + ' Curados: ' + str(popMenor50) + ' Percentual: ' + str((popMenor50 * 100)/float(numTrials)) + ' %'

    pylab.figure()
    pylab.hist(finalPop, bins=10, label = 'timeStepsDelay: ' + str(timeStepsDelay) + ' Curados: '
               + str(popMenor50) + ' Percent: ' + str((popMenor50 * 100)/float(numTrials)) + ' %')
    pylab.title('Resistant Virus simulation')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    pylab.legend(loc=0)
    print datetime.now()
    print
    #pylab.show()
    pylab.savefig('Graph-timeStepsDelay' + str(timeStepsDelay) + '.png')


##for i in [300, 150, 75, 0]:
##    simulationTwoDrugsDelayedTreatment(1000, i)

for i in [0.005, 0.015, 0.025, 0.035, 0.045]:
    simulationTwoDrugsDelayedTreatment(1000, i)

##for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
##for i in [1, 10, 100, 1000, 100000]:
##for i in [100000]:
##for i in [0.05, 0.10, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
##    simulationDelayedTreatment(1000, 150, i)
