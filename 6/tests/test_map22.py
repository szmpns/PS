import pytest
from model.map import InfiniteMap
from model.animal import Animal
from model.core import Vector2d, MoveDirection
        
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
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, -1)) is True
    animal1.move(MoveDirection.FORWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, 0)) is True
    assert infinite_map.place(animal1) is True
    assert infinite_map.place(animal2) is True
    assert infinite_map.place(animal3) is True
    assert infinite_map.place(animal4) is True
    assert infinite_map.canMoveTo(Vector2d(0, 0)) is False
    assert infinite_map.canMoveTo(Vector2d(-2, -1)) is True
    assert infinite_map.objectAt(Vector2d(3, 3)) is animal2
    infinite_map.move(animal2, MoveDirection.LEFT)
    assert infinite_map.objectAt(Vector2d(2, 3)) is animal2
    assert infinite_map.objectAt(Vector2d(3, 3)) is None

def test_move_invalid_directions(infinite_map, animal1):
    assert animal1.isAt(Vector2d(0, 0)) is True
    initial_position = animal1.position  
    try:
        animal1.move("INVALID_DIRECTION", infinite_map)
    except ValueError:
        pass 
    assert animal1.position == initial_position

# def test_move_invalid_directions(infinite_map, animal1):
#     assert animal1.isAt(Vector2d(0, 0)) is True
#     # Moving in an invalid direction should not change animal's position
#     animal1.move("INVALID_DIRECTION", infinite_map)
#     assert animal1.isAt(Vector2d(0, 0)) is True
