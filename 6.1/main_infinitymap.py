#!/usr/bin/env python3
import sys
from model.core import Vector2d, MoveDirection
from model.interface import IWorldMap
from model.map import InfiniteMap
from controller5 import Simulation, OptionsParser
from model.occupiedError import PositionAlreadyOccupiedError

try:
    directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
    positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4)]
    map: IWorldMap = InfiniteMap()
    simulation: Simulation = Simulation(map ,directions, positions)
    simulation.run()
except ValueError as error:
    print(f"Error: {error}")
except PositionAlreadyOccupiedError as error:
    print(f"Error: {error}")