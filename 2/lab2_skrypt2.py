import sys

command = sys.argv[1]

if command == "cut":

    import cut

    d = None
    f = None

    i = 2

    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            d = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-f":
            f = sys.argv[i + 1]
            i += 2
        else:
            print("Fail")

    lines = sys.stdin.read().splitlines() #wpisywanie wartosci / ctrl + d konczy
    result = cut.cut(lines , d , f)

    for i in result:
        print(i)

if command == "grep":
    import grep

    args = sys.argv[2:]
    lines = sys.stdin.read().splitlines()
    whole_word = '-w' in args
    case_insensitive = '-i' in args
    pattern = args[-1]
    result = grep.grep(lines, pattern, whole_word, case_insensitive)

    for i in result:
        print(i)

