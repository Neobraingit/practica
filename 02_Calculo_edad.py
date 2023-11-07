#  Calculadora de edad: Pide al usuario su año de nacimiento y calcula su edad.
añoactual = int(input('Dime cual es el año actual: '))
añonacimiento = int(input('Dime tu año de nacimiento: '))

edad = añoactual - añonacimiento

print ('Tu edad es de {} años'.format(edad))