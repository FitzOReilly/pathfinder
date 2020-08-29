from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from pathfinder.enums import NodeStyle

tile_colors = {
    NodeStyle.PASSABLE: [0, 1, 1, 1],
    NodeStyle.UNPASSABLE: [0, 0, 0, 0],
    NodeStyle.OUT_OF_BOUNDS: [0, 0, 0, 0],
    NodeStyle.START: [0, 1, 0, 1],
    NodeStyle.GOAL: [1, 0, 0, 1],
    NodeStyle.FRONTIER: [1, 0, 1, 1],
    NodeStyle.VISITED: [0, 0, 1, 1],
    NodeStyle.PATH: [1, 1, 0, 1],
}


class KivyPathfinderApp(App):
    def bind(self, pathfinder):
        self._update_interval_in_sec = 0.01

        self._pathfinder = pathfinder
        self._pathfinder.subscribe(self)

        self._node_style = NodeStyle.PASSABLE

        self.layout()

    def __del__(self):
        self._pathfinder.unsubscribe(self)

    def draw_grid(self):
        rows = self._pathfinder.grid.height
        cols = self._pathfinder.grid.width
        grid_layout = GridLayout(rows=rows, cols=cols)
        for _ in range(rows * cols):
            btn = Button(background_color=tile_colors[NodeStyle.PASSABLE])
            grid_layout.add_widget(btn)
        return grid_layout

    def layout(self):
        main_layout = BoxLayout(orientation="vertical")
        grid_layout = self.draw_grid()
        main_layout.add_widget(grid_layout)
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))
        passable_btn = Button(text="Passable")
        unpassable_btn = Button(text="Wall")
        start_btn = Button(text="Start")
        goal_btn = Button(text="Goal")
        go_btn = Button(text="Fire!")
        button_layout.add_widget(passable_btn)
        button_layout.add_widget(unpassable_btn)
        button_layout.add_widget(start_btn)
        button_layout.add_widget(goal_btn)
        button_layout.add_widget(go_btn)
        main_layout.add_widget(button_layout)
        self.root = main_layout

    def build(self):
        return self.root
