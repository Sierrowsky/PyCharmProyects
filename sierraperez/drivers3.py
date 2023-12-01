import locale

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QComboBox, QCheckBox
from PyQt6.uic.properties import QtGui

import conexion
import var
from PyQt6 import QtWidgets, QtCore


class Drivers():
    @staticmethod
    def LimpiarPanel(self):
        try:
            listawidgets = [var.ui.txtNombre, var.ui.txtApel, var.ui.txtDir, var.ui.txtSalario,
                            var.ui.txtTlf, var.ui.txtDni, var.ui.txtFecha, var.ui.txtNombre,
                            var.ui.txtApel, var.ui.txtDir, var.ui.txtSalario, var.ui.txtTlf,
                            var.ui.lblValidarDni]
            for i in listawidgets:
                i.setText(None)
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                i.setChecked(False)

            var.ui.cmbProv.setCurrentText(' ')
            var.ui.cmbMun.setCurrentText(' ')
        except Exception as error:
            print("Error en LimpiarPanel", error)

    @staticmethod
    def CargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:04d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("Error cargaFecha ", error)



    @staticmethod
    def ValidarDni(self=None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:  # Comprobamos que son 9
                dig_control = dni[8]  # Tomamos la letra del DNI
                dni = dni[:8]  # Tomamos los numeros del DNI
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni ", error)

    def altadriver(self):
        try:
            driver = [var.ui.txtDni, var.ui.txtFecha,
                      var.ui.txtApel, var.ui.txtNombre,
                      var.ui.txtDir, var.ui.txtTlf, var.ui.txtSalario]
            newdrivers = []
            for i in driver:
                if i.text().strip():
                    newdrivers.append(i.text().title())
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Tods los campos deben ser rellenados: \n DNI, Nombre, Fecha de alta y Movil")
                    mbox.exec()
                    return
            prov = var.ui.cmbProv.currentText()
            newdrivers.insert(5, prov)
            muni = var.ui.cmbMun.currentText()
            newdrivers.insert(6, muni)
            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdrivers.append(' - '.join(licencias))
            print(newdrivers)
            conexion.Conexion.guardardri(newdrivers)
            '''
            index = 0
            var.ui.tabDrivers.setRowCount(index + 1)  # Crea una fila
            var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newdrivers[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdrivers[1])))
     +       var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdrivers[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdrivers[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdrivers[4])))
            var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)            
            '''
        except Exception as error:
            print("Error en alta Driver", error)

    def cargartabladri(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)  # crea una fila
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1


        except Exception as error:
            print('error alta cliente', error)

    def buscarDri(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)

            Drivers.cargadriver(registro)

            registros = conexion.Conexion.mostrardrivers(self=None)
            Drivers.cargartabladri(registros)
            codigo = var.ui.lblcoddb.text()
            Drivers.colorearFila(codigo)

        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def colorearFila(codigo):
        for fila in range(var.ui.tabDrivers.rowCount()):
            if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tabDrivers.columnCount()):
                    item = var.ui.tabDrivers.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def buscarDriverTabla(codigo):
        try:
            tabla = var.ui.tabDrivers
            for fila in range(tabla.rowCount()):
                item = tabla.item(fila, 0)
                valorCelda = item.text()
                if valorCelda == str(codigo):
                    tabla.selectRow(fila)
                    tabla.scrollToItem(item)
                    Drivers.cargadriver(self=None)
                    item.setBackground(QtGui.QColor(255, 241, 150))


        except Exception as error:
            print('No se ha podido seleccionar al driver en la tabla', error)

    def bucarDni(self):
        try:
            registro = conexion.Conexion.codDri(var.ui.txtDni.text())
            if registro is not None:
                Drivers.buscarDriverTabla(registro[0])

        except Exception as error:
            print('error al buscar dni ', error)

    def cargadriver(registro):
        try:
            datos = [var.ui.lblcoddb, var.ui.txtDni, var.ui.txtFecha, var.ui.txtApel,
                     var.ui.txtNombre, var.ui.txtDir, var.ui.cmbProv, var.ui.cmbMun,
                     var.ui.txtTlf, var.ui.txtSalario]
            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
        except Exception as error:
            print(error, "error en cargar datos drivers")

    def b(self):
        try:
            Drivers.LimpiarPanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registros = conexion.Conexion.onedriver(fila[0])
            datos = [var.ui.lblcoddb, var.ui.txtDni, var.ui.txtFecha, var.ui.txtApel, var.ui.txtNombre, var.ui.txtDir,
                     var.ui.cmbProv, var.ui.cmbMun, var.ui.txtTlf, var.ui.txtSalario]
            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registros[i]))
                else:
                    dato.setText(str(registros[i]))
            if 'A' in registros[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registros[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registros[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registros[10]:
                var.ui.chkD.setChecked(True)
        except Exception as error:
            print('Error en cargadriver', error)

    def a(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            if registro is None:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error en la busqueda de dni")
                mbox.exec()
            else:
                Drivers.cargadriver(registro)
                Drivers.buscarDriverTabla(registro[0])
        except Exception as error:
            print('error en busca de datos conductor', error)

    def c(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.cargadriver(registro)
            registros = conexion.Conexion.mostrardrivers(self=None)
            Drivers.cargartabladri(registros)
            codigo = var.ui.lblcoddb.text()
            for fila in range(var.ui.tabDrivers.rowCount()):
                if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    # var.ui.tabDrivers.selectRow(fila)
                    var.ui.tabDrivers.scrollToItem(var.ui.tabDrivers.item(fila, 0))
                    var.ui.tabDrivers.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tabDrivers.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[3])))
                    var.ui.tabDrivers.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[4])))
                    var.ui.tabDrivers.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[8])))
                    var.ui.tabDrivers.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[10])))
                    var.ui.tabDrivers.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(registro[11])))
                    var.ui.tabDrivers.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 0).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 1).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 2).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 3).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 4).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 5).setBackground(QtGui.QColor(255, 241, 150))
                    break
        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def modifDri(self):
        try:
            driver = [var.ui.lblcoddb,
                      var.ui.txtDni,
                      var.ui.txtFecha,
                      var.ui.txtApel,
                      var.ui.txtNombre,
                      var.ui.txtDir,
                      var.ui.txtTlf,
                      var.ui.txtSalario]
            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            modifdriver.insert(6, prov)
            muni = var.ui.cmbMun.currentText()
            modifdriver.insert(7, muni)

            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            modifdriver.append('/'.join(licencias))
            conexion.Conexion.modifDriver(modifdriver)
        except Exception as error:
            print('Error en modifDri', error)

    def borrarDri(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borrarDri(dni)
            conexion.Conexion.mostrardrivers()
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error al borrrar al Driver")
            mbox.exec()
