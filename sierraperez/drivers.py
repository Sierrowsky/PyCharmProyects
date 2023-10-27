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
    def ValSalario(self=None):
        try:
            Salario = var.ui.txtSalario.text()

        except Exception as error:
            print("Error en ValSalario", error)

    @staticmethod
    def valTelefono():
        try:
            telefono = var.ui.txtTlf.text()
            numeros = '1234567890'
            if len(telefono) == 9:
                if len(telefono) == len([n for n in telefono if n in numeros]):
                    var.ui.lblValidarTlf.setStyleSheet('color:green;')
                    var.ui.lblValidarTlf.setText('V')
                    print("perfecto")
                else:
                    var.ui.lblValidarTlf.setStyleSheet('color:red;')
                    var.ui.lblValidarTlf.setText('X')
                    var.ui.txtTlf.setText(None)
                    var.ui.txtTlf.setFocus()
                    print("no perfecto")
            else:
                var.ui.lblValidarTlf.setStyleSheet('color:red;')
                var.ui.lblValidarTlf.setText('X')
                var.ui.txtTlf.setText(None)
                var.ui.txtTlf.setFocus()
                print("no perfecto")
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
                    print("perfecto")
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
                    print("no perfecto")
            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()
                print("no perfecto")
        except Exception as error:
            print("error en validar dni ", error)

    def altadriver(self):
        try:
            driver = [var.ui.txtApel, var.ui.txtNombre, var.ui.txtTlf]
            newdrivers = []
            newdrivers.append(1)
            for i in driver:
                newdrivers.append(i.text().title())
            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                licencias.append(i.text())
            newdrivers.append(' - '.join(licencias))
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
            print(newdrivers)
        except Exception as error:
            print("Error en alta Driver", error)
