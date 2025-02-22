class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.adj = []
        self.discovered = False
        self.d = None
        self.pi = None


def bfs(graph, source):
    assert isinstance(source, Vertex), 'incorrect source type'
    assert source in graph, 'source not in graph'
    for vertex in graph:
        assert isinstance(vertex, Vertex), 'invalid vertices in graph'
        if vertex is not source:
            vertex.discovered = False
            vertex.d = float('inf')
            vertex.pi = None
    source.discovered = True
    source.d = 0
    source.pi = None
    queue = [source]
    while queue:
        vertex_u = queue.pop(0)
        assert isinstance(vertex_u,Vertex), 'vertex_u is not a vertex'
        for vertex_v in vertex_u.adj:
            assert isinstance(vertex_v, Vertex), 'vertex_v is not a vertex'
            if not vertex_v.discovered:
                vertex_v.discovered = True
                vertex_v.d = vertex_u.d + 1
                vertex_v.pi = vertex_u
                queue.append(vertex_v)

def get_path(graph, source, vertex):
    assert isinstance(vertex, Vertex), 'invalid vertex'
    assert isinstance(source, Vertex), 'invalid source'
    assert source in graph
    assert vertex in graph
    path = str(vertex.key)
    while True:
        vertex = vertex.pi
        if vertex is source: return path + ' -> ' + str(source.key)
        elif vertex is None: return path + ' -> ' + str('discontinuity')
        path += ' -> ' + str(vertex.key)
