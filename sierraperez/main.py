import sys, eventos, var

import drivers
from Calendar import *
from MainWindow import *
from Salir import *
from About import *
from datetime import datetime


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_digCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.Calendar.setSelectedDate((QtCore.QDate(ano, mes, dia)))
        var.calendar.Calendar.clicked.connect(drivers.Drivers.CargaFecha)


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self).__init__()
        var.salir = Ui_dlgSalir()
        var.salir.setupUi(self)
        var.salir.btnSalirAceptar.clicked.connect(eventos.Eventos.btnSalir)
        var.salir.btnSalirCancelar.clicked.connect(eventos.Eventos.btnCancelar)


class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        var.about = Ui_dlgAbout()
        var.about.setupUi(self)
        var.about.btnCerrraAbout.clicked.connect(eventos.Eventos.btnCerrarAbout)


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Encargado de generar la interfaz
        var.calendar = Calendar()
        var.salir = Salir()
        var.about = About()
        var.driver = drivers.Drivers()
        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        """
        Zona de eventos del MenuBar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        """
        Zona de eventos de las cajas de texto
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.ValidarDni)
        """
        Eventos del ToolBar
        """
        var.ui.barSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.barLimpiarPanel.triggered.connect(drivers.Drivers.LimpiarPanel)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
