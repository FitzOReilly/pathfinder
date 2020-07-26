from queue import Queue


def breadth_first_search(graph, start_node, goal_node):
    frontier = Queue()
    frontier.put(start_node)
    came_from = {}
    came_from[start_node] = None

    while not frontier.empty():
        current_node = frontier.get()

        if current_node == goal_node:
            break

        for next_node in graph.neighbors(current_node):
            if next_node not in came_from:
                frontier.put(next_node)
                came_from[next_node] = current_node

    return came_from
