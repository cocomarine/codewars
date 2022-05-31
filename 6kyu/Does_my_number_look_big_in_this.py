def narcissistic(value):

    l = len(str(value))
    sum = 0

    for i in str(value):
        sum += int(i)**l

    return sum == value
