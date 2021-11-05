import unittest
from dijkstra import number_vertices

graph = {'a': {'b': 7, 'd': 9, 'c': 14},
     'b': {'d': 10, 'e': 15},
     'c': {'d': 2, 'f': 9},
     'd': {'e': 11},
     'e': {'f': 6}}

class TestNumberVerticesSimple(unittest.TestCase):

    def test_number_vertices_simple(self):
        self.assertEqual(number_vertices(graph), 6)

if __name__ == '__main__':
    unittest.main()
