
from model.core import Vector2d, MapDirection, MoveDirection

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