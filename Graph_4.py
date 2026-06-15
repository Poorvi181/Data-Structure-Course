# Undirected Graph, Printing all the connected Components

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def DFSUtil(self, temp, v, visited): 
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)

        return temp
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []

        for i in range(self.v):
            visited.append(False)

        for v in range(self.v):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))

        return cc
    
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 0)
    g.addEdge(1, 0)
    print(g)
    cc = g.connectedComponents()
    print("Following are connected components: ")
    print(cc)
