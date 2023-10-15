import unittest
import operations  # Twój moduł

class TestOperations(unittest.TestCase):
    def test_first_character(self):
        self.assertEqual(operations.first_character("abcdefg"), "a")
        self.assertEqual(operations.first_character("12345"), "1")
        self.assertEqual(operations.first_character("A"), "A")

    def test_first_two_characters(self):
        self.assertEqual(operations.first_two_characters("abcdefg"), "ab")
        self.assertEqual(operations.first_two_characters("12345"), "12")
        self.assertEqual(
            operations.first_two_characters("A"), ""
        )  # Ciąg "A" jest za krótki.

    def test_all_characters_except_first_two(self):
        self.assertEqual(operations.all_characters_except_first_two("abcdefg"), "cdefg")
        self.assertEqual(operations.all_characters_except_first_two("12345"), "345")
        self.assertEqual(
            operations.all_characters_except_first_two("A"), ""
        )  # Ciąg "A" jest za krótki.

    def test_penultimate_character(self):
        self.assertEqual(operations.penultimate_character("abcdefg"), "f")
        self.assertEqual(operations.penultimate_character("12345"), "4")
        self.assertEqual(
            operations.penultimate_character("A"), ""
        )  # Ciąg "A" jest za krótki.

    def test_last_three_characters(self):
        self.assertEqual(operations.last_three_characters("abcdefg"), "efg")
        self.assertEqual(operations.last_three_characters("12345"), "345")
        self.assertEqual(
            operations.last_three_characters("A"), ""
        )  # Ciąg "A" jest za krótki.

    def test_all_characters_in_even_positions(self):
        self.assertEqual(
            operations.all_characters_in_even_positions("abcdefg"), "aceg"
        )
        self.assertEqual(
            operations.all_characters_in_even_positions("12345"), "135"
        )
        self.assertEqual(operations.all_characters_in_even_positions("A"), "A")

if __name__ == "__main__":
    unittest.main()
