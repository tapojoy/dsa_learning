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
    for vertex in graph:
        if not vertex.d:
            time, edges = dfs_visit(vertex, time, edges)
    return edges

def dfs_visit(vertex_u, time, edges):
    time += 1
    vertex_u.d = time
    vertex_u.set_color_gray()
    for vertex_v in vertex_u.adj:
        if not vertex_v.d:
            vertex_v.pi = vertex_u
            edges.append((vertex_u, vertex_v, 'T'))
            time, edges = dfs_visit(vertex_v, time, edges)
        elif not vertex_v.f:
            edges.append((vertex_u, vertex_v, 'B'))
        elif vertex_u.d < vertex_v.d:
            edges.append((vertex_u, vertex_v, 'F'))
        else:
            edges.append((vertex_u, vertex_v, 'C'))
    time += 1
    vertex_u.f = time
    return time, edges
