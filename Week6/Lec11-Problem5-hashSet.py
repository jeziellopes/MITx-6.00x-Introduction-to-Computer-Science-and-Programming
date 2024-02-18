class hashSet(object):
    
    def __init__(self, numBuckets):
        '''
        numBuckets: int. The number of buckets this hash set will have.
        Raises ValueError if this value is not an integer, or if it is not greater than zero.

        Sets up an empty hash set with numBuckets number of buckets.
        '''
        self.buckets = []

        if type(numBuckets) != int or numBuckets < 1:
            raise ValueError()
        else:
            self.numBuckets = numBuckets

        for i in range(numBuckets):
            self.buckets.append([])
        
    def hashValue(self, e):
        '''
        e: an integer
        
        returns: a hash value for e, which is simply e modulo the number of 
         buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()
        else:
            return e % self.numBuckets

    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()

        return e in self.buckets[self.hashValue(e)]

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()
        
        if not self.member(e):
            self.buckets[self.hashValue(e)].append(e)
        
    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        if not self.member(e) and type(e) != int:
            raise ValueError()
        
        else:
            self.buckets[self.hashValue(e)].remove(e)
        
            
    def getNumBuckets(self):
        return self.numBuckets
            
    def __str__(self):
        return '<' + ','.join([str(self.buckets[i]) for i in range (self.numBuckets)]) + '>'

    
        
