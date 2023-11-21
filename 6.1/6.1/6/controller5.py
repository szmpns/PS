from typing import Any, List
from model.core import MoveDirection, Vector2d
from model.animal import Animal
from model.interface import IWorldMap
from model.occupiedError import PositionAlreadyOccupiedError

import time

class OptionsParser:
	@staticmethod
	def parse(move_directions: List[Any]) -> List[MoveDirection]:
		valid_moves: List[MoveDirection] = []
		for move in move_directions:
			try:
				valid_moves.append(MoveDirection(move))
			except ValueError:
				print(f'{move} is not legal move specification')
		
		return valid_moves
	
class Simulation:
    def __init__(self, world_map: IWorldMap, directions: list[MoveDirection], positions: list[Vector2d]) -> None:
        self.world_map = world_map
        self.directions = directions
        self.animals = []

        for position in positions:
            animal = Animal(position)
            try:
                if world_map.place(animal):
                    self.animals.append(animal)
            except PositionAlreadyOccupiedError as error:
                 print(f"{error}")

            self.animals.append(animal)

    def run(self) -> None:
        for direction in self.directions:
            for animal in self.animals:
                self.world_map.move(animal, direction)
                time.sleep(1)
                print(self.world_map)
            else:
                print(self.world_map)