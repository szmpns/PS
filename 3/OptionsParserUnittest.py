
from controller import OptionsParser
from model import MoveDirection
import unittest

class TestOptionsPraser(unittest.TestCase):
    def test_ok_parse(self):
        arguments = ["FORWARD" , "BACKWARD" , "FORWARD" , "LEFT" , "RIGHT"]
        result = OptionsParser.parse(arguments)
        expected_result = [MoveDirection.FORWARD , MoveDirection.BACKWARD , MoveDirection.FORWARD , MoveDirection.LEFT , MoveDirection.RIGHT]
        self.assertEqual(result , expected_result)
    
    def test_not_ok_prase(self):
        arguments = ["LAJKONIK" , "LEFT" , ";EFT" , "LEFT" , "FORWARD" , "BACKWARD" , "RIGHT"]
        result = OptionsParser.parse(arguments)
        expected_result = [MoveDirection.LEFT , MoveDirection.LEFT , MoveDirection.FORWARD , MoveDirection.BACKWARD , MoveDirection.RIGHT]
        self.assertEqual(result , expected_result)