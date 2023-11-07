

from model4 import MoveDirection, Vector2d, Animal

class OptionsParser:
    
    def parse(args):
        dictionary = {
            "f": MoveDirection.FORWARD,
            "b": MoveDirection.BACKWARD,
            "l": MoveDirection.LEFT,
            "r": MoveDirection.RIGHT
        }
        bucket = []

        for move in args:
            if move in dictionary:
                bucket.append(dictionary[move])

        return bucket
    
class Simulation:
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d]) -> None:
        self.directions = directions
        self.animals = [Animal(position) for position in positions]
        self.current_animal = 0

    def run(self) -> None:
        n_animals = len(self.animals)
        for direction in self.directions:
            animal = self.animals[self.current_animal]
            animal.move(direction)
            print(f"Zwierzę {self.current_animal} : {animal.position} {animal.orientation}")
            self.current_animal = (self.current_animal + 1) % n_animals  # Popraw ta linijkę
