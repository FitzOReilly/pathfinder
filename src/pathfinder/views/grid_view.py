import tkinter as tk
from functools import partial

from pathfinder.algorithms import a_star_search, reconstruct_path

tile_colors = {
    "passable": "grey",
    "unpassable": "black",
    "out_of_bounds": "black",
    "start": "green",
    "goal": "red",
    "frontier": "purple",
    "visited": "blue",
    "path": "yellow",
}


class GridView:
    def __init__(self, grid):
        self._grid = grid
        self._mark_style = "passable"
        self._start = None
        self._goal = None
        self._path = None

    def set_style(self, style):
        self._mark_style = style

    def mark_tile(self, widget, style):
        widget["bg"] = tile_colors[style]

    def update_tile(self, event, node_id):
        self.clear_path()

        if self._start == node_id:
            self._start = None
        elif self._goal == node_id:
            self._goal == None

        if node_id in self._grid.walls:
            self._grid.walls.remove(node_id)

        if self._mark_style == "start":
            if self._start is not None:
                x, y = self._start
                idx = self._grid.width * y + x
                self.mark_tile(self._frm_tiles[idx], "passable")
            self._start = node_id
        if self._mark_style == "goal":
            if self._goal is not None:
                x, y = self._goal
                idx = self._grid.width * y + x
                self.mark_tile(self._frm_tiles[idx], "passable")
            self._goal = node_id
        if self._mark_style == "unpassable":
            self._grid.walls.append(node_id)

        x, y = node_id
        idx = self._grid.width * y + x
        self.mark_tile(self._frm_tiles[idx], self._mark_style)

    def search(self):
        self.clear_path()

        if None in [self._start, self._goal]:
            return

        came_from, cost_so_far = a_star_search(self._grid, self._start, self._goal)
        self._path = reconstruct_path(came_from, self._start, self._goal)
        for node_id in self._path:
            x, y = node_id
            idx = self._grid.width * y + x
            self.mark_tile(self._frm_tiles[idx], "path")

    def clear_path(self):
        if self._path is not None:
            for node_id in self._path:
                x, y = node_id
                idx = self._grid.width * y + x
                self.mark_tile(self._frm_tiles[idx], "passable")
            self._path = None

    def draw_grid(self, master):
        frm_map = tk.Frame(master=master)
        self._frm_tiles = self._grid.height * self._grid.width * [None]
        for row in range(self._grid.height):
            for col in range(self._grid.width):
                idx = self._grid.width * row + col
                self._frm_tiles[idx] = tk.Frame(
                    master=frm_map, width=20, height=20, bg=tile_colors["passable"]
                )
                self._frm_tiles[idx].grid(row=row, column=col, padx=1, pady=1)
                self._frm_tiles[idx].bind(
                    "<Button-1>", partial(self.update_tile, node_id=(col, row))
                )

        frm_map.grid(row=0, column=0)

        frm_buttons = tk.Frame(master=master)
        btn_empty = tk.Button(
            master=frm_buttons,
            text="Empty",
            command=partial(self.set_style, style="passable"),
        )
        btn_wall = tk.Button(
            master=frm_buttons,
            text="Wall",
            command=partial(self.set_style, style="unpassable"),
        )
        btn_start = tk.Button(
            master=frm_buttons,
            text="Start",
            command=partial(self.set_style, style="start"),
        )
        btn_goal = tk.Button(
            master=frm_buttons,
            text="Goal",
            command=partial(self.set_style, style="goal"),
        )

        btn_search = tk.Button(master=frm_buttons, text="Fire!", command=self.search)

        btn_empty.grid(row=0, column=0)
        btn_wall.grid(row=0, column=1)
        btn_start.grid(row=0, column=2)
        btn_goal.grid(row=0, column=3)
        btn_search.grid(row=0, column=4)

        frm_buttons.grid(row=1, column=0)
