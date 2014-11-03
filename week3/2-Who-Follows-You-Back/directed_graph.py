from collections import defaultdict
from queue import Queue


class DirectedGraph:

    def __init__(self):
        self.nodes = defaultdict(set)

    def add_edge(self, node_a, node_b):
        self.nodes[node_a].add(node_b)
        if node_b not in self.nodes:
            self.nodes[node_b] = set()

    def get_neighbours_for(self, node):
        return self.nodes[node]

    def path_between(self, node_a, node_b):
        visited = {node: False for node in self.nodes}
        visited[node_a] = True
        queue = Queue()
        queue.put(node_a)
        while not queue.empty():
            node = queue.get()
            neighbours = self.get_neighbours_for(node)
            for n in neighbours:
                if n == node_b:
                    return True
                if not visited[n]:
                    visited[n] = True
                    queue.put(n)
        return False

    def __str__(self):
        string_nodes = []
        for node in self.nodes:
            string_node = [node, ':']
            string_node.extend(self.nodes[node])
            string_node = " ".join(string_node)
            string_nodes.append(string_node)
        return '\n'.join(string_nodes)
