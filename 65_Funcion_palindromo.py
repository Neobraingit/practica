
def palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
    
print (palindromo('qqqqq'))