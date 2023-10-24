
from model import MoveDirection

class OptionsParser:
    
    def parse(args):
        directions = [MoveDirection.FORWARD , MoveDirection.BACKWARD , MoveDirection.LEFT , MoveDirection.RIGHT]
        bucket = []

        for move in args:
            if move == "FORWARD":
                bucket.append(MoveDirection.FORWARD)
            elif move == "BACKWARD":
                bucket.append(MoveDirection.BACKWARD)
            elif move == "LEFT":
                bucket.append(MoveDirection.LEFT)
            elif move == "RIGHT":
                bucket.append(MoveDirection.RIGHT)

        return bucket