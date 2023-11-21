
from functools import wraps
from typing import Any, Callable

def log_to(file: str) -> Callable:
    def decorator(cls):
        for attr_name, attr_value in vars(cls).items():
            if callable(attr_value) and not attr_name.startswith("__"):
                setattr(cls, attr_name, log_method_to(attr_value, file))
        return cls
    return decorator

def log_method_to(func: Callable, file: str) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        qual_name = func.__qualname__
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        args_str = ', '.join(map(repr, args))
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))

        log_entry = f"{qual_name} | {all_args}\n"

        with open(file, 'a+') as log_file:
            log_file.write(log_entry)

        return func(*args, **kwargs)
    return wrapper

@log_to('dziennik.txt')
class Vector2d:
    
    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    @property
    @log_to('dziennik.txt')
    def x(self) -> int:
        return self.__x
    
    @x.setter
    def x(self, value: int) -> None:
        self.__x = value
    
    @property
    @log_to('dziennik.txt')
    def y(self) -> int:
        return self.__y
    
    @y.setter
    def y(self, value: int) -> None:
        self.__y = value

    @log_to('dziennik.txt')
    def __str__(self) -> str:
        return f'({self.__x},{self.__y})'

    @log_to('dziennik.txt')
    def precedes(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x <= other_Vector2d.x and self.__y <= other_Vector2d.y

    @log_to('dziennik.txt')
    def follows(self, other_Vector2d: 'Vector2d') -> bool:
        return self.__x >= other_Vector2d.x and self.__y >= other_Vector2d.y
    
    @log_to('dziennik.txt')
    def add(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x + other_Vector2d.x
        new_y = self.__y + other_Vector2d.y
        return Vector2d(new_x, new_y)

    @log_to('dziennik.txt')
    def subtract(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        new_x = self.__x - other_Vector2d.x
        new_y = self.__y - other_Vector2d.y
        return Vector2d(new_x, new_y)
    
    @log_to('dziennik.txt')
    def upperRight(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        max_x = max(self.__x, other_Vector2d.x)
        max_y = max(self.__y, other_Vector2d.y)
        return Vector2d(max_x, max_y)

    @log_to('dziennik.txt')
    def lowerLeft(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        min_x = min(self.__x, other_Vector2d.x)
        min_y = min(self.__y, other_Vector2d.y)
        return Vector2d(min_x, min_y)

    @log_to('dziennik.txt')
    def opposite(self) -> 'Vector2d':
        return Vector2d(-self.__x, -self.__y)

    @log_to('dziennik.txt')
    def __eq__(self, other_Vector2d: object) -> bool:
        if isinstance(other_Vector2d, Vector2d):
            return self.x == other_Vector2d.x and self.y== other_Vector2d.y
        return False
    
    @log_to('dziennik.txt')
    def __ne__(self, other_Vector2d: object) -> bool:
        return not self.__eq__(other_Vector2d)

    @log_to('dziennik.txt')
    def __hash__(self):
        return hash((self.__x, self.__y))