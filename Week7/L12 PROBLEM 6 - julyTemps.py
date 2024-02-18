import pylab

inFile = open('L12 PROBLEM 3 - julyTemps.txt')
lowTemps = []
highTemps = []
for line in inFile:
    fields = line.split()
    if len(fields) == 3 and fields[0].isdigit():
        highTemps.append(fields[1])
        lowTemps.append(fields[2])
def producePlot(lowTemps, highTemps):
    pylab.figure(1)
    pylab.plot(range(1,32), highTemps)
    pylab.plot(range(1,32), lowTemps)
    pylab.title('Day by Day Maximum and Minimum Temperatures in Boston in July 2012')
    pylab.legend(('Maximum Temperatures', 'Minimum Temperatures'))
    pylab.xlabel('Days')
    pylab.ylabel('Temperatures')
    pylab.show()
    
producePlot(lowTemps, highTemps)
