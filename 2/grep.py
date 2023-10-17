
import re

def grep(lines, pattern, whole_word=False, case_insensitive=False):
    flags = re.IGNORECASE if case_insensitive else 0
    if whole_word:
        pattern = r'\b{}\b'.format(re.escape(pattern))
    result = []

    for line in lines:
        line_to_check = line.lower() if case_insensitive else line

        if re.search(pattern, line_to_check, flags):
            result.append(line)

    return result