import random

def generador_horoscopo(signo):
    horoscopos = {
        'Aries': ['Hoy es un buen día para tomar decisiones importantes.', 'Tu creatividad estará en su punto máximo hoy.'],
        'Tauro': ['La paciencia será clave en tus relaciones hoy.', 'Es un buen momento para iniciar nuevos proyectos.'],
        'Géminis': ['La comunicación será tu fuerte hoy.', 'Cuida de tu salud y toma tiempo para descansar.'],
        'Cáncer': ['Momento propicio para fortalecer lazos familiares.', 'Sé honesto contigo mismo en tus decisiones.'],
        'Leo': ['Hoy es un día para destacar en tu carrera.', 'Tómate un tiempo para disfrutar de las pequeñas cosas.'],
        'Virgo': ['La organización será clave en tus tareas hoy.', 'Aprovecha para aprender algo nuevo.'],
        'Libra': ['Buena jornada para expresar tus sentimientos.', 'Sé consciente de tus gastos y ahorra.'],
        'Escorpio': ['La intuición te guiará en tus decisiones hoy.', 'No temas enfrentar los desafíos que se presenten.'],
        'Sagitario': ['La aventura te espera hoy, ¡sé valiente!', 'Es un buen momento para planificar tus metas a largo plazo.'],
        'Capricornio': ['La perseverancia te llevará lejos hoy.', 'Cuida de tus relaciones personales.'],
        'Acuario': ['Tu originalidad destacará hoy.', 'Mantén la mente abierta a nuevas ideas.'],
        'Piscis': ['La empatía será clave en tus relaciones hoy.', 'Busca el equilibrio entre el trabajo y el descanso.']
    }

    if signo.capitalize() in horoscopos:
        return random.choice(horoscopos[signo.capitalize()])
    else:
        return "Lo siento, no tengo información para ese signo zodiacal."

# Ejemplo de uso
signo_usuario = input("Introduce tu signo zodiacal: ")
horoscopo_del_dia = generador_horoscopo(signo_usuario)
print(f'\nHoróscopo para {signo_usuario}: {horoscopo_del_dia}')
