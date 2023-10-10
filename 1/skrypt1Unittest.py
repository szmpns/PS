
import unittest
import skrypt1 as s1
from unittest.mock import patch
from io import StringIO
import sys

class TestDisplayAndRun(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_without_index(self , stdout):
        arguments = ['skrypt.py', '1', 'a', '4', 'b']
        s1.display(arguments , False)
        expected_output = 'skrypt.py\n1\na\n4\nb\n'
        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_with_index(self, stdout):
        args = ['skrypt.py', '1', 'a', '4', 'b']
        s1.display(args, True)
        expected_output = 'args[0] = skrypt.py\nargs[1] = 1\nargs[2] = a\nargs[3] = 4\nargs[4] = b\n'
        self.assertEqual(stdout.getvalue(), expected_output)

    def test_run(self):
        moves = ['f', 'f', 'r', 'q' , 'l']
        move_descriptions = {
            'f': 'Zwierzak idzie do przodu',
            'b': 'Zwierzak idzie do tyłu',
            'l': 'Zwierzak skręca w lewo',
            'r': 'Zwierzak skręca w prawo',}
    
        expected_result = [
            'Zwierzak idzie do przodu',
            'Zwierzak idzie do przodu',
            'Zwierzak skręca w prawo',
            'Zwierzak skręca w lewo']
    
        result = s1.run(moves, move_descriptions)
    
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()