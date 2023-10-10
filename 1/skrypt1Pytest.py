
import pytest
import skrypt1 as s1
from io import StringIO

def test_display_without_index(capsys):
    arguments = ['skrypt.py', '1', 'a', '4', 'b']
    s1.display(arguments , False)
    variable = capsys.readouterr()
    expected_output = 'skrypt.py\n1\na\n4\nb\n'
    assert variable.out == expected_output

def test_display_with_index(capsys):
    args = ['skrypt.py', '1', 'a', '4', 'b']
    s1.display(args, True)
    variable = capsys.readouterr()
    expected_output = 'args[0] = skrypt.py\nargs[1] = 1\nargs[2] = a\nargs[3] = 4\nargs[4] = b\n'
    assert variable.out == expected_output

def test_run():
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

    assert result == expected_result

