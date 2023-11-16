
numeros_primos = []
numero = int(input('Numero a introducir: '))


while numero != 0:
     numeros_primos.append(numero)
     print (numeros_primos)
     numero = int(input('Numero a introducir: '))
     for i in range(numeros_primos):
         print (i)
