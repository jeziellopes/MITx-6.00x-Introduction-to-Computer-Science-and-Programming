def numPens(n):
    """
    n is an int

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """

    packs = {8:0, 5:0}
    while n>4:
        for i in packs.keys():
            print n
            print i
            print n-i
            print
            if n-i >= 0:
                n-=i
                packs[i] += 1
    print 'o valor de n é '+str(n)
    for i in range(len(packs)):
        print str(packs.values()[i])+' caixas de '+str(packs.keys()[i]) + ' unidades'
    if n==0 and packs[8] != 0 or packs[5] != 0:
        return True
    return False

def numPens24(n):
    """
    n is an int

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """

    packs = {24:0, 8:0, 5:0}
    while n>4:
        for i in packs.keys():
            print n
            print i
            print n-i
            print
            if n-i >= 0:
                n-=i
                packs[i] += 1
    print 'o valor de n é '+str(n)
    for i in range(len(packs)):
        print str(packs.values()[i])+' caixas de '+str(packs.keys()[i]) + ' unidades'
    if n==0 and packs[24] != 0 or packs[8] != 0 or packs[5] != 0:
        return True
    return False
            
def numPensRecur(n):
    """
    n is an int

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n<0:
        return False
    elif n==0:
        return True
    for c in [8, 5]:
        if numPensRecur(n-c):
            print n
            print c
            print n-c
            print
            return True
    return False
            
