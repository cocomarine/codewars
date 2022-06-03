# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n_floors):
    result = []

    for i in range(1, n_floors+1):
        x = (i * 2 -1) * "*"
        space = (n_floors - i) * " "
        result.append(space + x + space)

    return result
