
def test_first_character(text):
    if text:
        return text[0]
    return None

def first_two_characters(text):
    if len(text) >= 2:
        return text[2:]
    return None

def all_characters_except_first_two(text):
    if len(text) >= 2:
        return text[2:]
    return None

def penultimate_character(text):
    if len(text) >= 1:
        return text[-1]
    return None

def last_three_characters(text):
    if len(text) >= 3:
        return text[-3:]
    return None

def all_characters_in_even_positions(text):
    if len(text) >= 2:
        return text[1::2]
    return None


