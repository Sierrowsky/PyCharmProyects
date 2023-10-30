from PyQt6 import QtWidgets, QtSql, QtCore
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
            query.bindValue(':prov',prov)
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