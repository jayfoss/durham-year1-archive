import networkx as nx
import matplotlib as plt
import time
import copy

def wpgma(fileName):
    f = open(fileName, 'r')
    m = []
    species = []
    first = True
    for line in f:
        lineTokens = line.strip().split(' ')
        lineTokensNoFirst = lineTokens[1:]
        if first:
            species = lineTokensNoFirst
            first = False
            continue
        m.append([float(x) for x in lineTokensNoFirst])
    f.close()
    originalSpecies = copy.copy(species)
    G = nx.Graph()
    level = 0
    print(species)
    for i in m:
        print(i)
    while(len(m) > 1):
        print()
        r = reduceMatrix(m, species, G, originalSpecies, level)
        m = r[0]
        species = r[1]
        level = r[2]
    nx.draw(G, with_labels=True)
    plt.pyplot.draw()
    plt.pyplot.savefig(fileName + '.png')
      
def reduceMatrix(m, species, G, originalSpecies, level):
    currentSpecies = species
    minRow = -1
    minCol = -1
    minVal = -1
    for i in range(0, len(m)):
        col, val = min(enumerate(m[i]), key=lambda x: x[1] if x[1] > 0 else float('inf'))
        if val != 0 and (minVal == -1 or val < minVal):
            minRow = i
            minCol = col
            minVal = val

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if ((i == minRow or i == minCol) and j != minRow and j != minCol):
                m[i][j] = (m[minRow][j] + m[minCol][j]) / 2
            elif ((j == minRow or j == minCol) and i != minRow and i != minCol):
                m[i][j] = (m[i][minRow] + m[i][minCol]) / 2
    speciesGroup = '(' + currentSpecies[minRow] + ',' + currentSpecies[minCol] + ')'
    if not G.has_node(currentSpecies[minRow]):
        G.add_node(currentSpecies[minRow])
    if not G.has_node(currentSpecies[minCol]):
        G.add_node(currentSpecies[minCol])
    if not G.has_node(speciesGroup):
        G.add_node(speciesGroup)
    G.add_edge(currentSpecies[minRow], speciesGroup)
    G.add_edge(currentSpecies[minCol], speciesGroup)
    currentSpecies[minRow] = speciesGroup
    currentSpecies.pop(minCol)
    print(currentSpecies)
    m.pop(minCol)
    for i in m:
        del i[minCol]
        print(i)
    return [m, currentSpecies, level + 1]

start = time.time()
wpgma('matrix2(1).txt')
stop = time.time()
print('Time taken to calculate matrices and draw phylogenetic tree: ' + str(stop - start))
