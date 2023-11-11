# Diccionario para la traducción de letras y números a código Morse
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Función para convertir texto a código Morse
def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        elif char == ' ':
            morse_code += ' '
    return morse_code

# Función para convertir código Morse a texto
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key
    return text

# Programa principal
choice = input("Seleccione una opción (1 para texto a Morse, 2 para Morse a texto): ")

if choice == '1':
    text_input = input("Ingrese el texto a convertir a código Morse: ")
    morse_output = text_to_morse(text_input)
    print(f"Texto a Morse: {morse_output}")
elif choice == '2':
    morse_input = input("Ingrese el código Morse a convertir a texto: ")
    text_output = morse_to_text(morse_input)
    print(f"Morse a Texto: {text_output}")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2.")
