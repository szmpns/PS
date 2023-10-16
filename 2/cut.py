
def cut(l , d , f):
    result = []

    for i in l:
        arguments = i.split(d)
        if f.isdigit() and 1 <= int(f) <= len(arguments):
            result.append(arguments[int(f) - 1])
        else:
            result.append("")
    
    return result