import itertools

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    # Your code here

    N = len(items)
    for i in itertools.product([0, 1, 2], repeat=N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if i[j] == 1:
                bag1.append(items[j])
            elif i[j] == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
            

l = ["x", "y", "z"]

gen = yieldAllCombos(l)

for i in gen:
    print i
