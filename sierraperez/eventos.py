import os.path
import shutil
import sys
from datetime import datetime

import xlrd
import xlwt

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
    def valSalario(self=None):
        try:
            salario = var.ui.txtSalario.text()
            valores = "1234567890., €"
            for n in salario:
                if n in valores:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Valor de Salario Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtSalario.setText("")
                    break
            var.ui.txtSalario.setText(str(locale.currency(round(float(var.ui.txtSalario.text()), 2), grouping=True)))
        except Exception as error:
            print('error en valSalario', error)

    @staticmethod
    def valTelefono(self=None):
        try:
            telefono = var.ui.txtTlf.text()
            numeros = '1234567890'
            for n in telefono:
                if n in numeros and len(telefono) == 9:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Escriba un número de móvil correcto')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtTlf.setText("")
                    break

        except Exception as error:
            print("Error en ValTelefono", error)
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
                conexion.Conexion.mostrardriver()
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Copia de seguridad Restaurada')
                mbox.exec()
            else:
                var.dlgAbrir.hide()
            conexion.Conexion.mostrardriver()

        except Exception as error:
            print('Error restaurar copias seguridad', error)
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error al restaurar copias seguridad')
            mbox.exec()

    def exportardatosxls(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + '_Datos.xls')
            directorio, filename = var.dlgAbrir.getSaveFileName(None, 'Exportar Datos en Fichero XLS', file, '.xls')
            if var.dlgAbrir.accept and filename != '':
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Dirección')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Telefono')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'TipoCarnet')
                sheet1.write(0, 11, 'Fechabaja')
                registros = conexion.Conexion.selectDriverstodos(self)
                for j, registros in enumerate(registros):
                    for i, valor in enumerate(registros):
                        sheet1.write(j + 1, i, str(valor))
                wb.save(directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setModal(True)
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Copia de seguridad creada')
                mbox.exec()



        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error al exportar datros', error)
            mbox.exec()

    def importardatosxls(self):
        try:
            filename = var.dlgAbrir.getOpenFileName(None, 'Importar datos', '',
                                                    '*.xls;;All Files(*)')
            if var.dlgAbrir.accept and filename != '':
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j == 1:
                                dato = xlrd.xldate_as_datetime(datos.cell_value(i, j), documento.datemode)
                                print(dato)
                                dato = dato.strftime('%d/%m/%Y')
                                print(dato)
                                new.append(str(dato))
                            else:
                                new.append(str(datos.cell_value(i, j)))
                        conexion.Conexion.guardardri(new)
                    if i == filas - 1:
                        msg = QtWidgets.QMessageBox()
                        msg.setModal(True)
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('Importación de Datos Realizada')
                        msg.exec()
                conexion.Conexion.SelectDrivers(0)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(error)
            msg.exec()
