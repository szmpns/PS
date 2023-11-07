
import sys
from model4 import Vector2d, MoveDirection
from controller4 import Simulation, OptionsParser

directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:]) 
positions: list[Vector2d] = [Vector2d(2,2), Vector2d(3,4)] # Pozycje początkowe dla zwierząt, odpowiednio, (2,2) oraz (3,4) 
simulation: Simulation = Simulation(directions, positions)
simulation.run()     

# animal_1 = Animal(Vector2d(4,7) , MapDirection.EAST)

# print(animal_1)