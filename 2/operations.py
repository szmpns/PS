def first_character(s):
    return s[0] if s else ""

def first_two_characters(s):
    return s[:2] if len(s) >= 2 else ""

def all_characters_except_first_two(s):
    return s[2:] if len(s) >= 2 else ""

def penultimate_character(s):
    return s[-2] if len(s) >= 2 else ""

def last_three_characters(s):
    return s[-3:] if len(s) >= 3 else ""

def all_characters_in_even_positions(s):
    # if len(s) >= 2:
    #     return s[0::2]
    return s[0::2]

def merge_characters_and_duplicate(string):
    pass