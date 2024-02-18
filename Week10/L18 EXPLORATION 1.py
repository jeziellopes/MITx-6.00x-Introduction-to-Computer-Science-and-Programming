def powerset(s):
    x = len(s)
    for i in range(1, 1 << x):
        print [s[j] for j in range(x) if (i & (1 << j))]

#powerset("abcd")

l = ["x", "y", "z", ]

from itertools import combinations

def powersetI(items):
    combo = []
    for r in range(1, len(items) + 1):
        #use a list to coerce a actual list from the combinations generator
        combo.append(list(combinations(items,r)))
    return combo

l_powerset = powersetI(l)

for item in l_powerset:
    #print "All sets of length ", i
    for i in item:
        print i
