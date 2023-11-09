import tkinter as tk
from tkinter import scrolledtext

def guardar_contenido():
    contenido = texto.get("1.0", tk.END)
    with open("archivo.txt", "w") as archivo:
        archivo.write(contenido)

def cargar_contenido():
    try:
        with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, contenido)
    except FileNotFoundError:
        pass  # Manejar el caso en que el archivo aún no exista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto Simple")

# Crear un widget de texto con barra de desplazamiento
texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
texto.pack(expand=True, fill="both")

# Crear botones para guardar y cargar contenido
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_contenido)
boton_guardar.pack(side=tk.LEFT, padx=5)
boton_cargar = tk.Button(ventana, text="Cargar", command=cargar_contenido)
boton_cargar.pack(side=tk.RIGHT, padx=5)

# Iniciar el bucle principal
ventana.mainloop()
