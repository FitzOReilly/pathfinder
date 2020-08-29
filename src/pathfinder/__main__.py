import threading
import tkinter as tk

from pathfinder.grid_pathfinder import GridPathfinder
from pathfinder.grids import WeightedGrid
from pathfinder.views.kivy_pathfinder_app import KivyPathfinderApp
from pathfinder.views.tk_grid_view import TkGridView


def tk_function(pathfinder):
    view = TkGridView(pathfinder)
    window = tk.Tk()
    view.draw_grid(window)
    window.mainloop()


def kivy_function(pathfinder):
    kivy_app = KivyPathfinderApp()
    kivy_app.bind(pathfinder)
    kivy_app.run()


def run():
    grid = WeightedGrid(30, 20)
    pathfinder = GridPathfinder(grid)

    tk_thread = threading.Thread(target=tk_function, args=(pathfinder,))
    kivy_thread = threading.Thread(target=kivy_function, args=(pathfinder,))

    tk_thread.start()
    kivy_thread.start()

    tk_thread.join()
    kivy_thread.join()


if __name__ == "__main__":
    run()
