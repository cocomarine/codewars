# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# Example: (input --> output)
#
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    compl = ''
    for i in dna:
        if i == 'A':
            compl += 'T'
        elif i == 'T':
            compl += 'A'
        elif i == 'G':
            compl += 'C'
        elif i == 'C':
            compl += 'G'

    return compl
