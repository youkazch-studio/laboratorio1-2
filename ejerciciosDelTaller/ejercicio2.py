
"""Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar los caracteres que la componen."""


#importacion de modulos

from PyQt5 import QtWidgets, uic
import sys

class VentanaClave(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaClave, self).__init__()
        uic.loadUi("clave_secreta.ui", self)  # Cargar el archivo .ui

        # Conectar el botón "Enviar" a la función de envío
        self.boton_enviar.clicked.connect(self.mostrar_clave)

    def mostrar_clave(self):
        # Obtener la clave introducida
        clave = self.lineEdit_clave.text()
        
        # Aquí puedes hacer lo que quieras con la clave
        # Por seguridad, evitamos mostrarla en consola.
        print("Clave ingresada correctamente.")

        # Limpiar el campo de texto
        self.lineEdit_clave.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaClave()
    ventana.show()
    sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaClave

    app = QtWidgets.QApplication(sys.argv)
   

    app = QtWidgets.QAppl
