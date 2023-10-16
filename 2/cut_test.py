
import cut

def test_cut():
    lines = ["apple:banana:cherry", "dog:elephant:fox", "grape:hamster:iguana"]

    delimiter = ":"
    
    field = "2"

    result = cut.cut(lines, delimiter, field)
    expected_result = ["banana", "elephant", "hamster"]
    assert result == expected_result

def test_cut_2():
    field = "abc"

    lines = []
    
    delimiter = ""

    result = cut.cut(lines, delimiter, field)
    expected_result = []
    assert result == expected_result