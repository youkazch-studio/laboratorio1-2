
"""Construir un programa que muestre una ventana a través de la cual se puedan leer 10 datos característicos de una persona."""


#importacion de modulos
from PyQt5 import QtWidgets, uic
import sys

class VentanaPersona(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaPersona, self).__init__()
        uic.loadUi("interfaz_persona.ui", self)  # Cargar el archivo .ui

        # Conectar el botón "Enviar" a la función mostrar_datos
        self.boton_enviar.clicked.connect(self.mostrar_datos)

    def mostrar_datos(self):
        # Obtener los datos ingresados
        nombre = self.lineEdit_nombre.text()
        edad = self.lineEdit_edad.text()
        genero = self.lineEdit_genero.text()
        ocupacion = self.lineEdit_ocupacion.text()
        direccion = self.lineEdit_direccion.text()
        telefono = self.lineEdit_telefono.text()
        email = self.lineEdit_email.text()
        nacionalidad = self.lineEdit_nacionalidad.text()
        estado_civil = self.lineEdit_estado_civil.text()
        hobbies = self.lineEdit_hobbies.text()

        # Validar que todos los campos estén llenos
        if all([nombre, edad, genero, ocupacion, direccion, telefono, email, nacionalidad, estado_civil, hobbies]):
            # Mostrar los datos en un mensaje
            mensaje = (f"Nombre: {nombre}\nEdad: {edad}\nGénero: {genero}\nOcupación: {ocupacion}\n"
                       f"Dirección: {direccion}\nTeléfono: {telefono}\nEmail: {email}\nNacionalidad: {nacionalidad}\n"
                       f"Estado Civil: {estado_civil}\nHobbies: {hobbies}")
            QtWidgets.QMessageBox.information(self, "Datos Ingresados", mensaje)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese todos los datos solicitados.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPersona()
    ventana.show()
    sys.exit(app.exec_())
