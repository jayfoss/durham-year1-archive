import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_smallest_color(G,i):
    n = len(G.nodes())
    neighbors = G.neighbors(i)
    colors = list(range(1, n + 1))
    for j in neighbors:
        if G.node[j]['color'] in colors:
            colors.remove(G.node[j]['color'])
    return colors[0]

def greedy(G):
    global kmax
    kmax = -1
    for i in G.nodes():
        color = find_smallest_color(G, i)
        if color > kmax:
            kmax = color
        G.node[i]['color'] = color
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    
print('Graph G1:')
G=graph1.Graph()
greedy(G)

print('Graph G2:')
G=graph2.Graph()
greedy(G)

print('Graph G3:')
G=graph3.Graph()
greedy(G)

print('Graph G4:')
G=graph4.Graph()
greedy(G)

print('Graph G5:')
G=graph5.Graph()
greedy(G)
