import unittest

from pathfinder.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_neighbors(self):
        graph = Graph()
        graph.edges = {
            "A": ["B"],
            "B": ["A", "C", "D"],
            "C": ["A"],
            "D": ["E", "A"],
            "E": ["B"],
        }
        self.assertEqual(graph.neighbors("A"), ["B"])
        self.assertEqual(graph.neighbors("D"), ["E", "A"])


if __name__ == "__main__":
    unittest.main()
