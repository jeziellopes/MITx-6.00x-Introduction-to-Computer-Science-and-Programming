testList = [1, 4, 8, 9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

        

def square(a):
    return a*a

applyToEach(testList, square)
