#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(snail_map):
    result = []

    # repeat the whole thing while snail_map contains items
    while len(snail_map) > 0:
        # go right and append numbers to result
        for a in snail_map[0]:
            result.append(a)
        # remove the first line of numbers that are added to result
        snail_map.pop(0)

        if len(snail_map) > 0:
            # go down and append numbers to result
            for b in snail_map:
                result.append(b[-1])
                # remove the number after it was appended to result
                b.pop(-1)

            # go left and append numbers to result
            for c in snail_map[-1][::-1]:
                result.append(c)
            snail_map.pop(-1)

            # go up and append numbers to result
            for d in snail_map[::-1]:
                result.append(d[0])
                d.pop(0)
                # End of a while loop. If there are any items remaining
                # in snail_map, it will go up to the first for loop

    return result
