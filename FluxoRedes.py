#
#
# Input:
# - Graph with n_connections (number of edges)
# Each connection have a weight and the two nodes that are connect by this edge
#
# The problem:
# - Find the shortest s-t path in network model
#
# Applying simplex algorithm to solution this case
#
# ---------------------
# This is a project of the discipline of Operational Research,
# taught by Professor Roberta.
# Federal University of Alagoas - 2017.2
#
# Team: Ana Geórgia, Eduarda Chagas, Júlia Albuquerque
#
#




from collections import namedtuple
from scipy.optimize import linprog
from time import sleep



def defineNodes(myGraph, init, end):
    nodes = []
    n = []
    for i in range(len(myGraph)):
        if len(nodes) > 0:
            equalA = 0
            equalB = 0
            for j in range(len(nodes)):
                if(myGraph[i].nodeA == nodes[j]):
                    equalA = equalA + 1
                if(myGraph[i].nodeB == nodes[j]):
                    equalB = equalB + 1
            if(equalA == 0):
                nodes.append(myGraph[i].nodeA)
            if(equalB == 0):
                nodes.append(myGraph[i].nodeB)
        else:
            nodes.append(myGraph[i].nodeA)
            nodes.append(myGraph[i].nodeB)
    n.append(init)
    for i in range(len(nodes)):
        if(nodes[i] != init and nodes[i] != end):
            n.append(nodes[i])
    n.append(end)
    return n



def defineWeigths(myGraph):
    weigth = []
    for i in range(len(myGraph)):
        weigth.append(myGraph[i].Weigth)
    return weigth

def defineMatrix(nodes,n_connections,myGraph):
    h, w = len(nodes), n_connections;
    matrixSimplex = [[0 for x in range(w)] for y in range(h)]
    w, h = len(nodes), 1;
    
    flow = [[0 for x in range(w)] for y in range(h)]
    for i in range(n_connections):
        for j in range(len(nodes)):
            if(nodes[j] == myGraph[i].nodeA):
                matrixSimplex[j][i] = 1
            if(nodes[j] == myGraph[i].nodeB):
                matrixSimplex[j][i] = -1
    flow[0][0] = 1
    flow[0][len(nodes)-1] = -1
    return matrixSimplex, flow

Graph = namedtuple('Graph', 'nodeA nodeB Weigth')


n_connections = int(input('Enter the number of connections: '))

init = input('Initial node: ')
end = input('End node: ')

sleep(0.5)

print("\nOK! Starting to build a graph with " + str(n_connections) + " connections...\n")
sleep(1)

print("We'll find the shortest path from " + str(init) + " to " + str(end) + "\n\n")
sleep(0.5)


myGraph = []


print("Let's start inserting the nodes and weights of each edge between them\n")


for i in range(n_connections):
    
    print("\n")
    nA = input('Enter the first Node: ')
    print("\nWho is connected to " + str(nA) + "?")
    
    nB = input(' ' )
    print("\nWhat's the weight of the connection between " + str(nA) + " and " + str(nB) + "?")
    
    w = int(input(' '))
    
    if i < n_connections-1:
        print("\nNext...")
    
    myGraph.append(Graph(nodeA = nA, nodeB = nB, Weigth = w))

nodes = defineNodes(myGraph, init, end)
weigths = defineWeigths(myGraph)



matrixSimplex, flow = defineMatrix(nodes,n_connections,myGraph)


res = linprog(weigths, matrixSimplex, flow)

print("\n")
print("Results:")
print("\n_______________________________________________\n")
print(res)

