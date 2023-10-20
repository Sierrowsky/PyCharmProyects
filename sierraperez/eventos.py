import sys
from datetime import datetime

import var
from Salir import *
from main import locale

class Eventos():
    def Salir(self):
        try:
            var.salir.show()
        except Exception as error:
            print(error, "en modulo eventos")

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error al abrir calendario", error)

    @staticmethod
    def acercade(self):
        try:
            var.about.show()
        except Exception as error:
            print("Error abrir ventana acerca de ", error)

    @staticmethod
    def btnSalir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error btnSalir, ", error)

    @staticmethod
    def btnCancelar(self):
        try:
            var.salir.hide()
        except Exception as error:
            print("Error btnCancelar, ", error)

    @staticmethod
    def btnCerrarAbout(self):
        try:
            var.about.hide()
        except Exception as error:
            print("Error en btnCerrarAbout, ", error)

    def cargarstatusvar(self):
        """
        Eventos StatusBar

        """
        try:
            fecha = datetime.now().strftime("%A - " + "%d/%m/%y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel(" Version :" + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)
        except Exception as error:
            print("Error en cargarstatusbar ", error)

    def cargapropia(self):
        try:
            prov = ['A Coruña', 'Lugo', 'Ferrol', 'Vigo', 'Santiago de Compostela', 'Ourense', 'Pontevedra']
            var.ui.cmbProv.clear()
            var.ui.cmbProv.addItem(' ')
            for i, m in enumerate(prov):
                var.ui.cmbProv.addItem(str(m))
        except Exception as error:
            print("Error en cargapropia ", error)

    def selEstado(self):
        try:
            if var.ui.rbtTodos.isChecked():
                print("pulsaste todos")
            if var.ui.rbtAlta.isChecked():
                print("pulsaste alta")
            if var.ui.rbtBaja.isChecked():
                print("pulsaste baha")
        except Exception as error:
            print("Error en selEstado", error)

    def resizetabdrivers(self):
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 3 or i == 4:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error resizetabdrivers ", error)
    def CajaText(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))
        except Exception as error:
            print("Error en LetCap ", error)
