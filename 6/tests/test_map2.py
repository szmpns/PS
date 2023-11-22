import pytest
from model.map import InfiniteMap
from model.animal import Animal
from model.core import Vector2d, MoveDirection
from model.occupiedError import PositionAlreadyOccupiedError
        
@pytest.fixture
def infinite_map():
    yield InfiniteMap()
    
@pytest.fixture
def animal1():
    yield Animal(Vector2d(0, 0))

@pytest.fixture
def animal2():
    yield Animal(Vector2d(3, 3))

@pytest.fixture
def animal3():
    yield Animal(Vector2d(1, 1))

@pytest.fixture
def animal4():
    yield Animal(Vector2d(-1, -2))

def test_for_infinite_map(
    infinite_map: InfiniteMap,
    animal1: Animal,
    animal2: Animal,
    animal3: Animal,
    animal4: Animal,
):
    # Testing methods of the 'Animal' class
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.RIGHT, infinite_map)
    animal1.move(MoveDirection.FORWARD, infinite_map)
    assert animal1.isAt(Vector2d(1, 0)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    animal1.move(MoveDirection.LEFT, infinite_map)
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, -1)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, 0)) is False
    # Testing the correctness of the implementation of methods inherited from abstract classes: 'IWorldMap' and 'IMoveValidator'
    assert infinite_map.canMoveTo(Vector2d(-1, -1)) is True
    assert infinite_map.canMoveTo(Vector2d(4, 4)) is True
    assert infinite_map.canMoveTo(Vector2d(0, 0)) is True
    assert infinite_map.place(animal1) is True
    assert infinite_map.canMoveTo(Vector2d(0, 0)) is False
    assert infinite_map.isOccupied(Vector2d(0, 0)) is True
    with pytest.raises(PositionAlreadyOccupiedError, match=r"Position \(-?\d+,-?\d+\) is already occupied"):
        infinite_map.place(animal1)
    assert infinite_map.place(animal2) is True
    assert infinite_map.place(animal3) is True
    assert infinite_map.place(animal4) is True
    assert infinite_map.objectAt(Vector2d(0, 0)) is animal1
    infinite_map.move(animal1, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(0, 1)) is animal1
    assert infinite_map.objectAt(Vector2d(0, 0)) is None
    infinite_map.move(animal1, MoveDirection.RIGHT)
    infinite_map.move(animal1, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(1, 1)) is not animal1
    assert infinite_map.objectAt(Vector2d(1, 1)) is animal3
    infinite_map.move(animal4, MoveDirection.LEFT)
    infinite_map.move(animal4, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(-1, -2)) is None
    assert infinite_map.objectAt(Vector2d(-2, -1)) is animal4
