from pathfinder import ascii_drawer
from pathfinder.search import breadth_first_search, dijkstra_search, reconstruct_path
from pathfinder.square_grid import SquareGrid, WeightedGrid

grid = SquareGrid(30, 15)
grid.walls = []
grid.walls.extend((x, y) for x in range(3, 5) for y in range(3, 12))
grid.walls.extend((x, y) for x in range(13, 15) for y in range(4, 15))
grid.walls.extend((x, y) for x in range(21, 23) for y in range(0, 5))
grid.walls.extend((x, y) for x in range(21, 26) for y in range(5, 7))

start = (8, 7)
goal = (17, 2)
print(ascii_drawer.draw_grid(grid))
print()
parents = breadth_first_search(grid, start, goal)
print(ascii_drawer.draw_grid(grid, point_to=parents, start=start, goal=goal))
print()

wgrid = WeightedGrid(10, 10)

wgrid.walls = []
wgrid.walls.extend((x, y) for x in range(1, 4) for y in range(7, 9))

wgrid.weights = {
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

start = (1, 4)
goal = (7, 8)

came_from, cost_so_far = dijkstra_search(wgrid, start, goal)
print(
    ascii_drawer.draw_grid(
        wgrid, tile_width=3, point_to=came_from, start=start, goal=goal
    )
)
print()
print(
    ascii_drawer.draw_grid(
        wgrid, tile_width=3, number=cost_so_far, start=start, goal=goal
    )
)
print()
print(
    ascii_drawer.draw_grid(
        wgrid, tile_width=3, path=reconstruct_path(came_from, start, goal)
    )
)
