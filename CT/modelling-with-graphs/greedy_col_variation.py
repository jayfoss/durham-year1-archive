import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    if visited_counter == 0:
        return list(G)[0]
    for i in G.nodes():
        if G.node[i]['visited'] == 'no':
            for n in G.neighbors(i):
                if G.node[n]['visited'] == 'yes':
                    return i

def find_smallest_color(G,i):
    n = len(G.nodes())
    neighbors = G.neighbors(i)
    colors = list(range(1, n + 1))
    for j in neighbors:
        if G.node[j]['color'] in colors:
            colors.remove(G.node[j]['color'])
    return colors[0]

def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter
    kmax = -1
    visited_counter = 0
    while visited_counter < n:
        nextVertex = find_next_vertex(G)
        color = find_smallest_color(G, nextVertex)
        G.node[nextVertex]['visited'] = 'yes'
        visited_counter += 1
        if color > kmax:
            kmax = color
        G.node[nextVertex]['color'] = color
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()

print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
