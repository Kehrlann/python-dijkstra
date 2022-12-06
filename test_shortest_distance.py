import unittest
from dijkstra import shortest_distance


class TestShortestDistance(unittest.TestCase):

    def test_shortest_distance_simple(self):
        graph = {'a': {'b': 7, 'd': 9, 'c': 14},
                 'b': {'d': 10, 'e': 15},
                 'c': {'d': 2, 'f': 9},
                 'd': {'e': 11},
                 'e': {'f': 6}}
        self.assertEqual(shortest_distance(graph, 'a', 'f'), 23)
        self.assertEqual(shortest_distance(graph, 'a', 'e'), 20)
        self.assertEqual(shortest_distance(graph, 'c', 'b'), None)

    def test_shortest_distance_many_hops(self):
        graph = {'a': {'b': 1, 'e': 10},
                 'b': {'c': 1},
                 'c': {'d': 1},
                 'd': {'e': 1}}
        self.assertEqual(shortest_distance(graph, 'a', 'e'), 4)


if __name__ == '__main__':
    unittest.main()
