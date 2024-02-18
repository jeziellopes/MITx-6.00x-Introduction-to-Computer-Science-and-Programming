def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls    
    for i in range(n+1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')
