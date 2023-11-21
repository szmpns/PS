from enum import Enum


class Vector2d:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def __str__(self) -> str:
        return f'({self.__x},{self.__y})'

    def precedes(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x <= other_Vector2d.get_x() and self.__y <= other_Vector2d.get_y()

    def follows(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x >= other_Vector2d.get_x() and self.__y >= other_Vector2d.get_y()

    def add(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x + other_Vector2d.get_x()
        new_y = self.__y + other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    def subtract(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x - other_Vector2d.get_x()
        new_y = self.__y - other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    def upperRight(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        max_x = max(self.__x, other_Vector2d.get_x())
        max_y = max(self.__y, other_Vector2d.get_y())
        return Vector2d(max_x, max_y)

    def lowerLeft(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        min_x = min(self.__x, other_Vector2d.get_x())
        min_y = min(self.__y, other_Vector2d.get_y())
        return Vector2d(min_x, min_y)

    def opposite(self) -> 'Vector2d':
        return Vector2d(-self.__x, -self.__y)

    def __eq__(self, other_Vector2d: object) -> bool:
        if isinstance(other_Vector2d, Vector2d):
            return self.get_x() == other_Vector2d.get_x() and self.get_y() == other_Vector2d.get_y()
        return False
    
    def __ne__(self, other_Vector2d: object) -> bool:
        return not self.__eq__(other_Vector2d)

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
            
    