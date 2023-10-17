
import sys
import argparse
import operations
import cut
import grep

def main():
    parser = argparse.ArgumentParser(description="Text Manipulation and Filtering Tool")

    subparsers = parser.add_subparsers(dest="command")

    parser_text = subparsers.add_parser("text", help="Text manipulation commands")
    parser_text.add_argument("text", help="Text to manipulate")

    parser_cut = subparsers.add_parser("cut", help="Cut command")
    parser_cut.add_argument("-d", required=True, help="Delimiter for cutting")
    parser_cut.add_argument("-f", required=True, help="Field to cut")

    parser_grep = subparsers.add_parser("grep", help="Grep command")
    parser_grep.add_argument("-w", action="store_true", help="Match whole words only")
    parser_grep.add_argument("-i", action="store_true", help="Case-insensitive matching")
    parser_grep.add_argument("pattern", help="Pattern to search")

    args = parser.parse_args()

    if args.command == "text":
        text = args.text
        print(operations.first_character(text))
        print(operations.first_two_characters(text))
        print(operations.all_characters_except_first_two(text))
        print(operations.penultimate_character(text))
        print(operations.last_three_characters(text))
        print(operations.all_characters_in_even_positions(text))
        print(operations.merge_characters_and_duplicate(text))
    elif args.command == "cut":
        lines = sys.stdin.read().splitlines()
        result = cut.cut(lines, args.d, args.f)
        for item in result:
            print(item)
    elif args.command == "grep":
        lines = sys.stdin.read().splitlines()
        result = grep.grep(lines, args.pattern, args.w, args.i)
        for item in result:
            print(item)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
