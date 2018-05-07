import collections
import math

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.weights = {}
    
    def addNodes(self,value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        if fromNode == toNode:
            pass
        self.edges[fromNode].append(toNode)
        self.weights[(fromNode, toNode)] = distance

# sdist defines the shortest distance paths from start of v, for v in sdist 
def dijkstra(graph,start):
    s = set()
    sdist = dict.fromkeys(list(graph.nodes), math.inf)
    prev = dict.fromkeys(list(graph.nodes), None)
    sdist[start] = 0
    while s != graph.nodes:
        v = min((set(sdist.keys()) - s), key=sdist.get)
        for n in set(graph.edges[v]) - s:
            newPath = sdist[v] + graph.weights[v,n]
            if newPath < sdist[n]:
                sdist[n] = newPath
                prev[n] = v
                s.add(v)
        return (sdist, prev)

def shortestPath(graph,start,end):
    sdist, prev = dijkstra(graph, start)
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
        path.reverse()
    return path

if __name__ == "__main__":
    G = Graph()
    
    G.addNodes('DisneyWorld')
    G.addNodes('Magic Mountain')
    G.addNodes('Disneyland')
    G.addNodes('SeaWorld')
    G.addNodes('Knotts Berry Farm')
    
    G.addEdge('DisneyWorld','Magic Mountain',4)
    G.addEdge('DisneyWorld','Disneyland',8)
    G.addEdge('DisneyWorld','SeaWorld',5)
    G.addEdge('DisneyWorld','Knotts Berry Farm',12)
    G.addEdge('Magic Mountain','SeaWorld',1)
    G.addEdge('Magic Mountain','DisneyWorld',4)
    G.addEdge('SeaWorld','Knotts Berry Farm',2)
    G.addEdge('Magic Mountain','Disneyland',3)
    G.addEdge('Disneyland','SeaWorld',7)
    G.addEdge('Knotts Berry Farm','Magic Mountain',6)
           
    print(dijkstra(G,'DisneyWorld'))
        
    print(shortestPath(G,'DisneyWorld','Knotts Berry Farm'))
