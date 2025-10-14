vowels = {'a', 'e', 'y', 'u', 'i', 'o'}
consonants = {'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' }
s = str(input())
sett = set(s)
print(sett & vowels, len(sett & vowels))
print(sett & consonants, len(sett & consonants))
