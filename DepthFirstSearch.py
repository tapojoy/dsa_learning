class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.adj = []
        self.d = None
        self.f = None
        self.pi = None


def dfs(graph):
    for vertex in graph:
        vertex.d = None
        vertex.f = None
        vertex.pi = None
    time = 0
    edges = []
    topologically_sorted_graph = []
    for vertex in graph:
        if not vertex.d:
            time, edges, topologically_sorted_graph = dfs_visit(
                vertex, time, edges, topologically_sorted_graph
            )
    return edges


def dfs_visit(vertex_u, time, edges, topologically_sorted_graph):
    time += 1
    vertex_u.d = time
    for vertex_v in vertex_u.adj:
        if not vertex_v.d:
            vertex_v.pi = vertex_u
            edges.append((vertex_u, vertex_v, 'T'))
            time, edges, topologically_sorted_graph = dfs_visit(
                vertex_v, time, edges, topologically_sorted_graph
            )
        elif not vertex_v.f:
            edges.append((vertex_u, vertex_v, 'B'))
        elif vertex_u.d < vertex_v.d:
            edges.append((vertex_u, vertex_v, 'F'))
        else:
            edges.append((vertex_u, vertex_v, 'C'))
    time += 1
    vertex_u.f = time
    topologically_sorted_graph.insert(0, vertex_u)
    return time, edges, topologically_sorted_graph
