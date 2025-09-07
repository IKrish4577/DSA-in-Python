class Graph:
    def __init__(self):
        #dictinary where key = node/vertex and value is list of neighbours
        self.graph = {} #dict
    #add a node/vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    #add an edge (undirected graph)
    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)  #comment this for direted graph
    #display graph
    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])
g = Graph()
#add vertex
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
#add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
#SHOW GRAPH
g.display()