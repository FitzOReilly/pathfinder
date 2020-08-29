import tkinter as tk

from pathfinder.grid_pathfinder import GridPathfinder
from pathfinder.grids import WeightedGrid
from pathfinder.views.tk_grid_view import TkGridView


def run():
    grid = WeightedGrid(30, 20)
    pathfinder = GridPathfinder(grid)
    view = TkGridView(pathfinder)

    window = tk.Tk()
    view.draw_grid(window)
    window.mainloop()


if __name__ == "__main__":
    run()
