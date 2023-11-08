
import math

def calcular_edad_humana(edad_perro):
    edad_humana = 16 * math.log(edad_perro) + 31
    return edad_humana

# Ingresa la edad de tu perro
edad_del_perro = float(input("Ingresa la edad de tu perro: "))

# Calcula la edad humana
edad_humana_calculada = calcular_edad_humana(edad_del_perro)

# Imprime el resultado
print(f"La edad humana equivalente de tu perro es aproximadamente {edad_humana_calculada} años.")
