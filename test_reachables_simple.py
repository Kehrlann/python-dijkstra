import unittest
from dijkstra import reachables

graph = {'a': {'b': 7, 'd': 9, 'c': 14},
     'b': {'d': 10, 'e': 15},
     'c': {'d': 2, 'f': 9},
     'd': {'e': 11},
     'e': {'f': 6}}

expected_reachables = [
    ('a', {'a', 'b', 'c', 'd', 'e', 'f'}),
    ('b', {'b', 'd', 'e', 'f'}),
    ('c', {'c', 'd', 'e', 'f'}),
    ('d', {'d', 'e', 'f'}),
    ('e', {'e', 'f'}),
    ('f', {'f'}),
]

class TestReachablesSimple(unittest.TestCase):

    def test_reachables_simple(self):
        for (s, expected) in expected_reachables:
            computed = reachables(graph, s)
            error_message = f"reachables does not work for vertex {s}"
            self.assertEqual(computed,  expected, error_message)

if __name__ == '__main__':
    unittest.main()
