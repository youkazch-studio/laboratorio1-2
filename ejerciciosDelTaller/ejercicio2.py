
"""Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar los caracteres que la componen."""

#En este caso se utilizara la biblioteca tkinter para poder contruir las interfaces graficas de los programas.

#importacion de modulos
import tkinter as tk

def mostrar_clave():
    clave = entry_clave.get()
    # Muestra un mensaje con la clave (solo para demostración)
    print(f"Clave ingresada: {clave}")

# Crear la ventana principal
root = tk.Tk()
root.title("Entrada de Clave Secreta")
root.geometry("300x150")

# Etiqueta para la clave
label_clave = tk.Label(root, text="Ingrese su clave:")
label_clave.pack(pady=10)

# Campo de entrada para la clave secreta (sin mostrar los caracteres)
entry_clave = tk.Entry(root, show="*", width=30)
entry_clave.pack(pady=5)

# Botón para mostrar la clave por consola(solo para fines de demostración)
boton_mostrar = tk.Button(root, text="Mostrar clave", command=mostrar_clave)
boton_mostrar.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
