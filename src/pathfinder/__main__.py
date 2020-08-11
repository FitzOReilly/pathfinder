import tkinter as tk

from pathfinder.grids import WeightedGrid
from pathfinder.views.grid_view import GridView


def run():
    grid = WeightedGrid(30, 20)
    view = GridView(grid)

    window = tk.Tk()
    view.draw_grid(window)
    window.mainloop()


if __name__ == "__main__":
    run()
