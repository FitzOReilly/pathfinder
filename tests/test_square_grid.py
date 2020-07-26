import unittest

from pathfinder.square_grid import SquareGrid


class TestSquareGrid(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_in_bounds(self):
        grid = SquareGrid(20, 10)
        self.assertTrue(grid.in_bounds((0, 0)))
        self.assertTrue(grid.in_bounds((0, 1)))
        self.assertTrue(grid.in_bounds((1, 0)))
        self.assertTrue(grid.in_bounds((19, 9)))
        self.assertFalse(grid.in_bounds((20, 9)))
        self.assertFalse(grid.in_bounds((19, 10)))
        self.assertFalse(grid.in_bounds((20, 10)))

    def test_passable(self):
        grid = SquareGrid(20, 10)
        grid.walls = [(5, 2), (6, 2), (7, 2), (10, 5), (10, 6), (10, 7)]
        self.assertTrue(grid.passable((0, 0)))
        self.assertTrue(grid.passable((4, 2)))
        self.assertFalse(grid.passable((5, 2)))
        self.assertFalse(grid.passable((6, 2)))
        self.assertFalse(grid.passable((7, 2)))
        self.assertTrue(grid.passable((8, 2)))
        self.assertTrue(grid.passable((5, 1)))
        self.assertTrue(grid.passable((5, 3)))
        self.assertTrue(grid.passable((9, 6)))
        self.assertFalse(grid.passable((10, 6)))
        self.assertTrue(grid.passable((11, 6)))

    def test_neighbors(self):
        grid = SquareGrid(20, 10)
        grid.walls = [(5, 2), (6, 2), (7, 2), (10, 5), (10, 6), (10, 7)]
        self.assertEqual(
            sorted(grid.neighbors((1, 1))), sorted([(1, 0), (1, 2), (0, 1), (2, 1)])
        )
        self.assertEqual(
            sorted(grid.neighbors((6, 3))), sorted([(6, 4), (5, 3), (7, 3)])
        )
        self.assertEqual(
            sorted(grid.neighbors((9, 7))), sorted([(9, 6), (9, 8), (8, 7)])
        )


if __name__ == "__main__":
    unittest.main()
