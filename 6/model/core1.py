
from enum import Enum
from functools import wraps
from typing import Any, Callable


def log(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        qual_name = func.__qualname__
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        args_str = ', '.join(map(repr, args))
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"Nazwa kwalifikowana: {qual_name}")
        print(f"Argumenty: ({all_args})")
        return func(*args, **kwargs)
    return wrapper


class Vector2d:

    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"
    
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    @log
    def __str__(self) -> str:
        return f'({self.__x},{self.__y})'

    @log
    def precedes(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x <= other_Vector2d.get_x() and self.__y <= other_Vector2d.get_y()

    @log
    def follows(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x >= other_Vector2d.get_x() and self.__y >= other_Vector2d.get_y()

    @log
    def add(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x + other_Vector2d.get_x()
        new_y = self.__y + other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    @log
    def subtract(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x - other_Vector2d.get_x()
        new_y = self.__y - other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    @log
    def upperRight(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        max_x = max(self.__x, other_Vector2d.get_x())
        max_y = max(self.__y, other_Vector2d.get_y())
        return Vector2d(max_x, max_y)

    @log
    def lowerLeft(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        min_x = min(self.__x, other_Vector2d.get_x())
        min_y = min(self.__y, other_Vector2d.get_y())
        return Vector2d(min_x, min_y)

    @log
    def opposite(self) -> 'Vector2d':
        return Vector2d(-self.__x, -self.__y)

    @log
    def __eq__(self, other_Vector2d: object) -> bool:
        if isinstance(other_Vector2d, Vector2d):
            return self.__x == other_Vector2d.get_x() and self.__y == other_Vector2d.get_y()
        return False
    
    @log
    def __ne__(self, other_Vector2d: object) -> bool:
        return not self.__eq__(other_Vector2d)

    @log
    def __hash__(self):
        return hash((self.__x, self.__y))
    
class MoveDirection(Enum):
    FORWARD = 'f'
    BACKWARD = 'b'
    LEFT = 'l'
    RIGHT = 'r'

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        directions = {
			MapDirection.NORTH: "↑",
			MapDirection.EAST: "→",
			MapDirection.SOUTH: "↓",
			MapDirection.WEST: "←",
		}
        return directions[self]

    def next(self) -> 'MapDirection':
        return MapDirection((self.value + 1) % 4)

    def previous(self) -> 'MapDirection':
        return MapDirection((self.value - 1) % 4)

    def toUnitVector(self):
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        else:
            return Vector2d(0, 0)