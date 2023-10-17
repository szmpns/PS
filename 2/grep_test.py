
import unittest
from grep import grep

class TestGrep(unittest.TestCase):

    def test_case_insensitive(self):
        lines = [
            "This is a test line",
            "This is another Test Line",
            "This line should not match"
        ]
        pattern = "test"
        result = grep(lines, pattern, case_insensitive=True)
        self.assertEqual(result, lines[:2])

    def test_whole_word(self):
        lines = [
            "This is a test line",
            "Testing is important",
            "This line should not match"
        ]
        pattern = "test"
        result = grep(lines, pattern, whole_word=True)
        self.assertEqual(result, [lines[0]])

    def test_case_insensitive_and_whole_word(self):
        lines = [
            "This is a test line",
            "Testing is important",
            "This line should not match"
        ]
        pattern = "test"
        result = grep(lines, pattern, case_insensitive=True, whole_word=True)
        self.assertEqual(result, [lines[0]])

if __name__ == '__main__':
    unittest.main()
