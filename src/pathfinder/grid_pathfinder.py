from pathfinder import algorithms as algos
from pathfinder.enums import NodeStyle
from pathfinder.event_manager import EventManager


class GridPathfinder:
    def __init__(self, grid):
        self._grid = grid
        self._start = None
        self._goal = None
        self._visited = set()
        self._path = None

        self._strategy = algos.a_star_search
        self._events = EventManager()

    @property
    def grid(self):
        return self._grid

    def modify_node(self, node_id, style):
        self.clear_path()
        pass

        if self._start == node_id:
            self._start = None
        elif self._goal == node_id:
            self._goal = None

        if node_id in self._grid.walls:
            self._grid.walls.remove(node_id)

        if style == NodeStyle.START:
            if self._start is not None:
                self._events.notify(self._start, NodeStyle.PASSABLE)
            self._start = node_id
        if style == NodeStyle.GOAL:
            if self._goal is not None:
                self._events.notify(self._goal, NodeStyle.PASSABLE)
            self._goal = node_id
        if style == NodeStyle.UNPASSABLE:
            self._grid.walls.append(node_id)

        self._events.notify(node_id, style)

    def search(self):
        self.clear_path()

        if None in [self._start, self._goal]:
            return

        came_from, cost_so_far = self._strategy(
            self._grid, self._start, self._goal, event_manager=self._events
        )
        self._path = algos.reconstruct_path(came_from, self._start, self._goal)
        for node_id in self._path:
            self._events.notify(node_id, NodeStyle.PATH)

    def clear_path(self):
        if self._path is not None:
            for node_id in self._path + list(self._visited):
                self._events.notify(node_id, NodeStyle.PASSABLE)
            self._path.clear()
        self._visited.clear()

    def subscribe(self, observer):
        self._events.subscribe(observer)

    def unsubscribe(self, observer):
        self._events.unsubscribe(observer)
