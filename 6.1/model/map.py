from typing import Dict, Optional

from model.core import Vector2d, MoveDirection, MapDirection
from model.animal import Animal
from model.view import MapVisualizer
from model.interface import IMoveValidator, IWorldMap
from abc import ABC

from model.occupiedError import PositionAlreadyOccupiedError


class WorldMap(IMoveValidator, IWorldMap, ABC):
    def __init__(self, width: int = -1, height: int = -1):
        self.width = width
        self.height = height
        self.animals: Dict[Vector2d, Animal] = {}

    def place(self, animal: Animal) -> bool:
        if self.canMoveTo(animal.position):
            self.animals[animal.position] = animal
            return True
        else:
            raise PositionAlreadyOccupiedError(animal.position)

    def move(self, animal: Animal, direction: MoveDirection) -> None:
        (new_position, orientation) = self._calculate_new_position(animal.position, direction)

        if self.canMoveTo(new_position):
            del self.animals[animal.position]
            animal.position = new_position
            animal.orientation = orientation
            self.animals[new_position] = animal

    def _calculate_new_position(self, position: Vector2d, direction: MoveDirection) -> tuple[Vector2d, MapDirection]:
        if direction == MoveDirection.FORWARD:
            return (position.add(MapDirection.NORTH.toUnitVector()), MapDirection.NORTH)
        elif direction == MoveDirection.BACKWARD:
            return (position.add(MapDirection.SOUTH.toUnitVector()), MapDirection.SOUTH)
        elif direction == MoveDirection.LEFT:
            return (position.add(MapDirection.WEST.toUnitVector()), MapDirection.WEST)
        elif direction == MoveDirection.RIGHT:
            return (position.add(MapDirection.EAST.toUnitVector()), MapDirection.EAST)

    def objectAt(self, position: Vector2d) -> Optional[Animal]:
        return self.animals.get(position, None)

    def isOccupied(self, position: Vector2d) -> bool:
        return self.objectAt(position) is not None

class RectangularMap(WorldMap):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def __str__(self) -> str:
        lower_left = Vector2d(0, 0)
        upper_right = Vector2d(self.width, self.height)
        visualizer = MapVisualizer(self)
        return visualizer.draw(lower_left, upper_right)

    def canMoveTo(self, position: Vector2d) -> bool:
        return position.follows(Vector2d(0, 0)) and position.precedes(Vector2d(self.width, self.height)) and not self.isOccupied(position)

class InfiniteMap(WorldMap):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        lower_left = Vector2d(0, 0)

        (max_x, max_y) = self.extract_max_coordinates(list(self.animals.keys()))
        
        upper_right = Vector2d(max_x, max_y)
        visualizer = MapVisualizer(self)
        return visualizer.draw(lower_left, upper_right)

    def extract_max_coordinates(self, vector_list: list[Vector2d]) -> tuple[int, int]:
        if not vector_list:
            return (0,0)

        max_x = max(vector_list, key=lambda v: v.get_x()).get_x()
        max_y = max(vector_list, key=lambda v: v.get_y()).get_y()

        return (max_x, max_y)

    def canMoveTo(self, position: Vector2d) -> bool:
        return not self.isOccupied(position)
