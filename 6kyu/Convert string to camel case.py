def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(s) == 0:
        return text

    x = s[0]
    for i in s[1:]:
        x += i.title()

    return x