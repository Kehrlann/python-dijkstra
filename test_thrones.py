import unittest
from dijkstra import *


class TestThrones(unittest.TestCase):

    def test_number_vertices(self):
        graph = parse_graph("thrones.csv")
        self.assertEqual(number_vertices(graph), 107)

    def test_reachables(self):
        graph = parse_graph("thrones.csv")
        self.assertEqual(len(reachables(graph, 'Eddard')), 88)
        self.assertEqual(len(reachables(graph, 'Bran')), 42)
        self.assertEqual(reachables(graph, 'Davos'), {'Cressen', 'Davos', 'Salladhor'})

    def test_shortest_distance(self):
        graph = parse_graph("thrones.csv")
        self.assertEqual(shortest_distance(graph, 'Eddard', 'Doran'), 15)
        self.assertEqual(shortest_distance(graph, 'Margery', 'Eddard'), None)

if __name__ == '__main__':
    unittest.main()
