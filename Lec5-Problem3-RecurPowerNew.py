def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 0:
        return 1
    elif exp > 0 and base == exp:
        return base * recurPowerNew((base*base), exp/2)
    elif exp > 0 and base != exp:    
        return base * recurPowerNew(base, exp-1)
