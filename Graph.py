class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = []
        self.adj_matrix = []

    def grow_matrix(self):
        if not self.adj_matrix:
            self.adj_matrix = [[0]]
        else:
            new_row = [0]
            for row in self.adj_matrix:
                row.append(0)
                new_row.append(0)
            self.adj_matrix.append(new_row)

    def add_vertex(self):
        self.adj_list.append(Vertex(len(self.adj_list) + 1))
        self.grow_matrix()

    def get_vertex_from_key(self, key):
        for s in self.adj_list:
            if s.key == key: return s
        return None

    def add_edge(self, u, v):
        vertex_u = self.get_vertex_from_key(u)
        vertex_v = self.get_vertex_from_key(v)
        assert isinstance(vertex_u, Vertex), 'u not in adj_list'
        assert isinstance(vertex_v, Vertex), 'v not in adj_list'
        vertex_u.edges.append(vertex_v)
        if not self.directed: vertex_v.edges.append(vertex_u)
        self.adj_matrix[u - 1][v - 1] = 1
        if not self.directed: self.adj_matrix[v - 1][u - 1] = 1

    def shrink_matrix(self, key=None):
        if key is None: key = len(self.adj_list)
        else: key -= 1
        assert key in range(0, len(self.adj_list)+1)
        if len(self.adj_matrix)>0:
            self.adj_matrix.pop(key)
            for row in self.adj_matrix:
                row.pop(key)

    def remove_vertex(self, key=None):
        assert len(self.adj_list)>0, 'no vertices to remove'
        if not key:
            popped = self.adj_list.pop()
        else:
            assert key in range(1,len(self.adj_list)+1)
            popped = self.adj_list.pop(key-1)
        for v in self.adj_list:
            if popped in v.edges:
                v.edges.remove(popped)
        self.shrink_matrix(key)
        return popped
    
    def get_edges_from_matrix(self):
        edges = []
        for row in range(len(self.adj_matrix)):
            for col in range(len(self.adj_matrix[row])):
                if self.adj_matrix[row][col] == 1:
                    edges.append([row + 1, col + 1])
        return edges

    def get_edges_from_list(self):
        edges = []
        for v in self.adj_list:
            for e in v.edges:
                edges.append([v.key, e.key])
        return edges


def in_degree(g, v):
    assert isinstance(g, Graph), 'graph is invalid'
    assert isinstance(v, Vertex), 'vertex is invalid'
    assert v in g.adj_list, 'given vertex is not in the given graph'
    sum1 = 0
    for vertex in g.adj_list:
        if v in vertex.edges:
            sum1 += 1
    key = g.adj_list.index(v)
    sum2 = 0
    for row in g.adj_matrix:
        sum2 += row[key]
    assert sum1 == sum2, 'sum mismatch'
    return sum2

def out_degree(g, v):
    assert isinstance(g, Graph), 'graph is invalid'
    assert isinstance(v, Vertex), 'vertex is invalid'
    assert v in g.adj_list, 'given vertex is not in the given graph'
    sum1 = len(v.edges)
    key = g.adj_list.index(v)
    sum2 = sum(g.adj_matrix[key])
    sum3 = sum(g.adj_matrix[v.key-1])
    assert sum1 == sum2 == sum3, 'sum mismatch'
    return sum1

def graph_transpose(g):
    assert isinstance(g, Graph), 'input graph is invalid'
    transpose = Graph(directed=g.directed)
    for _ in range(len(g.adj_list)):
        transpose.add_vertex()
    assert g.get_edges_from_list() == g.get_edges_from_matrix()
    for e in g.get_edges_from_list():
        transpose.add_edge(e[1], e[0])
    return transpose

def multi_graph_to_undirected_graph(g):
    assert isinstance(g, Graph), 'input graph is invalid'
    assert g.directed == True, 'input graph should be directed'
    for v in g.adj_list:
        if v in v.edges: v.edges.remove(v)
        v.edges = list(set(v.edges))
        for e in v.edges:
            if v not in e.edges: e.edges.append(v)
    edges = g.get_edges_from_list()
    g.adj_matrix = [
        [0 for _ in range(len(g.adj_list))] for _ in range(len(g.adj_list))
    ]
    for e in edges:
        g.adj_matrix[e[0]-1][e[1]-1] = 1
    g.directed = not g.directed
    return g

