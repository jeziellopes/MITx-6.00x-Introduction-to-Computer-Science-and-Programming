def isPrime(n):
    if n<1:
        raise ValueError()
    if type(n) != int:
        raise TypeError()    
    else:
        if n == 2 or n == 3:
            return True
        for i in range(n-(n-2), n, 1):
            if n%i == 0:
                return False
        return True


def isPrime2(n):
    if type(n) != int:
        raise TypeError()
    if n <= 0:
        raise ValueError()
    if n == 2:
        return True
    elif n < 2:
        return False
    for divisor in range(2, int(n**0.5+1)):
        if n % divisor == 0:
            return False

    return True
