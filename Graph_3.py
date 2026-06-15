graph = {}


def createEdge(graph, x, y):
    if x not in graph:
        graph[x] = []

    if y not in graph:
        graph[y] = []

    graph[x].append(y)
    graph[y].append(x)


createEdge(graph, 1, 2)
print(graph)