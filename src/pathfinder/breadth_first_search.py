from queue import Queue


def breadth_first_search(graph, start_node):
    frontier = Queue()
    frontier.put(start_node)
    visited = set()
    visited.add(start_node)

    while not frontier.empty():
        current_node = frontier.get()
        print("Visiting {!r}".format(current_node))
        for next_node in graph.neighbors(current_node):
            if next_node not in visited:
                frontier.put(next_node)
                visited.add(next_node)
