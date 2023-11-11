from datetime import datetime, timedelta

def dias_laborables_entre_fechas(fecha_inicio, fecha_fin):
    # Convierte las fechas de cadena a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    # Define la lista de días no laborables (sábados y domingos)
    dias_no_laborables = [5, 6]  # 5 es sábado, 6 es domingo

    # Inicializa el contador de días laborables
    dias_laborables = 0

    # Itera sobre cada día entre las fechas de inicio y fin
    current_date = fecha_inicio
    while current_date <= fecha_fin:
        # Verifica si el día actual no es un día no laborable
        if current_date.weekday() not in dias_no_laborables:
            dias_laborables += 1

        # Avanza al siguiente día
        current_date += timedelta(days=1)

    return dias_laborables

# Ejemplo de uso
fecha_inicio = "2023-11-01"
fecha_fin = "2023-11-10"
resultado = dias_laborables_entre_fechas(fecha_inicio, fecha_fin)
print(f"Días laborables entre {fecha_inicio} y {fecha_fin}: {resultado}")
