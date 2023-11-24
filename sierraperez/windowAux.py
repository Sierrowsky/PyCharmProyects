import sys, eventos, var
import drivers
from Calendar import *
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
        var.about.lblVersion.setText(var.version)
        var.about.btnCerrraAbout.clicked.connect(eventos.Eventos.btnCerrarAbout)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
