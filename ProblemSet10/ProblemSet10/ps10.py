# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
       mapFilename : name of the map file

    Assumes:
       Each entry in the map file consists of the following four positive
       integers, separated by a blank space:
          From To TotalDistance DistanceOutdoors
       e.g.
          32 76 54 23
       This entry would become an edge from 32 to 76.

    Returns:
       a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    mapFile = open(mapFilename, "r")   
    edges = [ line.rstrip() for line in mapFile.readlines() ]
    edges = [ item.split(' ') for item in edges]

    g = WeightedDigraph()
    for e in edges:
       src = Node(int(e[0]))
       dest = Node(int(e[1]))
       tDict = int(e[2])
       oDict = int(e[3])

       if not g.hasNode(src):
          g.addNode(src)
       if not g.hasNode(dest):
          g.addNode(dest)
       
       we = WeightedEdge(src, dest, tDict, oDict)
       g.addEdge(we)

    return g 

##PROBLEM 2

mitMap = load_map("mit_map.txt")
##print isinstance(mitMap, Digraph)
##print 
##print isinstance(mitMap, WeightedDigraph)
##print 
##print mitMap.Nodes
##print
##print mitMap.edges
       

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def calcTDist(path):
    return sum(int(edge.tDist) for edge in path)

def calcODist(path):
    return sum(int(edge.oDist) for edge in path)

def isVisited(Node, path):
    for edge in path:
       if Node in (edge.getSource(), edge.getDestination()):
          return True
    return False

def getNList(path):
    list = [str(edge.getSource()) for edge in path]
    list.append(str(path[-1].getDestination()))
    return list

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
       digraph: instance of class Digraph or its subclass
       start, end: start & end building numbers (strings)
       maxTotalDist : maximum total distance on a path (integer)
       maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
       start and end are numbers for existing buildings in graph

    Returns:
       The shortest-path from start to end, represented by 
       a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
       where there exists an edge from n_i to n_(i+1) in digraph, 
       for all 1 <= i < k.

       If there exists no path that satisfies maxTotalDist and
       maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO

    pilha = [[edge] for edge in digraph.edges[Node(start)]]
    paths = []
 
    while pilha:
        path = pilha.pop(-1)
              
        if path[-1].getDestination().getName() == end and calcODist(path) <= maxDistOutdoors:
            paths.append(path)
            continue
 
        for edge in digraph.edges[path[-1].getDestination()]:
            if not isVisited(edge.getDestination(), path):
                new_path = path + [edge]
                if calcODist(new_path) <= maxDistOutdoors:
                    pilha.append(new_path)
 
    shortest = None
    minDist = maxTotalDist
    
    for path in paths:
       distance = calcTDist(path)
       if distance <= minDist:
          shortest = path
          minDist = distance
 
    if shortest is None:
       raise ValueError()
 
    return getNList(shortest)


##map3 = WeightedDigraph()
##
##n1 = Node('1')
##n2 = Node('2')
##n3 = Node('3')
##n4 = Node('4')
##map3.addNode(n1)
##map3.addNode(n2)
##map3.addNode(n3)
##map3.addNode(n4)
##randomEdge = WeightedEdge(n1, n2, 10, 5)
##map3.addEdge(randomEdge)
##randomEdge = WeightedEdge(n1, n4, 15, 1)
##map3.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n3, 8, 5)
##map3.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n3, 8, 5)
##map3.addEdge(randomEdge)
##
##print
##print map3
##print
##
###1->2 (10.0, 5.0)
###1->4 (15.0, 1.0)
###2->3 (8.0, 5.0)
###4->3 (8.0, 5.0)
##print bruteForceSearch(map3, "1", "3", 100, 100)
###['1', '2', '3']
##print
##print bruteForceSearch(map3, "1", "3", 18, 18)
##print
##print bruteForceSearch(map3, "1", "3", 18, 0)
##print
##print bruteForceSearch(map3, "1", "3", 10, 10)




##Looking at map 4:
##1->2 (5.0, 2.0)
##3->5 (6.0, 3.0)
##2->3 (10.0, 5.0)
##2->4 (20.0, 10.0)
##4->3 (2.0, 1.0)
##4->5 (20.0, 10.0)
##bruteForceSearch(map4, "1", "3", 100, 100)
##['1', '2', '3']
##bruteForceSearch(map4, "1", "5", 100, 100)
##['1', '2', '3', '5']
##Test completed

##map4 = WeightedDigraph()
##
##n1 = Node('1')
##n2 = Node('2')
##n3 = Node('3')
##n4 = Node('4')
##n5 = Node('5')
##map4.addNode(n1)
##map4.addNode(n2)
##map4.addNode(n3)
##map4.addNode(n4)
##map4.addNode(n5)
##randomEdge = WeightedEdge(n1, n2, 5, 2)
##map4.addEdge(randomEdge)
##randomEdge = WeightedEdge(n3, n5, 6, 3)
##map4.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n3, 10, 5)
##map4.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n4, 20, 10)
##map4.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n3, 2, 1)
##map4.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n5, 20, 10)
##map4.addEdge(randomEdge)
##
##print
##print map4
##print
##print bruteForceSearch(map4, "1", "3", 100, 100)
##print 
##print bruteForceSearch(map4, "1", "5", 100, 100)
##print
##print bruteForceSearch(map4, "1", "5", 21, 10)
###print
###print bruteForceSearch(map4, "1", "5", 21, 9)
##print 
##print bruteForceSearch(map4, "1", "5", 20, 20)
##
##
##




