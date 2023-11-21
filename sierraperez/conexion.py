from datetime import datetime

from PyQt6 import QtWidgets, QtSql, QtCore

import drivers
import var


class Conexion():
    @staticmethod
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("conexion realizada")
            return True

    @staticmethod
    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                var.ui.cmbProv.addItem(' ')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print("Error en cargaProv", error)

    @staticmethod
    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMun.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select IdProv from provincias where provincia  = :prov")
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            queryM = QtSql.QSqlQuery()
            queryM.prepare("select municipio from municipios where IdProv = :id")
            queryM.bindValue(':id', int(id))
            if queryM.exec():
                var.ui.cmbMun.addItem('')
                while queryM.next():
                    var.ui.cmbMun.addItem(queryM.value(0))
        except Exception as error:
            print("Error en cargaMun", error)

    @staticmethod
    def guardardri(newdrivers):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into drivers(dnidri, altadri, apeldri, nombredri, direcciondri, '
                          ' provdri, munidri, movildri, salario, carnet) VALUES(:dni, :alta, :apel '
                          ' , :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newdrivers[0]))
            query.bindValue(':alta', str(newdrivers[1]))
            query.bindValue(':apel', str(newdrivers[2]))
            query.bindValue(':nombre', str(newdrivers[3]))
            query.bindValue(':direccion', str(newdrivers[4]))
            query.bindValue(':provincia', str(newdrivers[5]))
            query.bindValue(':municipio', str(newdrivers[6]))
            query.bindValue(':movil', str(newdrivers[7]))
            query.bindValue(':salario', str(newdrivers[8]))
            query.bindValue(':carnet', str(newdrivers[9]))
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Listo')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Empleado dado de alta')
                mbox.exec()
                Conexion.mostrardrivers()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("Error guardardri ", error)

    @staticmethod
    def mostrardrivers(self=None):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            drivers.Drivers.cargartabladri(registros)
        except Exception as error:
            print('Error al mostrar resultados', error)

    @staticmethod
    def SelectDrivers(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, '
                    'bajadri from drivers where bajadri is null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, bajadri '
                    'from drivers where bajadri is not null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
        except Exception as error:
            print("Error SelectDrivers ", error)

    @staticmethod
    def onedriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print('Error en onedriver', error)

    @staticmethod
    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri= :dni')
            query.bindValue(':dni', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.onedriver(codigo)
                    return registro

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('El conductor no existe')
                mbox.exec()
        except Exception as error:
            print('Error al buscar driver', error)

    @staticmethod
    def modifDriver(modifdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri = :dni, altadri = :alta ,nombredri = :nombre, apeldri = :apel, '
                          'direcciondri = :direccion, provdri = :provincia, munidri = :municipio,'
                          'movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

            query.bindValue(':codigo', int(modifdriver[0]))
            query.bindValue(':dni', str(modifdriver[1]))
            query.bindValue(':alta', str(modifdriver[2]))
            query.bindValue(':apel', str(modifdriver[3]))
            query.bindValue(':nombre', str(modifdriver[4]))
            query.bindValue(':direccion', str(modifdriver[5]))
            query.bindValue(':provincia', str(modifdriver[6]))
            query.bindValue(':municipio', str(modifdriver[7]))
            query.bindValue(':movil', str(modifdriver[8]))
            query.bindValue(':salario', str(modifdriver[9]))
            query.bindValue(':carnet', str(modifdriver[10]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Datos conductor modificados")
                mbox.exec()
                Conexion.mostrardrivers()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al modificar los datos del conductor")
                mbox.exec()
        except Exception as error:
            print("error en modificar driver conexion", error)

    @staticmethod
    def borrarDri(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('Select bajadri from drivers')
            fecha = datetime.today()
            fecha = fecha.strftime('%d/%m/%y')
            query = QtSql.QSqlQuery()
            query.prepare(' Update drivers set bajadri = :fechabaja where '
                          'dnidri = :dni')
            query.bindValue(':fechabaja', str(fecha))
            query.bindValue(':dni', str(dni))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Todo bien')
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text() + 'Error baja Driver')
                mbox.exec()
        except Exception as error:
            print('Error al borrar Driver', error)
    @staticmethod
    def selEstado(self):
        try:
            if var.ui.rbtTodos.isChecked():
                estado = 0
                Conexion.SelectDrivers(estado)
            elif var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.SelectDrivers(estado)
            elif var.ui.rbtBaja.isChecked():
                estado = 2
                Conexion.SelectDrivers(estado)
        except Exception as error:
            print("Error en selEstado", error)
    @staticmethod
    def consulta_drivers(fechaBaja):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()

            if fechaBaja == 2:
                query1.prepare("select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers")
            elif fechaBaja == 1:
                query1.prepare(
                    "select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers where fechaBaja is null")
            elif fechaBaja == 0:
                query1.prepare(
                    "select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers where fechaBaja is not null")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('Erros mostrar Resultados', error)
