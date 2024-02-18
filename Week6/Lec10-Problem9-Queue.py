class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)        
    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError()
