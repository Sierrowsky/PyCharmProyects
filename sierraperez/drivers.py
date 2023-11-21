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
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdrivers[2])))
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
                index += 1

        except Exception as error:
            print('error alta cliente', error)

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
        except Exception as error:
            print('No se ha podido seleccionar al driver en la tabla', error)

    def bucarDni(self):
        try:
            registro = conexion.Conexion.codDri(var.ui.txtDni.text())
            if registro is not None:
                Drivers.buscarDriverTabla(registro[0])

        except Exception as error:
            print('error al buscar dni ', error)

    def cargadriver(self):
        try:
            Drivers.LimpiarPanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onedriver(fila[0])
            datos = [var.ui.lblcoddb, var.ui.txtDni, var.ui.txtFecha, var.ui.txtApel, var.ui.txtNombre, var.ui.txtDir,
                     var.ui.cmbProv, var.ui.cmbMun, var.ui.txtTlf, var.ui.txtSalario,
                     var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            j = 0
            carnets = registro[10]
            for i in datos:

                if type(i) == QComboBox:
                    i.setCurrentText(str(registro[j]))
                    j = j + 1
                elif type(i) == QCheckBox:
                    Drivers.ValidarDni(carnets)
                    j = j + 1
                else:
                    i.setText(registro[j])
                    j = j + 1
        except Exception as error:
            print('error al cargar datos de 1 cliente ', error)

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