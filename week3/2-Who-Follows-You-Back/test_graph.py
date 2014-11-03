import unittest

from directed_graph import DirectedGraph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_edge('Ivan', 'Ivo')
        self.graph.add_edge('Ivan', 'Joro')
        self.graph.add_edge('Joro', 'Krasi')
        self.graph.add_edge('Krasi', 'Rado')

    def test_add_edge(self):
        self.assertIn('Ivan', self.graph.nodes)
        self.assertIn('Ivo', self.graph.nodes)
        self.assertIn('Ivo', self.graph.nodes['Ivan'])

    def test_get_neighbours_for(self):
        self.assertSetEqual(
            self.graph.get_neighbours_for('Ivan'), {'Ivo', 'Joro'})

    def test_path_between_exists(self):
        self.assertTrue(self.graph.path_between('Ivan', 'Rado'))

    def test_path_between_not_exist(self):
        self.assertFalse(self.graph.path_between('Krasi', 'Joro'))

    def test_str_graph(self):
        print(self.graph)

if __name__ == '__main__':
    unittest.main()
