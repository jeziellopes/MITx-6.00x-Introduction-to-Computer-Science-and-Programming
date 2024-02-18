def isPrime(n):
    if n == 2 or n == 3:
        return True
    for i in range(n-(n-2), n, 1):
        if n%i == 0:
            return False
    return True
