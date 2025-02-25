class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.adj = []
        self.d = 0
        self.f = 0
        self.color = None
        self.pi = None

    def set_color_white(self):
        self.color = 'white'

    def is_color_white(self):
        if self.color == 'white': return True
        return False

    def set_color_gray(self):
        self.color = 'gray'

    def is_color_gray(self):
        if self.color == 'gray': return True
        return False

    def set_color_black(self):
        self.color = 'black'

    def is_color_black(self):
        if self.color == 'black': return True
        return False


def dfs(graph):
    for vertex in graph:
        vertex.d = 0
        vertex.f = 0
        vertex.pi = None
        vertex.set_color_white()
    time = 0
    edges = []
    for vertex in graph:
        if vertex.is_color_white():
            time, edges = dfs_visit(vertex, time, edges)
    return edges

def dfs_visit(vertex_u, time, edges):
    time += 1
    vertex_u.d = time
    vertex_u.set_color_gray()
    for vertex_v in vertex_u.adj:
        if vertex_v.is_color_white():
            vertex_v.pi = vertex_u
            edges.append((vertex_u, vertex_v, 'T'))
            time, edges = dfs_visit(vertex_v, time, edges)
        elif vertex_v.is_color_gray():
            edges.append((vertex_u, vertex_v, 'B'))
        elif vertex_v.is_color_black():
            if vertex_u.d < vertex_v.d:
                edges.append((vertex_u, vertex_v, 'F'))
            else:
                edges.append((vertex_u, vertex_v, 'C'))
    time += 1
    vertex_u.f = time
    vertex_u.set_color_black()
    return time, edges
