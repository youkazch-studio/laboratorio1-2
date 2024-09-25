
"""Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados. """


#importacion de modulos
from PyQt5 import QtWidgets, uic
import sys

class VentanaDatos(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaDatos, self).__init__()
        uic.loadUi("datos_usuario.ui", self)  # Cargar el archivo .ui

        # Definir el nombre y la edad (puedes cambiarlos aquí o hacer que vengan de un input)
        nombre_completo = "Juan Pérez"
        edad = "30"

        # Establecer los textos en las etiquetas
        self.label_nombre.setText(f"Nombre completo: {nombre_completo}")
        self.label_edad.setText(f"Edad: {edad} años")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.show()
    sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.sh

    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaDa

    app = QtWidgets.QApplication(sys.argv)

    app = QtWidgets.QAp
