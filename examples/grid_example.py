from pathfinder.square_grid import SquareGrid
from pathfinder import ascii_drawer

grid = SquareGrid(30, 15)
grid.walls = []
grid.walls.extend((x, y) for x in range(3, 5) for y in range(3, 12))
grid.walls.extend((x, y) for x in range(13, 15) for y in range(4, 15))
grid.walls.extend((x, y) for x in range(21, 23) for y in range(0, 5))
grid.walls.extend((x, y) for x in range(21, 26) for y in range(5, 7))

print(ascii_drawer.draw_grid(grid))
