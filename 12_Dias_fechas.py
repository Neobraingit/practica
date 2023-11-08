# Calculadora de días entre fechas: Calcula la cantidad de días entre dos fechas ingresadas por el usuario.
from datetime import datetime

fecha1 =datetime(2023, 8, 11)
fecha3 = datetime(2023, 8, 13)

fecha_definitiva = fecha1 - fecha3
print (fecha_definitiva)