
class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_X(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    

vector = Vector2d(88 , 75)
x = vector.get_X()
y = vector.get_y()

print(f"x: {x}, y: {y}")