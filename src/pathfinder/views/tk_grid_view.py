import time
import tkinter as tk
from functools import partial

from pathfinder.enums import NodeStyle

tile_colors = {
    NodeStyle.PASSABLE: "grey",
    NodeStyle.UNPASSABLE: "black",
    NodeStyle.OUT_OF_BOUNDS: "black",
    NodeStyle.START: "green",
    NodeStyle.GOAL: "red",
    NodeStyle.FRONTIER: "purple",
    NodeStyle.VISITED: "blue",
    NodeStyle.PATH: "yellow",
}


class TkGridView:
    def __init__(self, pathfinder):
        self._update_interval_in_sec = 0.01

        self._pathfinder = pathfinder
        self._pathfinder.subscribe(self)

        self._node_style = NodeStyle.PASSABLE

    def __del__(self):
        self._pathfinder.unsubscribe(self)

    def set_style(self, style):
        self._node_style = style

    def paint_tile(self, widget, style):
        widget["bg"] = tile_colors[style]

    def modify_tile(self, event, node_id):
        self._pathfinder.modify_node(node_id, self._node_style)

    def update(self, node_id, style):
        idx = self.to_idx(node_id)
        self.paint_tile(self._frm_tiles[idx], style)
        self._frm_tiles[idx].update()
        time.sleep(self._update_interval_in_sec)

    def search(self):
        self._pathfinder.search()

    def to_idx(self, node_id):
        x, y = node_id
        idx = self._pathfinder.grid.width * y + x
        return idx

    def draw_grid(self, master):
        frm_map = tk.Frame(master=master)
        self._frm_tiles = (
            self._pathfinder.grid.height * self._pathfinder.grid.width * [None]
        )
        for row in range(self._pathfinder.grid.height):
            for col in range(self._pathfinder.grid.width):
                idx = self._pathfinder.grid.width * row + col
                self._frm_tiles[idx] = tk.Frame(
                    master=frm_map,
                    width=20,
                    height=20,
                    bg=tile_colors[NodeStyle.PASSABLE],
                )
                self._frm_tiles[idx].grid(row=row, column=col, padx=1, pady=1)
                self._frm_tiles[idx].bind(
                    "<Button-1>", partial(self.modify_tile, node_id=(col, row))
                )

        frm_map.grid(row=0, column=0)

        frm_buttons = tk.Frame(master=master)
        btn_empty = tk.Button(
            master=frm_buttons,
            text="Empty",
            command=partial(self.set_style, style=NodeStyle.PASSABLE),
        )
        btn_wall = tk.Button(
            master=frm_buttons,
            text="Wall",
            command=partial(self.set_style, style=NodeStyle.UNPASSABLE),
        )
        btn_start = tk.Button(
            master=frm_buttons,
            text="Start",
            command=partial(self.set_style, style=NodeStyle.START),
        )
        btn_goal = tk.Button(
            master=frm_buttons,
            text="Goal",
            command=partial(self.set_style, style=NodeStyle.GOAL),
        )

        btn_search = tk.Button(master=frm_buttons, text="Fire!", command=self.search)

        btn_empty.grid(row=0, column=0)
        btn_wall.grid(row=0, column=1)
        btn_start.grid(row=0, column=2)
        btn_goal.grid(row=0, column=3)
        btn_search.grid(row=0, column=4)

        frm_buttons.grid(row=1, column=0)
