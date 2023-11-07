
from typing import Self
from enum import Enum

class MoveDirection(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        if self == MapDirection.EAST:
            return "→"
        elif self == MapDirection.WEST:
            return "←"
        elif self == MapDirection.NORTH:
            return "↑"
        elif self == MapDirection.SOUTH:
            return "↓"
    
    def next(self) -> "MapDirection":
        if self == MapDirection.EAST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.NORTH
        elif self == MapDirection.NORTH:
            return MapDirection.EAST
        
    def previous(self) -> "MapDirection":
        if self == MapDirection.EAST:
            return MapDirection.NORTH
        elif self == MapDirection.NORTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.EAST
    
    def toUnitVector(self) -> "Vector2d":
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)
        
class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def precedes(self , other_Vector2d):
        return self.__x <= other_Vector2d.get_x() and self.__y <= other_Vector2d.get_y()

    def follows(self , other_Vector2d):
        return self.__x >= other_Vector2d.get_x() and self.__y >= other_Vector2d.get_y()

    def add(self , other_Vector2d):
        x_n = self.__x + other_Vector2d.get_x()
        y_n = self.__y + other_Vector2d.get_y()
        return Vector2d(x_n , y_n)

    def subtract(self , other_Vector2d):
        x_n = self.__x - other_Vector2d.get_x()
        y_n = self.__y - other_Vector2d.get_y()
        return Vector2d(x_n , y_n)
    
    def upperRight(self , other_Vector2d):
        x_n = max(self.__x , other_Vector2d.get_x())
        y_n = max(self.__y , other_Vector2d.get_y())
        return Vector2d(x_n , y_n)
    
    def lowerLeft(self , other_Vector2d):
        x_n = min(self.__x , other_Vector2d.get_x())
        y_n = min(self.__y , other_Vector2d.get_y())
        return Vector2d(x_n , y_n)
    
    def opposite(self):
        x_n = self.__x * -1
        y_n = self.__y * -1
        return Vector2d(x_n , y_n)
    
    def __eq__(self, other_Vector2d):
        return self.__x == other_Vector2d.get_x() and self.__y == other_Vector2d.get_y()

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"({self.position.get_x()},{self.position.get_y()}) {self.orientation}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def isAt(self, position: Vector2d) -> bool:
        return self.position == position
    
    def isMap(self, position: Vector2d) -> bool:
        return 0 <= position.get_x() and position.get_x() <=4 and 0 <= position.get_y() and position.get_y() <=4 

    def move(self, direction: MoveDirection) -> None:
        if direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
        elif direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        elif direction == MoveDirection.FORWARD:
            new_position = self.position.add(self.orientation.toUnitVector())
            if self.isMap(new_position):
                self.position = new_position
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position.subtract(self.orientation.toUnitVector())
            if self.isMap(new_position):
                self.position = new_position