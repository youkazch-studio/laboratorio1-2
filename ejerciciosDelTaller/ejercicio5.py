
"""Construir un programa que muestre una ventana a través de la cual se puedan leer 10 datos característicos de una persona."""

#En este caso se utilizara la biblioteca tkinter para poder contruir las interfaces graficas de los programas.

#importacion de modulos
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    # Obtener los datos de los campos de entrada
    datos = [
        entry_nombre.get(),
        entry_edad.get(),
        entry_genero.get(),
        entry_direccion.get(),
        entry_telefono.get(),
        entry_email.get(),
        entry_nacionalidad.get(),
        entry_ocupacion.get(),
        entry_estado_civil.get(),
        entry_fecha_nacimiento.get()
    ]
    
    # Etiquetas para los campos de datos
    etiquetas = [
        "Nombre:", "Edad:", "Género:", "Dirección:", "Teléfono:",
        "Email:", "Nacionalidad:", "Ocupación:", "Estado Civil:", "Fecha de Nacimiento:"
    ]
    
    # Validación básica
    if any(not dato for dato in datos):
        messagebox.showerror("Error", "Por favor, ingrese todos los datos.")
        return
    
    # Mostrar los datos en un mensaje
    mensaje = "\n".join(f"{etiqueta} {dato}" for etiqueta, dato in zip(etiquetas, datos))
    messagebox.showinfo("Datos Ingresados", mensaje)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Datos Personales")
root.geometry("350x500")

# Crear etiquetas y campos de entrada para los 10 datos
etiquetas = [
    "Nombre:", "Edad:", "Género:", "Dirección:", "Teléfono:",
    "Email:", "Nacionalidad:", "Ocupación:", "Estado Civil:", "Fecha de Nacimiento:"
]

entradas = []

for etiqueta in etiquetas:
    tk.Label(root, text=etiqueta).pack(pady=5, anchor='w')
    entrada = tk.Entry(root, width=40)
    entrada.pack(pady=5)
    entradas.append(entrada)

# Asignar las entradas a variables
(entry_nombre, entry_edad, entry_genero, entry_direccion,
 entry_telefono, entry_email, entry_nacionalidad,
 entry_ocupacion, entry_estado_civil, entry_fecha_nacimiento) = entradas

# Botón para mostrar los datos
boton_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_datos)
boton_mostrar.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()
