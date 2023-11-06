from PyQt6 import QtWidgets, QtSql, QtCore

import drivers
import var


class Conexion():

    def conexion(self=None):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("conexion realizada?")
            return True

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
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()
            #drivers.Drivers.cargarTabla(datosDri)
        except Exception as error:
            print("Error guardardri ", error)

    def mostrardrivers(self):
        try:
            registros=[]
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            drivers.Drivers.cargartabladri(registros)
            print(registros)
        except Exception as error:
                print('Error al mostrar resultados',error)
