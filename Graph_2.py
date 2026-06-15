class Graph:
    def __init__(self, n):
        self.adj = [[] for i in range (n)]
        self.n=n

    def createEdge(self, x, y):
        self.adj[x - 1].append(y - 1)
        self.adj[y - 1].append(x - 1)

    def DFS_Util(self, src, visited, res):
        visited[src] = True
        for node in self.adj[src]:
            if visited[node] == False:
                self.DFS_Util(node, visited, res)

    def DFS(self, src):
        visited = [False] * self.n
        res = []
        self.DFS_Util(src, visited, res)
        return res
    
n = int(input("Enter the number of node you want:"))
g = Graph(n)
m = n = int(input("Enter the number of edges you want:"))
for i in range(m):
    x, y = map(int, list(input()))
    g.createEdge(x, y)

result = g.DFS(0)
print(result)