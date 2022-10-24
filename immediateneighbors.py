import time
def immediateNeighbors(pattern):
    neighborhood=set()

    for i in range(len(pattern)):
        symbol=pattern[i]
        bases = ['A', 'T', 'C', 'G']
        for nuc in bases:
            if nuc!=symbol:
                 neighbor=pattern[:i]+nuc+pattern[i+1:]
                 neighborhood.add(neighbor)
    return neighborhood



def iterativeneighbors(pattern,d):
    neighborhood=set()
    neighborhood.add(pattern)

    for i in range(d):
        temp=set()
        for string in neighborhood:
            for j in immediateNeighbors(string):
                if j not in neighborhood:
                    temp.add(j)
        for t in temp:
            neighborhood.add(t)
    return neighborhood


start_time=time.time()

print("Neighbours found (iterative method)")
print(iterativeneighbors("ACG",2))


print("--- %s seconds ---" % (time.time() - start_time))
