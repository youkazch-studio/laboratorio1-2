
"""Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados. """

#En este caso se utilizara la biblioteca tkinter para poder contruir las interfaces graficas de los programas.

#importacion de modulos
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    # Validación básica de los datos
    if not nombre or not edad.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un nombre válido y una edad numérica.")
        return

    # Crear una nueva ventana para mostrar los datos
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")
    ventana_datos.geometry("300x150")

    # Etiqueta para mostrar el nombre centrado
    label_nombre = tk.Label(ventana_datos, text=f"Nombre completo: {nombre}")
    label_nombre.pack(pady=10)
    label_nombre.config(anchor="center")

    # Etiqueta para mostrar la edad centrada
    label_edad = tk.Label(ventana_datos, text=f"Edad: {edad} años")
    label_edad.pack(pady=10)
    label_edad.config(anchor="center")

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_datos, text="Cerrar", command=ventana_datos.destroy)
    boton_cerrar.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Entrada de datos")
root.geometry("400x200")

# Etiqueta y entrada para el nombre
label_nombre = tk.Label(root, text="Nombre completo:")
label_nombre.pack(pady=5)

entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack(pady=5)

# Etiqueta y entrada para la edad
label_edad = tk.Label(root, text="Edad:")
label_edad.pack(pady=5)

entry_edad = tk.Entry(root, width=40)
entry_edad.pack(pady=5)

# Botón para mostrar los datos
boton_mostrar = tk.Button(root, text="Mostrar datos", command=mostrar_datos)
boton_mostrar.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
