import unittest
from dijkstra import parse_graph

expected_graph = {'a': {'b': 7, 'd': 9, 'c': 14},
     'b': {'d': 10, 'e': 15},
     'c': {'d': 2, 'f': 9},
     'd': {'e': 11},
     'e': {'f': 6}}

class TestParseGraph(unittest.TestCase):

    def test_parse_graph(self):
        parsed = parse_graph("graph.csv")
        self.assertEqual(parsed, expected_graph)

if __name__ == '__main__':
    unittest.main(verbosity=2)
