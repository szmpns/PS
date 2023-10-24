
from controller import OptionsParser
from model import MoveDirection

##### 
# Z LAB 1
#####

def run(moves , move_descriptions):

    move_list = []

    p_moves = OptionsParser.parse(moves)

    helper = [MoveDirection.FORWARD, MoveDirection.BACKWARD, MoveDirection.LEFT, MoveDirection.RIGHT]

    for move in p_moves:
        if move in helper:
            move_list.append(move_descriptions[move])

    return move_list 

# Przykład użycia:
md = {
    MoveDirection.FORWARD: "Idź do przodu",
    MoveDirection.BACKWARD: "Idź do tyłu",
    MoveDirection.LEFT: "Skręć w lewo",
    MoveDirection.RIGHT: "Skręć w prawo"
}

m = ["FORWARD", "LEFT", "UASDASDAS", "BACKWARD", "RIGHT" , "AHSGDJAGS"] 


print(run(m , md))