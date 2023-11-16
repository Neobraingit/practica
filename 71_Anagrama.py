
# Vamos a hacer un anagram
anagrama  = input('Introduce tu anagrama: ')

if anagrama[:0] == anagrama[::-1]:
    print ('Es un anagrama...')
else:
    print ('No es un anagrama...')
