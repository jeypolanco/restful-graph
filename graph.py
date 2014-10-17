import random
import itertools

def random_edges(vertices_num, edge_num):
    # the random edges must not repeat (i, e) != (e, i), a vertice cannot
    # touch itself ! (i, i)
    combinations = itertools.combinations(xrange(vertices_num), 2)
    # randomly choose amongst the combinations and don't repeat        
    edges = random.sample(list(combinations), edge_num)
    for edge in edges:
        yield edge
