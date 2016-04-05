

class Graph:
    '''adjacency-list graph representation

    Each node within the list of vertices contains a list which contains
    the vertices that the node is connected to.

    Example:

        [[1, 2], [0], [0]] -> 1-0-2
        [[1, 2], [0, 2], [0, 2]] -> 0-1-2-0
    '''

    def __init__(self, vertices=1):
        self.vertices = vertices
        self.edges = 0
        self.adjacency = [[] for _ in range(vertices)]

    def __len__(self):
        return self.vertices

    def adjacent(self, vertex):
        return self.adjacency[vertex]

    def connect(self, a, b):
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)
        self.edges += 1

    def degree(self, vertex):
        return len(self.adjacency[vertex])

    def average_degree(self):
        return 2 * self.edges / self.vertices

    def maximum_degree(self):
        degrees = [degree(v) for v in range(self.vertices)]
        degrees.sort()
        return degrees[-1]

