import pylab

inFile = open('words.txt')
list = {}

for line in inFile:
    listWords = line.split()

largeWord = 0
for word in listWords:
    if len(word) > largeWord:
        largeWord = len(word)
        
for l in range(largeWord+1):
    list[l] = 0

for word in listWords:
    list[len(word)] += 1


def producePlot(list):
    pylab.figure(1)
    pylab.plot(list.keys(), list.values())
    pylab.title('Number of Existing Words by Word Length in the File "words.txt" of Problem Set 3')
    pylab.xlabel('Word Length')
    pylab.ylabel('Number of Words')
    pylab.show()

producePlot(list)


proportionX = {}

for line in inFile:
    listWords = line.split()

for word in listWords:
    proportionX[listWords.index(word)] = (word.count('x') + word.count('X'))/len(word)

def producePlot(list):
    pylab.figure(1)
    pylab.plot(list.keys(), list.values())
    pylab.title('Number of Existing Words by Word Length in the File "words.txt" of Problem Set 3')
    pylab.xlabel('Word Length')
    pylab.ylabel('Number of Words')
    pylab.show()

producePlot(proportionX)
