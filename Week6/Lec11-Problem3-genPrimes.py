def genPrimes():
    n=1
    while True:
        p=2
        n+=1
        while (n%p) != 0 and p<n:
            p+=1
        if p == n:
            yield n



def genPrimesEDX():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
