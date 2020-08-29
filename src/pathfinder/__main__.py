import tkinter as tk

from pathfinder.grid_pathfinder import GridPathfinder
from pathfinder.grids import WeightedGrid
from pathfinder.views.kivy_pathfinder_app import KivyPathfinderApp
from pathfinder.views.tk_grid_view import TkGridView


def run():
    grid = WeightedGrid(30, 20)
    pathfinder = GridPathfinder(grid)

    view = TkGridView(pathfinder)
    window = tk.Tk()
    view.draw_grid(window)
    window.mainloop()

    kivy_app = KivyPathfinderApp()
    kivy_app.bind(pathfinder)
    kivy_app.run()


if __name__ == "__main__":
    run()
