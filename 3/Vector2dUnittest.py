
from model import Vector2d
import unittest

class TestVector2d(unittest.TestCase):
    def test_precedes(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v1.precedes(v2)
        self.assertTrue(result)  

    def test_does_not_precede(self):
        v1 = Vector2d(3, 4)
        v2 = Vector2d(1, 2)
        result = v1.precedes(v2)
        self.assertFalse(result)  

    def test_add(self):
        v1 = Vector2d(55 , 66)
        v2 = Vector2d(14 , 89)
        result = v1.add(v2)
        self.assertEqual(result.get_x() , 69)
        self.assertEqual(result.get_y() , 155)
    
    def test_subtract(self):
        v1 = Vector2d(13 , 27)
        v2 = Vector2d(5 , 11)
        result = v1.subtract(v2)
        self.assertEqual(result.get_x() , 8)
        self.assertEqual(result.get_y() , 16)
    
    def test_upperRight(self):
        v1 = Vector2d(15 , 27)
        v2 = Vector2d(400 , 11)
        result = v1.upperRight(v2)
        self.assertEqual(result.get_x() , 400)
        self.assertEqual(result.get_y() , 27)

    def test_lowerLeft(self):
        v1 = Vector2d(27 , 27)
        v2 = Vector2d(26, 11)
        result = v1.lowerLeft(v2)
        self.assertEqual(result.get_x() , 26)
        self.assertEqual(result.get_y() , 11)

    def test_opposite(self):
        v1 = Vector2d(44 , 49)
        result = v1.opposite()
        self.assertEqual(result.get_x() , -44)
        self.assertEqual(result.get_y() , -49)


if __name__ == "__main__":
    unittest.main()