from __future__ import annotations
from typing import Any
from model.core import Vector2d, MapDirection, MoveDirection
# from model.interface import IMoveValidator

from model.occupiedError import PositionAlreadyOccupiedError


class Animal:
    def __init__(self, position: Vector2d = Vector2d(0,0), orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"{self.orientation}"

    def __repr__(self) -> str:
        return str(self)

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection, validator: Any) -> None:

        valid_moves = {MoveDirection.FORWARD, MoveDirection.BACKWARD, MoveDirection.LEFT, MoveDirection.RIGHT}
        if direction not in valid_moves:
            raise ValueError(f'{direction.value} is not a legal move specification')

        new_position = self.position

        if direction == MoveDirection.RIGHT:
            self.orientation = MapDirection((self.orientation.value + 1) % 4)
        elif direction == MoveDirection.LEFT:
            self.orientation = MapDirection((self.orientation.value - 1) % 4)
        elif direction == MoveDirection.FORWARD:
            new_position = self.position.add(self.orientation.toUnitVector())
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position.subtract(self.orientation.toUnitVector())

        try:
            if validator.canMoveTo(new_position):
                self.position = new_position
        except PositionAlreadyOccupiedError as e:
            print(f"Encountered PositionAlreadyOccupiedError: {e}")