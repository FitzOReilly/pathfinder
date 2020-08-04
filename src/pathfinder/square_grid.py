class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, node_id):
        (x, y) = node_id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, node_id):
        return node_id not in self.walls

    def neighbors(self, node_id):
        (x, y) = node_id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        # TODO Understand what's going on here
        if (x + y) % 2 == 0:
            results.reverse()  # Aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class WeightedGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        # Ignore from_node
        return self.weights.get(to_node, 1)
