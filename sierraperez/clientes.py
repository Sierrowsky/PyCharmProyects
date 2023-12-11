import locale
import conexion
import drivers
import var, eventos
from PyQt6 import QtWidgets, QtCore, QtGui


class Clientes():
    @staticmethod
    def limpiarpanelcli(self):
        try:
            listawidgets = [var.ui.txtDniCli, var.ui.txtFechaBajaCliente, var.ui.RazonSocial, var.ui.DireccionCli,
                            var.ui.txtTlfCli, var.ui.lblValidarDniCli]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbProvCli.setCurrentText('')
            var.ui.cmbMunCli.setCurrentText('')
            var.ui.lblCodCliDB.setText('')
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Fallo al limpiar panel clientes , ', error)
            mbox.exec()

    def validardnicli(self=None):
        try:

            dni = var.ui.txtDniCli.text()

            dni = dni.upper()  # poner mayúscula
            var.ui.txtDniCli.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            if len(dni) == 9:  # comprueba que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDniCli.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    var.ui.lblValidarDniCli.setText('V')
                    return True
                else:
                    var.ui.lblValidarDniCli.setStyleSheet('color:red;')  # y si no un aspa en color rojo
                    var.ui.lblValidarDniCli.setText('X')
                    var.ui.txtDniCli.setText(None)
                    var.ui.txtDniCli.setFocus()
            else:
                var.ui.lblValidarDniCli.setStyleSheet('color:red;')
                var.ui.lblValidarDniCli.setText('X')
                var.ui.txtDniCli.setText(None)
                var.ui.txtDniCli.setFocus()

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Fallo al validar dni clientes , ', error)
            mbox.exec()

    def altacliente(self):
        try:
            if not all([var.ui.txtDniCli.text(), var.ui.txtRazonSocial.text(), var.ui.txtTlfCli.text(),
                        ]):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Faltan datos obligatorios')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtTlf.setText("")
                return
            cliente = [var.ui.txtDniCli, var.ui.txtRazonSocial, var.ui.txtDireccionCli,
                       var.ui.txtTlfCli, var.ui.txtFechaBajaCliente]
            newcliente = []

            for i in cliente:
                newcliente.append(i.text().title())

            prov = var.ui.cmbProvCli.currentText()
            newcliente.insert(4, prov)
            muni = var.ui.cmbMunCli.currentText()
            newcliente.insert(5, muni)
            print(newcliente)
            conexion.Conexion.guardarcliente(newcliente)
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Fallo en alta clientes , ', error)
            mbox.exec()

    def cargarTablaCli(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                index += 1
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error en cargar tabla cliente(clientes.Clientes.cargarTablaCli), ", error)
            mbox.exec()

    def cargarcliente(self):
        try:

            # Clientes.limpiarpanelcli(self)

            row = var.ui.tabClientes.selectedItems()
            fila = [dato.text() for dato in row]

            registro = conexion.Conexion.onecliente(fila[0])

            Clientes.cargardatos(registro)

        except Exception as error:
            print('error al cargar datos de un cliente en tabla', error)

    def cargardatos(registro):
        try:
            datos = [var.ui.lblCodCliDB, var.ui.txtDniCli, var.ui.txtRazonSocial, var.ui.txtFechaBajaCliente
                , var.ui.txtDireccionCli, var.ui.txtTlfCli, var.ui.cmbProvCli, var.ui.cmbMunCli]
            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
        except Exception as error:
            print(error, "Cargar datos cliente")

    def bajacli(self):
        try:
            dni = var.ui.txtDniCli.text()
            conexion.Conexion.bajacli(dni)
            conexion.Conexion.mostrarCliente(self)

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('El conductor no existe o ya dado de baja')
            mbox.exec()
            print('error al borrar datos de un cliente en tabla', error)
