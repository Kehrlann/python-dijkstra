import unittest
from dijkstra import reachables

graph = {'a': {'b': 7, 'c': 14},
     'b': {'c': 10, 'a': 6},
     'c': {'b': 2}}

expected_reachables = [
    ('a', {'a', 'b', 'c'}),
    ('b', {'a', 'b', 'c'}),
    ('c', {'a', 'b', 'c'}),
]

class TestReachablesLoop(unittest.TestCase):

    def test_reachables_loop(self):
        for (s, expected) in expected_reachables:
            computed = reachables(graph, s)
            error_message = f"reachables does not work for vertex {s}"
            self.assertEqual(computed,  expected, error_message)

if __name__ == '__main__':
    unittest.main()
