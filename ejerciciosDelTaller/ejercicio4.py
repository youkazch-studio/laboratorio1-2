
"""Construir un programa que muestre una ventana a través de la cual se pueda leer tres datos básicos de 3 mascotas diferentes."""


#importacion de modulos
from PyQt5 import QtWidgets, uic
import sys

class VentanaMascotas(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaMascotas, self).__init__()
        uic.loadUi("interfaz_mascotas.ui", self)  # Cargar el archivo .ui

        # Conectar el botón "Enviar" a la función mostrar_datos
        self.boton_enviar.clicked.connect(self.mostrar_datos)

    def mostrar_datos(self):
        # Obtener los datos de las 3 mascotas
        nombre1 = self.lineEdit_nombre1.text()
        edad1 = self.lineEdit_edad1.text()
        tipo1 = self.lineEdit_tipo1.text()

        nombre2 = self.lineEdit_nombre2.text()
        edad2 = self.lineEdit_edad2.text()
        tipo2 = self.lineEdit_tipo2.text()

        nombre3 = self.lineEdit_nombre3.text()
        edad3 = self.lineEdit_edad3.text()
        tipo3 = self.lineEdit_tipo3.text()

        # Validar que los campos no estén vacíos para todas las mascotas
        if all([nombre1, edad1, tipo1, nombre2, edad2, tipo2, nombre3, edad3, tipo3]):
            # Mostrar los datos en un mensaje
            mensaje = (f"Mascota 1: {nombre1}, Edad: {edad1}, Tipo: {tipo1}\n"
                       f"Mascota 2: {nombre2}, Edad: {edad2}, Tipo: {tipo2}\n"
                       f"Mascota 3: {nombre3}, Edad: {edad3}, Tipo: {tipo3}")
            QtWidgets.QMessageBox.information(self, "Datos Ingresados", mensaje)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese todos los datos de las mascotas.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMascotas()
    ventana.show()
    sys.exit(app.exec_())

