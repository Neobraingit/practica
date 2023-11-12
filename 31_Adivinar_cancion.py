



# Definir la canción
cancion_correcta = "oldie"

# Mensaje de bienvenida
print("¡Bienvenido al juego Adivina la Canción!")


# Inicializar intentos
intentos = 3

# Bucle principal
while intentos > 0:
    # Solicitar la respuesta al usuario
    respuesta = input("¿Cuál es la canción? ")

    # Verificar si la respuesta es correcta
    if respuesta == cancion_correcta:
        print("¡Correcto! ¡Has adivinado la canción!")
        break
    else:
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")

# Mensaje de despedida
if intentos == 0:
    print("¡Agotaste tus intentos! La canción correcta era:", cancion_correcta)
