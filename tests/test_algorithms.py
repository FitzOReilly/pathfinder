import unittest

from pathfinder.algorithms import a_star_search, dijkstra_search, manhattan_dist
from pathfinder.grids import WeightedGrid


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.weighted_grid = WeightedGrid(10, 10)

        self.weighted_grid.walls = []
        self.weighted_grid.walls.extend(
            (x, y) for x in range(1, 4) for y in range(7, 9)
        )

        self.weighted_grid.weights = {
            loc: 5
            for loc in [
                (3, 4),
                (3, 5),
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 4),
                (4, 5),
                (4, 6),
                (4, 7),
                (4, 8),
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
                (5, 6),
                (5, 7),
                (5, 8),
                (6, 2),
                (6, 3),
                (6, 4),
                (6, 5),
                (6, 6),
                (6, 7),
                (7, 3),
                (7, 4),
                (7, 5),
            ]
        }

        self.weighted_grid_start = (1, 4)
        self.weighted_grid_goal = (7, 8)

    def tearDown(self):
        pass

    def test_manhattan_dist(self):
        self.assertEqual(manhattan_dist((3, 5), (4, 7)), 3)
        self.assertEqual(manhattan_dist((10, 5), (4, 7)), 8)
        self.assertEqual(manhattan_dist((10, 10), (4, 7)), 9)
        self.assertEqual(manhattan_dist((1, 10), (4, 7)), 6)

    def test_dijkstra(self):
        _, cost_dijkstra = dijkstra_search(
            self.weighted_grid, self.weighted_grid_start, self.weighted_grid_goal
        )
        self.assertEqual(cost_dijkstra[self.weighted_grid_goal], 14)

    def test_a_star(self):
        _, cost_a_star = a_star_search(
            self.weighted_grid, self.weighted_grid_start, self.weighted_grid_goal
        )
        self.assertEqual(cost_a_star[self.weighted_grid_goal], 14)


if __name__ == "__main__":
    unittest.main()
