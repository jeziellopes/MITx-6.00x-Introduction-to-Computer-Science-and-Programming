import pylab

inFile = open('L12 PROBLEM 3 - julyTemps.txt')
lowTemps = []
highTemps = []
diffTemps = []
for line in inFile:
    fields = line.split()
    if len(fields) == 3 and fields[0].isdigit():
        highTemps.append(fields[1])
        lowTemps.append(fields[2])
        diffTemps.append(str(int(fields[1])-int(fields[2])))

def producePlot(lowTemps, highTemps):
    pylab.figure(1)
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

producePlot(lowTemps, highTemps)
