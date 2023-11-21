import os.path
import shutil
import sys
from datetime import datetime
from conexion import *
import conexion
import var
from Salir import *
from main import locale
import zipfile


class Eventos():
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def cargapropia(self):
        try:
            prov = ['A Coruña', 'Lugo', 'Ferrol', 'Vigo', 'Santiago de Compostela', 'Ourense', 'Pontevedra']
            var.ui.cmbProv.clear()
            var.ui.cmbProv.addItem(' ')
            for i, m in enumerate(prov):
                var.ui.cmbProv.addItem(str(m))
        except Exception as error:
            print("Error en cargapropia ", error)


    @staticmethod
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

    @staticmethod
    def CajaText(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))
        except Exception as error:
            print("Error en LetCap ", error)

    @staticmethod
    def crearCopiaSeguridad(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = (str(fecha + '_backup.zip'))
            directorio, filename = var.dlgAbrir.getSaveFileName(None, 'Guardar Copia Seguridad', copia, '.zip')
            if var.dlgAbrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Copia de seguridad creada')
                mbox.exec()

        except Exception as error:
            print('Error crear copias seguridad', error)
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error crear copias seguridad')
            mbox.exec()

    @staticmethod
    def restaurarCopiaSeguridad(self):
        try:

            filename = var.dlgAbrir.getOpenFileName(None, 'Restaurar copias de seguridad', '', '*.zip;;All Files(*)')
            if var.dlgAbrir.accept and filename:
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                conexion.Conexion.mostrardrivers()
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Copia de seguridad Restaurada')
                mbox.exec()
            else: var.dlgAbrir.hide()
            conexion.Conexion.mostrardrivers()

        except Exception as error:
            print('Error restaurar copias seguridad', error)
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error al restaurar copias seguridad')
            mbox.exec()
