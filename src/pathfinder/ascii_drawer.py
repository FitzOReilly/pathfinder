def draw_tile(grid, node_id, tile_width):
    tile_str = "."
    if node_id in grid.walls:
        tile_str = "#" * tile_width
    return "{0:{width}}".format(tile_str, width=tile_width)


def draw_grid(grid, tile_width=2):
    grid_str = "\n".join(
        "".join(draw_tile(grid, (x, y), tile_width) for x in range(grid.width))
        for y in range(grid.height)
    )
    return grid_str
