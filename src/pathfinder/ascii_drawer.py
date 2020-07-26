def draw_tile(grid, node_id, tile_width, style):
    tile_str = "."
    if "point_to" in style and style["point_to"].get(node_id) is not None:
        (x0, y0) = node_id
        (x1, y1) = style["point_to"][node_id]
        dx = x1 - x0
        dy = y1 - y0
        if dx == 1 and dy == 0:
            tile_str = ">"
        if dx == -1 and dy == 0:
            tile_str = "<"
        if dx == 0 and dy == 1:
            tile_str = "v"
        if dx == 0 and dy == -1:
            tile_str = "^"
    if "start" in style and node_id == style["start"]:
        tile_str = "A"
    if "goal" in style and node_id == style["goal"]:
        tile_str = "Z"
    if node_id in grid.walls:
        tile_str = "#" * tile_width
    return "{0:{width}}".format(tile_str, width=tile_width)


def draw_grid(grid, tile_width=2, **style):
    grid_str = "\n".join(
        "".join(draw_tile(grid, (x, y), tile_width, style) for x in range(grid.width))
        for y in range(grid.height)
    )
    return grid_str
