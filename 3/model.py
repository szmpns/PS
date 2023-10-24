
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

vector = Vector2d(88 , 75)
x = vector.get_x()
y = vector.get_y()

print(vector)

print(f"x: {x}, y: {y}")

v1 = Vector2d(1 , 2)
v2 = Vector2d(55, 95)
v3 = Vector2d(0 , 0)

print(v1.precedes(v2))
print(v1.precedes(v3))