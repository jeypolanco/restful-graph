import random

class RandomGraph(object):
    def __init__(self, vertices_num, edges_num):
        self.vertices_num = vertices_num
        self.vertices = range(vertices_num)
        self.edges = self.gen_edges(edges_num)
        self.random_vertice = random.randrange(0, self.vertices_num)
        
    def gen_edges(self, edges_num):
        x = map(lambda x: random.randrange(0, self.vertices_num), xrange(10))
        y = map(lambda x: random.randrange(0, self.vertices_num), xrange(10))
        edges = []
        for i,j in zip(x,y):
            edges.append((i,j))
        return edges


z = RandomGraph(4,5)
j = [random.randrange(0, 10) for x in xrange(10)]
