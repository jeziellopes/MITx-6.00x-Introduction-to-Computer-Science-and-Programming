def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if (a%b==0):
        return b;
    elif (a%b!=0):
        return gcdRecur(b, a%b)
