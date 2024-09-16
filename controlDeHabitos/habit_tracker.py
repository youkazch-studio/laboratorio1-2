import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("habit_tracker.ui", self)
        
        # Conectar el botón de enviar con la función que maneja el evento
        self.button_submit.clicked.connect(self.mostrar_datos)
        
    def mostrar_datos(self):
        # Obtener el hábito seleccionado
        if self.radio_exercise.isChecked():
            habit = "Exercise"
        elif self.radio_reading.isChecked():
            habit = "Reading"
        elif self.radio_meditation.isChecked():
            habit = "Meditation"
        else:
            QMessageBox.warning(self, "Input Error", "Please select a habit.")
            return
        
        # Obtener la frecuencia seleccionada
        frequency = self.combo_frequency.currentText()
        
        # Obtener el número de veces
        count = self.spin_count.value()
        
        # Mostrar los datos en un mensaje
        message = (f"Habit: {habit}\n"
                   f"Frequency: {frequency}\n"
                   f"Number of times: {count}")
        QMessageBox.information(self, "Habit Data", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HabitTracker()
    window.show()
    sys.exit(app.exec_())


"""Problema que resuelve: El programa ayuda a las personas a llevar un registro de sus hábitos saludables y fomentar una rutina diaria. 
Muchas personas quieren seguir hábitos saludables pero a menudo olvidan hacerlo. Este programa les permite registrar y hacer seguimiento de sus 
actividades, ayudando así a mejorar su bienestar."""

"""Se va a utilizar Radiobox (Radio Buttons): El cual permite seleccionar el tipo de hábito saludable que se desea registrar 
(Ejercicio, Lectura, Meditación)."""

"""Tambien se va utilizar Combobox (ComboBox): El cual permite seleccionar la frecuencia con la que se practica el hábito ya sea
(Diariamente, Semanalmente, Mensualmente)."""

"""Y tambien se va a ocupar Spinbox (SpinBox): Para poder ingresar el número de veces que se practica el hábito"""

