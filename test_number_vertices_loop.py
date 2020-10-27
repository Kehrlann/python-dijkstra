import unittest
from dijkstra import number_vertices

graph = {'a': {'b': 7, 'c': 14},
     'b': {'c': 10, 'a': 6},
     'c': {'b': 2}}

class TestNumberVerticesLoop(unittest.TestCase):

    def test_number_vertices_loop(self):
        self.assertEqual(number_vertices(graph), 3)

if __name__ == '__main__':
    unittest.main()
