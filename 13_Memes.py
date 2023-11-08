from PIL import Image, ImageDraw, ImageFont

def generar_meme(imagen_path, texto_superior, texto_inferior, output_path):
    # Cargar la imagen
    imagen = Image.open(imagen_path)

    # Obtener el tamaño de la imagen
    ancho, alto = imagen.size

    # Crear un objeto Draw
    draw = ImageDraw.Draw(imagen)

    # Cargar una fuente
    fuente = ImageFont.load_default()

    # Configurar el tamaño del texto
    tamaño_texto = 40

    # Calcular la posición para el texto superior
    x_superior = ancho // 2
    y_superior = 10

    # Calcular la posición para el texto inferior
    x_inferior = ancho // 2
    y_inferior = alto - tamaño_texto - 10

    # Agregar texto superior
    draw.text((x_superior, y_superior), texto_superior, font=fuente, fill="white", anchor="mm")

    # Agregar texto inferior
    draw.text((x_inferior, y_inferior), texto_inferior, font=fuente, fill="white", anchor="mm")

    # Guardar la imagen con el texto agregado
    imagen.save(output_path)

if __name__ == "__main__":
    # Ruta de la imagen de fondo
    imagen_path = "ejemplo.jpg"

    # Texto superior e inferior para el meme
    texto_superior = "Texto superior"
    texto_inferior = "Texto inferior"

    # Ruta de salida del meme
    output_path = "meme_generado.jpg"

    # Generar el meme
    generar_meme(imagen_path, texto_superior, texto_inferior, output_path)
