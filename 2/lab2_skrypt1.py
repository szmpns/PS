
import operations
import sys

text = sys.argv

if len(text) != 2:
    print("Fail")
else:
    argument = text[1]
    print(operations.first_character(argument))
    print(operations.first_two_characters(argument))
    print(operations.all_characters_except_first_two(argument))
    print(operations.penultimate_character(argument))
    print(operations.last_three_characters(argument))
    print(operations.all_characters_in_even_positions(argument))
    print(operations.merge_characters_and_duplicate(argument))