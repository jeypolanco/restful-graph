import random

class RandomGraph(object):
    def __init__(self, vertices_num):
        self.vertices = xrange(vertices_num)
        self.graph = dict(enumerate(self.edges(vertices_num)))

    def edges(self, vert_num):
        # Maps each possible vertice to a list of possible adjacent vertices.
        # The lambda ensures that the vertice being mapped isn't included as a
        # possible adjacent vertice
        verts = map(lambda x: (y for y in xrange(vert_num) if x != y), xrange(vert_num))
        for edges in verts:
            # Yields a list of vertices connected to single vertex.  The lambda
            # function filters the possible vertices randomly.
            yield filter(lambda x: random.choice([True, False]), edges)
