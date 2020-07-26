from pathfinder.square_grid import SquareGrid
from pathfinder import ascii_drawer
from pathfinder.breadth_first_search import breadth_first_search

grid = SquareGrid(30, 15)
grid.walls = []
grid.walls.extend((x, y) for x in range(3, 5) for y in range(3, 12))
grid.walls.extend((x, y) for x in range(13, 15) for y in range(4, 15))
grid.walls.extend((x, y) for x in range(21, 23) for y in range(0, 5))
grid.walls.extend((x, y) for x in range(21, 26) for y in range(5, 7))

start_node = (8, 7)
goal_node = (17, 2)
print("{}\n".format(ascii_drawer.draw_grid(grid)))
parents = breadth_first_search(grid, start_node, goal_node)
print(ascii_drawer.draw_grid(grid, point_to=parents, start=start_node, goal=goal_node))
