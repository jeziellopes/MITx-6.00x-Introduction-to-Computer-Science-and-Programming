def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    for i in range(min(a,b), 0, -1):
        if (a%i==0 and b%i==0):
            return i
            
