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
            query.prepare("select provincia from provincia")
            if query.next():
                var.ui.cmbProv.addItem(' ')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print("Error en cargaProv", error)
    def cargamun(self=None):
        try:
            var.ui.cmbMun.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select municipio from municipio")
            if query.next():
                var.ui.cmbMun.addItem(' ')
                while query.next():
                    var.ui.cmbMun.addItem(query.value(0))
        except Exception as error:
            print("Error en cargaMun", error)