#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
       digraph: instance of class Digraph or its subclass
       start, end: start & end building numbers (strings)
       maxTotalDist : maximum total distance on a path (integer)
       maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
       start and end are numbers for existing buildings in graph

    Returns:
       The shortest-path from start to end, represented by 
       a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
       where there exists an edge from n_i to n_(i+1) in digraph, 
       for all 1 <= i < k.

       If there exists no path that satisfies maxTotalDist and
       maxDistOutdoors constraints, then raises a ValueError.
    """

    pilha = [[edge] for edge in digraph.edges[Node(start)]]

    shortest = None
    minDist = maxTotalDist
 
    while pilha:
        path = pilha.pop(-1)
              
        if path[-1].getDestination().getName() == end:
            if shortest == None or calcTDist(path)<=calcTDist(shortest) or len(path)<=len(shortest):
                distance = calcTDist(path)
                if distance <= minDist:
                    shortest = path
                    minDist = distance
            continue
 
        for edge in digraph.edges[path[-1].getDestination()]:
            if not isVisited(edge.getDestination(), path):
                new_path = path + [edge]
                if calcODist(new_path) <= maxDistOutdoors:
                    pilha.append(new_path)
 
    if shortest is None:
       raise ValueError()
 
    return getNList(shortest)


##Looking at map 5:
##1->2 (5.0, 2.0)
##3->5 (6.0, 3.0)
##2->3 (20.0, 10.0)
##2->4 (10.0, 5.0)
##4->3 (2.0, 1.0)
##4->5 (20.0, 10.0)
##directedDFS(map5, "1", "3", 100, 100)
##['1', '2', '4', '3']
##directedDFS(map5, "1", "5", 100, 100)
##['1', '2', '3', '5']
##Test completed

##map5 = WeightedDigraph()
##
##n1 = Node('1')
##n2 = Node('2')
##n3 = Node('3')
##n4 = Node('4')
##n5 = Node('5')
##map5.addNode(n1)
##map5.addNode(n2)
##map5.addNode(n3)
##map5.addNode(n4)
##map5.addNode(n5)
##randomEdge = WeightedEdge(n1, n2, 5, 2)
##map5.addEdge(randomEdge)
##randomEdge = WeightedEdge(n3, n5, 6, 3)
##map5.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n3, 20, 10)
##map5.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n4, 10, 5)
##map5.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n3, 2, 1)
##map5.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n5, 20, 10)
##map5.addEdge(randomEdge)

##print 
##print directedDFS(map5, "1", "3", 100, 100)
##print 
##print directedDFS(map5, "1", "5", 100, 100)
##print 
##print directedDFS(map5, "1", "3", 17, 8)
##print
##print directedDFS(map5, "1", "5", 23, 11)
##print
##print directedDFS(map5, "4", "5", 21, 11)
print
##print directedDFS(map5, "5", "1", 100, 100)
##print
##print directedDFS(map5, "4", "5", 8, 2)
##print

##Looking at map 6:
##1->2 (5.0, 2.0)
##3->5 (5.0, 1.0)
##2->3 (20.0, 10.0)
##2->4 (10.0, 5.0)
##4->3 (5.0, 1.0)
##4->5 (20.0, 1.0)
##directedDFS(map6, "1", "3", 100, 100)
##['1', '2', '4', '3']
##directedDFS(map6, "1", "5", 100, 100)
##['1', '2', '3', '5']
##Test completed

##map6 = WeightedDigraph()
##
##n1 = Node('1')
##n2 = Node('2')
##n3 = Node('3')
##n4 = Node('4')
##n5 = Node('5')
##map6.addNode(n1)
##map6.addNode(n2)
##map6.addNode(n3)
##map6.addNode(n4)
##map6.addNode(n5)
##randomEdge = WeightedEdge(n1, n2, 5, 2)
##map6.addEdge(randomEdge)
##randomEdge = WeightedEdge(n3, n5, 5, 1)
##map6.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n3, 20, 10)
##map6.addEdge(randomEdge)
##randomEdge = WeightedEdge(n2, n4, 10, 5)
##map6.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n3, 5, 1)
##map6.addEdge(randomEdge)
##randomEdge = WeightedEdge(n4, n5, 20, 1)
##map6.addEdge(randomEdge)
##
##print directedDFS(map6, "1", "3", 100, 100)
##print
##print directedDFS(map6, "1", "5", 100, 100)
##print
##print
##print directedDFS(map6, "1", "5", 35, 9)
##print
##print directedDFS(map6, "1", "5", 35, 8)
##print 
##print directedDFS(map6, "4", "5", 21, 11)
##print 
##print directedDFS(map6, "4", "5", 21, 1)
##print 
##print directedDFS(map6, "4", "5", 19, 1)
##print 
##print directedDFS(map6, "3", "2", 100, 100)
##print 
##print directedDFS(map6, "4", "5", 8, 2)



# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #Test cases
##    mitMap = load_map("mit_map.txt")
##    print isinstance(mitMap, Digraph)
##    print isinstance(mitMap, WeightedDigraph)
##    print 'Nodes', mitMap.Nodes
##    print 'edges', mitMap.edges


    #LARGE_DIST = 1000000
    LARGE_DIST = 1000

    #Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

    #Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

    #Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

    #Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

    #Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

    #Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

    #Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

    #Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
