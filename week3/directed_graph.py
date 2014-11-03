from collections import defaultdict


class DirectedGraph:

    def __init__(self):
        self.nodes = defaultdict(list)

    def add_edge(self, node_a, node_b):
        self.nodes[node_a].append(node_b)
        if node_b not in self.nodes:
            self.node[node_b] = []



