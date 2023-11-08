import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "juego", "ahorcado", "teclado", "computadora"]

# Selecciona una palabra al azar
palabra_secreta = random.choice(palabras)

# Inicializa las variables
intentos = 6
letras_adivinadas = []

# Bucle principal del juego
while intentos > 0:
    # Muestra la palabra oculta con guiones bajos (_) para las letras no adivinadas
    palabra_oculta = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    
    # Muestra la palabra oculta y las letras adivinadas
    print("Palabra: ", palabra_oculta)
    print("Letras adivinadas: ", letras_adivinadas)
    
    # Solicita al jugador que ingrese una letra
    letra_ingresada = input("Ingresa una letra: ").lower()
    
    # Verifica si la letra ya fue ingresada
    if letra_ingresada in letras_adivinadas:
        print("Ya has ingresado esa letra. ¡Intenta con otra!\n")
        continue
    
    # Verifica si la letra está en la palabra secreta
    if letra_ingresada in palabra_secreta:
        print("¡Correcto! La letra está en la palabra.\n")
        letras_adivinadas.append(letra_ingresada)
    else:
        print("Incorrecto. Pierdes un intento.\n")
        intentos -= 1
    
    # Verifica si todas las letras han sido adivinadas
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break

# Si se agotan los intentos, muestra la palabra secreta
if intentos == 0:
    print("¡Oh no! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)

