# Generador de contraseñas: Crea una contraseña segura aleatoria.

import random
import string

# Longitud de la contraseña deseada
longitud_contraseña = 12

# Caracteres posibles para la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Genera la contraseña aleatoria
contraseña_aleatoria = ''.join(random.choice(caracteres) for i in range(longitud_contraseña))

print(contraseña_aleatoria)



