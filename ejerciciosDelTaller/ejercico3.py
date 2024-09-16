
"""Construir un programa que muestre una ventana a través de la cual se pueda leer su número de cédula y su nombre completo."""

#En este caso se utilizara la biblioteca tkinter para poder contruir las interfaces graficas de los programas.

#importacion de modulos
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    
    # Validación básica
    if not cedula or not nombre:
        messagebox.showerror("Error", "Por favor, ingrese tanto la cédula como el nombre.")
        return
    
    # Mostrar los datos en un mensaje
    mensaje = f"Número de Cédula: {cedula}\nNombre Completo: {nombre}"
    messagebox.showinfo("Datos Ingresados", mensaje)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Datos")
root.geometry("300x200")

# Etiqueta y campo de entrada para la cédula
label_cedula = tk.Label(root, text="Número de Cédula:")
label_cedula.pack(pady=10)

entry_cedula = tk.Entry(root, width=40)
entry_cedula.pack(pady=5)

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(root, text="Nombre Completo:")
label_nombre.pack(pady=10)

entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack(pady=5)

# Botón para mostrar los datos
boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_datos)
boton_mostrar.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()
