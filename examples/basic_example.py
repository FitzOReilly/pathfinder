from pathfinder.graph import Graph
from pathfinder.breadth_first_search import breadth_first_search

example_graph = Graph()
example_graph.edges = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["A"],
    "D": ["E", "A"],
    "E": ["B"],
}

breadth_first_search(example_graph, "A")
