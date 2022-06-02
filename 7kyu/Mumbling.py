# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    l = []

    for x in s:
        # capitalised letter concateated with low case letter len(l) times
        char = x.upper() + (len(l) * x).lower()
        l.append(char)

    # return items in list l joined by '-'
    return "-".join(i for i in l)
