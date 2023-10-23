# wieghted graph implementation using adjacency matrix


class AMGraph:

    def __init__(self, num_vertices, undir = True):

        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.undir = undir

    def __iter__(self):
        yield from [vtx_list for vtx_list in self.graph]

    def __str__(self):

        res = ''
        idx = 0

        for vtx in self.graph:
            res += f'{idx} -> {' '.join(map(str, vtx))}' + '\n'
            idx += 1

        return res


    def add_edge(self, vtx1, vtx2, weight):

        if 0 <= vtx1 < self.num_vertices and 0 <= vtx2 < self.num_vertices:
            self.graph[vtx1][vtx2] = weight

            if self.undir:
                self.graph[vtx2][vtx1] = weight

    def add_vertex(self):

        self.num_vertices += 1

        for vtx in self.graph:
            vtx.append(0)
        
        self.graph.append([0]*self.num_vertices)

    def remove_edge(self, vtx1, vtx2):

        if 0 <= vtx1 < self.num_vertices and 0 <= vtx2 < self.num_vertices:
            self.graph[vtx1][vtx2] = 0

            if self.undir:
                self.graph[vtx2][vtx1] = 0
    
    def remove_vertex(self, vtx):
        pass