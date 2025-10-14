import timeit

def letters(s):
    vowels = {'a', 'e', 'y', 'u', 'i', 'o'}
    consonants = {'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' }
    sett = set(s)
    return ((sett & vowels, len(sett & vowels)), (sett & consonants, len(sett & consonants)))

s = input()
print(timeit.Timer("letters(s)", globals=globals()).autorange())
