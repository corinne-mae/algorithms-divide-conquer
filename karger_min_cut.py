import re
import random
import sys


# Load the file into a graph represented by a dict of lists
def load_graph(fpath):
    g = {}

    with open(fpath) as f:
        for line in f.readlines():
            line = line.strip('\t\\\n').split("\t")
            g[int(line[0])] = [int(s) for s in line[1:]]

    return g


# Contract an edge between 2 vertices
def contract_edge(edge):
    global g

    # merge v2 into v1 and remove v2 from graph
    v1l = g[edge[0]]
    v1l.extend(g[edge[1]])
    del g[edge[1]]

    # replace all occurrences of v2 value with v1
    for k, l in g.iteritems():
        g[k] = [edge[0] if x == edge[1] else x for x in g[k]]

    # remove all edges of v1 that point to itself
    g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]]


# Pick random edge in the current graph
def get_random_edge():
    v1 = g.keys()[random.randint(0, len(g) - 1)]
    v2 = g[v1][random.randint(0, len(g[v1]) - 1)]
    return (v1, v2)


if __name__ == '__main__':

    file_path = sys.argv[1]

    min_list = []

    # Repeat 10 times
    for i in xrange(0, 20):
        g = load_graph(file_path)

        # Keep contracting the graph until we have 2 vertices
        while len(g) > 2:
            contract_edge(get_random_edge())

        min_list.append(len(g[g.keys()[0]]))

    sys.stdout.write("minimum cut is : {0}".format(min(min_list)))
