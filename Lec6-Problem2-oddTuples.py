def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    Tup = ()
    for i in range(len(aTup)):
        if i%2==0:
            Tup += (aTup[i],)         
    return Tup
    
def oddTuples2(aTup):
    return aTup[::2]
