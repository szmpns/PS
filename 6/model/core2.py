
from enum import Enum
from functools import wraps
from typing import Any, Callable


def log(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any):
        is_property = isinstance(getattr(args[0].__class__, func.__name__, None), property)
        instance = args[0]
        class_name = instance.__class__.__name__
        method_name = func.__name__
        qualified_name = f"{class_name}.{method_name}"
        result = func(*args, **kwargs)

        if is_property:
            def log() -> int:
                print(f"Nazwa kwalifikowana: {qualified_name}")
                print(f"Value {result}")
                return result
            return log
        else:
            arguments = ", ".join(map(str, args))
            print(f"Nazwa kwalifikowana: {qualified_name}")
            print(f"Argumenty: {arguments}")
            return result

    return wrapper




class Vector2d:

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"
    
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

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