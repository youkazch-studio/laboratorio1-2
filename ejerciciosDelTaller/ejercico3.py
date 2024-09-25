
"""Construir un programa que muestre una ventana a través de la cual se pueda leer su número de cédula y su nombre completo."""


#importacion de modulos
from PyQt5 import QtWidgets, uic
import sys

class VentanaDatos(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaDatos, self).__init__()
        uic.loadUi("interfaz.ui", self)  # Cargar el archivo .ui

        # Conectar el botón "Enviar" a la función mostrar_datos
        self.boton_enviar.clicked.connect(self.mostrar_datos)

    def mostrar_datos(self):
        # Obtener los datos introducidos
        nombre = self.lineEdit_nombre.text()
        cedula = self.lineEdit_cedula.text()

        # Validar que los campos no estén vacíos
        if nombre and cedula:
            # Mostrar los datos en un mensaje
            mensaje = f"Nombre completo: {nombre}\nNúmero de cédula: {cedula}"
            QtWidgets.QMessageBox.information(self, "Datos Ingresados", mensaje)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese ambos datos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.show()
    sys.exit(app.exec_())
