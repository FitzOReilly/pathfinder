from math import dist
from queue import PriorityQueue, Queue

from pathfinder.enums import NodeStyle


def breadth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_ in graph.neighbors(current):
            if next_ not in came_from:
                frontier.put(next_)
                came_from[next_] = current

    return came_from


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for next_ in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_)
            if next_ not in cost_so_far or new_cost < cost_so_far[next_]:
                came_from[next_] = current
                cost_so_far[next_] = new_cost
                frontier.put((new_cost, next_))

    return came_from, cost_so_far


def manhattan_dist(a, b):
    (x0, y0) = a
    (x1, y1) = b
    return abs(x1 - x0) + abs(y1 - y0)


def euclidean_dist(a, b):
    return dist(a, b)


def a_star_search(graph, start, goal, heuristic=euclidean_dist, event_manager=None):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        if current != start:
            if event_manager:
                event_manager.notify(current, NodeStyle.VISITED)

        for next_ in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_)
            if next_ not in cost_so_far or new_cost < cost_so_far[next_]:
                came_from[next_] = current
                cost_so_far[next_] = new_cost
                priority = new_cost + heuristic(next_, goal)
                frontier.put((priority, next_))
                if next_ != goal:
                    if event_manager:
                        event_manager.notify(next_, NodeStyle.FRONTIER)

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []

    current = came_from[goal]
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
