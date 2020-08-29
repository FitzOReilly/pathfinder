from functools import partial
from queue import Queue

from kivy.app import App
from kivy.clock import Clock
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
    def __init__(self):
        super().__init__()
        self._update_interval_in_sec = 0.001
        self._pathfinder = None
        self._node_style = NodeStyle.PASSABLE
        self._paint_queue = Queue()
        self._clock_event = None

    def on_stop(self):
        self._pathfinder.unsubscribe(self)
        self.root_window.close()

    def bind(self, pathfinder):
        if self._pathfinder is not None:
            self._pathfinder.unsubscribe(self)

        self._pathfinder = pathfinder
        self._pathfinder.subscribe(self)

        self._layout()

    def set_style(self, instance, style):
        self._node_style = style

    def modify_tile(self, instance, node_id):
        self._pathfinder.modify_node(node_id, self._node_style)

    def paint_tile(self, widget, style):
        widget.background_color = tile_colors[style]

    def paint_callback(self, instance, *args):
        if self._paint_queue.empty():
            Clock.unschedule(self._clock_event)
            self._clock_event = None
            return

        node_id, style = self._paint_queue.get()
        idx = self.to_idx(node_id)
        grid_layout = self.root.children[1]
        widget = grid_layout.children[idx]
        self.paint_tile(widget, style)

    def update(self, node_id, style):
        self._paint_queue.put((node_id, style))
        if self._clock_event is None:
            self._clock_event = Clock.schedule_interval(
                self.paint_callback, self._update_interval_in_sec
            )

    def to_idx(self, node_id):
        x, y = node_id
        grid_layout = self.root.children[1]
        idx = self._pathfinder.grid.width * y + x
        return len(grid_layout.children) - 1 - idx

    def search(self, instance):
        self._pathfinder.search()

    def build(self):
        return self.root

    def _draw_grid(self):
        rows = self._pathfinder.grid.height
        cols = self._pathfinder.grid.width
        grid_layout = GridLayout(rows=rows, cols=cols)
        for row in range(rows):
            for col in range(cols):
                btn = Button(background_color=tile_colors[NodeStyle.PASSABLE])
                btn.bind(on_press=partial(self.modify_tile, node_id=(col, row)))
                grid_layout.add_widget(btn)
        return grid_layout

    def _layout(self):
        main_layout = BoxLayout(orientation="vertical")
        grid_layout = self._draw_grid()
        main_layout.add_widget(grid_layout)
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))
        passable_btn = Button(text="Passable")
        passable_btn.bind(on_press=partial(self.set_style, style=NodeStyle.PASSABLE))
        unpassable_btn = Button(text="Wall")
        unpassable_btn.bind(
            on_press=partial(self.set_style, style=NodeStyle.UNPASSABLE)
        )
        start_btn = Button(text="Start")
        start_btn.bind(on_press=partial(self.set_style, style=NodeStyle.START))
        goal_btn = Button(text="Goal")
        goal_btn.bind(on_press=partial(self.set_style, style=NodeStyle.GOAL))
        search_btn = Button(text="Fire!")
        search_btn.bind(on_press=self.search)
        button_layout.add_widget(passable_btn)
        button_layout.add_widget(unpassable_btn)
        button_layout.add_widget(start_btn)
        button_layout.add_widget(goal_btn)
        button_layout.add_widget(search_btn)
        main_layout.add_widget(button_layout)
        self.root = main_layout
