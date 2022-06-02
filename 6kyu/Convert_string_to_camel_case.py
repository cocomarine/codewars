# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    # replacing hyphen and underscore with space
    s = text.replace("-", " ").replace("_", " ")
    # splitting by space
    s = s.split()

    # if empty string, return emtpy string
    if len(s) == 0:
        return text

    # keep the first word as it is, convert first letters of the rest into capital letter,
    # and concatenate them
    x = s[0]
    for i in s[1:]:
        x += i.title()

    return x
