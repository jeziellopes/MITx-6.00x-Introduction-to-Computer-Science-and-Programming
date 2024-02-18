# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''
random.seed(0)

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        #random.seed(0)
        if random.random() < self.getClearProb():
            return True
        return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.getMaxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        #random.seed(0)
        prob = self.getMaxBirthProb * (1 - popDensity)
        if random.random() > prob:
            raise NoChildException()
        else:
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        listViruses = self.viruses[:]
        for virus in listViruses:
            if virus.doesClear():
                self.viruses.remove(virus)
               
        popDensity = self.getTotalPop()/self.getMaxPop() * 1.0
        
        listViruses = self.viruses[:]
        for virus in listViruses:
            if self.getTotalPop() < self.getMaxPop():
                try:
                    self.viruses.append(virus.reproduce(popDensity))
                except NoChildException:
                    pass
            
        return self.getTotalPop()

#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    listPopSizeTotal = []
    for trial in range(numTrials):
        listViruses = []
        for i in range(numViruses):
            listViruses.append(SimpleVirus(maxBirthProb,clearProb))
        patient = Patient(listViruses,maxPop)

        listPopSize = []
        for step in range(300):
            listPopSize.append(patient.update())
        listPopSizeTotal.append(listPopSize)

    listPopSizeAvg = {}
    for step in range(300):
        listPopSizeAvg[step] = 0
        for trial in range(numTrials):
            listPopSizeAvg[step] += listPopSizeTotal[trial][step]
        listPopSizeAvg[step] = listPopSizeAvg[step]/float(numTrials)

    print listPopSizeAvg.values()
    
    pylab.figure()
    pylab.plot(listPopSizeAvg.keys(), listPopSizeAvg.values())
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend(('Average',))
    pylab.show()

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug in self.resistances:
            return self.resistances[drug]
        return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.getMaxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb, clearProb, and mutProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
            
        reProb = self.getMaxBirthProb() * (1 - popDensity)
        if random.random() < reProb:
            newResistances = self.getResistances().copy()
            for drug in newResistances:
                if random.random() < self.getMutProb():
                    newResistances[drug] = not newResistances[drug]
                    
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(),
                                    newResistances, self.getMutProb())
        raise NoChildException()

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        
        Patient.__init__(self, viruses, maxPop)
        self.prescriptions = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.prescriptions:
            self.prescriptions.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.prescriptions

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        
        pop = 0        
        for virus in self.viruses:
            drugN = 0
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    drugN += 1
            if drugN == len(drugResist):
                pop += 1
                
        return pop

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        listViruses = self.viruses[:]
        for virus in listViruses:
            if virus.doesClear():
                self.viruses.remove(virus)
               
        popDensity = self.getTotalPop()/float(self.getMaxPop())

        listViruses = self.viruses[:]
        for virus in listViruses:
            try:
                self.viruses.append(virus.reproduce(popDensity, self.getPrescriptions()))
            except NoChildException:
                pass
            
        return self.getTotalPop()

#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    listPop = [[] for i in range(300)]
    listResistPop = [[] for i in range(300)]

    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances,
                                  mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)

    for step in range(300):
        if step == 150:
            patient.addPrescription('guttagonol')
        listPop[step].append(patient.update())
        listResistPop[step].append(patient.getResistPop(patient.getPrescriptions()))

    avgPop = []
    for pop in listPop:
        avgPop.append(sum(pop)/float(numTrials))
        
    avgResistPop = []
    for pop in listResistPop:
        avgResistPop.append(sum(pop)/float(numTrials))   

    pylab.figure()
    pylab.plot(listPopSizeAvg.keys(), listPopSizeAvg.values())
    pylab.plot(listPopResistAvg.keys(), listPopResistAvg.values())
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Population')
    pylab.legend(('Virus Population Size','Guttagonol-Resistant Virus',))
    pylab.show()

    print avgPop.values()
    print avgResistPop.values()


    '''listPopSizeTotal = []
    listPopResistTotal = []
    
    for trial in range(numTrials):
        listViruses = []
        for i in range(numViruses):
            virus = ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
            listViruses.append(virus)
        patient = TreatedPatient(listViruses,maxPop)

        listPopSize = []
        listPopResist = []
        for step in range(300):
            if step == 150:
                patient.addPrescription('guttagonol')
            patient.update()
            listPopSize.append(patient.getTotalPop())
            listPopResist.append(patient.getResistPop(patient.getPrescriptions()))
        listPopSizeTotal.append(listPopSize)
        listPopResistTotal.append(listPopResist)

    listPopSizeAvg = {}
    listPopResistAvg = {}
    for step in range(300):
        listPopSizeAvg[step] = 0
        listPopResistAvg[step] = 0
        for trial in range(numTrials):
            listPopSizeAvg[step] += listPopSizeTotal[trial][step]
            listPopResistAvg[step] += listPopResistTotal[trial][step]
        listPopSizeAvg[step] = listPopSizeAvg[step]/float(numTrials)
        listPopResistAvg[step] = listPopResistAvg[step]/float(numTrials)

    print listPopSizeAvg.values()
    print listPopResistAvg.values()'''

#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
    
#virus = SimpleVirus(1.0, 0.0)
virus = ResistantVirus(1.0, 0.0, {}, 1.0)
patient = TreatedPatient([virus], 100)

for i in range(10):
    print patient.update()
