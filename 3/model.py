
from enum import Enum

class MoveDirection(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def precedes(self , other_Vector2d):
        return self.__x <= other_Vector2d.get_x() and self.__y <= other_Vector2d.get_y()

    def follows(self , other_Vector2d):
        return self.__x >= other_Vector2d.get_x() and self.__y >= other_Vector2d.get_y()

    def add(self , other_Vector2d):
        x_n = self.__x + other_Vector2d.get_x()
        y_n = self.__y + other_Vector2d.get_y()
        return Vector2d(x_n , y_n)

    def subtract(self , other_Vector2d):
        x_n = self.__x - other_Vector2d.get_x()
        y_n = self.__y - other_Vector2d.get_y()
        return Vector2d(x_n , y_n)
    
    def upperRight(self , other_Vector2d):
        x_n = max(self.__x , other_Vector2d.get_x())
        y_n = max(self.__y , other_Vector2d.get_y())
        return Vector2d(x_n , y_n)
    
    def lowerLeft(self , other_Vector2d):
        x_n = min(self.__x , other_Vector2d.get_x())
        y_n = min(self.__y , other_Vector2d.get_y())
        return Vector2d(x_n , y_n)
    
    def opposite(self):
        x_n = self.__x * -1
        y_n = self.__y * -1
        return Vector2d(x_n , y_n)
    
    def __eq__(self, other_Vector2d):
        return self.__x == other_Vector2d.get_x() and self.__y == other_Vector2d.get_y()

# vector = Vector2d(88 , 75)
# x = vector.get_x()
# y = vector.get_y()

# print(vector)

# print(f"x: {x}, y: {y}")

# v1 = Vector2d(1 , 2)
# v2 = Vector2d(55, 95)
# v3 = Vector2d(0 , 0)

# print("Precedes")

# print(v1.precedes(v2))
# print(v1.precedes(v3))

# print()

# print("Follows")

# print(v1.follows(v2))
# print(v1.follows(v3))

# print()

# print("Add")

# v4 = v1.add(v2)

# print(v4)

# print()

# print("Subtract")

# v5 = v1.subtract(v2)

# print(v5)

# print()

# print("UpperRight")

# v7 = Vector2d(110 , 23)
# v6 = v2.upperRight(v7)

# print(v6)

# print()
# print("LowerLeft")

# v50 = Vector2d(2 , 4)
# v51 = Vector2d(2 , 3)

# print(v50.__eq__(v51))