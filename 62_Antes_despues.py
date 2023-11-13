
# Definir la función simple
def funcion_simple():
    print("¡Esta es una función simple!")

# Definir el decorador
def decorador_mensaje(funcion):
    def wrapper():
        print("Antes de llamar a la función.")
        funcion()  # Llamar a la función original
        print("Después de llamar a la función.")
    return wrapper

# Aplicar el decorador a la función
funcion_decorada = decorador_mensaje(funcion_simple)

# Llamar a la función decorada
funcion_decorada()

print ('Después de la función¡¡¡')



