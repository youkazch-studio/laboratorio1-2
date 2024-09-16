
"""Construir un programa que muestre una ventana a través de la cual se pueda leer tres datos básicos de 3 mascotas diferentes."""

#En este caso se utilizara la biblioteca tkinter para poder contruir las interfaces graficas de los programas.

#importacion de modulos
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    # Obtener los datos de cada mascota
    nombre_mascota1 = entry_nombre1.get()
    edad_mascota1 = entry_edad1.get()
    tipo_mascota1 = entry_tipo1.get()

    nombre_mascota2 = entry_nombre2.get()
    edad_mascota2 = entry_edad2.get()
    tipo_mascota2 = entry_tipo2.get()

    nombre_mascota3 = entry_nombre3.get()
    edad_mascota3 = entry_edad3.get()
    tipo_mascota3 = entry_tipo3.get()
    
    # Validación básica
    if not all([nombre_mascota1, edad_mascota1, tipo_mascota1,
                nombre_mascota2, edad_mascota2, tipo_mascota2,
                nombre_mascota3, edad_mascota3, tipo_mascota3]):
        messagebox.showerror("Error", "Por favor, ingrese todos los datos para cada mascota.")
        return
    
    # Mostrar los datos en un mensaje
    mensaje = (
        f"Datos de Mascota 1:\nNombre: {nombre_mascota1}\nEdad: {edad_mascota1}\nTipo: {tipo_mascota1}\n\n"
        f"Datos de Mascota 2:\nNombre: {nombre_mascota2}\nEdad: {edad_mascota2}\nTipo: {tipo_mascota2}\n\n"
        f"Datos de Mascota 3:\nNombre: {nombre_mascota3}\nEdad: {edad_mascota3}\nTipo: {tipo_mascota3}"
    )
    messagebox.showinfo("Datos de Mascotas", mensaje)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Mascotas")
root.geometry("350x350")

# Crear etiquetas y campos de entrada para la primera mascota
tk.Label(root, text="Mascota 1").pack(pady=10)
tk.Label(root, text="Nombre:").pack(pady=2)
entry_nombre1 = tk.Entry(root, width=40)
entry_nombre1.pack(pady=2)

tk.Label(root, text="Edad:").pack(pady=2)
entry_edad1 = tk.Entry(root, width=40)
entry_edad1.pack(pady=2)

tk.Label(root, text="Tipo:").pack(pady=2)
entry_tipo1 = tk.Entry(root, width=40)
entry_tipo1.pack(pady=10)

# Crear etiquetas y campos de entrada para la segunda mascota
tk.Label(root, text="Mascota 2").pack(pady=10)
tk.Label(root, text="Nombre:").pack(pady=2)
entry_nombre2 = tk.Entry(root, width=40)
entry_nombre2.pack(pady=2)

tk.Label(root, text="Edad:").pack(pady=2)
entry_edad2 = tk.Entry(root, width=40)
entry_edad2.pack(pady=2)

tk.Label(root, text="Tipo:").pack(pady=2)
entry_tipo2 = tk.Entry(root, width=40)
entry_tipo2.pack(pady=10)

# Crear etiquetas y campos de entrada para la tercera mascota
tk.Label(root, text="Mascota 3").pack(pady=10)
tk.Label(root, text="Nombre:").pack(pady=2)
entry_nombre3 = tk.Entry(root, width=40)
entry_nombre3.pack(pady=2)

tk.Label(root, text="Edad:").pack(pady=2)
entry_edad3 = tk.Entry(root, width=40)
entry_edad3.pack(pady=2)

tk.Label(root, text="Tipo:").pack(pady=2)
entry_tipo3 = tk.Entry(root, width=40)
entry_tipo3.pack(pady=10)

# Botón para mostrar los datos
boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_datos)
boton_mostrar.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()
