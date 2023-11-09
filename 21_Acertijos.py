import random

# Lista de acertijos y sus respuestas
acertijos = [
    {"pregunta": "¿Qué tiene ojos pero no puede ver?", "respuesta": "un hoyo"},
    {"pregunta": "¿Qué siempre está en frente pero nunca puede ver?", "respuesta": "el futuro"},
    {"pregunta": "¿Qué tiene patas pero no puede caminar?", "respuesta": "una mesa"},
    
]

# Elegir un acertijo aleatorio
acertijo_actual = random.choice(acertijos)

# Mostrar el acertijo al usuario
print("Acertijo: " + acertijo_actual["pregunta"])

# Pedir al usuario que ingrese su respuesta
respuesta_usuario = input("¿Cuál es tu respuesta? ")

# Verificar si la respuesta del usuario es correcta
if respuesta_usuario.lower() == acertijo_actual["respuesta"]:
    print("¡Correcto! ¡Eres un genio!")
else:
    print(f"Incorrecto. La respuesta correcta es: {acertijo_actual['respuesta']}")


    
    