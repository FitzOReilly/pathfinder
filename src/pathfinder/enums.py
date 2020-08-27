from enum import Enum, auto


class NodeStyle(Enum):
    PASSABLE = auto()
    UNPASSABLE = auto()
    OUT_OF_BOUNDS = auto()
    START = auto()
    GOAL = auto()
    FRONTIER = auto()
    VISITED = auto()
    PATH = auto()
