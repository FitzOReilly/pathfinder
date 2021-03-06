from pathfinder.algorithms import breadth_first_search
from pathfinder.graph import Graph

example_graph = Graph()
example_graph.edges = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["A"],
    "D": ["E", "A"],
    "E": ["B"],
}

breadth_first_search(example_graph, "A", "E")
