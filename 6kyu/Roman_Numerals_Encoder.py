# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(n):
    # numbers in num tuple matching roman numerals in rom tuple with matching index
    num = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    rom = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

    result = ''

    # for-loop going through num tuple
    for i in range(len(num)):
        # any multiples of num item stored as count integer
        count = int(n / num[i])
        # matching rom item repeated by count times added to result
        result += str(rom[i] * count)
        # once added to result, that portion of number removed from input n
        n -= num[i] * count

    return result
