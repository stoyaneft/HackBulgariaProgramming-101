import unittest

from directed_graph import DirectedGraph


class GraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_edge(self):
        self.graph.add_edge('Ivan', 'Ivo')
        self.assertIn('Ivan', self.graph.nodes)
        self.assertIn('Ivo', self.graph.nodes)
        self.assertIn('Ivo', self.graph.nodes['Ivan'])

if __name__ == '__main__':
    unittest.main()
