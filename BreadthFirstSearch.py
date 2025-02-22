import random

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

def get_path(source, vertex):
    assert isinstance(vertex, Vertex), 'invalid vertex'
    assert isinstance(source, Vertex), 'invalid source'
    path = [vertex]
    while True:
        vertex = vertex.pi
        if vertex is source: break
        elif vertex is None: return None
        path.append(vertex)
    path.append(source)
    return path

def get_path_str(source, vertex):
    path = get_path(source, vertex)
    if path:
        path_str = str(path.pop(0).key)
        while path:
            path_str += ' -> ' + str(path.pop(0).key)
        return path_str
    return ('no path found from vertex:' +
            str(vertex.key) +
            ' to source:' +
            str(source.key))

def get_diameter(graph, source):
    assert isinstance(graph, list)
    assert isinstance(source, Vertex)
    assert source in graph
    graph = graph.copy()
    graph.remove(source)
    diameter = 0
    while graph:
        random_vertex = random.randint(0, len(graph)-1)
        path = get_path(source, graph[random_vertex])
        if not path: break
        if len(path)-1 > diameter: diameter = len(path)-1
        for vertex in path:
            if vertex in graph:
                graph.remove(vertex)
    return diameter

