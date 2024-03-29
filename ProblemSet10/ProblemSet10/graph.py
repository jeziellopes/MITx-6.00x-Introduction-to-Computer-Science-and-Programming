# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class SmartNode(Node):

    def __hash__(self):
        return int(self.name)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]
    

class WeightedEdge(Edge):
    def __init__(self, src, dest, tDist, oDist):
        Edge.__init__(self, src, dest)
        self.oDist = oDist
        self.tDist = tDist
    def getTotalDistance(self):
        return self.tDist
    def getOutdoorDistance(self):
        return self.oDist
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.tDist, self.oDist)

class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(edge)
    def childrenOf(self, node):
        child = []
        for e in self.edges[node]:
            child.append(e.dest)
        return child
    def __str__(self):
        res = ''
        for k in self.edges:
            for e in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, e.src, e.dest, float(e.tDist), float(e.oDist))
        return res[:-1]

#### PROBLEM 1

g = WeightedDigraph()
na = Node('a')
nb = Node('b')
nc = Node('c')
g.addNode(na)
g.addNode(nb)
g.addNode(nc)
e1 = WeightedEdge(na, nb, 15, 10)
print e1
#a->b (15, 10)
print e1.getTotalDistance()
#15
print e1.getOutdoorDistance()
#10
e2 = WeightedEdge(na, nc, 14, 6)
e3 = WeightedEdge(nb, nc, 3, 1)
print e2
#a->c (14, 6)
print e3
#b->c (3, 1)
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print    
print g
#a->b (15.0, 10.0)
#a->c (14.0, 6.0)
#b->c (3.0, 1.0)

nh = Node('h')
nj = Node('j')
nk = Node('k')
nm = Node('m')
ng = Node('g')
g = WeightedDigraph()
g.addNode(nh)
g.addNode(nj)
g.addNode(nk)
g.addNode(nm)
g.addNode(ng)
randomEdge = WeightedEdge(nj, nh, 45, 35)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nh, 43, 32)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nm, 57, 53)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nh, 58, 28)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nh, nj, 36, 11)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, nm, 94, 84)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, nh, 29, 19)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nh, 36, 19)
g.addEdge(randomEdge)
print
print g.childrenOf(nh)
print g.childrenOf(nj)
print g.childrenOf(nk)
print g.childrenOf(nm)
print g.childrenOf(ng)
