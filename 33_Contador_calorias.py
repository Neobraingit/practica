

       
       
        
        
        # Inicializamos el contador de calorías
calorias_totales = 0

# Menú principal
while True:
    print("1. Agregar alimento")
    print("2. Ver calorías totales")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar alimento y sus calorías
        alimento = input("Ingrese el nombre del alimento: ")
        calorias = float(input("Ingrese la cantidad de calorías: "))
        
        # Sumar calorías al total
        calorias_totales += calorias
        print(f"{alimento} añadido. Calorías totales: {calorias_totales}")

    elif opcion == "2":
        # Mostrar calorías totales
        print(f"Calorías totales: {calorias_totales}")

    elif opcion == "3":
        # Salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")

    
    
    

