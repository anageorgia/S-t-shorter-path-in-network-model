from collections import namedtuple
from scipy.optimize import linprog
    
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
        print(myGraph[i].nodeA)
        print(myGraph[i].nodeB)
        print('\n')
        for j in range(len(nodes)):
            if(nodes[j] == myGraph[i].nodeA):
                matrixSimplex[j][i] = 1
            if(nodes[j] == myGraph[i].nodeB):
                matrixSimplex[j][i] = -1
    flow[0][0] = 1
    flow[0][len(nodes)-1] = -1
    return matrixSimplex, flow

def result(myGraph, resX):
    j = 0
    print('The Best Way is: ')
    for i in range(len(resX)):
        if(resX[i] != 0):
            if(j == 0):
                print(myGraph[i].nodeA)
                print(myGraph[i].nodeB)
                j = j + 1
            else:
                print(myGraph[i].nodeB)

Graph = namedtuple('Graph', 'nodeA nodeB Weigth')

n_connections = int(input('Number of connections: '))

init = input('Initial node: ')
end = input('End node: ')

myGraph = []

for i in range(n_connections):
    nA = input('First Node: ')
    nB = input('Second Node: ')
    w = int(input('Weigth of connection: '))
    myGraph.append(Graph(nodeA = nA, nodeB = nB, Weigth = w))

nodes = defineNodes(myGraph, init, end)
weigths = defineWeigths(myGraph)

matrixSimplex, flow = defineMatrix(nodes,n_connections,myGraph)
res = linprog(weigths, matrixSimplex, flow)   
result(myGraph, res.x)         