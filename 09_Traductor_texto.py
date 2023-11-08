# Traductor de texto

from googletrans import Translator

def traducir_texto(texto, destino='en'):
    traductor = Translator()
    traduccion = traductor.translate(texto, dest=destino)
    return traduccion.text

if __name__ == "__main__":
    texto_a_traducir = input("Ingresa el texto que quieres traducir: ")
    idioma_destino = input("Ingresa el código del idioma al que quieres traducir (por defecto es 'en' para inglés): ")

    if not idioma_destino:
        idioma_destino = 'en'

    resultado = traducir_texto(texto_a_traducir, idioma_destino)
    print(f"\nTexto original: {texto_a_traducir}")
    print(f"Traducción ({idioma_destino}): {resultado}")
