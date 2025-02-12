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

    def get_vertex(self, key):
        for s in self.adj_list:
            if s.key == key: return s
        return None

    def add_edge(self, u, v):
        vertex_u = self.get_vertex(u)
        vertex_v = self.get_vertex(v)
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

