def numPensRecur(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    
    if n < 0:
        return False

    if n == 0:
        return True

    for x in (24, 8, 5):    
        if numPens(n - x):            
            return True

    return False



def numPens2(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    
    """a=5
    b=8
    c=24"""

    a=b=c=0
    p=n
    
    while 5*a+8*b+24*c != n:
        a+=1
        b+=1
        c+=1
        
    return True

    


def numPens1(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    # Your Code Here

    if n==0:
        return True
    
    elif not numPens1(n-24):
        return numPens1(n-24)

    elif numPens1(n-8):
        return numPens1(n-8)
    
    elif numPens1(n-5):
        return numPens1(n-5)
            
    return False

def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    # Your Code Here

    a=b=c=0
    p=n
    
    while p>0:
        if p>=24:
            c+=1                    
            p-=24
            if p>=8:
                b+=1
                p-=8
                if p>=5:
                    a+=1
                    p-=5
        else:
            break
        
    if 5*a+8*b+24*c == n:        
        return True
    else:
        return False

def numPensN(n):
    a=b=c=0
    while n>0:
        if n>=5:
            a+=1
            n-=5
            if n>=8:
                b+=1
                n-=8
                if n>=24:                
                    c+=1                    
                    n-=24                
        else:            
            return False
    if n==0 and a and b and c != 0:    
        return True
    else:
        return False





def numPensR(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    """a = 0
    b = 0
    c = 0

    if n==0:
        return True
    elif n>=5:
            print n
            a+=1
            n-=5
            if n>=8:
                print n
                b+=1
                n-=8
                if n>=13:
                    print n
                    a+=1
                    b+=1
                    n-=13
                    if n>=24:
                        print n
                        c+=1
                        n-=24
                        if n>=29:
                            print n
                            a+=1
                            c+=1
                            n-=29
                            if n>=32:
                                print n
                                b+=1
                                c+=1
                                n-=32
                                if n>=37:
                                    print n
                                    a+=1
                                    b+=1
                                    c+=1
        else:
            print n
            return False
    if n==0 and a and b and c != 0:
        print a
        print b
        print c
        return True
    else:
        return False"""
            

def numPensRecurJ(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n==0:
        return True
    if n>=24:
        return numPens(n-24)
    elif n>=8:
        return numPens(n-8)
    elif n>=5:
        return numPens(n-5)
    return False
