class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.adj = []
        self.d = 0
        self.f = 0
        self.discovered = False
        self.pi = None


def dfs(graph):
    for vertex in graph:
        vertex.d = 0
        vertex.f = 0
        vertex.pi = None
        vertex.discovered = False
    time = 0
    for vertex in graph:
        if not vertex.discovered:
            time = dfs_visit(vertex, time)

def dfs_visit(vertex_u, time):
    time += 1
    vertex_u.d = time
    vertex_u.discovered = True
    for vertex_v in vertex_u.adj:
        if not vertex_v.discovered:
            vertex_v.pi = vertex_u
            time = dfs_visit(vertex_v, time)
    time += 1
    vertex_u.f = time
    return time
