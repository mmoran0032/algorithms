

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
        self.adjacency = [set() for _ in range(vertices)]

    def __len__(self):
        return self.vertices

    def adjacent(self, vertex):
        return self.adjacency[vertex]

    def connect(self, a, b):
        if a not in self.adjacency[b] and a != b:
            self.adjacency[a].add(b)
            self.adjacency[b].add(a)
            self.edges += 1

    def degree(self, vertex):
        return len(self.adjacency[vertex])

    def average_degree(self):
        return 2 * self.edges / self.vertices

    def maximum_degree(self):
        degrees = [self.degree(v) for v in range(self.vertices)]
        degrees.sort()
        return degrees[-1]


if __name__ == '__main__':
    with open('tiny_graph.txt', 'r') as f:
        data = [line.strip().split() for line in f]
        data = [[int(i) for i in row] for row in data]
    g = Graph(data[0][0])
    for pair in data[1:]:
        g.connect(*pair)
    print(g.adjacency)

